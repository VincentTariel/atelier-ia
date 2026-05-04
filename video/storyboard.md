# Storyboard slides — Atelier IA · Avocats (~3:30)

> Format : slides animées style PowerPoint / GDCP whiteboard. Pas de talking head.
> Voix off seule. Sous-titres FR brûlés en post pour LinkedIn (80% des vues sans son).
> Voir `video/script.md` pour le texte intégral et `video/pipeline_production.md` pour la production technique.

---

## Direction visuelle (cohérence Atelier IA)

**Palette** (alignée site éditorial, pas la magenta GDCP) :
- Fond : papier vélin `#f5efe2`
- Encre : noir brunâtre `#1a1614`
- Accent principal : bordeaux notarial `#7a2e2a`
- Highlight mots-clés : ocre/sable doré `#d4a843` (équivalent jaune fluo GDCP en plus sobre cabinet)
- Ombres de cards : bordeaux atténué

**Typographie** :
- Titres : **Instrument Serif** (cohérent site) en gras
- Body et exemples : **Newsreader** Regular ou **Inter** Regular
- Citations utilisateur (bulles dialogue) : **Newsreader Italic**
- Datelines / micro-typo : **JetBrains Mono**

**Composition** :
- Cards rectangulaires angles à 4px max (proche carré, sobre)
- Hairlines 1px noires partout
- Illustrations sketch crayon **monochromes** (encre noire + un trait bordeaux occasionnel) — pas la palette colorée GDCP
- Animations : fade-in + scale 0.95→1.0 (300-500 ms), pas de bounce/wow excessif

→ **Esprit "PowerPoint cabinet d'avocat" plutôt que "PowerPoint startup growth"**.

---

## Storyboard plan-par-plan

| # | Durée | Visuel slide | Voix off | Animation |
|---|---|---|---|---|
| **HOOK** ||||
| 1 | 0:00–0:08 | Plein écran : titre serif "Vous êtes avocat à Nouméa." sur fond vélin, dateline "Atelier IA · Édition 2026" en haut | « Vous êtes avocat à Nouméa. Vous avez trente dossiers en cours. » | Fade-in titre, puis "trente dossiers" qui s'affiche en plus gros |
| 2 | 0:08–0:18 | Liste à puces en hairlines : "créer un dossier · classer les pièces · retranscrire les attestations manuscrites · vérifier l'indexation · mettre en page selon les conventions" | « Pour chaque nouveau client, c'est la même routine : créer un dossier, classer les pièces, retranscrire les attestations manuscrites, vérifier l'indexation, mettre en page. » | Chaque ligne apparaît en cascade, surlignée en ocre fugace |
| 3 | 0:18–0:25 | Card centrée bordeaux : "3 h ? 5 h ? 10 h par semaine ?" + petit chrono dessiné | « Combien d'heures par semaine passées sur cette plomberie ? Voici comment Claude Desktop peut vous en rendre la moitié. » | Card scale-in, chiffres "3 h ? 5 h ? 10 h ?" qui s'incrémentent rapidement |
| **ACTE 1 — Chat vs Cowork** ||||
| 4 | 0:25–0:40 | Split-screen : à gauche capture sketch d'un onglet ChatGPT avec icône upload + flèches "fichier 1 fichier 2 fichier 3", à droite capture sketch de Claude Desktop avec dossier ouvert et fichiers déjà dedans | « Vous utilisez peut-être déjà Claude — ou ChatGPT — dans un onglet de votre navigateur. Le chat web fonctionne bien pour les questions ponctuelles. Mais pour intégrer l'IA dans votre quotidien de cabinet, il y a un mur. » | Apparition côté gauche d'abord, puis côté droit (3s plus tard) |
| 5 | 0:40–0:55 | Plein écran : capture stylisée de Claude Desktop avec dans la sidebar le label "📁 Dossier Madame X — divorce" + 8 fichiers visibles | « À chaque session, il faut redéposer les fichiers, réexpliquer le contexte, retaper le rôle. Avec Claude Desktop installé sur votre Mac ou votre PC, ce mur tombe : l'application travaille directement sur votre disque. » | Curseur souligne la sidebar, mise en évidence des fichiers présents |
| 6 | 0:55–1:00 | Card titre "Pas un onglet de plus." + sous-titre "Un véritable cowork sur votre poste." | « Pas un onglet de plus dans le navigateur. Un véritable cowork sur votre poste de travail. » | Card centrale, fade-in lent |
| **ACTE 2 — Le Project = dossier client** ||||
| 7 | 1:00–1:10 | Grand titre serif "ÉTAPE 1." sur fond ocre léger, sous-titre "Le Project = le dossier client" | « La première brique s'appelle un Project. Concrètement, c'est le dossier de votre client. » | Numéro romain "I." qui apparaît en bordeaux, puis le titre |
| 8 | 1:10–1:30 | Capture animée : un dossier sketch s'ouvre, on dépose dedans 5 documents (icônes : assignation, courrier, attestation manuscrite, code civil, modèle Word) avec leurs étiquettes | « Vous le nommez "Dossier Madame X — divorce". Et vous y déposez tout ce qui concerne ce dossier : l'assignation, les courriers de la partie adverse, les attestations scannées, le code civil annoté, et — élément clé — votre modèle Word de mise en page. » | Chaque document tombe dans le dossier en cascade, son nom apparaît à droite |
| 9 | 1:30–1:45 | Schéma : un Project = un dossier client. Petit graphique "30 dossiers en cours = 30 Projects" avec mini-icônes en grille | « À partir de ce moment, Claude a tous ces documents sous les yeux en permanence. Trente dossiers en cours = trente Projects. » | Multiplication visuelle des Projects en bas de l'écran |
| **ACTE 3 — Le Skill = conventions cabinet** ||||
| 10 | 1:45–1:55 | Grand titre "ÉTAPE 2." + sous-titre "Le Skill = vos conventions cabinet" | « La deuxième brique s'appelle un Skill. C'est l'endroit où vous écrivez, une fois pour toutes, les conventions de votre cabinet. » | Même apparition que l'étape 1 |
| 11 | 1:55–2:25 | Card type "fichier de skill" qui se remplit ligne par ligne : <br>↳ "Tu rédiges au format Word du cabinet" <br>↳ "Tu numérotes les pièces selon ma nomenclature" <br>↳ "Tu vérifies l'indexation" <br>↳ "Tu poses des questions si manque info" <br>↳ "Tu n'inventes jamais de jurisprudence" | Voix off lit chaque ligne au rythme | Apparition ligne par ligne (typewriter effect), highlight ocre sur les mots-clés ("format Word", "nomenclature", "indexation", "questions", "jurisprudence") |
| 12 | 2:25–2:30 | Card centrale "Vos conventions cabinet, en mémoire permanente." | « Une fois ce Skill enregistré, Claude le respecte sans qu'on ait besoin de le lui rappeler. » | Card emphasis bordeaux |
| **DÉMO — retranscription + indexation** ||||
| 13 | 2:30–2:40 | Image : un scan d'attestation manuscrite (cursive bleu, illisible volontairement par flou) | « Lundi matin, votre cliente vous remet une attestation manuscrite. Trois pages au stylo bleu, écriture serrée. » | Léger zoom-in sur le scan |
| 14 | 2:40–2:55 | Capture Claude Desktop : prompt qui se tape "Voici l'attestation manuscrite scannée. Retranscris-la au format de notre modèle Word. Indexe-la comme Pièce 7. Mets à jour la liste des pièces du dossier." | « Vous l'ajoutez au Project, et vous écrivez à Claude... » | Texte tapé en temps réel à l'écran |
| 15 | 2:55–3:05 | Capture Claude Desktop : la réponse apparaît en streaming — un beau document propre + une liste numérotée de pièces (1, 2, 3, 4, 5, 6, **7 (nouveau)**) | « Trente secondes plus tard : un texte propre, dans votre format cabinet, indexé Pièce 7, prêt à être imprimé. » | Speed-up x3 sur la génération |
| 16 | 3:05–3:10 | Card finale "40 minutes ➜ 5 minutes" en gros chiffres bordeaux | « La tâche qui prenait quarante minutes en prend désormais cinq, dont quatre à relire le brouillon. » | Animation chiffre "40" → "5" qui décompte |
| **CTA** ||||
| 17 | 3:10–3:25 | Plein écran : logo Atelier IA en haut, "Coaching individuel à Nouméa" en serif gras, encadré bordeaux "Tarif Fondateurs : 50 000 XPF (au lieu de 100 000)" + "10 places réservées" | « Atelier IA — coaching individuel à Nouméa, en présentiel, pour intégrer Claude Desktop dans votre cabinet. Les dix premiers clients fondateurs bénéficient d'un tarif réduit. » | Apparition par cascade |
| 18 | 3:25–3:30 | End-card statique : "atelier-ia.ovh" en gros, sous-titre "Réservez un entretien découverte gratuit", coordonnées "Vincent Tariel · +687 95 07 86 · tariel.vincent@gmail.com" | « Atelier IA. Atelier-ia.ovh. » | Hold 4 secondes, fade out |

