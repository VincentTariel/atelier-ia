# Prompt Claude for Chrome — Sourcing avocats à Nouméa

> **Cible** : 15 avocats à Nouméa avec emails publics (cf. `acquisition/strategies/avocats.md`).
> **Sortie attendue** : 15 lignes CSV prêtes à coller dans `acquisition/prospects.csv`.
> **Avantage vs sourcing com/marketing** : les emails d'avocats sont quasi
> toujours publics (sites de cabinet) → étape "trouver l'email" intégrée
> dans ce sourcing, plus besoin d'un second prompt.

---

## Le prompt à coller (tout ce qui suit)

```
# CONTEXTE

Je m'appelle Vincent Tariel, solopreneur à Nouméa. Je propose Atelier IA :
du coaching individuel sur Claude Desktop, en présentiel à Nouméa, pour
intégrer l'IA dans le quotidien des professionnels qui produisent
beaucoup d'écrit.

Pour mon premier batch outbound, je cible les avocats à Nouméa.
Mon PDF de présentation contient l'histoire de "Maître Adam", avocat
généraliste à Nouméa qui utilise Claude Desktop pour rédiger
attestations, courriers et inventaires de pièces — donc le prospect
avocat reconnaît immédiatement son métier en lisant le guide.

Je dois sourcer 15 avocats inscrits à Nouméa, avec leur email
professionnel direct.

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
- Pénalistes purs (volume rédactionnel moindre que civilistes)
- Très grosses structures internationales (Cabinet Calédonia, etc. si >5 avocats)
- Notaires (autre profession, autre stratégie)
- Conseils juridiques en entreprise (in-house) — on cible les libéraux
- Retraités / mentions "honoraire" sur leur intitulé

# SOURCES À UTILISER (par ordre de priorité)

1. **Annuaire officiel du barreau de Nouvelle-Calédonie**
   Cherche : "Ordre des avocats Nouvelle-Calédonie annuaire" sur Google.
   URL probable : https://www.barreau-noumea.nc/ ou variante.
   Cet annuaire liste tous les inscrits avec coordonnées du cabinet.

2. **Recherche Google par spécialité**
   Requêtes utiles :
     - `avocat Nouméa droit civil`
     - `avocat Nouméa droit de la famille`
     - `cabinet avocat Nouméa baux commerciaux`
     - `avocat Nouméa droit des sociétés`
     - `site:.nc avocat cabinet`

3. **LinkedIn (en complément)**
   Recherche : Lieu = Nouvelle-Calédonie, Fonction = "avocat" OR "avocate"
   Filtrer sur cabinets libéraux (pas conseil en entreprise).

# CE QUE TU DOIS FAIRE — POUR CHAQUE AVOCAT

Étape 1 — Identifie le nom complet, le cabinet, et la spécialité principale.

Étape 2 — Visite le site web du cabinet (souvent via Google) et récupère :
  - L'email DIRECT de l'avocat·e (préférer prenom@cabinet.nc à cabinet@cabinet.nc)
  - Si pas d'email individuel, l'email général du cabinet (cabinet@xxx.nc)
  - Le numéro de téléphone du cabinet
  - L'URL du site cabinet ou de la page profil

Étape 3 — Note dans la colonne "notes" :
  - La spécialité principale
  - Une accroche personnalisée (1 phrase) basée sur ce que tu as vu sur le
    site : type de clientèle, ancienneté du cabinet, mention récente dans la
    presse, particularité (ex: cabinet bilingue français/anglais, spécialiste
    droit minier NC, etc.).
  - Exemple BON : "Cabinet généraliste, fort en droit de la famille à Nouméa
                   depuis 2008, accueil bilingue."
  - Exemple INUTILE : "Avocat à Nouméa."

# CAS PARTICULIERS À ANTICIPER

- L'avocat de Vincent (divorce) ne doit PAS apparaître dans la liste.
  Comme tu ne sais pas qui c'est, je vérifierai après réception du CSV
  et l'écarterai si besoin.
- Si un cabinet a 2-3 associés (ex: SCP), liste UN avocat (l'associé
  principal ou celui dont la spécialité matche le mieux). Pas tous.
- Si un site renvoie vers un répertoire général sans page individuelle,
  retiens uniquement le mail général + le nom du gérant si mentionné.

# CE QUE TU NE DOIS PAS FAIRE

- Inventer un email plausible sans l'avoir vu (les bounces dégradent la
  réputation d'expéditeur).
- Citer un avocat dont tu n'as pas vérifié qu'il exerce bien à Nouméa
  ACTUELLEMENT (vérifier la mention "Inscrit au barreau de NC" ou
  l'adresse postale du cabinet à Nouméa).
- Inclure les notaires (différente profession).

# FORMAT DE SORTIE

Retourne UNIQUEMENT un bloc CSV avec ces colonnes (15 colonnes,
mêmes que prospects.csv) :

prenom,nom,fonction,entreprise,secteur,email,telephone,linkedin,source,statut,date_premier_contact,date_dernier_contact,prochaine_action,notes

Pour chaque ligne :
  - prenom : prénom seul (parfois précédé de "Maître" dans la présentation,
    mais à mettre uniquement le prénom dans cette colonne)
  - nom : nom de famille
  - fonction : "Avocat·e" ou "Avocat associé·e"
  - entreprise : nom complet du cabinet (ex: "Cabinet Tariel & Associés")
  - secteur : "Avocat - [spécialité principale]" (ex: "Avocat - Droit de la famille")
  - email : adresse email pro trouvée
  - telephone : numéro standard du cabinet
  - linkedin : URL profil LinkedIn si trouvée, sinon vide
  - source : "Annuaire Ordre Avocats NC 2026-05-XX" ou "Google search 2026-05-XX"
  - statut : "À contacter"
  - date_premier_contact : vide
  - date_dernier_contact : vide
  - prochaine_action : "Envoyer cold-intro avocat (template à adapter)"
  - notes : accroche personnalisée d'1 phrase + spécialités secondaires si pertinent

Exemple de ligne attendue :

Marie,Dupont,Avocate,Cabinet Dupont,Avocat - Droit de la famille,marie.dupont@cabinet-dupont.nc,+687 27 XX XX,https://www.linkedin.com/in/marie-dupont-xxx/,Annuaire Ordre Avocats NC 2026-05-04,À contacter,,,Envoyer cold-intro avocat (template à adapter),"Cabinet généraliste à Nouméa centre, fort en divorces et successions, exerce depuis 2010."

# QUALITÉ AVANT QUANTITÉ

Si tu ne peux fournir que 10 avocats vraiment qualifiés au lieu de 15 médiocres,
c'est mieux. Vincent envoie 15 emails maximum (limite compte pro Gmail) — autant
qu'ils soient bien ciblés.

# COMMENCE MAINTENANT

Lance l'étape 1 (annuaire de l'Ordre des Avocats NC). Pour chaque profil
retenu, tu m'indiques en chat (en plus du CSV final) :
  - Nom + cabinet
  - Spécialité retenue
  - Email récupéré (et la page où tu l'as trouvé)

Comme ça je peux suivre en temps réel.
```
