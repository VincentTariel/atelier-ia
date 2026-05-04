#!/usr/bin/env python3
"""
Génère la voix off prototype (gTTS, gratuit) pour la vidéo Atelier IA.

V2 après audit subagent du 2026-05-05 — corrections majeures :
  - Cas démo : assignation PDF (au lieu d'attestation manuscrite)
  - Pas de mention concurrent ("ChatGPT" → "un autre assistant")
  - Slide confidentialité ajoutée
  - CTA inversé (entretien gratuit d'abord, coaching ensuite)
  - "15-20 dossiers" (réaliste solo NC, au lieu de "30")
  - 5s autorité Vincent (Polytechnique + NC depuis 2020)

Découpage en 8 segments correspondant aux séquences du storyboard.

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
        "Vous êtes avocat à Nouméa. Vous avez quinze, vingt dossiers en cours. "
        "Pour chaque nouveau client, c'est la même routine : créer un dossier, "
        "classer les pièces, vérifier l'indexation, mettre en page selon les "
        "conventions du cabinet. "
        "Combien d'heures par semaine sur cette plomberie ? "
        "Voici comment Claude Desktop peut vous en rendre la moitié."
    ),
    "02_chat_vs_cowork.mp3": (
        "Vous avez peut-être essayé Claude — ou un autre assistant — dans un "
        "onglet de votre navigateur. Ça marche pour des questions ponctuelles. "
        "Pour intégrer l'intelligence artificielle dans votre cabinet, il faut "
        "autre chose : Claude Desktop, installé sur votre Mac ou votre PC, qui "
        "travaille directement sur vos dossiers locaux."
    ),
    "03_project.mp3": (
        "La première brique s'appelle un Project. Concrètement, c'est le dossier "
        "de votre client. "
        "Vous le nommez « Dossier Madame X — divorce ». Et vous y déposez tout : "
        "l'assignation, les courriers reçus de la partie adverse, les pièces, le "
        "code civil annoté que vous utilisez, et — élément clé — votre modèle Word "
        "de mise en page du cabinet. "
        "À partir de ce moment, Claude a tous ces documents en permanence sous "
        "les yeux quand vous lui parlez dans ce Project. "
        "Un dossier client, un Project."
    ),
    "04_confidentialite.mp3": (
        "Vos données restent sur votre poste. Elles ne servent pas à entraîner "
        "les modèles. Pour les dossiers les plus sensibles, on en reparle en "
        "détail au coaching."
    ),
    "05_skill.mp3": (
        "La deuxième brique s'appelle un Skill — vos consignes permanentes. "
        "Vous y écrivez une fois pour toutes : "
        "« Tu rédiges toujours au format de mon modèle Word. Tu numérotes les "
        "pièces selon ma nomenclature. À la fin de chaque document, tu listes "
        "les pièces référencées et tu vérifies qu'elles sont jointes. Si une "
        "information manque, tu poses la question avant de continuer. Tu "
        "n'inventes jamais une jurisprudence sans source explicite. » "
        "Une fois ce Skill enregistré, Claude le respecte sans qu'on ait à le "
        "rappeler. Vos conventions cabinet, en mémoire permanente."
    ),
    "06_demo.mp3": (
        "Concrètement : ce matin, vous recevez une assignation par email — "
        "vingt pages au format PDF, dactylographiée. "
        "Vous l'ajoutez au Project du dossier, et vous écrivez à Claude : "
        "« Résume cette assignation. Extrais les dates clés et les délais à "
        "respecter. Propose-moi un plan de conclusions au format de mon "
        "cabinet. » "
        "Trente secondes plus tard : un résumé structuré, un tableau des dates "
        "d'audience et des délais de procédure, un plan de conclusions déjà "
        "mis en forme. "
        "La tâche qui prenait quarante minutes en prend cinq, dont quatre passés "
        "à relire le brouillon."
    ),
    "07_auteur.mp3": (
        "Je suis Vincent Tariel, docteur de l'École Polytechnique en "
        "informatique, installé en Nouvelle-Calédonie depuis 2020."
    ),
    "08_cta.mp3": (
        "Premier pas : un entretien découverte gratuit de trente minutes, en "
        "présentiel à Nouméa ou en visio. Si on est alignés, trois heures de "
        "coaching à cinquante mille francs Pacifique — au lieu de cent mille — "
        "pendant les dix places fondateurs. "
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
        "\n  2. Construire les 16 slides selon video/storyboard.md"
        "\n  3. Monter dans DaVinci Resolve : voix off + slides + sous-titres"
    )


if __name__ == "__main__":
    main()
