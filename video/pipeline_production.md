# Pipeline de production — Vidéo Atelier IA

> Workflow technique pour produire la vidéo en 2 phases : prototype gTTS rapide
> pour valider, puis version finale ElevenLabs pour publier.
> Vincent maîtrise déjà ce type de pipeline (CommeUnJeu utilise Manim + ElevenLabs + gTTS).

---

## Phase 1 — Prototype gTTS (objectif : valider en 1 jour)

### Objectif
Avoir une vidéo complète et présentable, **avant la fin de la semaine**, pour :
- Valider le timing des slides
- Valider le découpage narratif
- Valider la copy à voix haute (révéle les phrases qui ne sonnent pas)
- Tester sur 2-3 personnes (avocat de divorce de Vincent + réseau)
- **Avant** d'investir dans ElevenLabs

### Étapes

#### 1. Générer la voix off avec gTTS
Voir `video/scripts/generate_voiceover_gtts.py` (script Python prêt). Il découpe automatiquement le script en 6 segments (un par séquence) pour permettre des ajustements ciblés.

```bash
cd video
python scripts/generate_voiceover_gtts.py
# → produit assets/voiceover/01_hook.mp3, 02_chat_vs_cowork.mp3, ..., 06_cta.mp3
```

Durée totale prévue : ~3:30. gTTS est moins naturel qu'ElevenLabs (intonation plate)
mais largement suffisant pour valider le rythme.

#### 2. Construire les slides
Outils possibles, par ordre de simplicité :

| Outil | Avantages | Inconvénients | Reco |
|---|---|---|---|
| **Google Slides** | Gratuit, collaboratif, export MP4 natif | Animations limitées | ✅ recommandé V1 |
| **Keynote** (Mac) | Belles animations, magic move puissant | Mac uniquement | Si Vincent est Mac |
| **PowerPoint** | Déjà installé, animations OK | Export MP4 moyen | Acceptable |
| **Canva** | Templates prêts, animations modernes | Compte payant pour export HD | Acceptable |
| **Manim** | Vincent maîtrise (CommeUnJeu) | Surdimensionné pour slides simples | ❌ pas pour ça |

→ **Pour le prototype, Google Slides** : couvre tout, gratuit, exportable en MP4.
   Pour le final, on peut basculer sur Canva ou Keynote si on veut un rendu plus polish.

#### 3. Produire les 18 slides selon `storyboard.md`
- Créer un slide par numéro du storyboard
- Respecter la palette Atelier IA (vélin, encre, bordeaux, ocre highlight)
- Pour les illustrations sketch : utiliser **noun project** (icônes hand-drawn, gratuites avec attribution) ou **storyset.com** (illustrations sketch gratuites)
- Pour les captures Claude Desktop : faire de vraies captures (pas de mockup), flouter les éléments perso

#### 4. Synchroniser slides + voix
- Exporter les slides en MP4 sans audio (Google Slides : "File > Download > Video MP4")
- Ouvrir DaVinci Resolve (gratuit, déjà installé chez Vincent ?)
- Importer le MP4 + les fichiers audio gTTS
- Ajuster la durée de chaque slide pour coller au timing voix off
- Ajouter sous-titres FR (auto-générés via DaVinci, corrigés à la main)
- Exporter MP4 final

