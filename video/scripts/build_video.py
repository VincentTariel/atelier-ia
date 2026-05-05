#!/usr/bin/env python3
"""
Production automatisée de la vidéo Atelier IA.

Pipeline :
  1. Capture chaque slide HTML via Google Chrome headless (1920x1080)
  2. Pour chaque slide, crée un mini-clip vidéo de la durée prescrite
  3. Concatène tous les clips en un grand MP4 silencieux
  4. Concatène les segments voix off en un grand MP3
  5. Mixe audio + vidéo en MP4 final

Les durées de slides sont calculées AUTOMATIQUEMENT à partir des durées
audio réelles (ffprobe). Quand plusieurs slides partagent un même segment
audio, on distribue la durée selon les poids relatifs (WEIGHT). Ça permet
de switcher entre gTTS et ElevenLabs sans rien retoucher.

Pré-requis :
  - google-chrome (déjà installé : /usr/bin/google-chrome)
  - ffmpeg (déjà installé)
  - voix off déjà générée (gTTS ou ElevenLabs) dans video/assets/voiceover/

Usage :
    cd video
    python scripts/build_video.py

Sortie : video/output/atelier_ia_video.mp4
"""

from pathlib import Path
import shutil
import subprocess
import sys

# --- Mapping slide → (segment audio, poids relatif) -------------------
# Quand N slides partagent un même segment audio, la durée du segment
# est divisée selon les poids. Les poids reproduisent les ratios validés
# en V4 gTTS (qui équilibrait visuellement le contenu de chaque slide).

SLIDES = [
    # (slide_num, audio_segment_filename, weight)
    (1,  "01_hook.mp3",              1.0),   # 1/3 du hook
    (2,  "01_hook.mp3",              1.0),   # 1/3 du hook
    (3,  "01_hook.mp3",              1.0),   # 1/3 du hook
    (4,  "02_promesse.mp3",          1.0),
    (5,  "03_usage.mp3",             1.0),
    (6,  "04_brique1_dossier.mp3",   1.0),   # ratio 10/12 (titre court)
    (7,  "04_brique1_dossier.mp3",   1.2),   # ratio 10/12 (animation longue)
    (8,  "05_confidentialite.mp3",   1.0),
    (9,  "06_brique2_consignes.mp3", 1.0),   # ratio 10/28 (titre court)
    (10, "06_brique2_consignes.mp3", 2.8),   # ratio 10/28 (skill qui se remplit)
    (11, "07_demo.mp3",              1.2),   # ratio 12/10/25
    (12, "07_demo.mp3",              1.0),   # ratio 12/10/25
    (13, "07_demo.mp3",              2.5),   # ratio 12/10/25 (résultat 3 zones)
    (14, "07b_manuscrit.mp3",        1.0),
    (15, "08_cta.mp3",               1.0),
]

# Audio playback order (un fichier joue une seule fois)
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
    if capture:
        return subprocess.run(cmd, check=True, capture_output=True, text=True)
    return subprocess.run(cmd, check=True)


def get_audio_duration(audio_path: Path) -> float:
    """Get audio duration in seconds via ffprobe."""
    out = subprocess.check_output([
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(audio_path),
    ], text=True).strip()
    return float(out)


def compute_slide_durations() -> list:
    """For each slide, compute its actual duration from real audio durations
    + relative weights. Returns list of (slide_num, audio, duration)."""
    # Sum of weights per audio segment
    weights_per_audio = {}
    for _, audio, weight in SLIDES:
        weights_per_audio.setdefault(audio, 0.0)
        weights_per_audio[audio] += weight

    # Real duration per audio
    durations_per_audio = {
        audio: get_audio_duration(VOICEOVER / audio)
        for audio in weights_per_audio
    }

    # Distribute
    result = []
    for slide_num, audio, weight in SLIDES:
        share = weight / weights_per_audio[audio]
        duration = durations_per_audio[audio] * share
        result.append((slide_num, audio, duration))
    return result


