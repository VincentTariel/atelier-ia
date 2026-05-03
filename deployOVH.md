# Deployment Guide — Atelier IA sur OVH

> Site en production : **https://atelier-ia.ovh**
> Serveur : `ubuntu@51.161.32.145`
> Dernière mise à jour : 2026-05-04

---

## Layout serveur

| Élément | Chemin / valeur |
|---|---|
| Code Django | `/home/ubuntu/atelier-ia/` |
| Virtualenv | `/home/ubuntu/atelier-ia/venv/` |
| Variables d'env | `/home/ubuntu/atelier-ia/.env` (chmod 600) |
| Base SQLite | `/home/ubuntu/atelier-ia/db.sqlite3` |
| Static collectés | `/home/ubuntu/atelier-ia/staticfiles/` |
| Service systemd | `atelier-ia.service` |
| Gunicorn bind | `127.0.0.1:8001` (3 workers) |
| Nginx site | `/etc/nginx/sites-enabled/atelier-ia` |
| Certificats SSL | Let's Encrypt (`/etc/letsencrypt/live/atelier-ia.ovh/`) |
| Repo Git | `https://github.com/VincentTariel/atelier-ia.git` (privé) |
| Branche prod | `main` |

Le serveur héberge aussi CommeUnJeu dans `/home/ubuntu/wwww/` — **ne pas confondre** les deux dossiers et les deux services systemd (`gunicorn.service` pour CommeUnJeu, `atelier-ia.service` pour Atelier IA).

---

## Quick deploy — Backend complet (le 9 fois sur 10)

Depuis le dossier local `/home/vtariel/cowork-sda2/atelier-ia/` :

```bash
# 1. Commit + push
git add <fichiers>
git commit -m "..."
git push origin main

# 2. Déploiement serveur en un seul SSH
ssh ubuntu@51.161.32.145 'bash -se' << 'EOF'
set -e
cd ~/atelier-ia
git fetch origin main && git reset --hard origin/main
source venv/bin/activate
pip install -q -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput
sudo systemctl restart atelier-ia
sudo systemctl is-active atelier-ia
EOF

# 3. Vérification
curl -s -o /dev/null -w "%{http_code}\n" https://atelier-ia.ovh/
```

Si tout est vert (`active` + `200`), c'est plié.

---

## Variables d'environnement — `.env` sur le serveur

Le fichier `/home/ubuntu/atelier-ia/.env` (chmod 600, jamais committé) contient :

```env
DJANGO_SECRET_KEY=<générée à l'install — voir ci-dessous>
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=atelier-ia.ovh,www.atelier-ia.ovh,51.161.32.145
EMAIL_HOST_USER=commeunjeu.ad@gmail.com
EMAIL_HOST_PASSWORD=<app password Gmail 16 chars>
DEFAULT_FROM_EMAIL=commeunjeu.ad@gmail.com
```

**Régénérer le `.env` sur le serveur** (si jamais perdu) :

```bash
ssh ubuntu@51.161.32.145
cd ~/atelier-ia
source venv/bin/activate
NEW_KEY=$(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
cat > .env <<EOF
DJANGO_SECRET_KEY=${NEW_KEY}
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=atelier-ia.ovh,www.atelier-ia.ovh,51.161.32.145
EMAIL_HOST_USER=commeunjeu.ad@gmail.com
EMAIL_HOST_PASSWORD=ejtswhmtdapzlema
DEFAULT_FROM_EMAIL=commeunjeu.ad@gmail.com
EOF
chmod 600 .env
sudo systemctl restart atelier-ia
```

**Modifier une variable** : éditer `~/atelier-ia/.env` puis `sudo systemctl restart atelier-ia`.

---

## Quick deploy — Templates / copy uniquement (pas de migration)

```bash
git add core/templates/ && git commit -m "..." && git push origin main
ssh ubuntu@51.161.32.145 "cd ~/atelier-ia && git fetch origin main && git reset --hard origin/main && python manage.py collectstatic --noinput --settings=atelier_ia.settings && sudo systemctl restart atelier-ia"
```

> Le `collectstatic` est inutile si on n'a touché qu'aux templates Django (les templates sont lus directement, pas collectés). Le restart suffit.

---

## Quick deploy — Modèle Django (avec migration)

Toujours :

1. **En local** : `python manage.py makemigrations` AVANT le push.
2. **Vérifier** que la migration n'entre pas en conflit avec une migration potentiellement générée côté serveur (ex : `0003_alter_lead_id` créée automatiquement par Django 5.2 lors d'un précédent restart). En cas de conflit :

   ```bash
   # Sync la migration serveur en local
   scp ubuntu@51.161.32.145:~/atelier-ia/core/migrations/<la_manquante>.py core/migrations/

   # Renumérote la tienne et corrige sa dépendance
   git mv core/migrations/00XX_old.py core/migrations/00YY_new.py
   sed -i "s/('core', '<old_dep>')/('core', '<new_dep>')/" core/migrations/00YY_new.py

   git add core/migrations/ && git commit -m "Fix migration order" && git push
   ```

3. **Sur le serveur** : pull + migrate + restart (le `git reset --hard` absorbe le rename).

---

## Sécurité — règles en vigueur

