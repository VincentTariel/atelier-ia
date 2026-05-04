# Stratégie d'acquisition — Secteur ACTIF : Avocats à Nouméa

**Période** : mai 2026 — premier batch outbound effectif.
**Objectif** : 15-20 prospects sourcés, 15-20 cold-emails envoyés, 3-5 RDV calés en 3-4 semaines.

---

## Pourquoi ce secteur (pivot du 2026-05-04)

Le sourcing initial visait Communication/marketing en PME (cf. `communication.md`).
Vincent a pivoté vers les **avocats** parce que :

1. **Confort personnel** : Vincent a déjà un avocat (celui de son divorce) — relation
   existante = porte d'entrée pour comprendre le métier de l'intérieur, premier
   client potentiel, ou introduction dans le réseau du barreau de Nouméa.
2. **Cohérence narrative** : le PDF lead-magnet contient l'histoire de
   **Maître Adam**, avocat à Nouméa. Le prospect avocat s'identifie immédiatement
   à la mise en scène — c'est exactement le cas d'usage qu'on lui présente.
3. **Sourcing facile** : les cabinets d'avocats publient leurs emails sur leur site
   (obligation déontologique partielle). Pas besoin de Hunter.io ni de chasse à
   l'email — quasi tous publics via Google.
4. **Volume raisonnable** : ~200-300 avocats inscrits au barreau de NC →
   bassin large, pas besoin de viser la totalité, juste les profils à
   forte production écrite (civil, famille, baux, conseil aux entreprises).
5. **Pain rédactionnel évident** : courriers, attestations, conclusions,
   inventaires de pièces — c'est leur quotidien.
6. **Cycle de décision** : un peu plus long que la com/marketing PME, mais le
   décideur est presque toujours l'avocat lui-même (cabinet solo ou petit), pas
   de hiérarchie à convaincre.

**Risque** : profession traditionnellement conservatrice envers les outils.
**Mitigation** : le PDF lead-magnet pose explicitement Claude Desktop comme
**l'assistant de rédaction** (et non pas une IA qui décide à leur place). Ça
désamorce.

## Cible précise

**Profil idéal** :
- Avocat·e inscrit·e au barreau de **Nouméa** (Ordre des Avocats de NC)
- **Cabinet solo** ou **petite structure** (1 à 5 avocats associés)
- Spécialités à privilégier (forte production écrite) :
  - Droit civil général
  - Droit de la famille / divorces
  - Baux commerciaux / immobilier
  - Droit des sociétés / conseil aux entreprises
  - Droit du travail
- À éviter (cycle long ou volume rédactionnel moindre) :
  - Pénalistes purs (plaidoirie > rédaction)
  - Très grosses structures internationales (cycle décision long)
  - Notaires (différente profession, autre stratégie possible plus tard)

## Sources de sourcing

### 1. Annuaire Ordre des Avocats de Nouvelle-Calédonie (priorité #1)

URL probable : https://www.barreau-noumea.nc/ ou via le site du Conseil de l'Ordre.

→ Liste exhaustive des avocats inscrits avec leur cabinet.
→ Pour chaque cabinet : visiter le site web pour récupérer email + spécialités.

### 2. Recherche Google directe

`site:.nc avocat Nouméa "droit de la famille"` (ou autre spécialité)
`avocat Nouméa cabinet site` → repérer les sites de cabinet et leur contact.

### 3. LinkedIn (en complément)

Recherche LinkedIn :
- Lieu : Nouvelle-Calédonie
- Fonction : `avocat` OR `avocate` OR `juriste`
- Filtrer pour cabinet libéral (pas conseil juridique en entreprise).

### 4. Réseau personnel — porte d'entrée stratégique

**Vincent a déjà un avocat (divorce)** → opportunité unique :
- **Option A** : lui pitcher Atelier IA en tant que client. S'il dit oui →
  premier client signé + témoignage anonyme "Avocat à Nouméa : [bénéfice]"
  qui devient marketing or pour le batch suivant.
- **Option B** : lui demander une recommandation vers 2-3 confrères en NC qui
  pourraient être intéressés (le barreau est petit, tout le monde se connaît).
