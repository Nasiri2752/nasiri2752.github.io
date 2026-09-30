# -*- coding: utf-8 -*-
import os, re, sys, base64
from weasyprint import HTML
sys.path.insert(0, os.path.dirname(__file__))
from content_cv import *

D = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(D, "img")
FONT = os.path.join(D, "fonts")
def img(k): return "img/" + k + (".png" if k.startswith("qr-") else ".jpg")

def ff(n, w):
    b = base64.b64encode(open(f"{FONT}/Vazirmatn-{n}.ttf", "rb").read()).decode()
    return f"@font-face{{font-family:'Vazirmatn';font-weight:{w};src:url(data:font/ttf;base64,{b}) format('truetype');}}"
FONTS = ff("Regular", 400) + ff("Medium", 500) + ff("Bold", 700)

LAT = re.compile(r"(?<![\w>=\"'/.:@-])([A-Za-z][A-Za-z0-9&;.,/+×’\-: ]*[A-Za-z0-9])")
def fa_en(s):
    """در متن فارسی، عبارت‌های لاتین را با span.en جداسازی جهت می‌کند (بیرون از تگ‌ها)."""
    parts = re.split(r"(<[^>]+>)", s)
    out = []
    for p in parts:
        if p.startswith("<"): out.append(p); continue
        out.append(LAT.sub(lambda m: f'<span class="en">{m.group(1)}</span>', p))
    return "".join(out)

CSS = FONTS + r"""
@page { size:A4; margin:16mm 15mm 17mm 15mm; }
@page en { @top-left{content:"__FOOT_EN__"; font:8pt Vazirmatn; color:#8793A8}
           @bottom-left{content:"__UPD_EN__"; font:7.5pt Vazirmatn; color:#9AA3B5}
           @bottom-right{content:counter(page); font:8.5pt Vazirmatn; color:#51607A} }
@page fa { @top-right{content:"__FOOT_FA__"; font:8pt Vazirmatn; color:#8793A8}
           @bottom-right{content:"__UPD_FA__"; font:7.5pt Vazirmatn; color:#9AA3B5}
           @bottom-left{content:counter(page, persian); font:8.5pt Vazirmatn; color:#51607A} }
@page :first { @top-left{content:none} @top-right{content:none} }
html{font-family:Vazirmatn; color:#1E2636; font-size:9.6pt; line-height:1.62;}
.doc-en{page:en; direction:ltr;} .doc-fa{page:fa; direction:rtl; page-break-before:always; line-height:1.9; font-size:9.8pt;}
p,li,.txt{text-align:justify;}
a{color:#1F4E8C; text-decoration:none;}
.en{direction:ltr; unicode-bidi:isolate;}
b{font-weight:700;}
/* ---------- سر رزومه ---------- */
.banner{height:46mm; border-radius:3.5mm; overflow:hidden; background:#0B1F3F;}
.banner img{width:100%; height:46mm; object-fit:cover; object-position:center 40%;}
table.ident{width:100%; border-collapse:collapse; margin-top:-15mm;}
table.ident td{vertical-align:bottom; padding:0;}
td.ph{width:36mm;}
.portrait{width:32mm; height:32mm; border-radius:50%; object-fit:cover; border:1.1mm solid #fff; background:#fff;}
td.nm{padding:0 5mm 1mm 5mm !important;}
.nm h1{font-size:21pt; line-height:1.15; color:#0B1F3F; margin:17mm 0 1.2mm; font-weight:700;}
.hl{font-size:9.8pt; color:#C8203A; font-weight:500; margin-bottom:1.5mm;}
.ct{font-size:8.6pt; color:#51607A;}
.ct span.sep{color:#C8203A; padding:0 1.6mm;}
td.qrs{width:40mm; text-align:center;}
.qrbox{display:inline-block; width:18mm; margin:0 0.8mm; text-align:center; font-size:7pt; color:#51607A;}
.qrbox img{width:18mm; height:18mm; display:block;}
/* ---------- بخش‌ها ---------- */
h2{font-size:11.2pt; color:#0B1F3F; margin:6.5mm 0 2.6mm; padding-bottom:1.2mm; border-bottom:0.5pt solid #D3DAE6;
   page-break-after:avoid; font-weight:700; letter-spacing:.2pt;}
h2 .bar{display:inline-block; width:2.4mm; height:2.4mm; background:#C8203A; margin:0 2mm 0.4mm 0; border-radius:.5mm;}
.doc-fa h2 .bar{margin:0 0 0.4mm 2mm;}
.summary{font-size:9.8pt; color:#2B3548;}
table.rows{width:100%; border-collapse:collapse;}
table.rows td{vertical-align:top; padding:0 0 2.8mm 0;}
table.rows tr{page-break-inside:avoid;}
td.when{width:35mm; color:#C8203A; font-weight:500; font-size:8.4pt; padding-top:.4mm !important;}
.doc-fa td.when{width:37mm; font-size:8.2pt;}
.ttl{font-weight:700; color:#0B1F3F; font-size:9.9pt;}
.org{color:#51607A; font-size:8.8pt;}
ul{margin:.8mm 0 0; padding:0 0 0 4.5mm;} .doc-fa ul{padding:0 4.5mm 0 0;}
li{margin:0 0 .4mm;}
li::marker{color:#C8203A;}
/* افتخارات ویژه */
table.top{width:100%; border-collapse:separate; border-spacing:2.2mm 0; margin:0 -2.2mm 3mm;}
table.top td{width:33.3%; vertical-align:top; background:#EEF2F8; border-top:1mm solid #C8203A; border-radius:1.5mm;
   padding:2.6mm 3mm 3mm;}
.top .yr{font-size:8pt; color:#C8203A; font-weight:700;}
.top .t{font-weight:700; color:#0B1F3F; font-size:9.4pt; line-height:1.4; margin:.6mm 0 1mm;}
.top .d{font-size:8.3pt; color:#3F4A60; line-height:1.55;}
.doc-fa .top .d{line-height:1.8;}
td.y{width:13mm; color:#C8203A; font-weight:500; font-size:8.4pt;}
/* پروژه‌ها */
.proj{page-break-inside:avoid; margin:0 0 4mm; border:0.5pt solid #DDE3EC; border-radius:2mm; padding:3mm;}
table.pj{width:100%; border-collapse:collapse;}
table.pj td{vertical-align:top;}
td.pim{width:44mm;}
.pim img{width:42mm; height:36mm; object-fit:contain; background:#fff;}
td.ptx{padding:0 0 0 3.5mm;} .doc-fa td.ptx{padding:0 3.5mm 0 0;}
.pt{font-weight:700; color:#0B1F3F; font-size:10.2pt;}
.pm{font-size:8.2pt; color:#C8203A; font-weight:500; margin-bottom:.8mm;}
.pd{font-size:8.9pt; color:#2B3548;}
.thumbs{margin-top:1.8mm;}
.th{display:inline-block; width:21mm; margin:0 1.5mm 0 0; text-align:center; vertical-align:top;}
.doc-fa .th{margin:0 0 0 1.5mm;}
.th img{width:21mm; height:17mm; object-fit:contain; border:0.4pt solid #E1E6EE; border-radius:1mm; background:#fff;}
.th div{font-size:6.8pt; color:#6B778C; line-height:1.3;}
.earlier{font-size:8.7pt; color:#3F4A60; margin-top:1mm;}
table.gal{width:100%; border-collapse:separate; border-spacing:2mm; margin:0 -2mm;}
table.gal td{width:20%; text-align:center; vertical-align:top; page-break-inside:avoid;}
.gal img{width:31mm; height:26mm; object-fit:cover; border-radius:1.2mm;}
.gal div{font-size:7.2pt; color:#51607A; line-height:1.35; margin-top:.6mm;}
/* انتشارات و رسانه */
.pubt{font-weight:700; color:#0B1F3F; direction:ltr; text-align:left; font-size:9.4pt;}
.pubm{font-size:8.6pt; color:#51607A;}
td.qr{width:19mm;} td.qr img{width:16mm; height:16mm;}
.mt{font-weight:700; color:#0B1F3F; font-size:9.3pt;}
.mm{font-size:8.3pt; color:#51607A;}
table.sk td.k{width:36mm; font-weight:700; color:#0B1F3F; font-size:8.9pt;}
table.sk td{font-size:8.8pt; padding-bottom:1.6mm;}
.keep{page-break-inside:avoid;}
"""

