#!/usr/bin/env python3
"""Generates the SVG assets for github.com/kyong-min profile README."""
import os
from xml.sax.saxutils import escape as esc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
os.makedirs(OUT, exist_ok=True)

MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'DejaVu Sans Mono','Liberation Mono',monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
CW = 0.602  # mono char width per em

THEMES = {
    "dark": dict(bg="#0d1117", card="#0d1117", border="#30363d", text="#e6edf3", muted="#8b949e",
                 faint="#6e7681", chip="#161b22", chipb="#30363d", accent="#58a6ff", green="#3fb950",
                 iconbg="#161b22", rowline="#21262d", head="#161b22", gold="#e3b341", silver="#b1bac4"),
    "light": dict(bg="#ffffff", card="#ffffff", border="#d0d7de", text="#1f2328", muted="#59636e",
                  faint="#818b98", chip="#f6f8fa", chipb="#d0d7de", accent="#0969da", green="#1a7f37",
                  iconbg="#f6f8fa", rowline="#eaeef2", head="#f6f8fa", gold="#9a6700", silver="#6e7781"),
}
# terminal (always dark)
T = dict(bg="#0a0e13", bar="#11161d", line="#1c232c", text="#e6edf3", muted="#7d8590", dim="#3d444d",
         blue="#79c0ff", green="#7ee787", teal="#39d3bb", amber="#e3b341", red="#ff7b72")


def write(name, body):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(body)


def svg(w, h, inner, style=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'fill="none" role="img">\n<style>.m{{font-family:{MONO}}}.s{{font-family:{SANS}}}{style}</style>\n'
            f'{inner}\n</svg>\n')


