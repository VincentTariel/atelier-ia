# Stratégie d'acquisition — Secteur 01 : Communication / Marketing en PME

**Période** : mai-juin 2026 — premier batch outbound après lancement.
**Objectif** : 30 prospects sourcés, 30 cold-emails envoyés, 5-8 RDV calés en 4 semaines.

---

## Pourquoi ce secteur en premier

Six secteurs étaient candidats (cf. `offre/persona.md`). J'ai tranché pour **Communication / marketing en PME** parce que :

1. **Le pain rédactionnel est leur métier**. Ils ne le perçoivent pas comme une corvée annexe — c'est leur livrable. Argumenter "vous gagnez du temps sur la production de contenu" entre directement dans leur quotidien, sans pédagogie préalable.
2. **Le profil est curieux des outils IA**. Beaucoup ont essayé ChatGPT et continuent de l'utiliser. La promesse "passez à Claude Desktop, on configure ensemble" résonne — pas de mur "l'IA ce n'est pas pour moi".
3. **Le décideur est souvent l'opérateur**. En PME, le responsable com/marketing est aussi celui qui produit. Il décide pour lui-même, pas besoin de convaincre une chaîne hiérarchique.
4. **Le budget existe**. La communication est un poste budgété, pas un coût exceptionnel à justifier.
5. **Timing favorable en mai-juin**. Pas de période bloquante (contrairement aux comptables en mai = bilans, ou aux notaires en juin = forte activité immobilier).
6. **Bouche-à-oreille structuré**. Les responsables com d'une même ville se parlent (associations pro, asso CCI, French Tech). Une recommandation = porte ouverte.
7. **Vincent peut tenir l'angle naturellement**. CommeUnJeu produit beaucoup de contenu (vidéos pédagogiques, copy d'app, posts) — la preuve par l'exemple est immédiate.

**Secteurs reportés** :
- Expertise comptable/juridique → reporter à juillet (sortie période bilans).
- Avocats/notaires → reporter à juillet (cycle décision long, mieux après avoir 2-3 témoignages anonymes).
- Immobilier → bon candidat pour batch 02.
- BTP, RH → garder pour batches ultérieurs après affinage du pitch.

---

## Cible précise

**Profil idéal** :
- Responsable communication, marketing manager, chargé·e de communication
- Dans une **PME calédonienne** (10-100 salariés), idéalement entre 20 et 50
- Établissement à Nouméa ou Grand Nouméa (présentiel = critère bloquant)
- Secteurs d'activité du PME (peu importe lequel) : banque/assurance, distribution, BTP, hôtellerie, mutuelle, association, etc.

**À EXCLURE** :
- Agences de communication (concurrents indirects, ils savent déjà)
- Communicants freelance solo (probablement déjà utilisateurs IA, peu de budget)
- Grands groupes (Carsud, OPT, Enercal…) → cycle d'achat trop long, comité de pilotage

---

## Sources de sourcing (par ordre de priorité)

### 1. LinkedIn (priorité #1 — 60% des leads cibles)

Recherche LinkedIn :
- **Lieu** : Nouvelle-Calédonie
- **Fonction (poste actuel)** : `responsable communication` OU `directeur·trice marketing` OU `chargé·e de communication` OU `community manager` OU `marketing manager`
- **Taille entreprise** : 11-50 / 51-200
- **Tri** : par récente activité (signal de présence sur LinkedIn → joignable)

**Récupération email** : Hunter.io extension Chrome (free tier 25/mois suffit) ou inspection du site web de la PME (souvent `prenom.nom@domaine.nc`).

### 2. Annuaire CCI Nouvelle-Calédonie (priorité #2)

URL : https://www.cci.nc/annuaire-entreprises

- Filtrer sur PME 11-100 salariés à Nouméa/Dumbéa/Mont-Dore/Païta
- Visiter les sites web des entreprises listées → page "Équipe" / "Contact" → repérer le poste com/marketing
- Si pas de poste com identifié : laisser de côté (la PME n'a peut-être pas d'interlocuteur dédié)

### 3. Presse économique locale (compléments)

- **DNC (Demain en Nouvelle-Calédonie)** — interviews et portraits de dirigeants/responsables com
- **Made in Nouvelle-Calédonie** — magazine éco
- **Les Nouvelles Calédoniennes** rubrique éco