def sep(): return '<span class="sep">|</span>'

def section(title, body, keep=False):
    return f'<div class="{"keep" if keep else ""}"><h2><span class="bar"></span>{title}</h2>{body}</div>'

def build_lang(L, full):
    t = T[L]; X = (lambda s: fa_en(s)) if L == "fa" else (lambda s: s)
    h = t["h"]; o = []
    # سر رزومه
    o.append(f'<div class="banner"><img src="{img("banner")}"></div>')
    o.append('<table class="ident"><tr>'
             f'<td class="ph"><img class="portrait" src="{img("portrait")}"></td>'
             f'<td class="nm"><h1>{t["name"]}</h1><div class="hl">{X(t["headline"])}</div>'
             f'<div class="ct">{sep().join(X(c) if not c.startswith("<a") else c for c in t["contact"])}</div></td>'
             f'<td class="qrs"><div class="qrbox"><img src="{img("qr-web")}">{t["qr_web"]}</div>'
             f'<div class="qrbox"><img src="{img("qr-li")}">{t["qr_li"]}</div></td></tr></table>')
    o.append(section(h["summary"], f'<p class="summary">{X(t["summary"])}</p>'))
    # سوابق
    rows = ""
    for e in EXP:
        w, ti, org, bl = e[L]
        li = "".join(f"<li>{X(b)}</li>" for b in bl)
        rows += (f'<tr><td class="when">{w}</td><td><div class="ttl">{X(ti)}</div><div class="org">{X(org)}</div>'
                 + (f"<ul>{li}</ul>" if li else "") + "</td></tr>")
    o.append(section(h["exp"], f'<table class="rows">{rows}</table>'))
    # افتخارات
    tops = "".join(f'<td><div class="yr">{y}</div><div class="t">{X(a)}</div><div class="d">{X(b)}</div></td>'
                   for y, a, b in (x[L] for x in HONORS_TOP))
    rest = "".join(f'<tr><td class="y">{y}</td><td>{X(a)}</td></tr>' for y, a in (x[L] for x in HONORS))
    body = f'<table class="top"><tr>{tops}</tr></table><table class="rows">{rest}</table>'
    if full:
        body += "<ul>" + "".join(f"<li>{X(c[L])}</li>" for c in COMPS) + "</ul>"
    o.append(section(h["honors"], body))
    # پروژه‌ها
    pj = ""
    for p in PROJ:
        ti, meta, desc = p[L]
        ims = p["imgs"]
        thumbs = ""
        if len(ims) > 1:
            thumbs = '<div class="thumbs">' + "".join(
                f'<div class="th"><img src="{img(k)}"><div>{X(c_en if L=="en" else c_fa)}</div></div>'
                for k, c_en, c_fa in ims[1:]) + "</div>"
        pj += (f'<div class="proj"><table class="pj"><tr><td class="pim"><img src="{img(ims[0][0])}"></td>'
               f'<td class="ptx"><div class="pt">{X(ti)}</div><div class="pm">{X(meta)}</div>'
               f'<div class="pd txt">{X(desc)}</div>{thumbs}</td></tr></table></div>')
    if not full:
        pj += f'<p class="earlier">{X(EARLIER_LINE[L])}</p>'
    o.append(f'<h2><span class="bar"></span>{h["proj"]}</h2>{pj}')
    if full:
        cells = [f'<td><img src="{img(k)}"><div>{X(e if L=="en" else f)}</div></td>' for k, e, f in EARLIER_PHOTOS]
        gal = "".join("<tr>" + "".join(cells[i:i+5]) + "</tr>" for i in range(0, len(cells), 5))
        lst = "<ul>" + "".join(f"<li>{X(e if L=='en' else f)}</li>" for e, f in EARLIER_LIST) + "</ul>"
        o.append(section(h["earlier"], f'<table class="gal">{gal}</table>{lst}'))
    # تحصیلات
    rows = ""
    for e in EDU:
        w, ti, org, bl = e[L]
        rows += (f'<tr><td class="when">{w}</td><td><div class="ttl">{X(ti)}</div><div class="org">{X(org)}</div>'
                 "<ul>" + "".join(f"<li>{X(b)}</li>" for b in bl) + "</ul></td></tr>")
    o.append(section(h["edu"], f'<table class="rows">{rows}</table><p class="txt">{X(EDU_NOTE[L])}</p>', keep=True))
    # انتشارات
    P = PUB[L]
    body = (f'<table class="rows"><tr><td class="qr"><a href="{DOI}"><img src="{img("qr-doi")}"></a></td><td>'
            f'<div class="pubt"><a href="{DOI}">{PUB["title"]}</a></div>'
            f'<div class="pubm en" style="display:block;text-align:left">{P["authors"]}</div>'
            f'<div class="pubm">{X(P["venue"])}</div><div class="pubm">{X(P["role"])}</div></td></tr></table>'
            f'<p class="txt">{X(P["book"])}</p>')
    o.append(section(h["pub"], body, keep=True))
    # مهارت‌ها و زبان
    sk = "".join(f'<tr><td class="k">{X(s[L][0])}</td><td>{X(s[L][1])}</td></tr>'
                 for s in SKILLS if full or not s.get("full"))
    o.append(section(h["skills"], f'<table class="rows sk">{sk}</table>', keep=True))
    o.append(section(h["lang"], f'<p>{X(LANGS[L])}</p>', keep=True))
    # رسانه
    md = "".join(f'<tr><td class="qr"><a href="{m["url"]}"><img src="{img("qr-"+m["qr"])}"></a></td>'
                 f'<td><div class="mt"><a href="{m["url"]}">{X(m[L][0])}</a></div><div class="mm">{X(m[L][1])}</div></td></tr>'
                 for m in MEDIA)
    o.append(section(h["media"], f'<table class="rows">{md}</table>', keep=True))
    return f'<div class="doc-{L}" lang="{L}">' + "".join(o) + "</div>"

def build(full, out):
    css = (CSS.replace("__FOOT_EN__", T["en"]["footer"]).replace("__UPD_EN__", T["en"]["updated"])
              .replace("__FOOT_FA__", T["fa"]["footer"]).replace("__UPD_FA__", T["fa"]["updated"]))
    html = f"<html><head><meta charset='utf-8'><style>{css}</style></head><body>{build_lang('en', full)}{build_lang('fa', full)}</body></html>"
    for bad in ("\u0654", "\u06C0", "\u064A", "\u0643"):
        assert bad not in html, f"forbidden char {hex(ord(bad))}"
    open(out.replace(".pdf", ".html"), "w", encoding="utf-8").write(html)
    HTML(string=html, base_url=os.path.dirname(out)).write_pdf(out)
    print("built", out)

if __name__ == "__main__":
    build(False, os.path.join(D, "resume-pro.pdf"))
    build(True, os.path.join(D, "resume-full.pdf"))
