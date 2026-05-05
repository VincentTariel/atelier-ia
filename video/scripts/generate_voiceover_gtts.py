#!/usr/bin/env python3
"""
Génère la voix off prototype (gTTS, gratuit) pour la vidéo Atelier IA.

V4 après seconde itération audit ChatGPT du 2026-05-05 — affinage des
tournures pour plus de sobriété et de crédibilité juridique.

Corrections principales vs V3 :
  - "combien d'heures" → "combien de temps"
  - "ce qui doit l'être" → "ce qui peut l'être"
  - Slide 5 reformulée : "méthode de travail" + "ce que Claude peut ou ne peut pas utiliser"
  - Slide 7 raccourcie : suppression "Claude retrouve le bon élément au bon moment"
  - Slide 10 synthétique : suppression de la répétition liste
  - "en mémoire permanente" → "dans vos consignes réutilisables"
  - "Trente secondes plus tard" → "Vous obtenez une première base de travail"
  - Slide 14 sobre : "j'aide les professionnels du droit à intégrer Claude
    dans leur pratique quotidienne, de façon concrète et cadrée"

Découpage en 8 segments correspondant aux séquences narratives.

Usage :
    cd video
    python scripts/generate_voiceover_gtts.py

Sortie : video/assets/voiceover/01_hook.mp3, ..., 08_cta.mp3
"""

from pathlib import Path
import sys

try:
    from gtts import gTTS
except ImportError:
    sys.exit(
        "Module 'gtts' manquant. Installer via :\n"
        "    pip install gtts\n"
        "OU activer le venv qui en dispose :\n"
        "    source /mnt/sda2/commeunjeu3/cours/static/video_production/.venv/bin/activate"
    )

# --- Découpage du script en 8 segments ----------------------------------

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
    "08_cta.mp3": (
        "Je suis Vincent Tariel, docteur de l'École Polytechnique en "
        "informatique, installé en Nouvelle-Calédonie depuis 2020. Avec "
        "Atelier IA, j'aide les professionnels du droit à intégrer "
        "Claude dans leur pratique quotidienne, de façon concrète et "
        "cadrée. "
        "Le premier pas : un entretien découverte gratuit de trente "
        "minutes, sans engagement, sur atelier-ia point ovh."
    ),
}

# --- Génération ---------------------------------------------------------

OUT_DIR = Path(__file__).resolve().parent.parent / "assets" / "voiceover"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def main() -> None:
    print(f"Sortie : {OUT_DIR}\n")

    total_chars = 0
    for filename, text in SEGMENTS.items():
        out_path = OUT_DIR / filename
        chars = len(text)
        total_chars += chars

        print(f"  → {filename}  ({chars} caractères, ~{chars / 14:.0f}s)")

        tts = gTTS(text=text, lang="fr", slow=False)
        tts.save(str(out_path))

    print(
        f"\n[OK] {len(SEGMENTS)} fichiers générés dans {OUT_DIR}"
        f"\n     Total : {total_chars} caractères, ~{total_chars / 14:.0f}s estimé"
    )

    print(
        "\nProchaines étapes :"
        "\n  1. Écouter chaque segment et ajuster le texte si besoin (ce script)"
        "\n  2. Construire les 14 slides selon video/storyboard.md"
        "\n  3. Monter dans DaVinci Resolve : voix off + slides + sous-titres"
    )


if __name__ == "__main__":
    main()
