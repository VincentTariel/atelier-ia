# Brief — Lead-magnet PDF

> Statut : **à produire**. Le PDF actuel `core/templates/pdf/Atelier_IA_Niveau_1.pdf` est aligné sur l'ancien positionnement (atelier groupe Niveau 1) et doit être remplacé.

## Titre de travail

**"10 façons d'utiliser Claude Desktop dans son quotidien de pro — sans coder."**

(Variantes à tester : "Le guide pratique Claude Desktop pour pros calédoniens" / "Faire travailler Claude pour vous : 10 cas d'usage immédiats")

## Format

- 8 à 12 pages, PDF.
- Lecture en 10 minutes.
- Capté en échange du formulaire (déjà branché dans `core/views.py`).

## Objectif

- **Démontrer la valeur** avant l'achat (le lecteur doit pouvoir essayer 1-2 cas d'usage seul et avoir un résultat).
- **Qualifier** : si le lecteur trouve ça intéressant mais bloque, il revient demander un coaching.
- **Crédibiliser** : montrer qu'on maîtrise et qu'on a une approche structurée.

## Plan suggéré

1. **Page 1** — Couverture + promesse en une ligne.
2. **Page 2** — "Pourquoi Claude (et pas ChatGPT)" — 3 paragraphes sobres.
3. **Page 3** — "La règle d'or : donner du contexte" — l'erreur n°1 des débutants.
4. **Pages 4-9** — **10 cas d'usage** (1/2 page chacun) :
   1. Rédiger un email professionnel difficile
   2. Synthétiser une réunion à partir de notes brutes
   3. Préparer un RDV client en 5 min
   4. Reformuler un texte trop technique pour un client
   5. Transformer des notes vocales en compte-rendu
   6. Faire un brainstorming structuré
   7. Analyser un document PDF long (contrat, étude, rapport)
   8. Préparer une réponse à appel d'offres
   9. Créer un poste / fiche de mission
   10. Rédiger des annonces (immobilier, recrutement, commercial)
5. **Page 10** — "Aller plus loin : les Projects Claude" (teasing du coaching).
6. **Page 11** — Bio Vincent + CTA "Réservez un entretien découverte gratuit (30 min)".

## Ton

- Sobre, professionnel, sans jargon. Aucun emoji.
- Captures d'écran de Claude Desktop en français.
- Exemples adaptés au contexte calédonien quand pertinent (mentions de la NC, secteurs locaux).

## Production

- Rédaction : Vincent (avec assistance Claude pour les brouillons).
- Mise en page : `[outil à choisir — Canva / Affinity / LaTeX ?]`
- Captures : à faire sur Claude Desktop avec un compte de démo (pas avec des données réelles de prospect).

## Une fois produit

1. Placer le PDF final dans `core/templates/pdf/` sous le nom `Atelier_IA_Claude_Desktop.pdf`.
2. Mettre à jour `core/views.py:landing_page_view` pour pointer vers ce nouveau fichier.
3. Mettre à jour le subject + body de l'email d'envoi (actuellement aligné sur l'ancien PDF).
4. Mettre à jour la copy de la landing pour mentionner le nouveau lead-magnet.
