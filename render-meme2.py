#!/usr/bin/env python3
"""Render meme #2 untuk gta6-meme-x-01 (akun 7): boarding pass ke Leonida.
Teks tajam via PIL (bukan AI image) supaya terbaca di 480px.
Output: meme2.png (1080x1080). Logo hantu dari press kit resmi make.fun.
"""
from PIL import Image, ImageDraw, ImageFont
import os
import random

W, H = 1080, 1080
ASSETS = os.path.expanduser('~/workspace/makefun/meme-x-assets')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'meme2.png')

DARK = (27, 16, 48)
PAPER = (245, 242, 235)
INK = (30, 26, 38)
MAGENTA = (214, 51, 132)
LABEL = (120, 110, 130)
WHITE = (255, 255, 255)
DIVIDER = (210, 202, 190)


def font(name, size):
    paths = [
        f'/usr/share/fonts/truetype/noto/NotoSans-{name}.ttf',
        f'/usr/share/fonts/truetype/dejavu/DejaVuSans-{name}.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


img = Image.new('RGB', (W, H), PAPER)
d = ImageDraw.Draw(img)

MX = 64  # margin x

# --- header band: ghost + make.fun + BOARDING PASS ---
d.rectangle([0, 0, W, 168], fill=DARK)
ghost = Image.open(os.path.join(ASSETS, 'mark-1024.png')).convert('RGBA')
ghost = ghost.resize((112, 112), Image.LANCZOS)
img.paste(ghost, (MX, 28), ghost)
d.text((MX + 132, 34), 'make.fun', font=font('Bold', 44), fill=WHITE)
d.text((MX + 132, 92), 'AIRLINES  •  EST. 2013  •  STILL WAITING', font=font('Regular', 24), fill=(158, 146, 172))
d.text((W - MX, 44), 'BOARDING', font=font('Black', 40), fill=MAGENTA, anchor='ra')
d.text((W - MX, 92), 'PASS', font=font('Black', 40), fill=MAGENTA, anchor='ra')

# --- route ---
d.text((MX, 225), '2013', font=font('Black', 100), fill=INK)
d.line([(340, 272), (520, 272)], fill=MAGENTA, width=10)
d.polygon([(520, 245), (520, 299), (552, 272)], fill=MAGENTA)
d.text((W - MX, 225), 'LEONIDA', font=font('Black', 100), fill=INK, anchor='ra')
d.text((MX, 352), 'DEPARTED 17 SEP 2013  •  ARRIVING 19 NOV 2026', font=font('Bold', 26), fill=LABEL)

# --- dashed divider ---
y = 418
x = MX
while x < W - MX:
    d.line([(x, y), (min(x + 22, W - MX), y)], fill=DIVIDER, width=3)
    x += 36

# --- fields grid ---
fields = [
    ('PASSENGER', 'ME  (AGE 15 TO 28)'),
    ('FLIGHT', 'GTA VI  •  GTAVI-001'),
    ('GATE', 'DELAYED ×2'),
    ('SEAT', '13 YEARS'),
    ('BOARDING', '19 NOV 2026'),
    ('BAGGAGE', '1 CHILDHOOD  (LOST)'),
]
col_x = [MX, W // 2 + 20]
row_y = [452, 588, 724]
for i, (label, value) in enumerate(fields):
    cx = col_x[i % 2]
    cy = row_y[i // 2]
    d.text((cx, cy), label, font=font('Bold', 25), fill=LABEL)
    d.text((cx, cy + 32), value, font=font('Bold', 40), fill=INK)

# --- punchline bar ---
bar_y0, bar_y1 = 856, 952
d.rounded_rectangle([(MX, bar_y0), (W - MX, bar_y1)], radius=22, fill=MAGENTA)
d.text((W // 2, bar_y0 + 16), 'FARE $79.99 — PAID BY MY AGENT', font=font('Bold', 34), fill=WHITE, anchor='ma')
d.text((W // 2, bar_y0 + 58), 'ON make.fun  —  REAL MONEY, REAL BOUNTIES.', font=font('Bold', 26), fill=WHITE, anchor='ma')

# --- barcode strip ---
random.seed(13)
bx = MX + 40
while bx < W - MX - 260:
    w = random.choice([3, 5, 8, 12])
    d.rectangle([bx, 984, bx + w, 1044], fill=INK)
    bx += w + random.choice([4, 7, 10])
d.text((W - MX, 1000), 'GTAVI-001', font=font('Bold', 26), fill=INK, anchor='ra')

img.save(OUT, 'PNG')
print('saved', OUT, img.size, os.path.getsize(OUT), 'bytes')
