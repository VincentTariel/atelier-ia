#!/usr/bin/env python3
"""
Génère la voix off finale (ElevenLabs, qualité pro) pour la vidéo Atelier IA.

Variante de generate_voiceover_gtts.py qui utilise l'API ElevenLabs.
Mêmes 9 segments, mêmes textes — seul le moteur de synthèse change.

CONFIGURATION REQUISE
---------------------
1. Compte ElevenLabs avec quota suffisant (~3500 caractères pour ce projet,
   le plan Starter gratuit 10 000 caractères/mois est suffisant pour itérer).

2. Récupérer la clé API : https://elevenlabs.io/app/settings/api-keys

3. Ajouter dans le .env du projet (à la racine de atelier-ia) :
       ELEVENLABS_API_KEY=sk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

   .env est déjà gitignored — la clé n'est jamais committée.

USAGE
-----
    cd video
    python scripts/generate_voiceover_elevenlabs.py

    # Tester d'abord sur un seul segment :
    python scripts/generate_voiceover_elevenlabs.py --only 02_promesse

    # Tester une autre voix :
    python scripts/generate_voiceover_elevenlabs.py --voice Charlie

VOIX RECOMMANDÉES POUR FR / TON CABINET
---------------------------------------
- Charlotte  (XB0fDUnXU5powFXDhCwa) — féminine, claire, articulée — RECO
- Stéphanie  (sgxOK5VkFi9uWO94UJ4U) — féminine, posée, plus douce
- Henri      (b78fjijwOPkJUZQK35sH) — masculine, sobre
- Adam       (pNInz6obpgDQGcFmaJgB) — masculine, chaleureuse (utilisée pour CommeUnJeu)

Pour comparer rapidement, lancer avec --only 02_promesse + --voice X
puis écouter chaque candidat.

Sortie : video/assets/voiceover/01_hook.mp3, ..., 08_cta.mp3
(écrase les fichiers gTTS — relancer le pipeline build_video.py ensuite).
"""

import argparse
import os
import sys
from pathlib import Path

# Charger .env du projet
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
try:
    from dotenv import load_dotenv
    load_dotenv(PROJECT_ROOT / ".env")
except ImportError:
    pass  # python-dotenv optionnel ; ELEVENLABS_API_KEY peut être déjà dans os.environ

try:
    from elevenlabs import ElevenLabs
except ImportError:
    sys.exit(
        "Module 'elevenlabs' manquant. Installer via :\n"
        "    pip install elevenlabs\n"
        "OU activer le venv qui en dispose :\n"
        "    source /mnt/sda2/commeunjeu3/cours/static/video_production/.venv/bin/activate"
    )

# --- Voice IDs ----------------------------------------------------------

VOICES = {
    "Charlotte": "XB0fDUnXU5powFXDhCwa",
    "Stephanie": "sgxOK5VkFi9uWO94UJ4U",
    "Henri":     "b78fjijwOPkJUZQK35sH",
    "Adam":      "pNInz6obpgDQGcFmaJgB",
    "Charlie":   "IKne3meq5aSn9XLyUdCD",
}

DEFAULT_VOICE = "Charlotte"

# --- Voice settings (ton posé cabinet) ---------------------------------

VOICE_SETTINGS = {
    "stability":         0.80,   # 0.0-1.0 — élevé = plus stable, moins expressif
    "similarity_boost":  0.75,   # 0.0-1.0 — fidélité au profil de voix
    "speed":             0.95,   # 0.7-1.2 — légèrement lent pour articulation
    "style":             0.30,   # 0.0-1.0 — un peu d'expressivité naturelle
    "use_speaker_boost": True,
}

MODEL = "eleven_multilingual_v2"
OUTPUT_FORMAT = "mp3_44100_128"

# --- Mêmes 9 segments que gTTS — source de vérité partagée -------------

