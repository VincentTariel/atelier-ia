# Prompt Claude for Chrome — Sourcing batch 01

> **Cible** : 30 responsables com/marketing en PME calédoniennes (cf. `acquisition/strategie_secteur_01.md`).
> **Outil** : Claude for Chrome (extension navigateur Anthropic — peut naviguer LinkedIn, lire les profils, extraire des données).
> **Sortie attendue** : 30 lignes CSV prêtes à coller dans `acquisition/prospects.csv`.

---

## Mode d'emploi

1. Sur Chrome, **se connecter à LinkedIn d'abord** avec ton compte personnel (sinon Claude verra une page de login, pas les profils).
2. Activer Claude for Chrome (icône extension).
3. Ouvrir une nouvelle conversation.
4. Coller le prompt ci-dessous (tout le bloc, du `# CONTEXTE` jusqu'à la fin).
5. Laisser Claude tourner. Surveiller pour valider les choix.
6. À la fin, copier le bloc CSV dans `acquisition/prospects.csv`.

---

## Le prompt à coller (tout ce qui suit)

```
# CONTEXTE

Je m'appelle Vincent Tariel. Je suis solopreneur à Nouméa
(Nouvelle-Calédonie) et je lance Atelier IA — un coaching individuel
en présentiel pour intégrer Claude Desktop dans le quotidien
professionnel des dirigeants et cadres calédoniens.

Voir mon site : https://atelier-ia.ovh

Je dois sourcer 30 prospects pour un premier batch outbound.

# PROFIL CIBLE EXACT

- Fonction : responsable communication, directeur·trice marketing,
  chargé·e de communication, marketing manager, community manager,
  responsable marketing & communication.
- Lieu de travail : Nouvelle-Calédonie (idéalement Nouméa, Dumbéa,
  Mont-Dore, Païta).
- Taille entreprise : entre 11 et 100 salariés (sweet spot 20-50).
- Type d'entreprise : PME calédoniennes — peu importe le secteur
  d'activité (banque, assurance, mutuelle, distribution, BTP,
  hôtellerie, association, industrie, etc.).

# À EXCLURE (important)

- Agences de communication ou agences digitales (concurrents indirects).
- Communicants freelance / indépendants solo.
- Très grandes structures (Carsud, OPT, Enercal, banques majeures à
  +200 salariés) — leur cycle de décision est trop long pour un solo.
- Profils basés en métropole avec mention "Nouvelle-Calédonie" dans
  l'historique uniquement (vérifier le poste ACTUEL).

# CE QUE TU DOIS FAIRE

Étape 1 — Ouvre LinkedIn (https://www.linkedin.com/) et lance la
recherche suivante :

  Onglet : "Personnes"
  Filtres :
    - Lieu : "Nouvelle-Calédonie"
    - Mots-clés (champ recherche principal) : essaie successivement
      les requêtes suivantes et garde les résultats pertinents :
        a) "responsable communication"
        b) "directrice communication" OR "directeur communication"
        c) "chargée de communication" OR "chargé de communication"
        d) "marketing manager"
        e) "responsable marketing"

Étape 2 — Pour chaque résultat pertinent, clique sur son profil
LinkedIn et vérifie ces 3 critères :

  ✓ Le poste ACTUEL est bien dans une PME calédonienne (pas en
    métropole, pas dans un grand groupe, pas en agence de com).
  ✓ La taille de l'entreprise est 11-200 (idéalement 20-50).
  ✓ La personne est ACTIVE sur LinkedIn (a posté ou commenté dans
    les 6 derniers mois — sinon elle n'ouvrira pas un cold-email).

Étape 3 — Pour chaque profil retenu, extrait ces informations :

  - prenom (Prénom seul)
  - nom (Nom de famille)
  - fonction (intitulé exact du poste actuel)
  - entreprise (nom légal de l'entreprise)
  - secteur (secteur d'activité de l'entreprise — banque, BTP, etc.)
  - linkedin (URL complète du profil LinkedIn)

Étape 4 — Pour CHAQUE prospect, regarde aussi le site web de son
entreprise (cherche dans Google "nom entreprise nouvelle calédonie").
Note dans la colonne "notes" UN détail spécifique à l'entreprise :
une actualité récente, un produit phare, un slogan, une particularité
locale, etc. Ce détail servira d'accroche personnalisée pour le
cold-email.

  Exemple de note utile : "Vient de lancer une nouvelle gamme bio en
                          mars 2026, fort engagement local."
  Exemple INUTILE : "Entreprise dans la distribution."

Étape 5 — Continue jusqu'à avoir 30 prospects valides. Si LinkedIn
te bloque (rate limit), passe à l'étape suivante avec ce que tu as.

# QUALITÉ AVANT QUANTITÉ

Si tu ne peux fournir que 15 prospects vraiment qualifiés au lieu de
30 médiocres, c'est mieux. Vincent envoie 10 emails par jour, donc
15 bons leads valent mieux que 30 mauvais.

# CE QUE TU NE DOIS PAS FAIRE

- Inventer des informations (si tu ne trouves pas la fonction exacte,
  laisse vide plutôt que d'inventer).
- Tenter de récupérer leur adresse email — c'est l'étape suivante
  (Vincent utilisera Hunter.io ou le site de l'entreprise).
- Inclure des profils dont le poste est en région parisienne ou
  ailleurs hors NC.
- Ajouter ton commentaire ou tes émojis dans le CSV final.

# FORMAT DE SORTIE

Quand tu as fini, retourne UNIQUEMENT un bloc CSV avec ces colonnes
exactes (séparateur virgule, valeurs entre guillemets si elles
contiennent une virgule) :

prenom,nom,fonction,entreprise,secteur,email,telephone,linkedin,source,statut,date_premier_contact,date_dernier_contact,prochaine_action,notes

Pour chaque ligne :
  - email : laisser vide ("" ou rien)
  - telephone : laisser vide
  - source : "LinkedIn search 2026-MM-JJ"
  - statut : "À contacter"
  - date_premier_contact : laisser vide
  - date_dernier_contact : laisser vide
  - prochaine_action : "Trouver email + envoyer cold-intro"
  - notes : la phrase d'accroche personnalisée (étape 4)

Exemple de ligne attendue :

Marie,Dupont,Responsable Communication,SOPACFA,Distribution alimentaire,,,https://www.linkedin.com/in/marie-dupont-12345/,LinkedIn search 2026-05-04,À contacter,,,Trouver email + envoyer cold-intro,"Vient de lancer une nouvelle gamme bio en mars 2026, fort engagement local."

# COMMENCE MAINTENANT

Ouvre LinkedIn et commence l'étape 1.
```

---

## Après que Claude a fini

1. Vérifier rapidement les 30 lignes (cohérence : noms français/calédoniens, vraies entreprises NC, pas de doublon, profils LinkedIn cliquables).
2. Coller dans `acquisition/prospects.csv` à la suite du header existant.
3. Pour chaque ligne, **trouver l'email** :
   - Méthode A : Hunter.io extension Chrome (free 25/mois) → copie automatique du format `prenom.nom@domaine.nc`
   - Méthode B : aller sur le site de l'entreprise → page contact / équipe
   - Méthode C : si rien, demander via LinkedIn (message direct sobre)
4. Mettre à jour la colonne `email` au fur et à mesure dans `prospects.csv`.

## Si Claude for Chrome bute sur LinkedIn

LinkedIn détecte parfois les automatisations et bloque. Dans ce cas :

- Faire la recherche LinkedIn manuellement (toi, dans ton navigateur).
- Pour chaque profil ouvert, cliquer sur l'extension Claude et lui demander :
  > *"Extrais les infos de ce profil au format CSV (colonnes ci-dessous), et propose UNE phrase d'accroche personnalisée basée sur le profil et le site de l'entreprise."*
- Coller son retour dans le CSV.

C'est plus lent (≈ 5 min par lead × 30 = 2h30) mais plus fiable.
