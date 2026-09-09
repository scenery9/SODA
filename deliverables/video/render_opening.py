from pathlib import Path
import math
import subprocess

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
OUT = ROOT / "SODA-opening-40s.mp4"
import imageio_ffmpeg  # noqa: E402

W, H, FPS, DURATION = 1280, 720, 24, 40
GREEN = (28, 150, 119)
MINT = (129, 229, 196)
NAVY = (13, 26, 55)
WHITE = (248, 251, 255)
CORAL = (255, 102, 91)
MUTED = (190, 202, 224)


def font(size, bold=False):
    name = "segoeuib.ttf" if bold else "segoeui.ttf"
    return ImageFont.truetype(str(Path(r"C:\Windows\Fonts") / name), size)


def ease(x):
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


def fade(t, start, end, fade_time=0.55):
    if t < start or t > end:
        return 0
    return int(255 * min(ease((t - start) / fade_time), ease((end - t) / fade_time)))


def cover(im):
    scale = max(W / im.width, H / im.height)
    size = (round(im.width * scale), round(im.height * scale))
    im = im.resize(size, Image.Resampling.LANCZOS)
    x = (im.width - W) // 2
    y = (im.height - H) // 2
    return im.crop((x, y, x + W, y + H)).convert("RGB")


def overlay_text(base, text, xy, size, color=WHITE, bold=False, alpha=255, anchor="la"):
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    c = color + (alpha,)
    d.text(xy, text, font=font(size, bold), fill=c, anchor=anchor)
    return Image.alpha_composite(base.convert("RGBA"), layer)


