#!/usr/bin/env python3
"""
Génère la voix off prototype (gTTS, gratuit) pour la vidéo Atelier IA.

Découpe automatique en 6 segments correspondant aux séquences du storyboard,
ce qui permet d'ajuster la durée d'un segment sans tout regénérer.

Usage :
    cd video
    python scripts/generate_voiceover_gtts.py

Sortie : video/assets/voiceover/01_hook.mp3, 02_chat_vs_cowork.mp3, etc.

Dépendances :
    pip install gtts pydub
    (apt install ffmpeg si pas déjà installé)
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

# --- Découpage du script en 6 segments ----------------------------------

SEGMENTS = {
    "01_hook.mp3": (
        "Vous êtes avocat à Nouméa. Vous avez trente dossiers en cours. "
        "Pour chaque nouveau client, c'est la même routine : créer un dossier, "
        "classer les pièces, retranscrire les attestations manuscrites, "
        "vérifier que chaque pièce citée est bien jointe, mettre en page "
        "selon les conventions du cabinet. "
        "Combien d'heures par semaine passées sur cette plomberie ? "
        "Trois ? Cinq ? Dix ? "
        "Voici comment Claude Desktop peut vous en rendre la moitié."
    ),
    "02_chat_vs_cowork.mp3": (
        "Vous utilisez peut-être déjà Claude — ou ChatGPT — dans un onglet "
        "de votre navigateur. Le chat web fonctionne bien pour les questions "
        "ponctuelles. Mais pour intégrer l'intelligence artificielle dans votre "
        "quotidien de cabinet, il y a un mur : à chaque session, il faut "
        "redéposer les fichiers, réexpliquer le contexte, retaper le rôle attendu. "
        "Avec Claude Desktop installé sur votre Mac ou votre PC, ce mur tombe. "
        "L'application travaille directement sur votre disque dur. Vos dossiers "
        "restent à leur place, vos modèles de courrier sont là tout le temps, "
        "votre nomenclature de pièces est connue par défaut. "
        "Pas un onglet de plus dans le navigateur — un véritable cowork sur "
        "votre poste de travail."
    ),
    "03_project.mp3": (
        "La première brique s'appelle un Project. Concrètement, c'est le dossier "
        "de votre client. "
        "Vous le nommez « Dossier Madame X — divorce ». Et vous y déposez tout "
        "ce qui concerne ce dossier : l'assignation, les courriers reçus de la "
        "partie adverse, les attestations manuscrites scannées, le code civil "
        "annoté que vous utilisez, et — élément clé — votre modèle Word de mise "
        "en page du cabinet. "
        "À partir de ce moment, Claude a tous ces documents en permanence sous "
        "les yeux quand vous lui parlez dans ce Project. Pas besoin de les "
        "redéposer à chaque demande. "
        "Un dossier client égale un Project. Trente dossiers en cours, égale "
        "trente Projects."
    ),
    "04_skill.mp3": (
        "La deuxième brique s'appelle un Skill. C'est l'endroit où vous "
        "écrivez, une fois pour toutes, les conventions de votre cabinet. "
        "Quelques exemples : « Tu rédiges toujours dans le format de mon "
        "modèle Word — colonnes, polices, marges. Tu numérotes les pièces "
        "selon ma nomenclature : Pièce un, exploit d'huissier ; Pièce deux, "
        "courrier adverse ; et ainsi de suite. À la fin de chaque document, "
        "tu listes les pièces référencées et tu vérifies qu'elles sont bien "
        "dans le dossier. Si une information manque, tu poses la question "
        "avant de continuer. Tu n'inventes jamais une jurisprudence sans "
        "source explicite. » "
        "Une fois ce Skill enregistré, Claude le respecte sans qu'on ait "
        "besoin de le lui rappeler. Vos conventions cabinet, en mémoire "
        "permanente."
    ),
    "05_demo.mp3": (
        "Concrètement : lundi matin, votre cliente vous remet une attestation "
        "manuscrite de témoin. Trois pages au stylo bleu, écriture serrée. "
        "Vous la scannez, vous l'ajoutez au Project du dossier, et vous "
        "écrivez à Claude : "
        "« Voici l'attestation manuscrite scannée. Retranscris-la au format "
        "de notre modèle Word. Indexe-la comme Pièce sept. Mets à jour la "
        "liste des pièces du dossier. » "
        "Trente secondes plus tard : un texte propre, dans votre format "
        "cabinet, indexé Pièce sept, ajouté à la liste des pièces, prêt à "
        "être imprimé. "
        "La tâche qui prenait quarante minutes — relecture, frappe, mise "
        "en page, vérification de l'indexation — en prend désormais cinq, "
        "dont quatre passés à relire le brouillon."
    ),
    "06_cta.mp3": (
        "Atelier IA — coaching individuel à Nouméa, en présentiel, pour "
        "intégrer Claude Desktop dans votre cabinet. Trois heures de "
        "coaching, on construit votre premier Project, votre premier Skill, "
        "sur votre vrai dossier en cours. "
        "Les dix premiers clients fondateurs bénéficient d'un tarif de "
        "cinquante mille francs au lieu de cent mille. "
        "Réservez votre entretien découverte gratuit en bas de la "
        "description. Atelier IA. Atelier hyphen ia point ovh."
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
        "\n  2. Construire les 18 slides selon video/storyboard.md"
        "\n  3. Monter dans DaVinci Resolve : voix off + slides + sous-titres"
    )


if __name__ == "__main__":
    main()