#### 5. Tester
- Envoyer la V1 à 2-3 personnes (commencer par l'avocat de Vincent)
- Recueillir feedback : "où tu décroches", "qu'est-ce qui te paraît évident", "qu'est-ce qui te paraît flou"
- Itérer 1-2 fois sur les slides + texte si besoin

### Estimation Phase 1
| Tâche | Temps |
|---|---|
| Affiner script + générer voix gTTS | 1h |
| Produire les 18 slides Google Slides | 4-5h |
| Captures Claude Desktop | 1h |
| Montage DaVinci + sous-titres | 2-3h |
| Tests + retours + 1 itération | 2-3h |
| **Total Phase 1** | **10-13 heures** sur 2 jours |

---

## Phase 2 — Production finale ElevenLabs (objectif : publier)

Déclenchée seulement si la Phase 1 a validé le storyboard.

### Étapes

#### 1. Compte ElevenLabs
- Créer un compte sur https://elevenlabs.io
- Plan **Starter** suffisant : 5 USD/mois, 30 000 caractères/mois (largement assez pour ce projet)
- ⚠️ Pour cette vidéo : ~3000 caractères de script → 1/10 du quota mensuel → on peut itérer plusieurs fois

#### 2. Choix de la voix française
Voix recommandées pour le ton avocat sobre :
- **Charlotte** (féminine, claire, articulée — meilleur fit pour le ton "cabinet")
- **Elliot** (masculine, posée, sans accent)
- **Adam** (masculine, chaleureuse)

→ **Recommandation : Charlotte**. Tester les 3 sur un échantillon court (le hook seul) avant de générer toute la voix off.

#### 3. Générer la voix avec ElevenLabs
Un script Python (à ajouter à `video/scripts/`) :

```python
from elevenlabs import generate, save, set_api_key
import os

set_api_key(os.environ['ELEVENLABS_API_KEY'])

scripts = {
    '01_hook.mp3': "...",  # texte du hook
    '02_chat_vs_cowork.mp3': "...",
    # etc.
}

for filename, text in scripts.items():
    audio = generate(
        text=text,
        voice="Charlotte",
        model="eleven_multilingual_v2"
    )
    save(audio, f"video/assets/voiceover/{filename}")
```

#### 4. Remontage final
- Remplacer les pistes audio gTTS par les pistes ElevenLabs dans DaVinci
- Ajuster le timing des slides si l'intonation ElevenLabs est différente
- Re-générer les sous-titres
- Ajouter une intro/outro discrète (sans musique de fond, juste un fondu)
- Export MP4 H.264, 1080p, 30 fps

### Estimation Phase 2
| Tâche | Temps |
|---|---|
| Compte ElevenLabs + tests voix | 1h |
| Génération voix ElevenLabs + scripts | 1h |
| Remontage DaVinci | 2-3h |
| Export final + tests qualité | 1h |
| **Total Phase 2** | **5-6 heures** sur 1 jour |

### Coût Phase 2
- ElevenLabs Starter : 5 USD (~600 XPF) — premier mois suffisant
- Aucun autre coût (DaVinci gratuit, Google Slides gratuit)

---

## Phase 3 — Diffusion

| Canal | Format | Taille recommandée |
|---|---|---|
| Landing atelier-ia.ovh | MP4 1080p | < 30 MB pour fluidité (compresser à 720p si > 50 MB) |
| LinkedIn post Vincent | MP4 1080p | <200 MB (limite LinkedIn), idéalement 30-50 MB |
| LinkedIn organic | Sous-titres OBLIGATOIRES (80% sans son) | brûlés dans la vidéo |
| Signature email | Lien YouTube non listé | crédibilise sans alourdir |
| Post-RDV | Lien YouTube ou MP4 attaché | au choix selon contexte |

### Hébergement YouTube
- Compte YouTube : Vincent peut utiliser son compte CommeUnJeu existant ou créer un compte Atelier IA dédié
- **Visibilité : "Non répertorié"** (pas privé, pas public — accessible via lien direct)
- Titre suggéré : "Claude Desktop pour avocats — comment intégrer l'IA dans votre cabinet"
- Description : reprendre la promesse + lien atelier-ia.ovh + tarif Fondateurs

---

## Décisions à prendre par Vincent (avant de démarrer Phase 1)

- [ ] **OK pour le storyboard validé** dans `video/storyboard.md` ?
- [ ] **Outil slides** : Google Slides (recommandé V1) ou autre ?
- [ ] **Captures Claude Desktop** : sur compte démo dédié ou compte perso (avec floutage) ?
- [ ] **Voix prototype gTTS** : OK pour démarrer aujourd'hui ?
- [ ] **Voix finale** : ElevenLabs Charlotte (féminine, recommandée) ou autre ?
- [ ] **Hébergement YouTube** : compte CommeUnJeu existant ou nouveau compte Atelier IA ?

Une fois ces 6 cases cochées, on démarre la Phase 1 le lendemain.