def capture_slide(slide_num: int, out_png: Path) -> None:
    url = f"file://{HTML_FILE}?slide={slide_num}"
    cmd = [
        CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
        "--hide-scrollbars",
        f"--window-size={WIDTH},{HEIGHT}",
        f"--screenshot={out_png}",
        "--virtual-time-budget=2500",
        url,
    ]
    print(f"  · capturing slide {slide_num:02d} → {out_png.name}")
    run(cmd, capture=True)
    if not out_png.exists():
        sys.exit(f"  ✗ Capture failed for slide {slide_num}")


def make_slide_clip(png: Path, duration: float, out_mp4: Path) -> None:
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-loop", "1",
        "-i", str(png),
        "-t", f"{duration:.3f}",
        "-vf", f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=decrease,"
               f"pad={WIDTH}:{HEIGHT}:(ow-iw)/2:(oh-ih)/2:color=0xf5efe2,"
               f"fps={FPS}",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "fast",
        str(out_mp4),
    ]
    run(cmd, capture=True)


def concat_videos(clip_paths, out_mp4: Path) -> None:
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

    if not HTML_FILE.exists():
        sys.exit(f"✗ HTML introuvable : {HTML_FILE}")
    if not VOICEOVER.exists():
        sys.exit(f"✗ Voix off introuvable : {VOICEOVER}")
    for _, audio_name, _ in SLIDES:
        if not (VOICEOVER / audio_name).exists():
            sys.exit(f"✗ Segment audio manquant : {audio_name}")

    if WORK_DIR.exists():
        shutil.rmtree(WORK_DIR)
    WORK_DIR.mkdir(parents=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Compute slide durations from real audio
    slides = compute_slide_durations()
    total_duration = sum(d for _, _, d in slides)
    print(f"\n[*] Mapping slides → durées (calculé depuis audio réel)")
    for n, a, d in slides:
        print(f"    slide {n:02d}  ({a:30s})  {d:6.2f}s")
    print(f"    {'─' * 50}")
    print(f"    TOTAL : {total_duration:.2f}s = "
          f"{int(total_duration // 60)}:{int(total_duration % 60):02d}")

    # ── Capture
    print("\n[1/4] Capture des slides via Chrome headless")
    png_paths = []
    for slide_num, _, _ in slides:
        png = WORK_DIR / f"slide_{slide_num:02d}.png"
        capture_slide(slide_num, png)
        png_paths.append(png)

    # ── Clips
    print(f"\n[2/4] Création de {len(slides)} clips vidéo")
    clip_paths = []
    for (slide_num, _, duration), png in zip(slides, png_paths):
        clip = WORK_DIR / f"clip_{slide_num:02d}.mp4"
        make_slide_clip(png, duration, clip)
        clip_paths.append(clip)

    # ── Concat
    print("\n[3/4] Concaténation vidéo + audio")
    video_concat = WORK_DIR / "video_only.mp4"
    audio_concat = WORK_DIR / "audio_only.mp3"
    concat_videos(clip_paths, video_concat)
    concat_audio([VOICEOVER / a for a in AUDIO_ORDER], audio_concat)

    # ── Mix
    print("\n[4/4] Mixage final audio + vidéo")
    final = OUTPUT_DIR / "atelier_ia_video.mp4"
    mix_av(video_concat, audio_concat, final)

    size_mb = final.stat().st_size / 1024 / 1024
    print(f"\n{'=' * 60}")
    print(f"✓ Vidéo produite : {final}")
    print(f"  - Taille     : {size_mb:.1f} MB")
    print(f"  - Durée      : {int(total_duration // 60)}:{int(total_duration % 60):02d}")
    print(f"  - Résolution : {WIDTH}×{HEIGHT}, {FPS} fps")
    print(f"  - Slides     : {len(slides)}")
    print(f"\n  Lecture : xdg-open {final}")
    print("=" * 60)


if __name__ == "__main__":
    main()