def pill(base, box, label, accent, alpha=255, icon=None):
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, radius=18, fill=(14, 27, 54, int(alpha * 0.82)),
                        outline=accent + (alpha,), width=2)
    if icon:
        d.ellipse((x0 + 18, y0 + 17, x0 + 46, y0 + 45), fill=accent + (alpha,))
        tx = x0 + 58
    else:
        tx = x0 + 24
    d.text((tx, (y0 + y1) // 2), label, font=font(25, True), fill=WHITE + (alpha,), anchor="lm")
    return Image.alpha_composite(base.convert("RGBA"), layer)


def safe_face_area(base, alpha=100):
    # A subtle guide that is fully covered when the presenter video is added.
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle((46, 502, 310, 682), radius=26,
                        fill=(7, 18, 38, 35), outline=(129, 229, 196, alpha), width=2)
    return Image.alpha_composite(base.convert("RGBA"), layer)


scene1 = cover(Image.open(ASSETS / "student-week-scene.png"))
scene2 = cover(Image.open(ASSETS / "calendar-pressure-scene.png"))
scene1_dark = ImageEnhance.Brightness(scene1).enhance(0.48).filter(ImageFilter.GaussianBlur(1.2))
scene2_dark = ImageEnhance.Brightness(scene2).enhance(0.52)


def frame_at(t):
    if t < 14:
        base = scene1.copy()
        dark = Image.new("RGBA", (W, H), (4, 15, 38, 0))
        ImageDraw.Draw(dark).rectangle((0, 0, W, H), fill=(4, 15, 38, 70))
        im = Image.alpha_composite(base.convert("RGBA"), dark)
        chips = [
            ("Assignment", (770, 126, 1088, 190), MINT, 1.0),
            ("Paid shift", (830, 212, 1138, 276), (108, 189, 231), 3.2),
            ("Club request", (742, 298, 1078, 362), (173, 151, 245), 5.4),
        ]
        for label, box, colour, start in chips:
            a = fade(t, start, 13.6, .45)
            if a:
                slide = int(35 * (1 - ease((t - start) / .6)))
                moved = (box[0] + slide, box[1], box[2] + slide, box[3])
                im = pill(im, moved, label, colour, a, icon=True)
        a = fade(t, 0.4, 7.0)
        if a:
            im = overlay_text(im, "An assignment. A paid shift.", (54, 75), 43, bold=True, alpha=a)
            im = overlay_text(im, "A club request.", (54, 128), 43, color=MINT, bold=True, alpha=a)
        a = fade(t, 7.0, 13.9)
        if a:
            im = overlay_text(im, "Each one looks manageable.", (54, 80), 45, bold=True, alpha=a)
            im = overlay_text(im, "Until they land in the same week.", (54, 139), 31,
                              color=MUTED, alpha=a)
    elif t < 26:
        local = t - 14
        im = scene2_dark.convert("RGBA")
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        d.rectangle((0, 0, 575, H), fill=(4, 15, 38, 165))
        im = Image.alpha_composite(im, layer)
        a = fade(local, 0.0, 6.1)
        if a:
            im = overlay_text(im, "When the week gets crowded,", (54, 78), 42, bold=True, alpha=a)
            im = overlay_text(im, "the real question is what one more", (54, 137), 29, color=MUTED, alpha=a)
            im = overlay_text(im, "commitment will cost.", (54, 178), 29, color=CORAL, bold=True, alpha=a)
        a = fade(local, 6.0, 11.9)
        if a:
            im = overlay_text(im, "Most planners show what", (54, 80), 40, bold=True, alpha=a)
            im = overlay_text(im, "you already agreed to.", (54, 132), 40, bold=True, alpha=a)
            im = overlay_text(im, "The warning arrives after the decision.", (54, 196), 27,
                              color=MUTED, alpha=a)
    else:
        local = t - 26
        blend = min(1, max(0, local / 1.0))
        im = Image.blend(scene2_dark, scene1_dark, blend).convert("RGBA")
        layer = Image.new("RGBA", (W, H), (4, 15, 38, 105))
        im = Image.alpha_composite(im, layer)
        a = fade(local, 0.0, 8.0)
        if a:
            im = overlay_text(im, "SODA", (640, 112), 82, color=MINT, bold=True, alpha=a, anchor="ma")
            im = overlay_text(im, "shows the cost before you say yes.", (640, 199), 39,
                              bold=True, alpha=a, anchor="ma")
            im = overlay_text(im, "A student workload planner for the moment when options still exist.",
                              (640, 258), 25, color=MUTED, alpha=a, anchor="ma")
        a = fade(local, 7.2, 13.9)
        if a:
            items = ["See total load", "Preview the cost", "Adjust safely", "Protect recovery"]
            widths = [220, 234, 206, 238]
            x = 166
            for i, (label, width) in enumerate(zip(items, widths)):
                im = pill(im, (x, 350, x + width, 410), label, GREEN if i < 3 else MINT, a)
                x += width + 24
                if i < 3:
                    im = overlay_text(im, "›", (x - 13, 380), 35, color=MUTED, bold=True,
                                      alpha=a, anchor="mm")
            im = overlay_text(im, "Now, meet Sam.", (640, 466), 31, color=WHITE, bold=True,
                              alpha=a, anchor="ma")
    im = safe_face_area(im)
    # Fade from/to black for clean editing handles.
    edge = min(1.0, t / .65, (DURATION - t) / .65)
    if edge < 1:
        black = Image.new("RGBA", (W, H), (3, 9, 22, 255))
        im = Image.blend(black, im, ease(edge))
    return im.convert("RGB")


ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
cmd = [ffmpeg, "-y", "-f", "rawvideo", "-vcodec", "rawvideo", "-pix_fmt", "rgb24",
       "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-an",
       "-vf", "scale=1920:1080:flags=lanczos,format=yuv420p", "-c:v", "libx264",
       "-preset", "medium", "-crf", "19", "-movflags", "+faststart", str(OUT)]
proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
for i in range(FPS * DURATION):
    proc.stdin.write(frame_at(i / FPS).tobytes())
proc.stdin.close()
code = proc.wait()
if code:
    raise SystemExit(code)
print(OUT)
