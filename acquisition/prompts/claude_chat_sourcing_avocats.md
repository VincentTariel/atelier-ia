# Prompt Claude.ai (chat web avec recherche web) — Sourcing avocats Nouméa

> **Outil** : Claude.ai dans un onglet navigateur, avec la **recherche web activée**
> (icône globe en bas du champ de saisie).
> **Avantage** : Claude peut chercher l'annuaire de l'Ordre + visiter les sites
> de cabinets via les résultats Google → récupération directe des emails publics.
> **Limite** : ne peut pas accéder à LinkedIn (interdit aux crawlers IA).
> **Complément** : utiliser ensuite `claude_chrome_linkedin_avocats.md` pour les profils LI.

---

## Mode d'emploi

1. Ouvrir un onglet sur https://claude.ai
2. **Activer la recherche web** (icône globe à côté du champ de saisie).
3. Coller le prompt ci-dessous (du `# CONTEXTE` à la fin).
4. Laisser Claude tourner. Le suivre.
5. Récupérer le CSV final.

---

## Le prompt à coller (tout ce qui suit)

```
# CONTEXTE

Je m'appelle Vincent Tariel, solopreneur à Nouméa (Nouvelle-Calédonie).
Je lance Atelier IA — du coaching individuel sur Claude Desktop, en
présentiel à Nouméa, pour intégrer l'IA dans le quotidien des
professionnels qui produisent beaucoup d'écrit.

Pour mon premier batch outbound, je cible les avocats à Nouméa.
Mon PDF de présentation contient l'histoire de "Maître Adam", avocat
généraliste à Nouméa qui utilise Claude Desktop pour rédiger
attestations, courriers et inventaires de pièces.

J'ai besoin que tu me sources 15 avocats inscrits à Nouméa, avec
leur email professionnel direct (publié sur leur site cabinet).

Tu as accès à la recherche web — utilise-la systématiquement.

# PROFIL CIBLE

À RETENIR :
- Avocat·e inscrit·e au barreau de Nouvelle-Calédonie
- Cabinet basé à Nouméa (centre-ville ou Grand Nouméa)
- Cabinet solo OU petite structure (1 à 5 avocats associés)
- Spécialités à privilégier (forte production écrite) :
    * Droit civil général
    * Droit de la famille / divorces
    * Baux commerciaux / immobilier
    * Droit des sociétés / conseil aux entreprises
    * Droit du travail
    * Droit administratif

À ÉVITER :
- Pénalistes purs (volume rédactionnel moindre)
- Très grosses structures internationales (cabinets >5 avocats)
- Notaires (autre profession)
- Conseils juridiques in-house (on cible les libéraux)
- Retraités / mention "honoraire"

# CE QUE TU DOIS FAIRE — recherches web à effectuer

Étape 1 — Annuaire de l'Ordre
  Recherche : "Ordre des avocats Nouvelle-Calédonie annuaire"
  Identifie le site officiel du barreau (probablement
  barreau-noumea.nc ou similaire) et l'URL d'accès à l'annuaire.
  Liste les noms des avocats inscrits avec coordonnées de cabinet.

Étape 2 — Recherches Google ciblées par spécialité
  Lance ces requêtes successivement :
    - "avocat Nouméa droit civil"
    - "avocat Nouméa droit de la famille"
    - "cabinet avocat Nouméa baux commerciaux"
    - "avocat Nouméa droit des sociétés"
    - "site:.nc avocat cabinet"
  Note pour chaque résultat pertinent : nom de l'avocat·e,
  cabinet, URL du site cabinet.

Étape 3 — Pour chaque candidat retenu, visite le site web du cabinet
  Récupère :
    - L'email DIRECT de l'avocat·e si publié (préférer
      prenom@cabinet.nc à cabinet@cabinet.nc)
    - À défaut, l'email général du cabinet
    - Le téléphone du cabinet
    - L'URL de la page de présentation de l'avocat (si elle existe)

Étape 4 — Note dans la colonne "notes" :
  - La spécialité principale annoncée
  - Une accroche personnalisée d'1 phrase basée sur ce que tu as vu
    sur le site : ancienneté du cabinet, type de clientèle, mention
    récente, particularité (cabinet bilingue, spécialiste droit
    minier NC, etc.)
  - Exemple BON : "Cabinet généraliste à Nouméa centre depuis 2010,
                   accent fort sur le droit de la famille et les
                   successions, accueil bilingue."
  - Exemple INUTILE : "Avocat à Nouméa."

# CAS PARTICULIERS

- Si un cabinet a 2-5 associés, retiens UN avocat (l'associé principal
  ou celui dont la spécialité matche le mieux notre cible).
- Si tu trouves un site sans email visible, note-le quand même avec
  email = "À CHERCHER MANUELLEMENT" + un commentaire dans notes.
- Vérifie systématiquement que l'avocat exerce ACTUELLEMENT à Nouméa
  (pas une mention historique) — la date du dernier post / actu est
  un bon indicateur.

# CE QUE TU NE DOIS PAS FAIRE

- Inventer un email plausible non vérifié.
- Inclure un avocat dont tu n'as pas vu confirmation qu'il exerce
  actuellement à Nouméa.
- Inclure des notaires.
- Donner une accroche générique du type "spécialiste en droit".

# FORMAT DE SORTIE

Quand tu as fini (15 prospects validés OU épuisé tes recherches),
retourne UNIQUEMENT un bloc CSV avec ces 15 colonnes (mêmes que
prospects.csv) :

prenom,nom,fonction,entreprise,secteur,email,telephone,linkedin,source,statut,date_premier_contact,date_dernier_contact,prochaine_action,notes

Pour chaque ligne :
  - prenom : prénom seul (sans "Maître")
  - nom : nom de famille
  - fonction : "Avocat" ou "Avocate" (ou "Avocat associé·e")
  - entreprise : nom complet du cabinet
  - secteur : "Avocat - [spécialité]" (ex: "Avocat - Droit de la famille")
  - email : adresse trouvée sur le site OU "À CHERCHER MANUELLEMENT"
  - telephone : numéro standard du cabinet
  - linkedin : vide (sera ajouté par l'autre source)
  - source : "Claude.ai web search 2026-05-04"
  - statut : "À contacter"
  - date_premier_contact : vide
  - date_dernier_contact : vide
  - prochaine_action : "Envoyer cold-intro avocat"
  - notes : accroche personnalisée (étape 4) entre guillemets droits

Exemple de ligne :

Marie,Dupont,Avocate,Cabinet Dupont,Avocat - Droit de la famille,marie.dupont@cabinet-dupont.nc,+687 27 XX XX,,Claude.ai web search 2026-05-04,À contacter,,,Envoyer cold-intro avocat,"Cabinet généraliste à Nouméa centre depuis 2010, fort en divorces et successions."

# QUALITÉ AVANT QUANTITÉ

Si tu ne peux fournir que 8-10 avocats vraiment qualifiés au lieu de 15
médiocres, c'est mieux. 10 bons leads valent mieux que 15 mauvais.

# COMMENCE MAINTENANT

Lance la recherche "Ordre des avocats Nouvelle-Calédonie annuaire" et
indique-moi en chat ce que tu trouves. Ensuite procède étape par étape.
```

---

## Après le retour

1. Coller le CSV à la suite des lignes existantes dans `acquisition/prospects.csv`.
2. Pour les `À CHERCHER MANUELLEMENT` : aller voir manuellement le site cabinet.
3. **Vérifier que ton avocat divorce n'est PAS dans la liste** (le retirer si oui).
4. Lancer ensuite `claude_chrome_linkedin_avocats.md` pour compléter avec les profils LinkedIn (URL profil + spécialités complémentaires éventuelles).
