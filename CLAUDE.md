# Atelier IA — Contexte projet

> Source de vérité pour tout assistant Claude travaillant sur ce dossier. Lire en entier avant toute action.

## 1. Identité

- **Porteur** : Vincent Tariel — solopreneur, basé à Nouméa (Nouvelle-Calédonie).
- **Email** : `tariel.vincent@gmail.com`
- **Statut** : Entreprise Individuelle en cours de structuration (voir `Administratif/Admin_Demarrage_EI_NC.md`).
- **Autres projets** : `commeunjeu3` — plateforme pédagogique de mathématiques, en ligne sur **https://commeunjeu.org**. Projet séparé situé hors de ce dossier — pas en scope ici.

## 1.bis À propos du formateur — bio canonique

> Version officielle de la bio de Vincent. À utiliser telle quelle (ou en variantes ci-dessous) dans toute la copy : site, PDF lead-magnet, cold-emails, signature, présentation vidéo, propositions commerciales.
> **Ne jamais inventer ni paraphraser** d'éléments biographiques sans relire ce bloc.

### Version longue (~200 mots — page "À propos" / fin de PDF)

> Vincent Tariel développe depuis 2024 **CommeUnJeu**, une plateforme pédagogique de mathématiques (mobile, web, vidéos) — qu'il construit seul en utilisant Claude tous les jours comme cowork(er) de développement, de production de contenu et de gestion. Cette pratique quotidienne nourrit directement le coaching qu'il propose à Nouméa : il transmet ce qui marche et ce qui fait perdre du temps, sur la base de cas réels.
>
> Avant CommeUnJeu, Vincent a fondé deux startups (Shinoe Software et AlphaNumeric-Vision, à Paris, 2010-2016) en traitement d'images puis en deep learning, et a enseigné l'IA en école d'ingénieurs (ISEN Nantes), formé des enseignants à l'université de Nouvelle-Calédonie (INSPE), et enseigné les maths et l'informatique en lycée international à Nouméa.
>
> Il est **docteur en informatique de l'École Polytechnique** (vision par ordinateur, 2009), agrégé de mathématiques (option Probabilités & Statistiques, 2017), et a effectué un post-doctorat à l'Australian National University.
>
> Installé en Nouvelle-Calédonie depuis 2020.

### Version courte (3-4 phrases — landing site / cold-email)

> Vincent Tariel — docteur en informatique de l'École Polytechnique, fondateur de plusieurs startups en IA, ancien enseignant-chercheur. Installé à Nouméa depuis 2020. Il développe aujourd'hui sa plateforme pédagogique CommeUnJeu (mobile, web, vidéos) en utilisant Claude au quotidien — et transmet ce qu'il apprend, sur le terrain, à des professionnels calédoniens en coaching individuel.

### Version une ligne (signature email / lower-third vidéo)

> Vincent Tariel — Docteur École Polytechnique · Coaching Claude Desktop · Nouméa

### Règles d'usage de la bio

- **Polytechnique** : toujours préciser **"docteur de l'École Polytechnique"** ou **"thèse à l'École Polytechnique"**. Ne JAMAIS écrire "diplômé de l'École Polytechnique" tout court (ambigu — confusion possible avec polytechnicien). Ne jamais écrire "polytechnicien".
- **CommeUnJeu** : présenter comme une activité **parallèle et complémentaire** au coaching, pas comme un projet "en attente de PMF". L'angle = *"je pratique ce que j'enseigne tous les jours"*.
- **NC depuis 2020** : à mentionner systématiquement, c'est un signal d'ancrage fort.
- **Startups** : on peut citer Shinoe Software / AlphaNumeric-Vision si la longueur le permet, sinon dire "fondateur de plusieurs startups en IA".
- **Diplôme d'ingénieur ESIEE (major de promo)** : à ne PAS mentionner dans la copy commerciale — trop spécifique pour la cible NC, et noyé par le doctorat. Garder pour le CV uniquement.
- **Post-doc Australie / agrégation** : à mentionner uniquement dans la version longue, pas dans le pitch court.

## 2. Activité — Atelier IA

Coaching **1-to-1** en présentiel à Nouméa, pour des **professionnels non-développeurs** qui veulent intégrer **Claude Desktop** dans leur quotidien de travail.

