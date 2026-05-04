# Prompt Claude for Chrome — Recherche emails Tier 1

> **Suite de** `claude_chrome_sourcing_secteur_01.md`. On a 7 prospects Tier 1
> dans `acquisition/prospects.csv`, sans email. On utilise Claude for Chrome
> pour les trouver (au lieu de Hunter.io ou similaire).
> **Sortie attendue** : 7 lignes CSV mises à jour avec la colonne `email`.

---

## Mode d'emploi

1. Reste connecté à LinkedIn et à Google sur Chrome.
2. Active Claude for Chrome.
3. Ouvre une nouvelle conversation.
4. Colle le bloc de prompt ci-dessous (du `# CONTEXTE` jusqu'à la fin).
5. Laisse-le tourner — il va visiter 7 sites d'entreprises, chercher les emails.
6. Récupère le CSV final, colle-le pour mettre à jour `prospects.csv`.

---

## Le prompt à coller (tout ce qui suit)

```
# CONTEXTE

Suite du sourcing batch 01 d'Atelier IA (Vincent Tariel, Nouméa).
Tu as déjà identifié 7 prospects Tier 1 (responsables com/marketing en
PME calédoniennes). Il manque leurs emails professionnels pour pouvoir
les contacter.

# LES 7 PROSPECTS À TRAITER

Pour chaque ligne ci-dessous : trouve son email pro.

1. Thi Mai Huong Julie Nguyen — Hyper U Païta — https://www.linkedin.com/in/thi-mai-huong-julie-nguyen-822997340/
2. Nina Néris — Groupe Cuenet — https://www.linkedin.com/in/ninaneris/
3. Marine Gachet — Quincaillerie Calédonienne — https://www.linkedin.com/in/marinehg/
4. Elise Millou — MDF (Mutuelle des Fonctionnaires de Nouvelle-Calédonie) — https://www.linkedin.com/in/elise-millou/
5. Laura Klotz — Grande Brasserie de Nouvelle-Calédonie (GBNC) — https://www.linkedin.com/in/laura-klotz-5ba8bb50/
6. Axelle Venard — Groupe Jeandot — https://www.linkedin.com/in/axelle-venard-094b50291/
7. Maurane Néris — Austral Import (Groupe SOL) — https://www.linkedin.com/in/maurane-n%C3%A9ris-66201b1b3/

# MÉTHODE — pour CHAQUE prospect, dans cet ordre

Étape A — Trouve le site officiel de l'entreprise.
  Recherche Google : "[nom entreprise] nouvelle calédonie"
  Identifie le domaine officiel (ex: hyperu.nc, gbnc.nc, etc.)

Étape B — Cherche l'email DIRECT du prospect.
  Visite ces pages dans cet ordre, jusqu'à trouver une adresse :
    1. Page "Contact" du site
    2. Page "Équipe" / "Notre équipe" / "Qui sommes-nous"
    3. Page "Mentions légales" (souvent un email général)
    4. Page "Communication" / "Presse" / "Service presse"
  Si tu trouves l'email DIRECT du prospect → c'est gagné, retourne-le.

Étape C — Si pas d'email direct, déduis le FORMAT du domaine.
  Cherche n'importe quel email pro de l'entreprise (autre personne
  citée). Identifie le format utilisé :
    - format A : prenom.nom@domaine.nc
    - format B : prenom-nom@domaine.nc
    - format C : pnom@domaine.nc (initiale + nom)
    - format D : prenom@domaine.nc
    - format E : nom@domaine.nc
    - autre : note exactement ce que tu observes

  Construis l'email probable du prospect avec ce format.
  Note dans la colonne "notes" : "Email déduit du format @domaine.nc
  observé sur la page X".

Étape D — Si tu ne trouves NI email direct NI format observé.
  Note dans la colonne email : "À CHERCHER MANUELLEMENT"
  Note dans la colonne notes : pourquoi (site sans email visible,
  refus de scraping, etc.) + suggère une action alternative pour
  Vincent (envoyer un message LinkedIn, appeler le standard, etc.)

# CAS PARTICULIERS À ANTICIPER

- Plusieurs noms composés (Thi Mai Huong Julie Nguyen, Maurane Néris) :
  privilégier le format COURT le plus probable (ex: julie.nguyen@,
  m.neris@) sauf si tu vois explicitement le format long utilisé.
- Accents dans les noms (Néris, Klotz) : tester sans accent en priorité
  (les emails français modernes acceptent l'accent mais beaucoup d'IT
  l'ont retiré pour compatibilité ASCII).
- Groupes avec plusieurs marques (Groupe Cuenet, Groupe Jeandot,
  Groupe SOL) : l'adresse peut être sur le domaine du groupe OU sur
  le domaine de la marque principale. Vérifier les deux.
- Brasseries / mutuelles / coopératives : le domaine est souvent
  identique au sigle ou à un raccourci (ex: gbnc.nc, mdf.nc).

# CE QUE TU NE DOIS PAS FAIRE

- Inventer un email plausible sans avoir vu AUCUN email pro de
  l'entreprise. (Sinon les bounces vont dégrader la réputation
  d'expéditeur de Vincent.)
- Fournir des emails @gmail.com ou @yahoo.com personnels (Vincent
  veut écrire à la fonction pro, pas à la personne perso).
- Sauter une étape pour aller plus vite (trouver le format est
  AUSSI utile que trouver l'email direct).

# QUALITÉ ATTENDUE

Pour chaque prospect, tu dois pouvoir CITER ta source :
  - "Email trouvé sur https://hyperu.nc/contact/"
  - "Email déduit du format jean.dupont@gbnc.nc observé sur la
     page mentions légales"
  - "Aucun format observé — site sans page contact public"

# FORMAT DE SORTIE

Retourne UNIQUEMENT un bloc CSV avec les 7 lignes mises à jour, mêmes
colonnes que prospects.csv (15 colonnes) :

prenom,nom,fonction,entreprise,secteur,email,telephone,linkedin,source,statut,date_premier_contact,date_dernier_contact,prochaine_action,notes

Attention :
  - colonne email : remplie avec l'adresse trouvée OU "À CHERCHER
    MANUELLEMENT" si introuvable
  - colonne notes : enrichie avec la SOURCE de l'email entre
    parenthèses, après l'accroche existante
    Exemple : "Hyper U Païta — centre commercial... (Email trouvé
              sur https://hyperu.nc/contact/)"
  - colonnes telephone, date_*, prochaine_action : INCHANGÉES par
    rapport à ce que je te donne

# DONNÉES SOURCE (à compléter)

Voici les 7 lignes existantes — tu enrichis la colonne email + notes
et tu me retournes le CSV complet :

Thi Mai Huong Julie,Nguyen,Responsable Marketing & Communication,Centre Commercial Hyper U Païta,Distribution / Grande surface,,,https://www.linkedin.com/in/thi-mai-huong-julie-nguyen-822997340/,LinkedIn search 2026-05-04,À contacter,,,Trouver email + envoyer cold-intro,"Hyper U Païta — centre commercial de proximité hors Nouméa, fort enjeu de communication locale et événementielle pour fidéliser la clientèle de la zone Païta-Dumbéa."
Nina,Néris,Responsable Communication et Marketing,Groupe Cuenet,Distribution / Multi-marques,,,https://www.linkedin.com/in/ninaneris/,LinkedIn search 2026-05-04,À contacter,,,Trouver email + envoyer cold-intro,"Groupe Cuenet — groupe familial calédonien multi-activités, com transversale sur plusieurs marques."
Marine,Gachet,Responsable communication marketing,Quincaillerie Calédonienne,BTP / Bricolage / Distribution spécialisée,,,https://www.linkedin.com/in/marinehg/,LinkedIn search 2026-05-04,À contacter,,,Trouver email + envoyer cold-intro,"Quincaillerie Calédonienne — enseigne historique du bricolage en NC, mix B2B (artisans) et B2C, gros catalogue produit à animer en com."
Elise,Millou,Responsable communication et culture mutualiste,MDF (Mutuelle des Fonctionnaires),Mutuelle / Assurance santé,,,https://www.linkedin.com/in/elise-millou/,LinkedIn search 2026-05-04,À contacter,,,Trouver email + envoyer cold-intro,"MDF : mutuelle dédiée aux agents publics de NC. Spécificité 'culture mutualiste' dans son intitulé de poste — angle pédagogie/sensibilisation des adhérents."
Laura,Klotz,Communication & Sustainability Lead,Grande Brasserie de Nouvelle-Calédonie (GBNC),Boissons / Brasserie,,,https://www.linkedin.com/in/laura-klotz-5ba8bb50/,LinkedIn search 2026-05-04,À contacter,,,Trouver email + envoyer cold-intro,"GBNC — brasseur historique de NC (Number One, Manta...), poste mixte com + RSE qui suggère une vraie maturité sur la transformation interne."
Axelle,Venard,Responsable communications,Groupe Jeandot,Distribution / Multi-enseignes,,,https://www.linkedin.com/in/axelle-venard-094b50291/,LinkedIn search 2026-05-04,À contacter,,,Trouver email + envoyer cold-intro,"Groupe Jeandot — groupe familial NC, com transverse multi-marques — angle 'gain de temps sur la production de contenus multi-enseignes'."
Maurane,Néris,Responsable communication,Austral Import (Groupe SOL),Import / Distribution,,,https://www.linkedin.com/in/maurane-n%C3%A9ris-66201b1b3/,LinkedIn search 2026-05-04,À contacter,,,Trouver email + envoyer cold-intro,"Groupe SOL — 5 marques différentes selon son intitulé (univers variés). Cas d'usage IA très net : décliner une com cohérente sur 5 identités."

# COMMENCE MAINTENANT

Démarre par le prospect numéro 1 (Hyper U Païta). Indique-moi à voix
haute (en chat) chaque action (recherche Google, page visitée, format
détecté) pour que je puisse suivre. Une fois les 7 traités, donne-moi
le CSV final.
```

---

## Après le retour de Claude for Chrome

1. Coller le CSV mis à jour dans `acquisition/prospects.csv` (remplacer les 7 premières lignes Tier 1).
2. Pour les éventuels `À CHERCHER MANUELLEMENT` → message LinkedIn court ou appel standard de l'entreprise.
3. Tu me redonnes le CSV final → je génère les 7 cold-emails personnalisés à partir du template.
