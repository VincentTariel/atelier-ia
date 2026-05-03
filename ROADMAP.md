# Roadmap — Atelier IA, du pivot aux 10 clients fondateurs

> Plan d'exécution post-structuration. À relire en début de chaque revue hebdo (`crm/revues/`) pour vérifier l'avancement.
> **Estimations** = temps Vincent en heures. À calibrer selon la disponibilité réelle (CommeUnJeu en parallèle).

---

## Phase 1 — Préparation produit (objectif : 2 semaines)

> **Objectif** : avoir un site, un PDF et un formulaire alignés sur le nouveau positionnement, avant d'envoyer le premier cold-email. Sans ça, la prospection brûle des contacts.

### 1.1 Refonte de la landing — copy + design

- **Action** : invoquer le skill `/frontend-design:frontend-design` sur `core/templates/core/landing.html` (et `base.html`).
- **Brief à donner au skill** :
  - Cible : pros calédoniens 35-55 ans, dirigeants TPE/PME, professions libérales (cabinet, immo, BTP, RH, com)
  - Positionnement : coaching 1-to-1 Claude Desktop, présentiel à Nouméa, "augmenter pas remplacer"
  - Sources de vérité : `CLAUDE.md` (sections 1.bis bio + 3 promesse + 7 règles), `offre/positionnement.md`, `offre/persona.md`, `offre/faq.md`, `offre/pricing.md`
  - Témoignages : **anonymisés par secteur uniquement** (pas de nom, pas de logo)
  - Hero : reformuler vers "Claude Desktop dans votre quotidien — sans coder"
  - CTA principal : "Réserver un entretien découverte gratuit"
  - CTA secondaire : "Télécharger le guide PDF" (lead-magnet)
  - Section "À propos" : version longue de la bio (CLAUDE.md §1.bis)
  - Tarifs : afficher "À partir de 50 000 XPF" + mention "10 clients fondateurs"
  - Esthétique : sobre, B2B, **pas startup-bro**, typo lisible, beaucoup de blanc, pas d'emojis
- **Estimation** : 2-4h de prompt + revue + ajustements
- **Sortie attendue** : `landing.html` redesignée + retouche `base.html` si besoin
- **Test** : `python manage.py runserver` → vérifier en local sur Chrome + Firefox + mobile

### 1.2 Mise à jour du formulaire Django

- **Fichier** : `core/forms.py` — modifier le dropdown `formation_interessee`
- **Nouveaux choix** (3 options simples) :
  1. *"Découvrir Claude Desktop pour mon métier"*
  2. *"J'ai un cas précis en tête"*
  3. *"Je veux juste recevoir le guide PDF"*
- **Migration Django** : pas besoin de migration sur le modèle (les choices sont stockés en string), mais relancer le serveur.
- **Estimation** : 30 min

### 1.3 Nouveau PDF lead-magnet

- **Suivre le brief** : `offre/lead_magnet/README.md` — *"10 façons d'utiliser Claude Desktop dans son quotidien de pro"*
- **Production** :
  - Rédaction : Vincent (avec brouillon Claude Desktop, finition manuelle)
  - Mise en page : à choisir (Canva = rapide, Affinity = mieux, LaTeX = si maîtrise)
  - Captures : sur compte démo Claude Desktop, en français, avec exemples NC quand pertinent
- **Livrable** : PDF placé dans `core/templates/pdf/Atelier_IA_Claude_Desktop.pdf`
- **Mise à jour Django** : modifier `core/views.py:landing_page_view` pour pointer vers le nouveau fichier + reformuler subject + body de l'email
- **Estimation** : 6-8h sur 2-3 jours
- **Bloquant pour** : capture d'inbound (le PDF actuel est aligné sur l'ancien positionnement, ne pas l'envoyer aux nouveaux leads)

### 1.4 Sécurisation Django prod (rapide)