→ Repérer les noms cités, vérifier sur LinkedIn, ajouter au CSV.

### 4. Réseaux pros

- **CCI Nouvelle-Calédonie** — événements business mensuels
- **French Tech NC** — communauté tech-com
- **Femmes Chefs d'Entreprise NC** — réseau accessible aux solos

(À activer en bouche-à-oreille après les premières signatures, pas avant.)

---

## Canal principal : LinkedIn (et non cold email)

**Décision** révisée après le sourcing : on attaque par **LinkedIn**, pas par
cold email. Justification :

- Cible com/marketing = profils LinkedIn-actifs par essence
- Taux d'ouverture LinkedIn (80-90%) >> cold email (20-40% après filtres)
- Profil de Vincent (Polytechnique, fondateur, etc.) visible immédiatement = crédibilité instant
- Pas de friction "trouver l'email" (canal natif)
- Pas de risque spam (pas de filtres Gmail à passer)
- Volume de 7 prospects = très loin des limites LinkedIn (~100/semaine)

**Cold email = fallback** uniquement si la demande de connexion est refusée
ou ignorée 21 jours.

Templates LinkedIn dans `acquisition/linkedin_templates/` :
- `01_demande_connexion.md` — demande courte (≤ 300 caractères) avec accroche personnalisée
- `02_message_post_connexion.md` — pitch complet une fois connecté (24-48h après acceptation)
- `03_relance_LI_J7.md` — relance courte si pas de réponse au message post-connexion

## Plan d'attaque sur 4 semaines (révisé)

### Semaine 1 — Sourcing (4-6h)  ✅ FAIT
- 11 prospects sourcés via Claude for Chrome → `acquisition/prospects.csv`
- 7 Tier 1 / 3 Tier 2 (watch) / 1 exclusion (Skazy NC)
- Détails du sourcing : `acquisition/prompts/claude_chrome_sourcing_secteur_01.md`

### Semaine 2 — Demandes de connexion LinkedIn (1h)
- 7 demandes de connexion personnalisées (~280 caractères chacune)
- Cadence : ~3-4 par jour mardi-jeudi pour ne pas paraître automatisé
- Mettre à jour le statut dans `prospects.csv` (`Connexion demandée` + date)

### Semaine 2-3 — Messages post-connexion
- Dès qu'une connexion est acceptée (notification LinkedIn) → message complet
  sous 24-48h via `02_message_post_connexion.md` (avec 3 créneaux concrets)
- Statut → `Message envoyé` + date

### Semaine 3-4 — Relances + premiers RDV
- J+7 sans réponse : `03_relance_LI_J7.md`
- Premiers RDV qui se calent → trame `acquisition/call_scripts/decouverte.md`

### Semaine 4 — Bilan + décision
- J+21 sans réponse : passage en `Sans suite` (pas de 3e relance)
- Bilan chiffré dans `crm/revues/AAAA-MM-JJ.md`
- Décider : continuer sur ce secteur, élargir, ou pivoter vers secteur 02

---

## Cibles chiffrées (pour pouvoir mesurer)

| Indicateur | Objectif batch 01 |
|---|---|
| Prospects sourcés | 30 |
| Cold-emails envoyés | 30 |
| Taux d'ouverture | > 40 % (12+) |
| Taux de réponse | > 5 % (2+) |
| RDV calés | 2-4 |
| Signatures (Tarif Fondateurs) | 1-2 |

Si on atteint ces chiffres → secteur validé, on continue.
Si on est en dessous (notamment < 30 % d'ouverture ou 0 réponse) → revoir l'objet email + l'accroche.

---

## Prochaine action concrète

**Pour Vincent** : prendre 30 minutes pour identifier **5 PME calédoniennes** dont tu connais soit le responsable com (réseau perso), soit l'entreprise (lecture éco). Me les donner sous la forme :

```
1. Nom entreprise — secteur — éventuellement nom du responsable com si tu le sais
2. ...
```

Avec ces 5 entrées comme amorce, je peux te montrer le pattern de sourcing complet (recherche LinkedIn, vérification email, accroche personnalisée) et tu réplique sur 25 autres.