**Pivot en cours** : l'activité initiale (ateliers de groupe de 3h sur Claude Projects/GPTs/n8n) est abandonnée au profit du 1-to-1. Toute mention de "Niveau 1 / Niveau 2", de "atelier 3h", ou de "n8n" dans le code/copy existant est de l'ancien positionnement et doit être retirée lors des prochaines passes.

## 3. Promesse et philosophie

> **Claude ne remplace pas votre travail. Il augmente votre productivité pour que vous restiez focus sur votre vraie valeur ajoutée.**

- **Ce qu'on enseigne** : utiliser Claude Desktop pour **FAIRE** son travail — rédiger, analyser, synthétiser, préparer des réunions, traiter des emails, automatiser des tâches récurrentes via Projects et MCP (Drive, Calendar, Gmail, filesystem).
- **Ce qu'on n'enseigne PAS** : coder, builder, prompter du Claude Code (CLI). Pas de dev, pas de notebook Python.
- **Cible** : professionnels 30-55 ans en NC, secteurs prioritaires à affiner dans `offre/persona.md`. Aucun pré-requis technique au-delà de "savoir utiliser un ordinateur".

## 4. Architecture du dossier

```
atelier-ia/
├── CLAUDE.md             ← ce fichier (source de vérité)
├── offre/                ← positionnement, persona, pricing, FAQ, brief lead-magnet
├── video/                ← script + storyboard + assets de la vidéo explicative courte
├── acquisition/          ← sources prospects, CSV, templates email, scripts d'appel, KPI
├── crm/                  ← pipeline + fiches leads/clients (gitignored) + revues hebdo
├── core/                 ← app Django (site public + admin = CRM inbound)
├── atelier_ia/           ← settings Django
├── Administratif/        ← admin EI Nouvelle-Calédonie
├── prompt/               ← prompts de build initial du site (archive)
├── manage.py, db.sqlite3, requirements.txt, venv/
└── GEMINI.md             ← ancien contexte projet (obsolète, à archiver)
```

**Pointeurs rapides** :
- Le pitch et la promesse → `offre/positionnement.md`
- À qui on parle → `offre/persona.md`
- Templates de prospection → `acquisition/email_templates/` et `acquisition/call_scripts/`
- État du pipeline commercial → `crm/pipeline.md`

## 5. Stack technique du site

- **Backend** : Django (Python), app principale `core`.
- **Frontend** : templates Django + Tailwind CSS via CDN.
- **Base** : SQLite (`db.sqlite3`).
- **Email** : SMTP Gmail (compte expéditeur configuré dans `atelier_ia/settings.py`).
- **Modèle Lead** (`core/models.py`) : `prenom`, `nom`, `email`, `entreprise`, `telephone`, `formation_interessee`, `date_inscription`. Étroit, suffisant pour l'inbound, à étendre avec un champ `notes` JSON si besoin plus tard.
- **Vue principale** : `core/views.py:landing_page_view` — sauvegarde le lead, envoie un email avec le PDF lead-magnet attaché.
- **Domaine** : `atelier-ia.ovh` (déjà actif).

## 6. Stratégie CRM

- **Inbound** (formulaire du site) → table `core_lead` SQLite, consultable via l'admin Django (`/admin/`).
- **Outbound** (prospection sortante) → `acquisition/prospects.csv` (liste large) + `crm/leads/<nom>.md` (fiche par lead chaud).
- **Convergence** → `crm/pipeline.md` (Kanban texte : Suspect → Contacté → RDV → Proposition → Signé / Perdu) cite manuellement les leads des deux sources.
- **Revue** : hebdomadaire, dans `crm/revues/AAAA-MM-JJ.md` (gabarit dans `crm/revues/_gabarit_revue_hebdo.md`).
- **Critère de bascule vers un outil dédié (Notion/Airtable/CRM Django étendu)** : >20 leads chauds simultanés OU fiches markdown devenues illisibles. Pas avant.

## 7. Règles pour Claude (l'assistant)

### Langue et ton
- Toute la **copy** (site, emails, scripts, PDF, vidéo) est en **français**.
- Ton **B2B sobre**, pas startup-bro, pas américanisé. Pas d'emojis sauf demande explicite de Vincent.
- **Code** en anglais, **commentaires de code** en français.