- `atelier_ia/settings.py` :
  - Passer `DEBUG = False` (avec gestion via variable d'env `DEBUG=True` en local)
  - Externaliser `SECRET_KEY` en variable d'env (lire via `os.environ.get`)
  - Nettoyer `ALLOWED_HOSTS` (retirer le `"https://atelier-ia.ovh"` qui est un schéma URL invalide)
- Créer un `.env.example` (committé) et un `.env` local (gitignored) avec les variables sensibles
- Tester en local avec DEBUG False (`python manage.py collectstatic` peut être nécessaire)
- **Estimation** : 1h
- **Bloquant pour** : déploiement sécurisé (à faire avant d'envoyer du trafic)

### 1.5 Vérifier l'envoi email Gmail SMTP

- Tester depuis le formulaire local que l'email part bien avec le NOUVEAU PDF attaché
- Vérifier que l'objet et le corps sont à jour
- Si le compte expéditeur (`commeunjeu.ad@gmail.com` aujourd'hui) doit être changé pour `tariel.vincent@gmail.com` → mettre à jour les settings + générer un app password Gmail
- **Estimation** : 30 min

### 1.6 Déploiement de la nouvelle version

- Push git → déploiement sur `atelier-ia.ovh`
- Tester en prod : remplir le formulaire avec un email à toi, vérifier réception
- **Estimation** : 30-60 min selon la chaîne de déploiement (à documenter dans `CLAUDE.md` après ce premier déploiement)

**🟢 Fin Phase 1** : site présentable, PDF aligné, formulaire qui marche. **Prêt à envoyer du trafic.**

---

## Phase 2 — Lancement acquisition (objectif : 1 mois)

> **Objectif** : 30 prospects sourcés, 30 cold-emails envoyés, 5-8 RDV calés.

### 2.1 Choisir le premier secteur cible

- **Critère** : un secteur où tu as un angle (relation existante, connaissance fine du métier, ou volume de production écrite évident)
- **Suggestions par ordre de fit** : expertise comptable → cabinets juridiques → conseil indépendant → immobilier
- **Décision Vincent** : un seul secteur pour la première vague — itérer après les premiers retours
- **Estimation** : 30 min de réflexion

### 2.2 Sourcer 30 prospects

- **Sources** : voir `acquisition/sources.md` (annuaire CCI, ordres professionnels, LinkedIn)
- **Méthode** : pour chaque prospect, trouver le **dirigeant nominatif** + son email direct (pas `contact@`)
- **Outils** : Hunter.io / Snov.io en complément si besoin de retrouver un email
- **Saisie** : remplir `acquisition/prospects.csv` avec statut `À contacter`
- **Estimation** : 4-6h sur 2-3 jours
- **Bloquant pour** : 2.3

### 2.3 Préparer le batch d'envoi

- Pour chaque prospect, écrire l'**accroche personnalisée** (1 phrase qui prouve les 30s passées sur leur entreprise/site)
- Utiliser le template `acquisition/email_templates/01_cold_intro.md` comme base
- Stocker le batch dans `acquisition/sends/AAAA-MM-JJ_batch_01.md` (gitignored)
- **Estimation** : 2-3h pour 30 prospects (4-6 min par prospect)

### 2.4 Envoi du batch 1

- **Cadence** : 10/jour max sur 3 jours
- **Heure** : mardi-jeudi, 8h-9h ou 17h-18h NC
- **Tracking** : Mailtrack ou équivalent pour mesurer les ouvertures
- **Mise à jour CRM** : passer chaque prospect en `Contacté` dans `prospects.csv` + créer une fiche `crm/leads/{nom}.md` pour chaque
- **Estimation** : 1h30 cumulé (envoi + suivi)

### 2.5 Relances

- **J+7** : template `02_relance_J7.md` → en réponse au premier mail
- **J+21** : template `03_relance_J21.md` → dernière tentative
- **Estimation** : 2h cumulé

### 2.6 Premiers RDV découverte

- **Dès le premier "oui"** : caler le RDV dans la semaine suivante
- **Préparation** : suivre la trame `acquisition/call_scripts/decouverte.md`
- **Format** : présentiel à Nouméa de préférence, visio en repli
- **Post-RDV** : mettre à jour `crm/leads/{nom}.md` + `crm/pipeline.md` + envoyer email post-RDV (`04_post_rdv.md`) sous 24h
- **Estimation** : ~1h30 par RDV (préparation + entretien + suivi)

**🟢 Fin Phase 2** : 5-8 RDV tenus, 2-4 propositions envoyées.

---

## Phase 3 — Conversion et premiers clients fondateurs (objectif : 2 mois après Phase 2)

> **Objectif** : signer les 10 clients fondateurs et délivrer leurs sessions.

### 3.1 Propositions et signatures

- **Sous 24h après chaque RDV** : envoyer la proposition PDF personnalisée (gabarit à créer après le premier RDV)
- **Suivi** : relance J+5 puis J+15 si pas de réponse
- **Signature** : devis signé + acompte 30 % reçu = bascule en `Signé`
- **Création dossier client** : `crm/clients/{nom-entreprise}/` à partir du gabarit

### 3.2 Délivrance des sessions Coaching Découverte

- **Avant la session** : échange email de pré-qualif (~30 min cumulées)
- **Pendant** : 2h sur place, 1 Project Claude Desktop construit en direct, PDF remis en main propre
- **Après** : compte-rendu de session dans `crm/clients/{nom}/sessions/`, email de suivi à J+15
- **Demande de retour d'expérience anonyme** à J+30 — **format secteur seulement, pas de nom**

### 3.3 Conversion vers Suivi mensuel

- À la fin de la première session, **identifier un deuxième cas d'usage** que tu pourrais traiter en suivi
- Proposer le passage en Suivi mensuel à 40 000 XPF/mois (3 mois min) à J+15 ou J+30
- Cible : 3-5 conversions sur les 10 fondateurs

### 3.4 Collecte des témoignages anonymes

- À J+30 de chaque coaching, demander un retour d'expérience par email
- Format imposé : *"Secteur + lieu : bénéfice constaté en chiffres si possible"*
- Stocker dans `offre/temoignages.md` (à créer)
- Intégrer 3-5 témoignages dans la landing dès qu'ils sont prêts

**🟢 Fin Phase 3** : 10 clients fondateurs signés, ~3 en suivi mensuel, 5+ témoignages anonymes activables.

---

## Phase 4 — Optimisation et passage au régime de croisière (après les 10 fondateurs)

### 4.1 Bascule du tarif Fondateurs → Démarrage

- Communication publique sur le site : retirer la mention "tarif fondateurs"
- Mise à jour `offre/pricing.md` : passer le tarif principal à 100 000 XPF
- Annoncer en cold-email : *"Les 10 places fondateurs sont prises — voici le tarif standard"*

### 4.2 Production de la vidéo explicative

- **À démarrer après** : avoir 2-3 témoignages anonymes pour nourrir le storyboard
- Suivre `video/script.md`, `video/storyboard.md`, `video/shot_list.md`
- Tournage en 1 demi-journée, montage en 1 jour
- Diffusion : intégrer en tête de landing + LinkedIn + signature email
- **Estimation** : 2-3 jours cumulés

### 4.3 Révision pricing

- **Indicateurs à examiner** :
  - Taux de conversion RDV → signature : si > 70 %, tarif sous-évalué
  - Objections sur le prix : si > 50 % des prospects, tarif au plafond
  - Ratio temps passé / CA : si < 20 000 XPF/h en moyenne, monter
- **Action possible** : passer Démarrage à 120-150K si tous les signaux verts

### 4.4 Affiner le persona

- Identifier les 2 secteurs qui convertissent le mieux → concentrer les futurs cold-emails dessus
- Identifier les secteurs où ça ne prend pas → arrêter de les contacter
- Mettre à jour `offre/persona.md`

### 4.5 PDF lead-magnet v2

- Si le v1 a généré beaucoup de leads → garder
- Sinon → version sectorielle (un PDF par secteur prioritaire)

### 4.6 Décision stratégique : continuer le coaching ou réduire ?

- À ce stade, tu auras la donnée pour décider :
  - **Si rentable et plaisant** : monter en gamme (formation à plusieurs collaborateurs d'un même client, journée d'intervention)
  - **Si rentable mais accaparant** : limiter à 4-5 clients/mois en simultané, garder du temps pour CommeUnJeu
  - **Si pas rentable** : pivoter vers un autre angle ou arrêter

---

## Décisions Vincent à prendre (en parallèle, n'attendent pas la roadmap)

- [ ] **Statut TVA NC** : confirmer le régime fiscal applicable (voir `Administratif/Admin_Demarrage_EI_NC.md`)
- [ ] **Compte bancaire pro** : si pas déjà fait
- [ ] **Outil de signature électronique** : DocuSign, Yousign, ou simple PDF + retour signé scanné ?
- [ ] **Outil de facturation** : Henrri (gratuit), Tiime, ou export Django ?
- [ ] **Compte Anthropic Pro** sur lequel faire tourner les démos clients (séparé de l'usage perso)
- [ ] **Numéro de téléphone pro** : utiliser le perso ou prendre une ligne pro ?
- [ ] **GEMINI.md** : à archiver dans `Administratif/` ou supprimer ? (Devenu obsolète, supplanté par `CLAUDE.md`)

---

## Ordre d'attaque recommandé

**Cette semaine** :
1. Lancer le redesign landing (1.1) — c'est le bloquant principal
2. Pendant ce temps, attaquer le PDF (1.3) en parallèle (rédaction tu peux le faire offline)

**Semaine prochaine** :
3. Sécurité Django (1.4) + form (1.2) + email (1.5)
4. Déploiement (1.6)
5. Démarrer le sourcing (2.1, 2.2)

**Dans 2 semaines** :
6. Premier batch cold-emails (2.3, 2.4)

**Dans 1 mois** :
7. Premiers RDV → premières signatures

**Dans 2-3 mois** :
8. 10 fondateurs signés → bascule régime + vidéo

---

## Hypothèses et risques

- **Hypothèse forte** : un dirigeant calédonien curieux est joignable par cold-email avec une bonne accroche personnalisée. À vérifier sur le batch 1 (taux de réponse cible > 5 %).
- **Risque 1** : sourcing plus lent que prévu (annuaires NC moins denses qu'en métropole). Mitigation : LinkedIn + recommandations + événements CCI.
- **Risque 2** : conversion RDV → signature plus faible que prévue. Mitigation : itérer la trame découverte après les 3 premiers RDV ratés.
- **Risque 3** : Vincent débordé entre CommeUnJeu et le coaching. Mitigation : plafonner à 4 nouveaux clients/mois et 5 RDV/semaine.
- **Risque 4** : un fondateur partage le tarif 50K → grogne du client #11. Mitigation : la communication "10 fondateurs, contrepartie retour d'expérience" assumée publiquement.