def txt(x, y, s, size, fill, cls="s", weight=400, anchor="start", extra=""):
    return (f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" {extra}>{esc(s)}</text>')


def chips(x, y, items, c, size=11, gap=6, h=22):
    out, cx = [], x
    for it in items:
        w = len(it) * size * CW + 18
        out.append(f'<rect x="{cx}" y="{y}" width="{w:.1f}" height="{h}" rx="{h/2}" fill="{c["chip"]}" stroke="{c["chipb"]}"/>')
        out.append(txt(cx + w / 2, y + h / 2 + size * 0.36, it, size, c["text"], "m", 500, "middle"))
        cx += w + gap
    return "\n".join(out), cx


def tchips(x, y, items, size=10.5, h=19):
    """chips inside the dark terminal"""
    out, cx = [], x
    for it in items:
        w = len(it) * size * CW + 14
        out.append(f'<rect x="{cx}" y="{y}" width="{w:.1f}" height="{h}" rx="3" fill="#0f141a" stroke="{T["dim"]}"/>')
        out.append(txt(cx + w / 2, y + h / 2 + size * 0.36, it, size, T["text"], "m", 500, "middle"))
        cx += w + 6
    return "\n".join(out)


# --------------------------------------------------------------------------- pixel font
FONT = {
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "G": ["01110", "10001", "10000", "10111", "10001", "10001", "01111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
}


def pixel_word(word, x0, y0, px, fill, shadow):
    back, front = [], []
    for i, ch in enumerate(word):
        for r, row in enumerate(FONT[ch]):
            for col, bit in enumerate(row):
                if bit == "1":
                    x = x0 + (i * 6 + col) * px
                    y = y0 + r * px
                    back.append(f'<rect x="{x+4}" y="{y+4}" width="{px}" height="{px}"/>')
                    front.append(f'<rect x="{x}" y="{y}" width="{px-1.2}" height="{px-1.2}"/>')
    return (f'<g fill="{shadow}" stroke="#39d3bb" stroke-opacity=".35" stroke-width=".8">{"".join(back)}</g>'
            f'<g fill="{fill}" filter="url(#glow)">{"".join(front)}</g>')


# --------------------------------------------------------------------------- hero
def hero():
    W, H = 1200, 580
    style = """
.ln{opacity:0;animation:in .01s linear forwards}
@keyframes in{to{opacity:1}}
.cur{animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
.scan{animation:scan 4s ease-in-out infinite}
@keyframes scan{0%{transform:translateY(0);opacity:0}8%{opacity:1}85%{opacity:1}100%{transform:translateY(196px);opacity:0}}
.bx{opacity:0;animation:bx 8s infinite}
@keyframes bx{0%,100%{opacity:0}20%,80%{opacity:1}}
.cap{opacity:0;animation:cap 16s infinite}
@keyframes cap{0%{opacity:0}2%,23%{opacity:1}25%,100%{opacity:0}}
.seg{animation:seg 16s infinite}
@keyframes seg{0%{fill:#39d3bb}24.9%{fill:#39d3bb}25%,100%{fill:#2a313a}}
.lbl{animation:lbl 16s infinite}
@keyframes lbl{0%{fill:#e6edf3}24.9%{fill:#e6edf3}25%,100%{fill:#4d5562}}
.bar1{animation:grow 8s ease-out infinite}
@keyframes grow{0%,10%{transform:scaleX(0)}40%,90%{transform:scaleX(1)}100%{transform:scaleX(1)}}
"""
    o = []
    o.append('<defs><linearGradient id="ng" x1="0" y1="0" x2="1" y2="1">'
             '<stop offset="0" stop-color="#d2fff1"/><stop offset=".45" stop-color="#7ee7c7"/>'
             '<stop offset="1" stop-color="#58a6ff"/></linearGradient>'
             '<filter id="glow" x="-10%" y="-10%" width="120%" height="120%">'
             '<feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/>'
             '<feMergeNode in="SourceGraphic"/></feMerge></filter>'
             '<clipPath id="doc"><rect x="752" y="78" width="300" height="214" rx="4"/></clipPath>'
             '<linearGradient id="sl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#39d3bb" stop-opacity="0"/>'
             '<stop offset="1" stop-color="#39d3bb" stop-opacity=".55"/></linearGradient></defs>')
    o.append(f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="{T["bg"]}" stroke="#262c34"/>')
    # title bar
    o.append(f'<path d="M14 .5h{W-28}a13.5 13.5 0 0 1 13.5 13.5v24H.5V14A13.5 13.5 0 0 1 14 .5z" fill="{T["bar"]}"/>')
    o.append(f'<line x1="0" y1="38" x2="{W}" y2="38" stroke="{T["line"]}"/>')
    for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        o.append(f'<circle cx="{24+i*20}" cy="19" r="6" fill="{c}"/>')
    o.append(txt(W / 2, 23, "kyungmin@kyonggi: ~/insight-lab — zsh", 12, T["muted"], "m", 400, "middle"))

    # name
    o.append(pixel_word("KYUNGMIN", 38, 66, 11, "url(#ng)", "#0e3b3a"))
    o.append(pixel_word("KANG", 38, 158, 11, "url(#ng)", "#0e3b3a"))
    o.append(txt(320, 226, "AI · vision-language · carbon", 12, T["muted"], "m"))

    # shell lines
    P = T["green"]
    lines = [
        [("❯ ", P), ("whoami", T["text"])],
        [("Kyungmin Kang", T["text"]), ("  ·  AI undergrad, Kyonggi Univ.  ·  PM @ INSIGHT LAB", T["muted"])],
        [("❯ ", P), ("cat focus.txt", T["text"])],
        [("Vision-language models that turn messy paperwork into verified numbers.", T["muted"])],
        [("❯ ", P), ("ls ~/building", T["text"])],
        [("carbix/   upright/   tinyllama-qlora/   pick-dream/", T["blue"])],
        [("❯ ", P), ("next --stop", T["text"])],
        [("CES 2027 · Las Vegas", T["amber"]), ("  (carbix, selected)", T["muted"])],
    ]
    y = 278
    for i, parts in enumerate(lines):
        x = 40
        segs = []
        for s, col in parts:
            segs.append(f'<tspan fill="{col}">{esc(s)}</tspan>')
        delay = 0.25 + i * 0.32
        o.append(f'<text class="m ln" x="{x}" y="{y}" font-size="14" style="animation-delay:{delay:.2f}s">{"".join(segs)}</text>')
        y += 27 if i % 2 == 1 else 23
    o.append(f'<text class="m ln" x="40" y="{y+4}" font-size="14" style="animation-delay:2.9s">'
             f'<tspan fill="{P}">❯ </tspan><tspan fill="{T["text"]}">_</tspan></text>')
    o.append(f'<rect class="cur" x="58" y="{y-9}" width="9" height="16" fill="{T["text"]}"/>')

    # ---------------- right panel: document scan
    X0 = 700
    # corner frame
    for (cx, cy, dx, dy) in [(X0, 52, 1, 1), (1160, 52, -1, 1), (X0, 312, 1, -1), (1160, 312, -1, -1)]:
        o.append(f'<path d="M{cx} {cy+14*dy}V{cy}H{cx+14*dx}" stroke="{T["muted"]}" stroke-width="1.2"/>')
    o.append(txt(X0 + 22, 66, "scan  bill_2026-05.jpg", 10, T["muted"], "m"))
    o.append(txt(1140, 66, "model carbix-vlm-ft · demo", 10, T["muted"], "m", 400, "end"))
    # paper
    o.append('<g clip-path="url(#doc)">')
    o.append('<rect x="752" y="78" width="300" height="214" rx="4" fill="#e9eef2"/>')
    o.append('<rect x="752" y="78" width="300" height="30" fill="#c9d6dd"/>')
    o.append('<rect x="766" y="88" width="90" height="10" rx="2" fill="#6b7d88"/>')
    o.append('<rect x="980" y="88" width="58" height="10" rx="2" fill="#8fa1ab"/>')
    for i, w in enumerate([150, 110, 170]):
        o.append(f'<rect x="766" y="{120+i*13}" width="{w}" height="6" rx="2" fill="#a8b6be"/>')
    # table
    o.append('<rect x="766" y="170" width="272" height="62" fill="none" stroke="#a8b6be"/>')
    for i in range(1, 4):
        o.append(f'<line x1="766" y1="{170+i*15.5}" x2="1038" y2="{170+i*15.5}" stroke="#c4ced4"/>')
    o.append('<line x1="900" y1="170" x2="900" y2="232" stroke="#c4ced4"/>')
    for i in range(4):
        o.append(f'<rect x="774" y="{175+i*15.5}" width="{70+(i%2)*30}" height="5" rx="2" fill="#94a3ab"/>')
        o.append(f'<rect x="{990-(i%3)*12}" y="{175+i*15.5}" width="{40+(i%3)*12}" height="5" rx="2" fill="#94a3ab"/>')
    o.append('<rect x="930" y="248" width="108" height="26" rx="3" fill="#d4dde2" stroke="#8fa1ab"/>')
    o.append('<text x="984" y="266" class="m" font-size="12" font-weight="700" fill="#33444e" text-anchor="middle">1,284 kWh</text>')
    o.append('<rect class="scan" x="752" y="58" width="300" height="34" fill="url(#sl)"/>')
    o.append('</g>')
    # detection boxes
    boxes = [(762, 84, 100, 18, "supplier", 0.0), (762, 114, 182, 36, "period", 0.6),
             (926, 244, 116, 34, "usage.kWh", 1.2), (762, 166, 280, 70, "line_items", 1.8)]
    for (bx, by, bw, bh, lab, d) in boxes:
        lw = len(lab) * 9.5 * CW + 10
        o.append(f'<g class="bx" style="animation-delay:{d}s">'
                 f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" stroke="{T["teal"]}" stroke-width="1.5" stroke-dasharray="4 3"/>'
                 f'<rect x="{bx}" y="{by-14}" width="{lw:.1f}" height="14" fill="{T["teal"]}"/>'
                 f'{txt(bx+5, by-3.5, lab, 9.5, "#04201c", "m", 700)}</g>')
    # extraction output
    oy = 334
    rows = [("scope_2.electricity", "1,284 kWh", T["text"]),
            ("× grid factor", "0.459 kgCO2e/kWh", T["muted"]),
            ("= emissions", "0.59 tCO2e  ✓", T["green"])]
    for i, (k, v, col) in enumerate(rows):
        o.append(txt(X0 + 4, oy + i * 19, k, 12, T["muted"], "m"))
        o.append(txt(1160, oy + i * 19, v, 12, col, "m", 600 if i == 2 else 400, "end"))
    o.append(f'<g style="transform-origin:{X0+4}px 0"><rect class="bar1" style="transform-origin:{X0+4}px 0" x="{X0+4}" y="{oy+44}" width="456" height="3" rx="1.5" fill="{T["teal"]}"/></g>')

    # rotating capability captions
    caps = [
        ("01/04", "VISION", "segment & read real-world documents",
         ["YOLOv11-seg", "YOLOE", "OpenCV", "MediaPipe"], "↳ carbix · upright"),
        ("02/04", "LANGUAGE", "VLMs and LLMs that output structure",
         ["Gemini API", "VLM fine-tune", "QLoRA", "LangChain"], "↳ carbix · pick-dream · tinyllama-qlora"),
        ("03/04", "CLOUD", "containerised, deployed, monitored",
         ["GCP", "Docker", "PMLE", "PDE"], "↳ google cloud certified ×2"),
        ("04/04", "ASSURANCE", "test it before you trust it",
         ["CSTS", "QA", "data augmentation", "validation"], "↳ certified software test specialist"),
    ]
    cy = 418
    for i, (n, name, sub, items, link) in enumerate(caps):
        o.append(f'<g class="cap" style="animation-delay:{i*4}s">')
        o.append(f'<text x="{X0+4}" y="{cy}" class="m" font-size="11"><tspan fill="{T["blue"]}">{n}</tspan>'
                 f'<tspan fill="{T["muted"]}"> — </tspan><tspan fill="{T["text"]}" font-weight="700">{name}</tspan></text>')
        o.append(txt(X0 + 4, cy + 17, sub, 11, T["muted"], "m"))
        o.append(tchips(X0 + 4, cy + 26, items))
        o.append(txt(X0 + 4, cy + 62, link, 11, T["green"], "m"))
        o.append('</g>')
    labels = ["vision", "language", "cloud", "assurance"]
    for i, lab in enumerate(labels):
        sx = X0 + 4 + i * 116
        o.append(f'<rect class="seg" style="animation-delay:{i*4}s" x="{sx}" y="502" width="106" height="2" fill="#2a313a"/>')
        o.append(f'<text class="m lbl" style="animation-delay:{i*4}s" x="{sx}" y="519" font-size="10.5" fill="#4d5562">{lab}</text>')

    # status bar
    o.append(f'<path d="M.5 540H{W-.5}v26a13.5 13.5 0 0 1-13.5 13.5H14A13.5 13.5 0 0 1 .5 566z" fill="{T["bar"]}"/>')
    o.append(f'<line x1="0" y1="540" x2="{W}" y2="540" stroke="{T["line"]}"/>')
    o.append(f'<text x="18" y="564" class="m" font-size="11.5"><tspan fill="{T["green"]}">[kk]</tspan>'
             f'<tspan fill="{T["text"]}" font-weight="700"> 0:carbix*</tspan>'
             f'<tspan fill="{T["muted"]}">   1:upright   2:qlora   3:pick-dream   4:ucsd</tspan></text>')
    o.append(f'<text x="{W-18}" y="564" class="m" font-size="11.5" text-anchor="end">'
             f'<tspan fill="{T["green"]}">●</tspan><tspan fill="{T["muted"]}"> suwon, kr   </tspan>'
             f'<tspan fill="{T["amber"]}">▲ gold · KIIT 2026</tspan><tspan fill="{T["dim"]}">   │   </tspan>'
             f'<tspan fill="{T["muted"]}">github.com/kyong-min</tspan></text>')
    write("hero.svg", svg(W, H, "\n".join(o), style))


# --------------------------------------------------------------------------- icons (24x24 stroke)
ICONS = {
    "vlm": '<rect x="4" y="3" width="11" height="15" rx="1.5"/><path d="M7 7h5M7 10h5M7 13h3"/><circle cx="16.5" cy="16.5" r="3.5"/><path d="M19 19l2.5 2.5"/>',
    "cv": '<path d="M3 8V4h4M17 4h4v4M21 16v4h-4M7 20H3v-4"/><rect x="8" y="8" width="8" height="8" rx="1"/>',
    "llm": '<path d="M4 5h16v10H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
    "cloud": '<path d="M7 18h10a4 4 0 0 0 .6-7.95A6 6 0 0 0 6.2 9.2 4.5 4.5 0 0 0 7 18z"/><path d="M12 11v5M9.5 13.5L12 11l2.5 2.5"/>',
    "qa": '<path d="M12 3l7 3v5c0 4.5-3 8.2-7 10-4-1.8-7-5.5-7-10V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
}


def icon(x, y, key, c):
    return (f'<rect x="{x}" y="{y}" width="38" height="38" rx="8" fill="{c["iconbg"]}" stroke="{c["border"]}"/>'
            f'<g transform="translate({x+7} {y+7})" stroke="{c["text"]}" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" fill="none">{ICONS[key]}</g>')


def card(x, y, w, h, c):
    return f'<rect x="{x+.5}" y="{y+.5}" width="{w-1}" height="{h-1}" rx="10" fill="{c["card"]}" stroke="{c["border"]}"/>'


def about(theme):
    c = THEMES[theme]
    W, H = 1200, 372
    items = [
        ("vlm", "Vision-Language Models", ["Fine-tuned VLMs that read energy bills,", "invoices and transport documents."]),
        ("cv", "Computer Vision", ["YOLOv11-seg · YOLOE · OpenCV ·", "MediaPipe real-time pose metrics"]),
        ("llm", "LLM Applications", ["Prompt engineering, LangChain,", "natural language → structured action"]),
        ("cloud", "Cloud & MLOps", ["Google Cloud Professional ML Engineer", "& Data Engineer · Docker on GCP"]),
        ("qa", "Software Assurance", ["CSTS-certified tester · model validation", "and QA for web & mobile releases"]),
    ]
    o = []
    layout = [(0, 0, 590), (605, 0, 290), (910, 0, 290), (0, 190, 440), (455, 190, 745)]
    for (key, title, desc), (x, y, w) in zip(items, layout):
        o.append(card(x, y, w, 182, c))
        o.append(icon(x + 22, y + 22, key, c))
        o.append(txt(x + 22, y + 96, title, 16, c["text"], "s", 600))
        for i, d in enumerate(desc):
            o.append(txt(x + 22, y + 122 + i * 20, d, 13, c["muted"]))
    write(f"about-{theme}.svg", svg(W, H, "\n".join(o)))


def stack(theme):
    c = THEMES[theme]
    rows = [
        ("vlm", "Vision-Language", ["Gemini API", "VLM fine-tuning", "Hugging Face", "Prompt engineering", "Data augmentation"]),
        ("cv", "Vision", ["YOLOv11-seg", "YOLOE", "OpenCV", "MediaPipe", "OCR"]),
        ("llm", "ML & LLM", ["PyTorch", "TensorFlow", "Keras", "QLoRA / PEFT", "LangChain", "DistilBERT"]),
        ("cloud", "Cloud", ["Google Cloud", "Docker", "PMLE", "PDE"]),
        ("qa", "Assurance", ["CSTS", "Test design", "Web & mobile QA", "Model validation"]),
        ("cv", "Apps & Languages", ["Python", "Kotlin", "Java", "Android Studio", "Next.js", "Flutter"]),
    ]
    W = 1200
    rh = 46
    H = 44 + rh * len(rows) + 1
    o = [card(0, 0, W, H, c)]
    o.append(f'<path d="M10.5 .5h{W-21}a10 10 0 0 1 10 10V44H.5V10.5a10 10 0 0 1 10-10z" fill="{c["head"]}" stroke="{c["border"]}"/>')
    o.append(txt(24, 27, "Layer", 12, c["muted"], "s", 600))
    o.append(txt(250, 27, "Technologies", 12, c["muted"], "s", 600))
    for i, (key, name, items) in enumerate(rows):
        y = 44 + i * rh
        if i:
            o.append(f'<line x1="1" y1="{y}" x2="{W-1}" y2="{y}" stroke="{c["rowline"]}"/>')
        o.append(f'<g transform="translate(24 {y+15}) scale(.66)" stroke="{c["muted"]}" stroke-width="2" '
                 f'stroke-linecap="round" stroke-linejoin="round" fill="none">{ICONS[key]}</g>')
        o.append(txt(52, y + 28, name, 13.5, c["text"], "s", 500))
        ch, _ = chips(250, y + 12, items, c)
        o.append(ch)
    write(f"stack-{theme}.svg", svg(W, H, "\n".join(o)))


def mini_term(x, y, w, h, title, lines, c=None):
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{T["bg"]}" stroke="#262c34"/>',
         f'<path d="M{x+8} {y}h{w-16}a8 8 0 0 1 8 8v18H{x}V{y+8}a8 8 0 0 1 8-8z" fill="{T["bar"]}"/>']
    for i, col in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        o.append(f'<circle cx="{x+16+i*13}" cy="{y+13}" r="4" fill="{col}"/>')
    o.append(txt(x + w - 12, y + 17, title, 10, T["muted"], "m", 400, "end"))
    o.append(lines)
    return "\n".join(o)


def badge(x, y, label, c, fill=None, tc=None):
    w = len(label) * 11 * 0.62 + 18
    return (f'<rect x="{x}" y="{y}" width="{w:.1f}" height="22" rx="11" fill="{fill or c["chip"]}" stroke="{c["chipb"]}"/>'
            + txt(x + w / 2, y + 15, label, 11, tc or c["text"], "s", 600, "middle")), w


def button(x, y, label, c):
    w = len(label) * 12.5 * 0.55 + 30
    return (f'<rect x="{x-w}" y="{y}" width="{w:.1f}" height="32" rx="6" fill="{c["card"]}" stroke="{c["border"]}"/>'
            + txt(x - w / 2, y + 21, label, 12.5, c["text"], "s", 500, "middle"))


def logo_box(x, y, inner, c):
    return (f'<rect x="{x}" y="{y}" width="58" height="58" rx="12" fill="{c["iconbg"]}" stroke="{c["border"]}"/>'
            f'<g transform="translate({x+9} {y+9})">{inner}</g>')


CARBIX_LOGO = ('<circle cx="20" cy="20" r="17" fill="none" stroke="#2ea043" stroke-width="3"/>'
               '<path d="M27 13.5a9 9 0 1 0 0 13" stroke="#2ea043" stroke-width="3.2" stroke-linecap="round" fill="none"/>'
               '<path d="M20 9c4 3 4 8 0 11" stroke="#39d3bb" stroke-width="2" fill="none" stroke-linecap="round"/>')


def carbix(theme):
    c = THEMES[theme]
    W, H = 1200, 400
    o = [card(0, 0, W, H, c)]
    o.append(logo_box(24, 24, CARBIX_LOGO, c))
    o.append(txt(98, 50, "Carbix", 24, c["text"], "s", 600))
    b, bw = badge(186, 32, "Flagship · PM & team lead", c)
    o.append(b)
    o.append(txt(98, 74, "Scope 1·2·3 carbon accounting from a photo of the paperwork.", 14, c["muted"]))
    # right badge
    b2, w2 = badge(0, 0, "★ Selected for CES 2027", c, "#9a6700" if theme == "light" else "#3d2e00", "#fff8c5" if theme == "dark" else "#ffffff")
    o.append(f'<g transform="translate({W-24-w2:.1f} 24)">{b2}</g>')
    desc = [
        "A multimodal VLM platform that turns SME suppliers' unstructured energy bills",
        "and transport documents into Scope 1·2·3 emissions. YOLOv11-seg isolates the",
        "regions that matter, a fine-tuned VLM extracts the fields, and T-map routing",
        "computes Scope 3 transport. Shipped as a Next.js web app and a Flutter mobile app.",
    ]
    for i, d in enumerate(desc):
        o.append(txt(98, 118 + i * 21, d, 13.5, c["text"]))
    o.append(txt(98, 218, "I proposed the idea and led a 7-person team across AI, software and business:", 13.5, c["muted"]))
    o.append(txt(98, 239, "augmentation pipeline for the VLM dataset, model validation, QA, and every pitch.", 13.5, c["muted"]))
    # outcomes
    outs = [("🥇", "Gold Prize", "KIIT 2026 · 1st author"), ("🏆", "2nd place", "SW Sangsang-Gieop 2026"),
            ("📄", "Patent", "KIPO 10-2026-0202274"), ("©", "SW copyright", "C-2026-037429")]
    for i, (e, a, s) in enumerate(outs):
        ox = 98 + i * 158
        o.append(f'<rect x="{ox}" y="262" width="150" height="52" rx="8" fill="{c["chip"]}" stroke="{c["chipb"]}"/>')
        o.append(txt(ox + 12, 283, a, 12.5, c["text"], "s", 600))
        o.append(txt(ox + 12, 302, s, 11, c["muted"], "s"))
    o.append(f'<line x1="1" y1="340" x2="{W-1}" y2="340" stroke="{c["rowline"]}"/>')
    ch, _ = chips(24, 356, ["VLM fine-tuning", "YOLOv11-seg", "Gemini API", "Next.js", "Flutter"], c)
    o.append(ch)
    o.append(button(W - 24, 351, "INSIGHT LAB  →", c))
    # terminal
    tx, ty, tw, th = 760, 70, 416, 250
    L = []
    def tl(i, parts):
        segs = "".join(f'<tspan fill="{col}">{esc(s)}</tspan>' for s, col in parts)
        L.append(f'<text x="{tx+16}" y="{ty+50+i*21}" class="m" font-size="11.5">{segs}</text>')
    tl(0, [("$ ", T["green"]), ("carbix scan ./bills/2026-05/*.jpg", T["text"])])
    tl(1, [("✓ ", T["green"]), ("segment  ", T["muted"]), ("YOLOv11-seg   ", T["blue"]), ("12 regions", T["text"])])
    tl(2, [("✓ ", T["green"]), ("extract  ", T["muted"]), ("carbix-vlm    ", T["blue"]), ("supplier·period·kWh", T["text"])])
    tl(3, [("✓ ", T["green"]), ("route    ", T["muted"]), ("T-map         ", T["blue"]), ("48.2 km", T["text"])])
    for i, (lab, val, frac, col) in enumerate([("scope 1", "0.8 t", .33, T["amber"]), ("scope 2", "2.4 t", 1.0, T["teal"]), ("scope 3", "0.6 t", .25, T["blue"])]):
        yy = ty + 140 + i * 21
        L.append(txt(tx + 16, yy, lab, 11.5, T["muted"], "m"))
        L.append(f'<rect x="{tx+86}" y="{yy-9}" width="230" height="10" rx="2" fill="#1c232c"/>')
        L.append(f'<rect x="{tx+86}" y="{yy-9}" width="{230*frac:.0f}" height="10" rx="2" fill="{col}"/>')
        L.append(txt(tx + tw - 16, yy, val, 11.5, T["text"], "m", 400, "end"))
    L.append(f'<line x1="{tx+16}" y1="{ty+210}" x2="{tx+tw-16}" y2="{ty+210}" stroke="#1c232c"/>')
    L.append(f'<text x="{tx+16}" y="{ty+232}" class="m" font-size="11.5"><tspan fill="{T["muted"]}">total </tspan>'
             f'<tspan fill="{T["text"]}" font-weight="700">3.8 tCO2e</tspan><tspan fill="{T["green"]}">  ✓ ready for report</tspan></text>')
    o.append(mini_term(tx, ty, tw, th, "~/carbix · demo", "\n".join(L)))
    write(f"carbix-{theme}.svg", svg(W, H, "\n".join(o)))


def awards(theme):
    c = THEMES[theme]
    rows = [
        ("Sep 2026", "Top Excellence Award · 2nd place", "SW Sangsang-Gieop SW/IT Startup Competition — Carbix, selected for CES 2027", c["gold"]),
        ("Jun 2026", "Gold Prize", "KIIT Undergraduate Paper Competition — Carbix, first author", c["gold"]),
        ("May 2026", "Outstanding Paper Award", "KAICTS Spring Conference — Upright, real-time posture correction", c["accent"]),
        ("Jul 2025", "Achievement Award", "Qualcomm Institute AI Entrepreneurship Program, UC San Diego", c["accent"]),
        ("Jun 2025", "Silver Prize", "KIIT Undergraduate Paper Competition — PickDream, LLM classroom booking", c["silver"]),
    ]
    W, rh = 1200, 58
    H = 20 + rh * len(rows) + 8
    o = [card(0, 0, W, H, c)]
    o.append(f'<line x1="132" y1="34" x2="132" y2="{H-34}" stroke="{c["border"]}" stroke-width="2"/>')
    for i, (d, t, s, col) in enumerate(rows):
        y = 20 + i * rh
        o.append(txt(110, y + 26, d, 12, c["muted"], "m", 400, "end"))
        o.append(f'<circle cx="132" cy="{y+22}" r="7" fill="{c["card"]}" stroke="{col}" stroke-width="3"/>')
        o.append(txt(156, y + 21, t, 15, c["text"], "s", 600))
        o.append(txt(156, y + 41, s, 13, c["muted"]))
    write(f"awards-{theme}.svg", svg(W, H, "\n".join(o)))


# --------------------------------------------------------------------------- project cards
def project(theme, key, title, badge_txt, tagline, desc, tags, btn, visual, award=None, logo=None):
    c = THEMES[theme]
    W, H = 590, 360
    o = [card(0, 0, W, H, c)]
    o.append(logo_box(20, 20, logo, c))
    o.append(txt(92, 44, title, 18, c["text"], "s", 600))
    b, bw = badge(92 + len(title) * 18 * 0.56 + 10, 28, badge_txt, c)
    o.append(b)
    o.append(txt(92, 66, tagline, 12.5, c["muted"]))
    if award:
        b2, w2 = badge(0, 0, award, c)
        o.append(f'<g transform="translate({W-20-w2:.1f} 26)">{b2}</g>')
    for i, d in enumerate(desc):
        o.append(txt(20, 104 + i * 19, d, 13, c["text"]))
    o.append(visual)
    o.append(f'<line x1="1" y1="308" x2="{W-1}" y2="308" stroke="{c["rowline"]}"/>')
    ch, _ = chips(20, 321, tags, c, 10.5, 5, 21)
    o.append(ch)
    o.append(button(W - 20, 316, btn, c))
    write(f"proj-{key}-{theme}.svg", svg(W, H, "\n".join(o)))


def emoji_logo(sym, col):
    return f'<text x="20" y="29" font-size="24" text-anchor="middle" fill="{col}" class="s" font-weight="700">{esc(sym)}</text>'


def projects(theme):
    c = THEMES[theme]
    vx, vy, vw, vh = 20, 168, 550, 126

    # Upright: stick figure + angle
    L = []
    hx, hy = vx + 120, vy + 58
    L.append(f'<line x1="{vx+70}" y1="{vy+112}" x2="{vx+92}" y2="{vy+70}" stroke="{T["muted"]}" stroke-width="2"/>')
    L.append(f'<line x1="{vx+92}" y1="{vy+70}" x2="{hx}" y2="{hy}" stroke="{T["teal"]}" stroke-width="2.5"/>')
    L.append(f'<circle cx="{hx+6}" cy="{hy-12}" r="11" stroke="{T["teal"]}" stroke-width="2"/>')
    for (px, py) in [(vx + 92, vy + 70), (hx, hy), (vx + 70, vy + 112)]:
        L.append(f'<circle cx="{px}" cy="{py}" r="3.5" fill="{T["green"]}"/>')
    L.append(f'<line x1="{vx+92}" y1="{vy+70}" x2="{vx+150}" y2="{vy+70}" stroke="{T["dim"]}" stroke-dasharray="3 3"/>')
    L.append(f'<path d="M{vx+122} {vy+70}A30 30 0 0 0 {vx+114} {vy+49}" stroke="{T["amber"]}" stroke-width="1.5"/>')
    L.append(txt(vx + 156, vy + 66, "CVA", 9.5, T["amber"], "m"))
    for i, (k, v, col) in enumerate([("cva", "48.2°", T["amber"]), ("head_tilt", "11.4°", T["text"]),
                                    ("shoulder_Δ", "2.1 cm", T["text"]), ("status", "forward head ⚠", T["red"])]):
        L.append(txt(vx + 230, vy + 50 + i * 19, k, 11, T["muted"], "m"))
        L.append(txt(vx + vw - 16, vy + 50 + i * 19, v, 11, col, "m", 600 if i == 3 else 400, "end"))
    up = mini_term(vx, vy, vw, vh, "~/upright · demo", "\n".join(L))
    project(theme, "upright", "Upright", "Pose", "Real-time AI posture correction.",
            ["A MediaPipe-based algorithm that scores forward-head posture in real",
             "time from multi-angle quantitative metrics, in a full web application."],
            ["Python", "MediaPipe", "OpenCV", "Web"], "View repository  →", up,
            "Outstanding Paper · KAICTS", emoji_logo("⌇", "#39d3bb"))

    # PickDream
    L = []
    L.append(f'<text x="{vx+16}" y="{vy+48}" class="m" font-size="11"><tspan fill="{T["green"]}">user ❯ </tspan>'
             f'<tspan fill="{T["text"]}">tomorrow 3pm, 30 people, need a projector</tspan></text>')
    L.append(f'<text x="{vx+16}" y="{vy+72}" class="m" font-size="11"><tspan fill="{T["muted"]}">llm  ❯ </tspan>'
             f'<tspan fill="{T["blue"]}">{{date:"+1d", time:"15:00", seats:30, projector:true}}</tspan></text>')
    for i, (room, ok, note) in enumerate([("8405", "✓", "32 seats · projector"), ("8210", "✓", "40 seats · projector"), ("6114", "✗", "24 seats")]):
        col = T["green"] if ok == "✓" else T["red"]
        L.append(f'<text x="{vx+16}" y="{vy+96+i*0}" class="m" font-size="11"></text>')
    L.append(f'<text x="{vx+16}" y="{vy+96}" class="m" font-size="11"><tspan fill="{T["muted"]}">rec  ❯ </tspan>'
             f'<tspan fill="{T["green"]}">✓ 8405</tspan><tspan fill="{T["muted"]}"> 32 seats · projector   </tspan>'
             f'<tspan fill="{T["green"]}">✓ 8210</tspan><tspan fill="{T["muted"]}"> 40 seats</tspan></text>')
    L.append(txt(vx + 16, vy + 114, "tap to reserve ›", 10.5, T["dim"], "m"))
    pd = mini_term(vx, vy, vw, vh, "~/pick-dream · demo", "\n".join(L))
    project(theme, "pickdream", "PickDream", "Android", "Natural-language classroom reservation.",
            ["An LLM extracts booking conditions from plain requests and recommends",
             "rooms. I built the Android front end in Kotlin, in a 7-member team."],
            ["Kotlin", "Android", "LLM"], "View repository  →", pd,
            "Silver Prize · KIIT 2025", emoji_logo("◎", "#58a6ff"))

    # Fridge AI (UCSD)
    L = []
    L.append(f'<rect x="{vx+16}" y="{vy+36}" width="74" height="78" rx="6" stroke="{T["muted"]}"/>')
    L.append(f'<line x1="{vx+16}" y1="{vy+62}" x2="{vx+90}" y2="{vy+62}" stroke="{T["muted"]}"/>')
    for (bx, by, bw, bh, col) in [(22, 42, 22, 16, T["teal"]), (50, 44, 34, 14, T["amber"]), (24, 68, 30, 20, T["green"]), (60, 70, 24, 38, T["blue"])]:
        L.append(f'<rect x="{vx+bx}" y="{vy+by}" width="{bw}" height="{bh}" stroke="{col}" stroke-dasharray="3 2"/>')
    for i, (k, v, col) in enumerate([("detected", "egg · milk · spinach · tofu", T["text"]),
                                    ("recipe", "spinach tofu scramble", T["green"]),
                                    ("allergens", "egg, milk, soy", T["amber"]),
                                    ("deploy", "docker → GCP", T["blue"])]):
        L.append(txt(vx + 112, vy + 50 + i * 19, k, 11, T["muted"], "m"))
        L.append(txt(vx + vw - 16, vy + 50 + i * 19, v, 11, col, "m", 400, "end"))
    fr = mini_term(vx, vy, vw, vh, "~/fridge-ai · demo", "\n".join(L))
    project(theme, "fridge", "Fridge AI", "UCSD", "Snap the fridge, get recipes and allergens.",
            ["Built in a 4-member international team at UC San Diego. I owned the",
             "backend and AI: Google generative AI prompting, data, Docker, GCP."],
            ["Gemini", "Docker", "GCP", "Backend"], "Qualcomm Institute  →", fr,
            "Achievement Award", emoji_logo("❄", "#79c0ff"))

    # TinyLlama QLoRA
    L = []
    pts = [(0, 92), (30, 70), (60, 56), (90, 47), (120, 41), (150, 37), (180, 34), (210, 32), (240, 31)]
    path = "M" + " L".join(f"{vx+20+x} {vy+y}" for x, y in pts)
    L.append(f'<path d="{path}" stroke="{T["teal"]}" stroke-width="2" fill="none"/>')
    L.append(f'<line x1="{vx+20}" y1="{vy+112}" x2="{vx+264}" y2="{vy+112}" stroke="{T["dim"]}"/>')
    L.append(txt(vx + 20, vy + 124 - 2, "", 1, T["dim"]))
    L.append(txt(vx + 264, vy + 108, "steps", 9.5, T["muted"], "m", 400, "end"))
    for i, (k, v, col) in enumerate([("base", "TinyLlama-1.1B", T["text"]), ("quant", "4-bit (QLoRA)", T["blue"]),
                                    ("adapter", "LoRA", T["text"]), ("loss", "↘ converging", T["green"])]):
        L.append(txt(vx + 300, vy + 50 + i * 19, k, 11, T["muted"], "m"))
        L.append(txt(vx + vw - 16, vy + 50 + i * 19, v, 11, col, "m", 400, "end"))
    ql = mini_term(vx, vy, vw, vh, "~/tinyllama-qlora · demo", "\n".join(L))
    project(theme, "qlora", "TinyLlama QLoRA", "Training", "Parameter-efficient fine-tuning on a budget.",
            ["4-bit quantised LoRA fine-tuning of a small open LLM: the same",
             "PEFT recipe I later applied to vision-language models."],
            ["PyTorch", "Hugging Face", "PEFT", "bitsandbytes"], "View repository  →", ql,
            None, emoji_logo("λ", "#e3b341"))


if __name__ == "__main__":
    hero()
    for th in THEMES:
        about(th); stack(th); carbix(th); awards(th); projects(th)
    print("ok", sorted(os.listdir(OUT)))
