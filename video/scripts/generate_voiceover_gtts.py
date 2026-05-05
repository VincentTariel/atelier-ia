#!/usr/bin/env python3
"""
Génère la voix off prototype (gTTS, gratuit) pour la vidéo Atelier IA.

V3 après audit ChatGPT du 2026-05-05 — refonte alignée sur le mantra
"Claude prépare. Vous décidez." Corrections principales :
  - Slide promesse centrale ajoutée
  - Confidentialité reformulée (cadre d'usage, pas "données restent sur votre poste")
  - "Plomberie" → "travail préparatoire" / "travail invisible mais nécessaire"
  - "Skill" et "Project" → "vos consignes cabinet" / "un dossier client organisé"
    (les termes Anthropic restent en sous-texte sur l'écran)
  - Démo : section "Points de vigilance à contrôler" mise en valeur
  - Slide "40 min → 5 min" supprimée
  - Bio Vincent : "Docteur de l'École Polytechnique en informatique"

Découpage en 8 segments correspondant aux séquences narratives.

Usage :
    cd video
    python scripts/generate_voiceover_gtts.py

Sortie : video/assets/voiceover/01_hook.mp3, ..., 08_cta.mp3

Dépendances :
    pip install gtts
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
        "simple : combien d'heures partez-vous dans le travail "
        "préparatoire avant même d'exercer votre vraie valeur ajoutée ?"
    ),
    "02_promesse.mp3": (
        "Claude ne remplace pas votre travail. Il prépare ce qui doit "
        "l'être, pour que vous restiez concentré sur l'analyse, la "
        "stratégie et la relation client. "
        "Claude prépare. Vous décidez."
    ),
    "03_usage.mp3": (
        "Dans un navigateur, on pose une question ponctuelle. "
        "Avec Claude Desktop, on peut construire un espace de travail : "
        "documents sélectionnés, consignes du cabinet, et — si le cadre "
        "est adapté — accès contrôlé à certains fichiers locaux."
    ),
    "04_brique1_dossier.mp3": (
        "Première brique : un espace par dossier client. Pour l'avocat, "
        "l'idée est simple — un dossier, son contexte, ses pièces, ses "
        "consignes. "
        "Vous le nommez « Dossier Madame X — divorce » et vous y déposez "
        "tout : l'assignation, les courriers de la partie adverse, les "
        "pièces, le code civil annoté, et — élément clé — votre modèle "
        "Word de mise en page du cabinet. "
        "Vous n'avez plus à tout réexpliquer : le contexte du dossier "
        "est déjà organisé. Claude retrouve le bon élément au bon moment "
        "quand vous lui posez une question."
    ),
    "05_confidentialite.mp3": (
        "Avant de parler productivité, on définit le cadre : quels "
        "documents peuvent être utilisés, quels dossiers restent exclus, "
        "quels réglages doivent être vérifiés, et comment préserver le "
        "secret professionnel dans votre pratique. "
        "Le coaching inclut une mise au point spécifique sur les dossiers "
        "sensibles."
    ),
    "06_brique2_consignes.mp3": (
        "Deuxième brique : vos consignes permanentes. Pas besoin de tout "
        "répéter à chaque fois — on formalise une fois pour toutes vos "
        "règles de travail. "
        "« Tu respectes le modèle Word du cabinet. Tu reprends la "
        "nomenclature des pièces. Tu signales les informations "
        "manquantes. Tu distingues faits, demandes et points à vérifier. "
        "Tu ne cites aucune jurisprudence sans source vérifiable. Et tu "
        "ajoutes systématiquement une section « À contrôler par "
        "l'avocat ». » "
        "Vos conventions cabinet, en mémoire permanente — avec un "
        "garde-fou explicite : la décision finale reste vôtre."
    ),
    "07_demo.mp3": (
        "Concrètement : ce matin, vous recevez une assignation par "
        "email — vingt pages au format PDF, dactylographiée. Vous "
        "l'ajoutez au dossier client, et vous écrivez à Claude : "
        "« Résume cette assignation. Extrais les dates, demandes et "
        "pièces citées. Signale les délais à vérifier. Propose un plan "
        "de conclusions selon le modèle du cabinet. » "
        "Trente secondes plus tard : un résumé structuré, un tableau des "
        "dates et délais à vérifier, un plan de conclusions au format "
        "Word de votre cabinet — et, à la fin, une section « Points de "
        "vigilance à contrôler » : références juridiques à sourcer, "
        "pièces manquantes, délais à confirmer. "
        "Le gain n'est pas de supprimer votre relecture. C'est d'arriver "
        "plus vite à un brouillon structuré, contrôlable, conforme à vos "
        "habitudes."
    ),
    "08_cta.mp3": (
        "Je suis Vincent Tariel, docteur de l'École Polytechnique en "
        "informatique, installé en Nouvelle-Calédonie depuis 2020. Je "
        "propose un coaching individuel, en présentiel à Nouméa, pour "
        "mettre en place Claude Desktop dans votre pratique quotidienne. "
        "Le premier pas : un entretien découverte gratuit de trente "
        "minutes, sans engagement. "
        "atelier tiret i a point o v h."
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
