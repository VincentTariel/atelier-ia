#!/usr/bin/env python3
"""
Production automatisée de la vidéo Atelier IA.

Pipeline :
  1. Capture chaque slide HTML via Google Chrome headless (1920x1080)
  2. Pour chaque slide, crée un mini-clip vidéo de la durée prescrite
  3. Concatène tous les clips en un grand MP4 silencieux
  4. Concatène les segments voix off gTTS en un grand MP3
  5. Mixe audio + vidéo en MP4 final

Pré-requis :
  - google-chrome (déjà installé : /usr/bin/google-chrome)
  - ffmpeg (déjà installé)
  - voix off déjà générée par scripts/generate_voiceover_gtts.py

Usage :
    cd video
    python scripts/build_video.py

Sortie : video/output/atelier_ia_video.mp4
"""

from pathlib import Path
import shutil
import subprocess
import sys

# --- Mapping slide → (segment audio, durée en secondes) ----------------
# La somme des durées par segment audio doit égaler la durée du segment
# (sinon désynchronisation). Vérifié : total = 231s = 3:51.

SLIDES = [
    # (slide_num, audio_segment_filename, duration_seconds)
    (1,  "01_hook.mp3",              10),
    (2,  "01_hook.mp3",              10),
    (3,  "01_hook.mp3",              10),
    (4,  "02_promesse.mp3",          13),
    (5,  "03_usage.mp3",             17),
    (6,  "04_brique1_dossier.mp3",   10),
    (7,  "04_brique1_dossier.mp3",   12),
    (8,  "05_confidentialite.mp3",   19),
    (9,  "06_brique2_consignes.mp3", 10),
    (10, "06_brique2_consignes.mp3", 28),
    (11, "07_demo.mp3",              12),
    (12, "07_demo.mp3",              10),
    (13, "07_demo.mp3",              25),
    (14, "07b_manuscrit.mp3",        19),
    (15, "08_cta.mp3",               30),
]

# Audio playback order (un fichier joue une seule fois, partagé entre N slides)
AUDIO_ORDER = [
    "01_hook.mp3",
    "02_promesse.mp3",
    "03_usage.mp3",
    "04_brique1_dossier.mp3",
    "05_confidentialite.mp3",
    "06_brique2_consignes.mp3",
    "07_demo.mp3",
    "07b_manuscrit.mp3",
    "08_cta.mp3",
]

# --- Chemins -----------------------------------------------------------

VIDEO_DIR    = Path(__file__).resolve().parent.parent
HTML_FILE    = VIDEO_DIR / "slides_prototype.html"
VOICEOVER    = VIDEO_DIR / "assets" / "voiceover"
OUTPUT_DIR   = VIDEO_DIR / "output"
WORK_DIR     = OUTPUT_DIR / "_work"

CHROME       = "/usr/bin/google-chrome"
WIDTH        = 1920
HEIGHT       = 1080
FPS          = 30


def run(cmd, capture=False):
    """Run a subprocess command, raise on failure."""
    if capture:
        return subprocess.run(cmd, check=True, capture_output=True, text=True)
    return subprocess.run(cmd, check=True)


def capture_slide(slide_num: int, out_png: Path) -> None:
    """Capture a single slide via Chrome headless."""
    url = f"file://{HTML_FILE}?slide={slide_num}"
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--hide-scrollbars",
        f"--window-size={WIDTH},{HEIGHT}",
        f"--screenshot={out_png}",
        "--virtual-time-budget=2500",  # let fonts load
        url,
    ]
    print(f"  · capturing slide {slide_num:02d} → {out_png.name}")
    run(cmd, capture=True)
    if not out_png.exists():
        sys.exit(f"  ✗ Capture failed for slide {slide_num}")


def make_slide_clip(png: Path, duration: int, out_mp4: Path) -> None:
    """Create a silent video clip from a still image with given duration."""
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-loop", "1",
        "-i", str(png),
        "-t", str(duration),
        "-vf", f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=decrease,"
               f"pad={WIDTH}:{HEIGHT}:(ow-iw)/2:(oh-ih)/2:color=0xf5efe2,"
               f"fps={FPS}",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", "fast",
        str(out_mp4),
    ]
    run(cmd, capture=True)