- **Option C** : juste prendre 30 min avec lui pour vérifier que l'angle
  "Maître Adam" du PDF tient la route et identifier ce qui manque (validation
  utilisateur sans coût).

Mes recos par ordre :
- Faire C **avant** la prospection (1 RDV avec ton avocat divorce, mode
  consultation gratuite, pour calibrer la prospection à venir).
- Puis A si l'angle tient et qu'il est ouvert.
- B en bonus.

## Canal principal : Cold-email

À l'inverse des com/marketing, **les avocats sont peu actifs sur LinkedIn**
mais traitent leurs emails pros quotidiennement. Inversement de la stratégie
précédente :

- **Cold-email** = canal #1 (template `acquisition/email_templates/01_cold_intro.md`,
  à adapter pour le ton avocat — voir ci-dessous).
- **LinkedIn** = canal de backup uniquement si l'email bounce ou pas de réponse
  à J+21.

## Adaptation du template email pour avocats

Sur le template existant (`01_cold_intro.md`), trois ajustements :

1. **Objet** : ajouter une variante adaptée :
   `Maître {nom}, une question rapide sur la rédaction au cabinet`

2. **Accroche contextuelle** : au lieu de "j'ai vu que vous travaillez avec
   les PME du BTP", aller chercher quelque chose de spécifique au cabinet :
   - mention dans la presse locale
   - spécialité affichée sur leur site
   - article publié par le cabinet
   - événement récent (mise à jour locale, jurisprudence calédonienne)

3. **Renvoi explicite vers le PDF** : *"vous y trouverez l'histoire de Maître
   Adam, exactement le cas que vous vivez peut-être au cabinet."* Le PDF
   devient un argument central (pas juste un lead-magnet).

## Plan d'attaque sur 4 semaines

### Semaine 1 — Validation + sourcing (3-5h)
- **Lundi** : prendre 30 min avec ton avocat divorce → calibrer l'angle (option C ci-dessus)
- **Mardi-jeudi** : sourcer 15-20 avocats à Nouméa via Ordre + Google + LinkedIn
- Renseigner dans `acquisition/prospects.csv` (colonnes habituelles + email direct récupéré)
- Détails sourcing dans `acquisition/prompts/claude_chrome_sourcing_avocats.md`

### Semaine 2 — Préparation + envoi (3h sur 1-2 jours)
- Pour chaque prospect : version personnalisée du template cold-email (renvoi explicite vers le PDF + Maître Adam)
- Stockage du batch dans `acquisition/sends/AAAA-MM-JJ_batch_avocats_01.md` (gitignored)
- **Cadence** : 15 envois OK en 1-2 jours (compte pro Gmail Vincent : 500/jour, 15 = no-stress).
  Recommandation : étaler sur 2 jours (ex. 8 mardi, 7 jeudi) pour pouvoir
  ajuster la copy si le 1er jour ne convertit pas comme attendu.

### Semaine 3 — Relances + premiers RDV
- J+7 sans réponse : `02_relance_J7.md`
- Premiers RDV calés : trame `acquisition/call_scripts/decouverte.md`

### Semaine 4 — Bilan
- J+21 sans réponse : `03_relance_J21.md` puis `Sans suite`
- Bilan dans `crm/revues/AAAA-MM-JJ.md`

## Cibles chiffrées

| Indicateur | Objectif batch avocats |
|---|---|
| Prospects sourcés | 15-20 |
| Cold-emails envoyés | 15-20 |
| Taux d'ouverture | > 50 % (cible plus attentive aux mails pros) |
| Taux de réponse | > 10 % (2-3) |
| RDV calés | 2-4 |
| Signatures Tarif Fondateurs | 1-2 |

Si on atteint > 1 signature → secteur validé, on continue à élargir.

## Prochaine action immédiate

1. **Toi** : prendre 30 min avec ton avocat (option C) pour calibrer l'angle.
2. **Moi** (en parallèle) : préparer le prompt Claude for Chrome pour sourcer 15-20 avocats à Nouméa via l'annuaire de l'Ordre + sites cabinets, avec récupération automatique des emails publics.