---

## Slides à produire (= 18 slides)

| # | Slide title (interne) | Contenu visuel principal |
|---|---|---|
| 01 | Hook · Vous êtes avocat | Titre serif + dateline |
| 02 | Hook · La routine | Liste 5 puces en cascade |
| 03 | Hook · Combien d'heures | Card "3h? 5h? 10h?" |
| 04 | Acte 1 · Chat vs Cowork (split) | Split-screen sketch |
| 05 | Acte 1 · Desktop = sidebar fichiers | Capture stylisée Claude Desktop |
| 06 | Acte 1 · Pas un onglet de plus | Card titre |
| 07 | Étape 1 · Titre Project | "I. Le Project = le dossier client" |
| 08 | Étape 1 · Dossier qui se remplit | Animation 5 docs déposés |
| 09 | Étape 1 · 30 dossiers = 30 Projects | Grille multiplicative |
| 10 | Étape 2 · Titre Skill | "II. Le Skill = vos conventions" |
| 11 | Étape 2 · Skill qui se remplit | Typewriter ligne par ligne |
| 12 | Étape 2 · Mémoire permanente | Card emphasis |
| 13 | Démo · L'attestation scannée | Scan manuscrit floué |
| 14 | Démo · Le prompt | Capture prompt qui se tape |
| 15 | Démo · La réponse Claude | Capture réponse + liste pièces |
| 16 | Démo · 40 min → 5 min | Card chiffres |
| 17 | CTA · Tarif Fondateurs | Slide structurée |
| 18 | CTA · End-card | atelier-ia.ovh + coordonnées |

---

## Décisions à arbitrer par Vincent

- [ ] **Outil de slides** (Keynote / Google Slides / Canva / PowerPoint / autre) — voir `video/pipeline_production.md`
- [ ] **Voix off** : Vincent lui-même (vrai mais moins pro pour format slides), ou ElevenLabs Charlotte/Elliot (recommandé pour ce format)
- [ ] **Cas démo** : on garde "attestation manuscrite + Pièce 7" ou on change ?
- [ ] **Logo Atelier IA** : on en a un ? Sinon, juste typographique "Atelier IA." en serif suffit ?
- [ ] **Fond sonore** : aucun (recommandé) ou très très discret ?