### Génération de contenu
- Avant de générer un email, un script ou de la copy, **lire** `offre/positionnement.md` et `offre/persona.md` pour rester aligné.
- **Ne jamais** réintroduire la dichotomie "Niveau 1 / Niveau 2", ni mentionner "ateliers de 3h", "n8n", "GPT" comme produit. Ce sont des reliques de l'ancien positionnement.
- Quand on parle de l'outil, dire **Claude Desktop** (pas "ChatGPT", pas "Claude Code", pas "l'IA" tout court).
- **Témoignages clients** : **toujours anonymisés par secteur**. Format autorisé : *"Avocat à Nouméa : [bénéfice]"*, *"Cabinet d'expertise comptable du Grand Nouméa : [bénéfice]"*. **Jamais** de nom de personne, de cabinet, de logo, de photo. Les pros NC sont attachés à la confidentialité — c'est aussi cohérent avec ce qu'on leur vend (FAQ q.2). Voir `offre/pricing.md` section "Communication publique du tarif Fondateurs" pour la formulation.

### CRM et données privées
- **Ne jamais committer** le contenu de `crm/leads/` ni de `crm/clients/` (gitignored). Vérifier avant `git add -A`.
- Ne pas afficher d'emails complets de prospects dans des outputs publics ou partagés.
- Quand on édite `acquisition/prospects.csv`, garder la même structure de colonnes (header).

### Workflow type — exemple
> *"Je veux envoyer 10 cold-emails cette semaine"*

1. Lire `acquisition/email_templates/01_cold_intro.md` pour le format de référence.
2. Lire `acquisition/prospects.csv` pour identifier les 10 prospects à contacter (statut `À contacter`).
3. Pour chaque prospect, générer une version personnalisée du template (mention du secteur, accroche contextuelle).
4. Proposer un fichier `acquisition/sends/AAAA-MM-JJ_batch.md` avec les 10 versions, prêtes à copier-coller.
5. Mettre à jour le statut dans `prospects.csv` (`Contacté` + date).
6. Créer une fiche dans `crm/leads/` pour chaque prospect contacté (gabarit dans `crm/leads/_gabarit.md`).

### Modifications du site Django
- Le site est en **production** sur `atelier-ia.ovh`. Toute modification de templates, vues, ou modèles est à faire avec prudence.
- Pour la copy : `core/templates/core/landing.html` (la hero, les services, les témoignages, le formulaire). `core/forms.py` pour les labels du dropdown `formation_interessee`.
- Pour le modèle : créer une migration Django avant de toucher `core/models.py` (`python manage.py makemigrations && migrate`).
- Toujours tester en local (`python manage.py runserver`) avant tout déploiement.

## 8. Dette technique connue (à traiter quand Vincent le demande)

- `DEBUG = True` dans `atelier_ia/settings.py` — risque en prod, à passer à `False` avec gestion d'env.
- `SECRET_KEY` en clair dans le code — à externaliser en variable d'environnement.
- `ALLOWED_HOSTS` contient une URL avec schéma (`"https://atelier-ia.ovh"`) qui n'est pas valide pour Django (attend juste le hostname). À nettoyer.
- Modèle `Lead` étroit — ajouter `notes`/`metadata` JSON quand le volume inbound le justifiera.
- `db.sqlite3` versionné (`.gitignore` actuel l'exclut, vérifier qu'il n'est pas déjà dans l'historique git).
- PDF lead-magnet `core/templates/pdf/Atelier_IA_Niveau_1.pdf` aligné sur l'ancien positionnement — à remplacer.

## 9. Hors-scope explicite

- **CommeUnJeu** (`/home/vtariel/cowork-sda2/commeunjeu3/`, en ligne sur **https://commeunjeu.org**) est un projet **séparé** (pédagogie mathématique, vidéos Manim). Ne jamais éditer de fichier dans CommeUnJeu depuis ce dossier. Ne pas mélanger les deux activités dans la copy ou la prospection.
- Ne pas créer d'intégration entre Atelier IA et CommeUnJeu sans demande explicite de Vincent.