def concat_videos(clip_paths, out_mp4: Path) -> None:
    """Concatenate video clips with ffmpeg concat demuxer."""
    list_file = WORK_DIR / "video_list.txt"
    list_file.write_text("\n".join(f"file '{p.name}'" for p in clip_paths))
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "concat", "-safe", "0",
        "-i", str(list_file),
        "-c", "copy",
        str(out_mp4),
    ]
    subprocess.run(cmd, check=True, cwd=WORK_DIR)


def concat_audio(audio_paths, out_mp3: Path) -> None:
    """Concatenate MP3 audio files."""
    list_file = WORK_DIR / "audio_list.txt"
    list_file.write_text("\n".join(f"file '{p}'" for p in audio_paths))
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "concat", "-safe", "0",
        "-i", str(list_file),
        "-c", "copy",
        str(out_mp3),
    ]
    run(cmd, capture=True)


def mix_av(video: Path, audio: Path, out_mp4: Path) -> None:
    """Combine video + audio into final MP4."""
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-i", str(video),
        "-i", str(audio),
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "128k",
        "-shortest",
        str(out_mp4),
    ]
    run(cmd, capture=True)


def main() -> None:
    print("=" * 60)
    print("Atelier IA — production vidéo automatisée")
    print("=" * 60)

    # Sanity checks
    if not HTML_FILE.exists():
        sys.exit(f"✗ HTML introuvable : {HTML_FILE}")
    if not VOICEOVER.exists():
        sys.exit(f"✗ Voix off introuvable : {VOICEOVER}")
    for _, audio_name, _ in SLIDES:
        if not (VOICEOVER / audio_name).exists():
            sys.exit(f"✗ Segment audio manquant : {audio_name}")

    # Reset workdir
    if WORK_DIR.exists():
        shutil.rmtree(WORK_DIR)
    WORK_DIR.mkdir(parents=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # ── Étape 1 : capture des slides ────────────────────────────────
    print("\n[1/4] Capture des slides via Chrome headless")
    png_paths = []
    for slide_num, _, _ in SLIDES:
        png = WORK_DIR / f"slide_{slide_num:02d}.png"
        capture_slide(slide_num, png)
        png_paths.append(png)

    # ── Étape 2 : création des clips vidéo silencieux ──────────────
    print(f"\n[2/4] Création de {len(SLIDES)} clips vidéo")
    clip_paths = []
    for (slide_num, _, duration), png in zip(SLIDES, png_paths):
        clip = WORK_DIR / f"clip_{slide_num:02d}.mp4"
        print(f"  · clip {slide_num:02d} ({duration}s)")
        make_slide_clip(png, duration, clip)
        clip_paths.append(clip)

    # ── Étape 3 : concaténation ────────────────────────────────────
    print("\n[3/4] Concaténation vidéo + audio")
    video_concat = WORK_DIR / "video_only.mp4"
    audio_concat = WORK_DIR / "audio_only.mp3"
    concat_videos(clip_paths, video_concat)
    concat_audio([VOICEOVER / a for a in AUDIO_ORDER], audio_concat)

    # ── Étape 4 : mixage final ─────────────────────────────────────
    print("\n[4/4] Mixage final audio + vidéo")
    final = OUTPUT_DIR / "atelier_ia_video.mp4"
    mix_av(video_concat, audio_concat, final)

    # ── Résumé ────────────────────────────────────────────────────
    size_mb = final.stat().st_size / 1024 / 1024
    duration_total = sum(d for _, _, d in SLIDES)
    print(f"\n{'=' * 60}")
    print(f"✓ Vidéo produite : {final}")
    print(f"  - Taille     : {size_mb:.1f} MB")
    print(f"  - Durée      : {duration_total // 60}:{duration_total % 60:02d}")
    print(f"  - Résolution : {WIDTH}×{HEIGHT}, {FPS} fps")
    print(f"  - Slides     : {len(SLIDES)}")
    print(f"\n  Lecture : xdg-open {final}")
    print(f"  Travail  : {WORK_DIR} (peut être supprimé)")
    print("=" * 60)


if __name__ == "__main__":
    main()
