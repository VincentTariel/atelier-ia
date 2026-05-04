# Prompt Claude for Chrome — Sourcing avocats LinkedIn

> **Outil** : Claude for Chrome (extension navigateur), connecté à LinkedIn.
> **Avantage** : trouve les profils LinkedIn (signal d'activité numérique du
> prospect → plus susceptible d'ouvrir un cold-email mentionnant l'IA).
> **Limite** : LinkedIn ne montre pas les emails → utilisé en COMPLÉMENT du
> sourcing Claude.ai (qui récupère les emails publics des sites cabinet).

---

## Mode d'emploi

1. Sur Chrome, **se connecter à LinkedIn** d'abord.
2. Activer Claude for Chrome.
3. Ouvrir une nouvelle conversation.
4. Coller le prompt ci-dessous.
5. Laisser tourner. Surveiller pour valider les choix.
6. Récupérer le CSV final.

---

## Le prompt à coller (tout ce qui suit)

```
# CONTEXTE

Je m'appelle Vincent Tariel, solopreneur à Nouméa (Nouvelle-Calédonie).
Je lance Atelier IA — coaching individuel sur Claude Desktop, en
présentiel à Nouméa.

Mon premier batch outbound cible les avocats à Nouméa. J'ai déjà lancé
une recherche via Claude.ai (web search) qui m'a sorti une liste basée
sur l'annuaire de l'Ordre + les sites cabinets.

Maintenant j'ai besoin de toi pour le complément : sourcer les profils
sur LinkedIn — pour avoir le signal "actif numérique" et les URL profil
LinkedIn des prospects (à utiliser plus tard si besoin de relance via LI).

# PROFIL CIBLE

À RETENIR :
- Avocat·e inscrit·e au barreau de Nouvelle-Calédonie
- Poste ACTUEL en cabinet libéral à Nouméa (cabinet solo ou 1-5 associés)
- Spécialités à privilégier (forte production écrite) :
    * Droit civil, famille, baux, sociétés, travail, administratif
- Idéalement actif sur LinkedIn (a posté ou commenté dans les 6 derniers mois)

À ÉVITER :
- Pénalistes purs (volume rédactionnel moindre)
- Très grosses structures (>5 avocats)
- Notaires
- Conseils juridiques in-house
- Profils anciens / inactifs LinkedIn (>1 an sans activité)

# CE QUE TU DOIS FAIRE

Étape 1 — Recherche LinkedIn
  Ouvre LinkedIn (https://www.linkedin.com/), onglet "Personnes",
  filtres :
    - Lieu : "Nouvelle-Calédonie"
    - Mots-clés à essayer successivement :
        a) "avocat" OR "avocate"
        b) "avocat associé" OR "avocate associée"
        c) "avocat droit"
  Garde les résultats correspondant à des cabinets libéraux à Nouméa.

Étape 2 — Pour chaque résultat pertinent, ouvre le profil et vérifie :

  ✓ Le poste ACTUEL est bien "avocat·e" en cabinet libéral à Nouméa
    (vérifie l'employeur ACTUEL, pas l'historique)
  ✓ La taille du cabinet est ≤ 5 avocats (regarde la page entreprise
    LinkedIn du cabinet si dispo, ou déduis du site cabinet)
  ✓ La personne est ACTIVE (post ou commentaire dans les 6 derniers mois)

Étape 3 — Pour chaque profil retenu, extrais :
  - prenom
  - nom
  - fonction (intitulé exact, ex: "Avocate associée")
  - entreprise (cabinet)
  - spécialité visible dans le profil (headline ou poste)
  - URL du profil LinkedIn
  - Une observation utile pour l'accroche (post récent intéressant,
    formation continue mentionnée, engagement local, etc.)

# CAS PARTICULIERS

- Si LinkedIn te bloque (rate limit), arrête-toi proprement avec ce
  que tu as et signale-le.
- Si un avocat apparaît dans plusieurs cabinets sur son profil, retiens
  l'employeur ACTUEL (le plus récent).
- Vincent a un avocat (divorce). Comme tu ne sais pas qui c'est, je
  vérifierai après et l'écarterai si nécessaire.

# CE QUE TU NE DOIS PAS FAIRE

- Inventer des informations.
- Inclure des profils dont l'employeur actuel est en métropole.
- Demander d'extraire l'email LinkedIn (LinkedIn ne le montre pas
  publiquement, ce sera l'autre source qui le fournira).

# FORMAT DE SORTIE

Retourne UNIQUEMENT un bloc CSV avec ces 15 colonnes (mêmes que
prospects.csv) :

prenom,nom,fonction,entreprise,secteur,email,telephone,linkedin,source,statut,date_premier_contact,date_dernier_contact,prochaine_action,notes

Pour chaque ligne :
  - prenom : prénom seul
  - nom : nom de famille
  - fonction : intitulé exact LinkedIn
  - entreprise : nom du cabinet
  - secteur : "Avocat - [spécialité]" si visible, sinon "Avocat - Généraliste"
  - email : laisser VIDE (sera complété par la source Claude.ai)
  - telephone : laisser VIDE
  - linkedin : URL complète du profil
  - source : "LinkedIn search 2026-05-04"
  - statut : "À contacter"
  - date_premier_contact : vide
  - date_dernier_contact : vide
  - prochaine_action : "Trouver email + envoyer cold-intro avocat"
  - notes : observation utile pour accroche personnalisée

Exemple de ligne :

Marie,Dupont,Avocate associée,Cabinet Dupont & Associés,Avocat - Droit de la famille,,,https://www.linkedin.com/in/marie-dupont-12345/,LinkedIn search 2026-05-04,À contacter,,,Trouver email + envoyer cold-intro avocat,"Profil très actif, post récent sur les nouvelles dispositions divorce 2026, semble engagée pédagogie."

# QUALITÉ AVANT QUANTITÉ

10 avocats vraiment actifs et qualifiés > 20 profils dormants.

# COMMENCE MAINTENANT

Lance la recherche LinkedIn (étape 1, requête "avocat" + lieu
Nouvelle-Calédonie) et indique-moi en chat les premiers résultats
pour validation avant de continuer.
```

---

## Après le retour des deux sources

1. Tu as deux CSV — un de Claude.ai (avec emails), un de Claude for Chrome (avec LinkedIn URLs).
2. **Dédoublonne par nom** : si Marie Dupont apparaît dans les deux, fusionner en une seule ligne (email de l'un + LinkedIn de l'autre).
3. Pour les profils présents UNIQUEMENT dans la source LinkedIn (sans email) : aller chercher manuellement l'email sur le site du cabinet.
4. Coller le CSV fusionné dans `acquisition/prospects.csv`.
5. Vérifier que ton avocat divorce n'apparaît pas.
6. Me redonner le CSV final → je génère les 15 cold-emails personnalisés adaptés au ton avocat (objet "Maître X, une question sur la rédaction au cabinet", renvoi explicite au PDF Maître Adam).