- `DEBUG=False` en prod (forcé par `DJANGO_DEBUG=False` dans `.env`).
- `SECRET_KEY` : générée aléatoirement à l'install, stockée dans `.env` chmod 600.
- `ALLOWED_HOSTS` : restreint aux domaines connus.
- HSTS 1 an + cookies Secure activés (settings.py, branche `if not DEBUG`).
- `db.sqlite3` non versionné, pas de backup automatisé pour l'instant — **dette à traiter**.
- `.env` jamais committé (gitignored ligne 22).
- `EMAIL_HOST_PASSWORD` est un app password Gmail (à révoquer/regénérer si fuite : https://myaccount.google.com/apppasswords).

---

## Vérifications post-deploy

```bash
# 1. HTTPS répond
curl -s -o /dev/null -w "%{http_code}\n" https://atelier-ia.ovh/         # → 200
curl -s -o /dev/null -w "%{http_code}\n" https://atelier-ia.ovh/inexistant  # → 404 (pas 500)

# 2. Pas de stack trace en cas d'erreur (DEBUG=False bien actif)
curl -s https://atelier-ia.ovh/inexistant | head -5  # doit être minimal, pas un Django error page

# 3. Service systemd actif
ssh ubuntu@51.161.32.145 "sudo systemctl is-active atelier-ia"  # → active

# 4. Logs propres (pas d'erreur récente)
ssh ubuntu@51.161.32.145 "sudo journalctl -u atelier-ia --since '5 minutes ago' --no-pager | tail -20"

# 5. Test bout-en-bout du formulaire (manuel)
# → ouvrir https://atelier-ia.ovh/
# → remplir le formulaire avec son propre email
# → vérifier réception du PDF lead-magnet
```

---

## Rollback — en cas de catastrophe

Si un déploiement casse la prod :

```bash
ssh ubuntu@51.161.32.145
cd ~/atelier-ia

# 1. Identifier le commit précédent qui marchait
git log --oneline -10

# 2. Reset hard sur ce commit
git reset --hard <sha>

# 3. Si la migration récente doit être annulée :
source venv/bin/activate
python manage.py migrate core <migration_précédente>

# 4. Restart
sudo systemctl restart atelier-ia

# 5. Vérifier
curl -s -o /dev/null -w "%{http_code}\n" https://atelier-ia.ovh/
```

> **Attention** : `git reset --hard` côté serveur écrase aussi le `.env` ? **Non** — `.env` est gitignored, donc préservé.

---

## Restart gunicorn sans déploiement

Si on veut juste recharger la config (ex : changement de `.env`) :

```bash
ssh ubuntu@51.161.32.145 "sudo systemctl restart atelier-ia && sudo systemctl is-active atelier-ia"
```

Pour reload nginx (config nginx changée — rare) :

```bash
ssh ubuntu@51.161.32.145 "sudo nginx -t && sudo systemctl reload nginx"
```

---

## Logs et debug

```bash
# Logs gunicorn / Django (journalctl)
ssh ubuntu@51.161.32.145 "sudo journalctl -u atelier-ia -f"

# Logs nginx access / error
ssh ubuntu@51.161.32.145 "sudo tail -f /var/log/nginx/access.log"
ssh ubuntu@51.161.32.145 "sudo tail -f /var/log/nginx/error.log"

# Status complet
ssh ubuntu@51.161.32.145 "sudo systemctl status atelier-ia --no-pager"
```

---

## Dette technique connue (à traiter quand on aura le temps)

- **Tailwind CDN** (`base.html` ligne 17) : OK pour le développement, pas idéal en prod (taille JS ~4 MB chargé client). À builder avec Tailwind CLI un jour.
- **Backup `db.sqlite3`** : pas de backup automatique. À mettre en place (cron `scp` quotidien vers une autre machine ou un bucket).
- **Renouvellement Let's Encrypt** : auto via certbot (snap). À surveiller via `sudo certbot certificates`.
- **Gunicorn workers** : 3 — suffisant pour le trafic actuel (low). À monitorer si trafic monte.

---

## Première installation — pour mémoire

Si on devait redéployer le projet sur un nouveau serveur :

```bash
# 1. Installer dépendances système
sudo apt update && sudo apt install -y python3 python3-venv python3-pip nginx certbot python3-certbot-nginx git

# 2. Cloner le repo
cd ~ && git clone https://github.com/VincentTariel/atelier-ia.git
cd atelier-ia

# 3. Créer le venv et installer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 4. Créer le .env (voir section "Variables d'environnement" ci-dessus)

# 5. Migrate + collectstatic + créer un superuser
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser

# 6. Créer le service systemd /etc/systemd/system/atelier-ia.service :
#    (voir contenu actuel : sudo cat /etc/systemd/system/atelier-ia.service)

# 7. Créer le site nginx /etc/nginx/sites-available/atelier-ia
#    + symlink vers sites-enabled
#    + nginx -t + reload

# 8. Obtenir le certificat
sudo certbot --nginx -d atelier-ia.ovh -d www.atelier-ia.ovh

# 9. Démarrer
sudo systemctl enable --now atelier-ia
```

---

## Contacts

- **Domaine** : OVH (atelier-ia.ovh) — manageable sur le compte OVH de Vincent
- **Hébergement** : OVH VPS — Ubuntu 22.04 (probablement)
- **Repo** : `github.com/VincentTariel/atelier-ia` (privé)