SEGMENTS = {
    "01_hook.mp3": (
        "Vous êtes avocat à Nouméa. Vous suivez quinze, vingt dossiers, "
        "parfois plus, avec peu de temps pour le travail de fond. "
        "À chaque nouveau dossier, il faut classer les pièces, retrouver "
        "les courriers, extraire les dates, vérifier les délais, puis "
        "produire un document propre. "
        "La question n'est pas de remplacer votre analyse. Elle est "
        "simple : combien de temps partez-vous dans le travail "
        "préparatoire avant même d'exercer votre vraie valeur ajoutée ?"
    ),
    "02_promesse.mp3": (
        "Claude ne remplace pas votre travail. Il prépare ce qui peut "
        "l'être, pour que vous restiez concentré sur l'analyse, la "
        "stratégie et la relation client. "
        "Claude prépare. Vous décidez."
    ),
    "03_usage.mp3": (
        "Dans un navigateur, on pose une question ponctuelle. "
        "Avec Claude Desktop, on peut mettre en place une méthode de "
        "travail : des documents sélectionnés, des consignes cabinet, et "
        "un cadre clair pour savoir ce que Claude peut — ou ne peut "
        "pas — utiliser."
    ),
    "04_brique1_dossier.mp3": (
        "Première brique : un espace par dossier client. "
        "Vous créez un espace pour le dossier Madame X — divorce. Vous y "
        "rassemblez l'assignation, les courriers adverses, les pièces, "
        "vos références utiles et votre modèle Word. "
        "Vous n'avez plus à tout réexpliquer : le contexte du dossier "
        "est organisé."
    ),
    "05_confidentialite.mp3": (
        "Avant de parler productivité, on définit le cadre d'usage : "
        "quels documents peuvent être utilisés, quels dossiers restent "
        "exclus, quels réglages doivent être vérifiés, et dans quels "
        "cas il vaut mieux ne pas utiliser Claude. "
        "Le coaching inclut une mise au point spécifique sur les "
        "dossiers sensibles."
    ),
    "06_brique2_consignes.mp3": (
        "Deuxième brique : vos consignes permanentes. Pas besoin de tout "
        "répéter à chaque fois — on formalise une fois pour toutes vos "
        "règles de travail. "
        "Ces consignes fixent vos habitudes : modèle Word, nomenclature "
        "des pièces, informations manquantes, distinction entre faits, "
        "demandes et points à vérifier. Et surtout : aucune jurisprudence "
        "sans source vérifiable, avec une section finale « À contrôler "
        "par l'avocat ». "
        "Vos conventions cabinet, dans vos consignes réutilisables — "
        "avec un garde-fou explicite : la décision finale reste vôtre."
    ),
    "07_demo.mp3": (
        "Concrètement : ce matin, vous recevez une assignation par "
        "email — vingt pages au format PDF, dactylographiée. Vous "
        "l'ajoutez au dossier client, et vous écrivez à Claude : "
        "« Résume cette assignation. Extrais les dates, demandes et "
        "pièces citées. Signale les délais à vérifier. Propose un plan "
        "de conclusions selon le modèle du cabinet. » "
        "Vous obtenez une première base de travail : un résumé "
        "structuré, un tableau des dates et délais à vérifier, un plan "
        "de conclusions au format du cabinet, et une section « Points "
        "de vigilance à contrôler ». "
        "Le gain n'est pas de supprimer votre relecture. C'est d'arriver "
        "plus vite à un brouillon structuré, contrôlable, conforme à vos "
        "habitudes."
    ),
    "07b_manuscrit.mp3": (
        "Autre cas typique : la transcription d'une attestation "
        "manuscrite courte. Claude propose le texte propre, dans le "
        "format du cabinet — vous relisez ligne à ligne en croisant "
        "avec l'original. Le gain reste le même : la frappe et la mise "
        "en forme automatisées, pas l'analyse juridique."
    ),
    "08_cta.mp3": (
        "Je suis Vincent Tariel, docteur en mathématiques de l'École "
        "Polytechnique, installé en Nouvelle-Calédonie depuis 2020. "
        "Avec Atelier IA, j'aide les professionnels du droit à intégrer "
        "Claude dans leur pratique quotidienne, de façon concrète et "
        "cadrée. "
        "Le premier pas : un entretien découverte gratuit de quinze "
        "minutes, sans engagement, sur https://atelier-ia.ovh"
    ),
}

# --- Génération ---------------------------------------------------------

OUT_DIR = Path(__file__).resolve().parent.parent / "assets" / "voiceover"


def main() -> None:
    parser = argparse.ArgumentParser(description="Génère la voix off ElevenLabs.")
    parser.add_argument("--voice", default=DEFAULT_VOICE,
                        choices=list(VOICES.keys()),
                        help=f"Voix à utiliser (défaut : {DEFAULT_VOICE})")
    parser.add_argument("--only", default=None,
                        help="Ne générer qu'un segment (ex : 02_promesse)")
    args = parser.parse_args()

    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        sys.exit(
            "❌ ELEVENLABS_API_KEY non définie.\n\n"
            "Ajouter dans le .env du projet (racine atelier-ia/) :\n"
            "    ELEVENLABS_API_KEY=sk_xxxxxxxxxxxx...\n\n"
            "Récupérer la clé : https://elevenlabs.io/app/settings/api-keys"
        )

    voice_id = VOICES[args.voice]
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"\nVoix      : {args.voice} ({voice_id})")
    print(f"Modèle    : {MODEL}")
    print(f"Settings  : {VOICE_SETTINGS}")
    print(f"Sortie    : {OUT_DIR}\n")

    client = ElevenLabs(api_key=api_key)

    segments_to_run = SEGMENTS.items()
    if args.only:
        match_key = next((k for k in SEGMENTS if args.only in k), None)
        if not match_key:
            sys.exit(f"❌ Segment '{args.only}' introuvable.")
        segments_to_run = [(match_key, SEGMENTS[match_key])]
        print(f"[mode --only] : seulement {match_key}\n")

    total_chars = 0
    for filename, text in segments_to_run:
        chars = len(text)
        total_chars += chars
        out_path = OUT_DIR / filename

        print(f"  → {filename}  ({chars} caractères)")

        # Streamed audio — concat into bytes
        audio_iter = client.text_to_speech.convert(
            voice_id=voice_id,
            model_id=MODEL,
            text=text,
            output_format=OUTPUT_FORMAT,
            voice_settings=VOICE_SETTINGS,
        )
        audio_bytes = b"".join(audio_iter)
        out_path.write_bytes(audio_bytes)

    print(
        f"\n[OK] {len(list(segments_to_run))} fichiers générés."
        f"\n     Total : {total_chars} caractères consommés sur ton quota ElevenLabs."
    )

    print(
        "\nProchaines étapes :"
        "\n  1. Écouter et valider chaque segment"
        "\n  2. Si une voix ne plait pas : --voice Stephanie / Henri / Adam"
        "\n  3. Re-build vidéo : python scripts/build_video.py"
    )


if __name__ == "__main__":
    main()
