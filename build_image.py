"""Draw the news-image-20261118 front page with PIL and save entry.png.

Newspaper front page for Wednesday 18 November 2026: lead story is the
Crimean bridge strike, then Iran/Bahrain, Trump in Manila, the Hormuz
tanker, Israel, Cyclone Akvan, Dhoni, plus an "Also today" ticker.
Run:  python3 build_image.py   -> writes entry.png next to this file.
Deterministic: no network, no randomness, no timestamps in the image.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (247, 242, 231)
INK = (17, 17, 17)
RED = (163, 22, 33)
BLUE = (29, 78, 137)
GREEN = (30, 107, 52)
GREY = (90, 84, 74)
LINE = (17, 17, 17)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit `width`."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, width, fill=INK, leading=None):
    """Draw wrapped paragraph; returns y after the last line."""
    lh = leading or int(fnt.size * 1.22)
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += lh
    return y


def kicker(draw, x, y, text, color=RED):
    draw.text((x, y), text, font=font(SANS_B, 19), fill=color)
    return y + 27


def headline(draw, x, y, text, size, width, fill=INK):
    fnt = font(SERIF_B, size)
    lh = int(size * 1.08)
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += lh
    return y


def hrule(draw, y, x0=34, x1=990, width=2):
    draw.line([(x0, y), (x1, y)], fill=LINE, width=width)


def draw_bridge(draw, x, y, w, h):
    """Kerch bridge: deck, arch, collapsed gap in the middle."""
    deck_y = y + h - 40
    draw.line([(x, deck_y), (x + w, deck_y)], fill=INK, width=6)
    draw.arc([x + 10, y + 10, x + w // 2 - 10, deck_y + 30], 180, 360,
             fill=INK, width=5)
    draw.arc([x + w // 2 + 10, y + 10, x + w - 10, deck_y + 30], 180, 300,
             fill=INK, width=5)
    draw.line([(x + w // 2 - 28, deck_y + 18), (x + w // 2 + 28, deck_y + 30)],
              fill=RED, width=6)
    draw.line([(x + w // 2 - 28, deck_y + 30), (x + w // 2 + 28, deck_y + 18)],
              fill=RED, width=6)
    for yy in (deck_y + 48, deck_y + 58):
        draw.arc([x + 10, yy - 8, x + w - 10, yy + 8], 0, 180,
                 fill=BLUE, width=3)
    for px in (x + 30, x + w - 36):
        draw.line([(px, deck_y), (px, deck_y + 44)], fill=INK, width=5)


def draw_radar(draw, x, y, w, h):
    """Radar dish with sweeping arcs."""
    cx, cy = x + w // 2, y + h // 2 + 10
    for r in (18, 34, 50):
        draw.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=BLUE, width=3)
    draw.pieslice([cx - 46, cy - 46, cx + 46, cy + 46], 300, 340, fill=RED)
    draw.line([(cx, cy), (cx + 40, cy - 24)], fill=RED, width=4)
    draw.line([(cx, cy), (cx, cy + 34)], fill=INK, width=5)
    draw.line([(cx - 26, cy + 34), (cx + 26, cy + 34)], fill=INK, width=5)


def draw_flags(draw, x, y, w, h):
    """Four summit flags (Quad: US, India, Japan, Australia)."""
    cols = [RED, (255, 153, 51), (200, 16, 46), BLUE]
    step = w // 4
    for i, c in enumerate(cols):
        fx = x + i * step + 6
        draw.line([(fx, y + 12), (fx, y + h - 22)], fill=INK, width=4)
        draw.polygon([(fx, y + 12), (fx + step - 8, y + 22),
                      (fx, y + 34)], fill=c)


def draw_tanker(draw, x, y, w, h):
    """Tanker with smoke and waves."""
    draw.polygon([(x + 14, y + h - 52), (x + w - 14, y + h - 52),
                  (x + w - 34, y + h - 22), (x + 34, y + h - 22)],
                 fill=INK)
    draw.rectangle([x + w // 2 - 8, y + 34, x + w // 2 + 26, y + h - 52],
                   fill=RED)
    draw.rectangle([x + w // 2 - 26, y + 48, x + w // 2 - 8, y + h - 52],
                   fill=(200, 60, 40))
    for yy in (y + h - 12, y + h - 2):
        draw.arc([x + 6, yy - 8, x + w - 6, yy + 8], 0, 180, fill=BLUE, width=3)
    for cx, cy, r in ((x + w // 2 + 8, y + 22, 10), (x + w // 2 + 22, y + 12, 13)):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREY)


def draw_knesset(draw, x, y, w, h):
    """Parliament building: columns and pediment."""
    draw.polygon([(x + 10, y + 34), (x + w // 2, y + 8),
                  (x + w - 10, y + 34)], fill=INK)
    for i in range(4):
        cx = x + 24 + i * ((w - 48) // 3)
        draw.rectangle([cx - 7, y + 40, cx + 7, y + h - 26], fill=INK)
    draw.rectangle([x + 10, y + h - 26, x + w - 10, y + h - 14], fill=INK)


def draw_cyclone(draw, x, y, w, h):
    """Cyclone spiral."""
    cx, cy = x + w // 2, y + h // 2
    for r, a0, a1 in ((46, 0, 300), (34, 40, 340), (22, 80, 380), (10, 120, 420)):
        draw.arc([cx - r, cy - r, cx + r, cy + r], a0, a1, fill=BLUE, width=5)
    draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=RED)


def draw_cricket(draw, x, y, w, h):
    """Cricket bat, ball and stumps."""
    draw.line([(x + 30, y + 10), (x + 62, y + h - 30)], fill=(150, 110, 60),
              width=12)
    draw.ellipse([x + w - 42, y + 16, x + w - 14, y + 44], fill=RED)
    for i in range(3):
        sx = x + 18 + i * 14
        draw.line([(sx, y + h - 34), (sx, y + h - 8)], fill=INK, width=4)


def story(draw, x, y, kicker_text, color, head, deck, icon=None, icon_xy=None,
          text_w=340, head_size=31, deck_size=20):
    """One story block: kicker, headline, deck, optional icon at right."""
    y = kicker(draw, x, y, kicker_text, color)
    y = headline(draw, x, y, head, head_size, text_w)
    y += 4
    y = para(draw, x, y, deck, font(SERIF, deck_size), text_w)
    if icon is not None and icon_xy is not None:
        icon(draw, icon_xy[0], icon_xy[1], 120, 100)
    return y


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    MX = 34

    # ---- Masthead ----
    title = "THE WORLD"
    tf = font(SERIF_B, 96)
    d.text(((W - d.textlength(title, font=tf)) / 2, 22), title, font=tf, fill=INK)
    df = font(SANS_B, 25)
    date = "WEDNESDAY  \u2022  18 NOVEMBER 2026  \u2022  ONE DAY, ONE PAGE"
    d.text(((W - d.textlength(date, font=df)) / 2, 128), date, font=df, fill=RED)
    hrule(d, 162, width=3)
    hrule(d, 168, width=1)

    # ---- LEAD: Crimea bridge ----
    y = 184
    y = kicker(d, MX, y, "WAR  \u2022  UKRAINE \u2014 RUSSIA", RED)
    y = headline(d, MX, y, "Crimea bridge arch collapses in Ukrainian strike",
                 44, 650)
    y += 6
    y = para(d, MX, y,
             "Kyiv says its missiles and drones destroyed the road arch; "
             "Moscow confirms damage and halts traffic. Russia says it "
             "downed 1,441 drones.",
             font(SERIF, 22), 650)
    draw_bridge(d, 712, 196, 268, 140)
    d.text((712, 366), "Kerch Bridge, Crimea",
           font=font(SANS, 17), fill=GREY)

    hrule(d, 404)

    # ---- Row 2 ----
    y2 = 418
    story(d, MX, y2, "MIDDLE EAST  \u2022  GULF", RED,
          "Iran drones target US radar in Bahrain",
          "Third Iranian strike in days on US targets in Bahrain; "
          "intercepted, with no damage, the US says.",
          icon=draw_radar, icon_xy=(380, 422))
    story(d, 524, y2, "ASIA  \u2022  DIPLOMACY", BLUE,
          "Trump lands in Manila for Quad talks",
          "First Quad leaders' meeting in two years. On Wednesday he meets "
          "Marcos, then heads to Shenzhen.",
          icon=draw_flags, icon_xy=(870, 422))
    hrule(d, 596)

    # ---- Row 3 ----
    y3 = 610
    story(d, MX, y3, "MIDDLE EAST  \u2022  SHIPPING", RED,
          "Hormuz tanker hit twice; one sailor missing",
          "LPG carrier Tara Gas attacked on 16\u201317 Nov; crew abandons "
          "ship, 21 Indians evacuated.",
          icon=draw_tanker, icon_xy=(380, 614))
    story(d, 524, y3, "ISRAEL  \u2022  POLITICS", BLUE,
          "Knesset picks Eisenkot ally as speaker",
          "Matan Kahana wins 66\u201352, a blow to Netanyahu. Britain "
          "sanctions eight settlement firms over E1.",
          icon=draw_knesset, icon_xy=(870, 614))
    hrule(d, 788)

    # ---- Bottom row ----
    y4 = 802
    # Weather (icon left, text indented)
    kicker(d, MX, y4, "WEATHER  \u2022  INDIA", BLUE)
    draw_cyclone(d, MX, y4 + 52, 56, 56)
    headline(d, MX + 64, y4 + 30, "Cyclone Akvan heads for Andhra coast",
             23, 242)
    para(d, MX + 64, y4 + 92,
         "Bay of Bengal storm; landfall Fri 20 Nov, winds 120\u2013130 km/h.",
         font(SERIF, 19), 242)
    # Sport
    kicker(d, 354, y4, "SPORT  \u2022  CRICKET", GREEN)
    draw_cricket(d, 354, y4 + 52, 56, 56)
    headline(d, 354 + 64, y4 + 30, "Dhoni retires from the IPL",
             23, 242)
    para(d, 354 + 64, y4 + 92,
         "CSK great, 45, ends 19-year career with five titles; mentor "
         "in 2027.",
         font(SERIF, 19), 242)
    # Also today
    d.text((674, y4), "ALSO TODAY", font=font(SANS_B, 19), fill=INK)
    d.line([(674, y4 + 27), (980, y4 + 27)], fill=LINE, width=2)
    ticker = [
        "Canada and China extend trade deals as Xi meets Carney.",
        "Amazon to invest $7bn in Indian renewables by 2030.",
        "India re-elected to the ITU Council for 2027\u20132030.",
    ]
    ty = y4 + 36
    for item in ticker:
        end = para(d, 688, ty, item, font(SERIF, 18), 292, leading=22)
        d.text((674, ty), "\u2022", font=font(SERIF_B, 18), fill=RED)
        ty = end + 5

    # ---- Footer ----
    hrule(d, 984, width=1)
    ff = font(SANS, 15)
    foot = ("The day's news as reported overnight and on Wednesday 18 November 2026  "
            "\u2022  Sources: Reuters, AP, BBC, CNN, India's MEA, IMD")
    d.text(((W - d.textlength(foot, font=ff)) / 2, 992), foot, font=ff, fill=GREY)

    img.save("entry.png", format="PNG", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
