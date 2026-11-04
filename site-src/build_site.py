# -*- coding: utf-8 -*-
"""سازنده‌ی سایت: همه‌ی صفحه‌ها (فارسی و انگلیسی) را از content_site.py و media.js می‌سازد.
اجرا از ریشه‌ی ریپازیتوری:  python3 site-src/build_site.py
خروجی‌ها در ریشه‌ی ریپازیتوری نوشته می‌شوند؛ HTMLهای خروجی را دستی ویرایش نکنید.
"""
import datetime, html, json, os, re, shutil, sys

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC)
sys.path.insert(0, SRC)
from content_site import *  # noqa

TODAY = datetime.date.today()
FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
LANGS = ("fa", "en")


def fa_num(s): return str(s).translate(FA_DIGITS)
def esc(s): return html.escape(str(s), quote=True)
def md(s): return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
def plain(s): return re.sub(r"<[^>]+>", "", re.sub(r"\*\*(.+?)\*\*", r"\1", s))


def jalali_year(d):
    return d.year - 621 if (d.month, d.day) >= (3, 21) else d.year - 622


# ---------------------------------------------------------------- آدرس‌ها
def url(page, L, slug=None):
    pre = "" if L == "fa" else "/en"
    if page == "index": return pre + "/"
    if page == "project": return f"{pre}/projects/{slug}.html"
    return f"{pre}/{page}.html"


def absu(path): return BASE + path


def out_path(path):
    p = path.lstrip("/")
    if p == "" or p.endswith("/"): p += "index.html"
    return os.path.join(ROOT, p)


# ---------------------------------------------------------------- داده‌ی رسانه
def load_media():
    s = open(os.path.join(SRC, "media.js"), encoding="utf-8").read()
    i = s.index("window.MEDIA = ") + len("window.MEDIA = ")
    M = json.loads(s[i:s.rindex("]") + 1])
    M = [m for m in M if m.get("aparat") or m.get("tw") or m.get("url")]
    return sorted(M, key=lambda m: m.get("d", ""), reverse=True)


MEDIA = load_media()
PROJ = {p["slug"]: p for p in PROJECTS}

# ---------------------------------------------------------------- آیکون‌ها
def svg(paths, w=24):
    return (f'<svg viewBox="0 0 24 24" width="{w}" height="{w}" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>')


ICON = {
 "medal": '<circle cx="12" cy="8" r="6"/><path d="M8.2 13.5L7 22l5-3 5 3-1.2-8.5"/>',
 "trophy": '<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0V4z"/><path d="M17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/>',
 "star": '<path d="M12 3l2.8 5.7 6.2.9-4.5 4.4 1.1 6.2L12 17.3 6.4 20.2l1.1-6.2L3 9.6l6.2-.9z"/>',
 "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>',
 "flask": '<path d="M9 3h6M10 3v6L4.5 19a2 2 0 0 0 1.8 3h11.4a2 2 0 0 0 1.8-3L14 9V3"/><path d="M7 15h10"/>',
 "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/>',
 "gear": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
 "robot": '<rect x="4" y="8" width="16" height="11" rx="2"/><path d="M12 8V4M9 4h6"/><circle cx="9" cy="13" r="1.3"/><circle cx="15" cy="13" r="1.3"/><path d="M7 19v2M17 19v2"/>',
 "layers": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/><path d="M3 17.5l9 5 9-5"/>',
 "cpu": '<rect x="6" y="6" width="12" height="12" rx="2"/><rect x="9.5" y="9.5" width="5" height="5"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/>',
 "refresh": '<path d="M21 12a9 9 0 1 1-2.6-6.4"/><path d="M21 4v5h-5"/>',
 "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
 "chat": '<path d="M21 12a8.5 8.5 0 0 1-12.4 7.6L3 21l1.4-5.4A8.5 8.5 0 1 1 21 12z"/>',
 "image": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="8.5" cy="9.5" r="1.8"/><path d="M21 16l-5-5-9 9"/>',
 "email": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 7l10 6 10-6"/>',
 "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8.1 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
 "linkedin": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7v.01M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/>',
 "telegram": '<path d="M21.5 4.5L2.5 11.5l6.5 2.2 2.3 6.8 3.5-4.2 5 3.7z"/><path d="M9 13.7l12.5-9.2"/>',
 "bale": '<path d="M21 12a8.5 8.5 0 0 1-12.4 7.6L3 21l1.4-5.4A8.5 8.5 0 1 1 21 12z"/>',
 "instagram": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6" fill="currentColor"/>',
}

# ---------------------------------------------------------------- داده‌ی ساخت‌یافته (JSON-LD)
PERSON_ID = BASE + "/#person"


def person_full(L):
    alumni = [
        {"@type": "CollegeOrUniversity", "name": "Sharif University of Technology", "alternateName": "دانشگاه صنعتی شریف",
         "sameAs": "https://en.wikipedia.org/wiki/Sharif_University_of_Technology"},
        {"@type": "CollegeOrUniversity", "name": "Iran University of Science and Technology", "alternateName": "دانشگاه علم و صنعت ایران",
         "sameAs": "https://en.wikipedia.org/wiki/Iran_University_of_Science_and_Technology"}]
    subject = []
    for m in MEDIA:
        t = "VideoObject" if (m.get("aparat") or m.get("tw")) else "NewsArticle"
        u = media_url(m)
        subject.append({"@type": t, "name": m["title_" + L], "url": u})
    return {
        "@type": "Person", "@id": PERSON_ID,
        "name": NAME[L], "alternateName": ["Hassan Nasiri Khonsari", "Hasan Nasiri Khonsari", "حسن نصیری خونساری", "Hassan Nasiri", "حسن نصیری"],
        "givenName": "Hassan" if L == "en" else "حسن", "familyName": "Nasiri Khonsari" if L == "en" else "نصیری خونساری",
        "description": plain(HOME[L]["intro"][0]), "disambiguatingDescription": DISAMBIG[L],
        "jobTitle": JOB[L],
        "hasOccupation": {"@type": "Occupation", "name": JOB[L],
                          "occupationLocation": {"@type": "Country", "name": "Iran"},
                          "skills": "Mechanical design, mechatronics, industrial robotics, custom machinery, automation, PLC, GD&T, batch production with quality control"},
        "url": BASE + "/", "image": BASE + "/hassan-720.jpg", "email": "mailto:" + EMAIL, "telephone": PHONE,
        "address": {"@type": "PostalAddress", "addressLocality": "Tehran", "addressCountry": "IR"},
        "nationality": {"@type": "Country", "name": "Iran"},
        "alumniOf": alumni,
        "hasCredential": [{"@type": "EducationalOccupationalCredential", "credentialCategory": "degree",
                           "name": "MSc in Mechanical Engineering (Applied Design)", "recognizedBy": {"@type": "CollegeOrUniversity", "name": "Sharif University of Technology"}},
                          {"@type": "EducationalOccupationalCredential", "credentialCategory": "degree",
                           "name": "BSc in Mechanical Engineering", "recognizedBy": {"@type": "CollegeOrUniversity", "name": "Iran University of Science and Technology"}}],
        "worksFor": {"@type": "Organization", "name": "Karun HiTech Solutions"},
        "award": [h["en"][0] for h in HONORS[:6]] + [h["fa"][0] for h in HONORS[:3]],
        "knowsAbout": ["Mechanical design", "Mechatronics", "Industrial robotics", "Mobile robot fleets", "Custom machinery", "Industrial automation",
                       "PLC programming", "Test rigs", "Medical test equipment", "ASTM F1223", "GD&T", "Batch production and quality control",
                       "طراحی مکانیک", "رباتیک صنعتی", "ماشین‌آلات سفارشی", "اتوماسیون صنعتی"],
        "knowsLanguage": ["fa", "en", "ar"],
        "sameAs": SAME_AS + [DOI],
        "subjectOf": subject,
    }


def person_ref(L): return {"@type": "Person", "@id": PERSON_ID, "name": NAME[L], "url": BASE + "/"}


def breadcrumbs(L, items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": absu(p)} for i, (n, p) in enumerate(items)]}


def scholarly():
    return {"@type": "ScholarlyArticle", "@id": DOI, "name": PUB["title"], "headline": PUB["title"], "url": DOI, "sameAs": DOI,
            "datePublished": PUB["year"], "isPartOf": {"@type": "Periodical", "name": PUB["journal"], "publisher": {"@type": "Organization", "name": "Nature Portfolio"}},
            "author": [{"@type": "Person", "name": n} if n != "Hasan Nasiri Khonsari" else {"@type": "Person", "@id": PERSON_ID, "name": n}
                       for n in PUB["authors_plain"]]}


def media_url(m):
    if m.get("tw"): return "https://telewebion.net/episode/" + m["tw"]
    if m.get("aparat"): return "https://www.aparat.com/v/" + m["aparat"]
    return m["url"]


def media_ld(m, L):
    common = {"name": m["title_" + L], "description": m.get("desc_" + L, ""), "about": {"@id": PERSON_ID},
              "url": media_url(m), "image": BASE + "/" + m["poster"] if m.get("poster") else None}
    if m.get("aparat") or m.get("tw"):
        o = {"@type": "VideoObject", **common, "thumbnailUrl": common["image"], "uploadDate": m.get("d"),
             "publisher": {"@type": "Organization", "name": m.get("source_" + L, "")}}
        if m.get("aparat"): o["embedUrl"] = "https://www.aparat.com/video/video/embed/videohash/" + m["aparat"] + "/vt/frame"
    else:
        o = {"@type": "NewsArticle", **common, "headline": m["title_" + L], "datePublished": m.get("d"),
             "publisher": {"@type": "Organization", "name": m.get("source_" + L, "")}}
    return {k: v for k, v in o.items() if v}


def ld_script(nodes):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": nodes}, ensure_ascii=False) + "</script>"


# ---------------------------------------------------------------- اسکلت صفحه
GA = f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_ID}');
</script>"""


def head(L, title, desc, path, alt_path, nodes, og_img="/og-image.jpg", og_type="website"):
    fa_p = path if L == "fa" else alt_path
    en_p = alt_path if L == "fa" else path
    return f"""<!DOCTYPE html>
<html lang="{L}" dir="{'rtl' if L == 'fa' else 'ltr'}">
<head>
<meta charset="UTF-8">
{GA}
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="author" content="{esc(NAME[L])}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{absu(path)}">
<link rel="alternate" hreflang="fa" href="{absu(fa_p)}">
<link rel="alternate" hreflang="en" href="{absu(en_p)}">
<link rel="alternate" hreflang="x-default" href="{absu(fa_p)}">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/favicon.png">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{esc(NAME[L])}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{absu(path)}">
<meta property="og:locale" content="{'fa_IR' if L == 'fa' else 'en_US'}">
<meta property="og:locale:alternate" content="{'en_US' if L == 'fa' else 'fa_IR'}">
<meta property="og:image" content="{BASE}{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{BASE}{og_img}">
{ld_script(nodes)}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css?v={TODAY.strftime('%Y%m%d')}">
</head>
<body>
"""


def nav(L, active, alt_path):
    u = UI[L]
    act = ' class="active" aria-current="page"'
    links = "".join(f'<a href="{url(p, L)}"{act if p == active else ""}>{t}</a>' for p, t in u["nav"])
    other = "en" if L == "fa" else "fa"
    return f"""<nav><div class="wrap">
  <div class="menu">
    {links}
    <a href="#contact" class="nav-cta">{u["contact"]}</a>
    <a href="{alt_path}" class="lang-sw" hreflang="{other}" lang="{other}">{u["lang_label"]}</a>
    <a href="tel:{PHONE}" class="nav-phone" aria-label="{u["call"]}">{svg(ICON["phone"], 18)}</a>
  </div>
</div></nav>
<main>
"""


def contact_section(L):
    c = CONTACT[L]
    ext = ' target="_blank" rel="noopener"'
    def dc(k): return f' data-contact="{k}"' if k in ("telegram", "bale", "instagram", "linkedin") else ""
    links = "".join(
        f'<a href="{h}"{ext if h.startswith("http") else ""}{dc(k)}>{svg(ICON[k], 18)}<span>{t}</span></a>'
        for k, h, t in c["links"])
    return f"""<section class="block contact" id="contact"><div class="wrap">
  <h2 class="reveal">{c["h"]}</h2>
  <p class="reveal">{c["p"]}</p>
  <form class="cform reveal" id="contactForm" action="{FORMSPREE}" method="POST">
    <div class="cf-row">
      <input type="text" name="name" placeholder="{c["name"]}" aria-label="{c["name"]}" required>
      <input type="email" name="email" placeholder="{c["email"]}" aria-label="{c["email"]}" required>
    </div>
    <textarea name="message" rows="4" placeholder="{c["msg"]}" aria-label="{c["msg"]}" required></textarea>
    <button type="submit" class="cf-btn">{c["send"]}</button>
    <div class="cf-status" id="cfStatus" role="status"></div>
  </form>
  <p class="reveal" style="color:#9fb0c9; font-size:14px; margin-bottom:6px;">{c["other"]}</p>
  <div class="c-links reveal">{links}</div>
</div></section>
"""


def footer(L):
    u = UI[L]
    yr = fa_num(jalali_year(TODAY)) if L == "fa" else str(TODAY.year)
    links = "".join(f'<a href="{url(p, L)}">{t}</a>' for p, t in u["nav"])
    return f"""</main>
<footer>
  <div class="f-links">{links}<a href="/Resume.pdf" download>{u["resume"]}</a></div>
  © {yr} {NAME[L]} — {u["footer"]}
</footer>
<a href="tel:{PHONE}" class="fab-phone" aria-label="{u["call"]}">{svg(ICON["phone"], 18)}</a>
<script src="/assets/site.js?v={TODAY.strftime('%Y%m%d')}" defer></script>
</body>
</html>
"""


def page_hero(L, kk, h1, lead="", crumbs=None, meta=None):
    c = ""
    if crumbs:
        c = '<div class="crumbs">' + '<span class="sep">/</span>'.join(
            f'<a href="{p}">{n}</a>' if p else f'<span>{n}</span>' for n, p in crumbs) + "</div>"
    m = ('<div class="ph-meta">' + "".join(meta) + "</div>") if meta else ""
    return f"""<header class="page-hero"><div class="wrap">
  {c}<div class="kk">{kk}</div><h1>{h1}</h1>{f'<p class="lead">{lead}</p>' if lead else ""}{m}
</div></header>
"""


def head_block(kk, h, p=""):
    return f'<div class="head reveal"><div class="kk">{kk}</div><h2>{h}</h2>{f"<p>{p}</p>" if p else ""}</div>'


# ---------------------------------------------------------------- کارت‌ها
def thumb(g): return re.sub(r"\.(\w+)$", r"-t.\1", g)


def media_card(m, L):
    u = UI[L]
    t = lambda k: m.get(k + "_" + L) or m.get(k + "_fa") or m.get(k + "_en") or ""
    title = t("title")
    meta = '<div class="m-meta">' + " · ".join(x for x in (t("source"), t("date")) if x) + "</div>"
    desc = f'<p class="m-desc">{t("desc")}</p>' if t("desc") else ""
    more = f'<a class="m-more" href="{esc(m["more_url"] if m["more_url"].startswith("http") else "/" + m["more_url"])}" target="_blank" rel="noopener">{t("more")}</a>' if m.get("more_url") else ""
    poster = f'<img src="/{m["poster"]}" alt="{esc(title)}" loading="lazy" width="960" height="540">' if m.get("poster") else ""
    gal = ""
    if m.get("gallery"):
        cnt = fa_num(len(m["gallery"])) if L == "fa" else len(m["gallery"])
        btns = "".join(
            f'<button type="button" data-full="/{g}" data-alt="{esc(title)}" aria-label="{esc(u["photo"])}{fa_num(i + 1) if L == "fa" else i + 1}">'
            f'<img src="/{thumb(g)}" alt="" loading="lazy"></button>' for i, g in enumerate(m["gallery"]))
        gal = f'<div class="m-gal" data-lb><div class="m-gal-h">{u["gallery"]} ({cnt})</div><div class="m-gal-g">{btns}</div></div>'
    if m.get("tw"):
        page = media_url(m)
        top = (f'<div class="m-vid"><a class="m-play" href="{page}" target="_blank" rel="noopener" aria-label="{esc(u["watch_tw"] + " " + title)}">'
               f'{poster}<span class="m-pbtn"></span><span class="m-ext">{u["watch_tw"]}</span></a></div>')
        h3 = f"<h3>{title}</h3>"
    elif m.get("aparat"):
        top = (f'<div class="m-vid"><button type="button" class="m-play" data-aparat="{esc(m["aparat"])}" aria-label="{esc(u["play"] + title)}">'
               f'{poster}<span class="m-pbtn"></span></button></div>')
        h3 = f"<h3>{title}</h3>"
    else:
        cta = t("cta") or u["read"]
        top = (f'<div class="m-vid"><a class="m-play" href="{esc(m["url"])}" target="_blank" rel="noopener" aria-label="{esc(title)}">'
               f'{poster}<span class="m-ext">{cta}</span></a></div>') if poster else ""
        h3 = f'<h3><a class="m-title" href="{esc(m["url"])}" target="_blank" rel="noopener">{title}</a></h3>'
    return f'<article class="m-card" data-id="{esc(m["id"])}">{top}<div class="m-bd">{h3}{meta}{desc}{more}{gal}</div></article>'


def project_card(p, L, place="page"):
    d = p[L]
    if p["imgs"]:
        src, w, h = p["imgs"][0][:3]
        img = f'<div class="pimg"><img src="/{src}" alt="{esc(d["title"])}" loading="lazy" width="{w}" height="{h}"></div>'
    else:
        img = f'<div class="pimg ph">{svg(ICON["robot"], 56)}</div>'
    return (f'<a class="pc reveal" href="{url("project", L, p["slug"])}" data-project="{p["slug"]}" data-place="{place}">{img}'
            f'<div class="pbd"><div class="pyr">{p["year"][0 if L == "fa" else 1]}</div><h3>{d["title"]}</h3><p>{d["short"]}</p></div></a>')


def honor_card(h, L):
    t, p = h[L]
    return (f'<div class="honor reveal{" top" if h.get("top") else ""}"><div class="ico">{svg(ICON[h["icon"]])}</div>'
            f'<div><h3>{t}</h3><p>{p}</p></div></div>')


def service_card(s, L, mini=False, link=None):
    t, p = s[L]
    proof = ""
    if s.get("proof") and not mini:
        proof = ('<div class="proof">' + UI[L]["proof"] + ": " + "".join(
            f'<a href="{url("project", L, sl)}" data-project="{sl}" data-place="services">{PROJ[sl][L]["title"]}</a>' for sl in s["proof"]) + "</div>")
    tag = "a" if link else "div"
    href = f' href="{link}"' if link else ""
    return (f'<{tag} class="svc reveal{" mini" if mini else ""}" id="{s["id"]}" data-service="{s["id"]}"{href}>'
            f'<div class="ico">{svg(ICON[s["icon"]])}</div><h3>{t}</h3><p>{p}</p>{proof}</{tag}>')


# ---------------------------------------------------------------- صفحه‌ها
def write(path, content):
    fp = out_path(path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w", encoding="utf-8").write(content)
    PAGES.append(path)


PAGES = []


def build_home(L):
    h, u = HOME[L], UI[L]
    path, alt = url("index", L), url("index", "en" if L == "fa" else "fa")
    nodes = [person_full(L),
             {"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": NAME[L], "inLanguage": ["fa", "en"], "publisher": {"@id": PERSON_ID}},
             {"@type": "ProfilePage", "@id": absu(path) + "#page", "url": absu(path), "name": h["title"], "inLanguage": L,
              "mainEntity": {"@id": PERSON_ID}, "isPartOf": {"@id": BASE + "/#website"}, "dateModified": TODAY.isoformat()}]
    stats = "".join(f'<div class="stat reveal"><div class="n">{n}</div><div class="l">{l}</div></div>' for n, l in h["stats"])
    svcs = "".join(service_card(s, L, mini=True, link=url("services", L) + "#" + s["id"]) for s in SERVICES)
    hons = "".join(honor_card(x, L) for x in HONORS if x.get("top"))
    projs = "".join(project_card(p, L, "home") for p in PROJECTS[:6])
    meds = "".join(media_card(m, L) for m in MEDIA[:4])
    body = f"""<header class="hero" id="top">
  <div class="cover">
    <picture>
      <source srcset="/cover.webp" type="image/webp">
      <img src="/cover.jpg" width="2172" height="724" alt="{'نمونه‌ای از ماشین‌ها و ربات‌هایی که حسن نصیری خونساری طراحی و ساخته است' if L == 'fa' else 'Machines and robots designed and built by Hassan Nasiri Khonsari'}" fetchpriority="high">
    </picture>
  </div>
  <div class="wrap profile">
    <div class="portrait">
      <picture>
        <source srcset="/hassan-720.webp" type="image/webp">
        <img src="/hassan-720.jpg" width="720" height="720" alt="{NAME[L]}">
      </picture>
    </div>
    <div class="intro">
    <span class="eyebrow">{h["eyebrow"]}</span>
    <h1>{NAME[L]}</h1>
    <p class="headline">{h["headline"]}</p>
    <p class="lead">{h["lead"]}</p>
    <div class="btns">
      <a class="btn btn-gold" href="{url("services", L)}">{h["cta1"]}</a>
      <a class="btn btn-ghost" href="{url("projects", L)}">{h["cta2"]}</a>
      <a class="btn-link" href="/Resume.pdf" download>{u["resume"]}</a>
    </div>
    </div>
  </div>
</header>
<section class="stats" aria-label="{'در یک نگاه' if L == 'fa' else 'At a glance'}"><div class="wrap">{stats}</div></section>

<section class="block" id="intro" style="padding-top:20px"><div class="wrap narrow">
  {head_block(h["intro_kk"], h["intro_h"])}
  <div class="reveal">{"".join(f"<p style='color:#3F454C;margin-bottom:16px'>{x}</p>" for x in h["intro"])}</div>
  <div class="center"><a class="more-link" href="{url("about", L)}">{u["more_about"]} ←</a></div>
</div></section>

<section class="block soft" id="services"><div class="wrap">
  {head_block(h["svc_kk"], h["svc_h"], h["svc_p"])}
  <div class="svc-grid">{svcs}</div>
  <div class="center"><a class="more-link" href="{url("services", L)}">{u["all_services"]} ←</a></div>
</div></section>

<section class="block" id="projects"><div class="wrap">
  {head_block(h["proj_kk"], h["proj_h"], h["proj_p"])}
  <div class="pc-grid">{projs}</div>
  <div class="center"><a class="more-link" href="{url("projects", L)}">{u["all_projects"]} ←</a></div>
</div></section>

<section class="block honors" id="honors"><div class="wrap">
  {head_block(h["hon_kk"], h["hon_h"])}
  <div class="h-grid">{hons}</div>
  <div class="center"><a class="more-link" href="{url("about", L)}#honors">{ABOUT[L]["hon_h"]} ←</a></div>
</div></section>

<section class="block media" id="media"><div class="wrap">
  {head_block(h["media_kk"], h["media_h"])}
  <div class="m-grid">{meds}</div>
  <div class="center"><a class="more-link" href="{url("media", L)}">{u["all_media"]} ←</a></div>
</div></section>
"""
    if L == "en": body = body.replace(" ←</a>", " →</a>")
    write(path, head(L, h["title"], h["desc"], path, alt, nodes, og_type="profile") + nav(L, "index", alt) + body + contact_section(L) + footer(L))


def build_services(L):
    s, u = SERVICES_PAGE[L], UI[L]
    path, alt = url("services", L), url("services", "en" if L == "fa" else "fa")
    faq = FAQ[L]
    nodes = [person_ref(L),
             {"@type": "WebPage", "@id": absu(path) + "#page", "url": absu(path), "name": s["title"], "description": s["desc"], "inLanguage": L, "about": {"@id": PERSON_ID}},
             breadcrumbs(L, [(u["home"], url("index", L)), (s["kk"], path)]),
             {"@type": "ItemList", "name": s["svc_h"], "itemListElement": [
                 {"@type": "ListItem", "position": i + 1, "item": {"@type": "Service", "name": x[L][0], "description": x[L][1],
                  "provider": {"@id": PERSON_ID}, "areaServed": {"@type": "Country", "name": "Iran"}, "url": absu(path) + "#" + x["id"]}}
                 for i, x in enumerate(SERVICES + CONSULTING)]},
             {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]
    svcs = "".join(service_card(x, L) for x in SERVICES)
    cons = "".join(service_card(x, L) for x in CONSULTING)
    steps = "".join(f'<div class="step reveal"><h3>{a}</h3><p>{b}</p></div>' for a, b in s["steps"])
    faqh = "".join(f'<details class="reveal"><summary>{q}</summary><p>{a}</p></details>' for q, a in faq)
    body = page_hero(L, s["kk"], s["h1"], s["lead"], crumbs=[(u["home"], url("index", L)), (s["kk"], None)]) + f"""
<section class="block soft" id="build"><div class="wrap">
  {head_block(s["kk"], s["svc_h"])}
  <div class="svc-grid">{svcs}</div>
</div></section>
<section class="block" id="consulting"><div class="wrap">
  {head_block(s["kk"], s["cons_h"], s["cons_p"])}
  <div class="svc-grid two">{cons}</div>
</div></section>
<section class="block soft" id="process"><div class="wrap">
  {head_block(s["kk"], s["steps_h"])}
  <div class="steps">{steps}</div>
</div></section>
<section class="block" id="faq"><div class="wrap">
  {head_block(s["kk"], s["faq_h"])}
  <div class="faq">{faqh}</div>
</div></section>
"""
    write(path, head(L, s["title"], s["desc"], path, alt, nodes) + nav(L, "services", alt) + body + contact_section(L) + footer(L))


def build_projects_index(L):
    s, u = PROJECTS_PAGE[L], UI[L]
    path, alt = url("projects", L), url("projects", "en" if L == "fa" else "fa")
    nodes = [person_ref(L),
             {"@type": "CollectionPage", "@id": absu(path) + "#page", "url": absu(path), "name": s["title"], "description": s["desc"], "inLanguage": L,
              "about": {"@id": PERSON_ID}, "mainEntity": {"@type": "ItemList", "itemListElement": [
                  {"@type": "ListItem", "position": i + 1, "url": absu(url("project", L, p["slug"])), "name": p[L]["title"]} for i, p in enumerate(PROJECTS)]}},
             breadcrumbs(L, [(u["home"], url("index", L)), (s["h1"], path)])]
    cards = "".join(project_card(p, L) for p in PROJECTS)
    body = page_hero(L, s["kk"], s["h1"], s["lead"], crumbs=[(u["home"], url("index", L)), (s["h1"], None)]) + f"""
<section class="block soft"><div class="wrap"><div class="pc-grid">{cards}</div></div></section>
"""
    write(path, head(L, s["title"], s["desc"], path, alt, nodes) + nav(L, "projects", alt) + body + contact_section(L) + footer(L))


def build_project(p, i, L):
    d, u = p[L], UI[L]
    path, alt = url("project", L, p["slug"]), url("project", "en" if L == "fa" else "fa", p["slug"])
    title = f'{d["title"]} | {NAME[L]}'
    desc = d["short"] + " " + plain(d["desc"][0])
    desc = desc if len(desc) < 300 else desc[:297].rsplit(" ", 1)[0] + "…"
    og = f"/og/{p['slug']}.jpg" if p["imgs"] else "/og-image.jpg"
    imgs_abs = [BASE + "/" + im[0] for im in p["imgs"]]
    work = {"@type": "CreativeWork", "@id": absu(path) + "#work", "name": d["title"], "description": plain(" ".join(d["desc"])),
            "creator": {"@id": PERSON_ID}, "dateCreated": p["date"], "keywords": ", ".join(d["tags"]), "inLanguage": L,
            "url": absu(path)}
    if imgs_abs: work["image"] = imgs_abs
    if d["awards"]: work["award"] = d["awards"]
    nodes = [person_ref(L), work,
             {"@type": "WebPage", "@id": absu(path) + "#page", "url": absu(path), "name": title, "inLanguage": L, "mainEntity": {"@id": absu(path) + "#work"}},
             breadcrumbs(L, [(u["home"], url("index", L)), (PROJECTS_PAGE[L]["h1"], url("projects", L)), (d["title"], path)])]
    # گالری
    if p["imgs"]:
        cap = lambda im: im[3] if L == "fa" else im[4]
        src, w, hgt = p["imgs"][0][:3]
        main = (f'<button type="button" class="main" data-full="/{src}" data-alt="{esc(cap(p["imgs"][0]) or d["title"])}" aria-label="{esc(d["title"])}">'
                f'<img src="/{src}" alt="{esc(d["title"] + ((" — " + cap(p["imgs"][0])) if cap(p["imgs"][0]) else ""))}" width="{w}" height="{hgt}" fetchpriority="high"></button>')
        thumbs = ""
        if len(p["imgs"]) > 1:
            thumbs = '<div class="thumbs">' + "".join(
                f'<button type="button" data-full="/{im[0]}" data-alt="{esc(cap(im) or d["title"])}" aria-label="{esc(cap(im) or d["title"])}">'
                f'<img src="/{im[0].replace(".webp", "-t.webp")}" alt="{esc(d["title"] + ((" — " + cap(im)) if cap(im) else ""))}" loading="lazy"></button>'
                for im in p["imgs"]) + "</div>"
        capline = f'<div class="cap">{cap(p["imgs"][0])}</div>' if cap(p["imgs"][0]) else ""
        gal = f'<div class="pp-gal" data-lb>{main}{capline}{thumbs}</div>'
    else:
        gal = f'<div class="pp-ph">{svg(ICON["image"], 64)}<span>{u["no_photo"]}</span></div>'
    vids = ""
    if p.get("videos"):
        vids = (f'<section class="block soft"><div class="wrap">{head_block(u["videos"], d["title"])}<div class="vid-grid">' + "".join(
            f'<div><div class="vid"><iframe src="https://www.aparat.com/video/video/embed/videohash/{esc(v["aparat"])}/vt/frame" title="{esc(v[L])}" loading="lazy" allowfullscreen></iframe></div><div class="vid-t">{v[L]}</div></div>'
            for v in p["videos"]) + "</div></div></section>")
    facts = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in d["facts"])
    awards = ("".join(f"<li>{a}</li>" for a in d["awards"]))
    rel = [m for m in MEDIA if p["slug"] in m.get("projects", [])]
    relh = (f'<section class="block media"><div class="wrap">{head_block(u["related_media"], d["title"])}<div class="m-grid">'
            + "".join(media_card(m, L) for m in rel) + "</div></div></section>") if rel else ""
    prev_p, next_p = PROJECTS[i - 1], PROJECTS[(i + 1) % len(PROJECTS)]
    meta = [f'<span class="yr">{u["year"]} {p["year"][0 if L == "fa" else 1]}</span>'] + [f"<span>{t}</span>" for t in d["tags"]]
    body = page_hero(L, PROJECTS_PAGE[L]["kk"], d["title"], d["short"],
                     crumbs=[(u["home"], url("index", L)), (PROJECTS_PAGE[L]["h1"], url("projects", L)), (d["title"], None)], meta=meta) + f"""
<section class="block"><div class="wrap">
  <div class="pp">
    <div class="reveal">{gal}</div>
    <div class="pp-txt reveal">
      {"".join(f"<p>{md(x)}</p>" for x in d["desc"])}
      <div class="pp-box"><h2>{u["my_role"]}</h2><p>{d["role"]}</p></div>
      <div class="pp-box"><h2>{u["key_facts"]}</h2><table class="pp-facts">{facts}</table></div>
      {f'<div class="pp-box"><h2>{u["awards"]}</h2><ul class="pp-awards">{awards}</ul></div>' if awards else ""}
    </div>
  </div>
</div></section>
{vids}
{relh}
<section class="block" style="padding-top:20px"><div class="wrap">
  <div class="pp-cta reveal"><div><h2>{u["similar"]}</h2><p>{u["similar_p"]}</p></div>
    <div class="btns"><a class="btn btn-gold" href="#contact">{u["start_chat"]}</a><a class="btn btn-ghost" href="{TELEGRAM}" target="_blank" rel="noopener" data-contact="telegram">Telegram</a></div></div>
  <div class="pp-nav">
    <a href="{url("project", L, prev_p["slug"])}" data-project="{prev_p["slug"]}" data-place="prev"><small>{u["prev"]}</small>{prev_p[L]["title"]}</a>
    <a href="{url("project", L, next_p["slug"])}" data-project="{next_p["slug"]}" data-place="next"><small>{u["next"]}</small>{next_p[L]["title"]}</a>
  </div>
</div></section>
"""
    write(path, head(L, title, desc, path, alt, nodes, og_img=og, og_type="article") + nav(L, "projects", alt) + body + contact_section(L) + footer(L))


def build_about(L):
    a, u = ABOUT[L], UI[L]
    path, alt = url("about", L), url("about", "en" if L == "fa" else "fa")
    nodes = [person_full(L), scholarly(),
             {"@type": "ProfilePage", "@id": absu(path) + "#page", "url": absu(path), "name": a["title"], "description": a["desc"], "inLanguage": L,
              "mainEntity": {"@id": PERSON_ID}, "dateModified": TODAY.isoformat()},
             breadcrumbs(L, [(u["home"], url("index", L)), (a["kk"], path)])]
    facts = "".join(f'<div class="fact"><span class="k">{k}</span><span class="v">{v}</span></div>' for k, v in a["facts"])
    hons = "".join(honor_card(x, L) for x in HONORS)
    tl = ""
    for e in EXPERIENCE:
        w, t, o, dsc = e[L]
        more = f'<a class="tl-more" href="{url("project", L, e["project"])}" data-project="{e["project"]}" data-place="about">{PROJ[e["project"]][L]["title"]} ←</a>' if e.get("project") else ""
        if L == "en": more = more.replace(" ←</a>", " →</a>")
        dp = f'<p class="tl-d">{dsc}</p>' if dsc else ""
        tl += f'<div class="tl reveal"><div class="when">{w}</div><h3>{t}</h3><div class="org">{o}</div>{dp}{more}</div>'
    edu = "".join(f'<div class="card reveal"><div class="when">{w}</div><h3>{t}</h3><div class="org">{o}</div><ul>{"".join(f"<li>{x}</li>" for x in li)}</ul></div>'
                  for w, t, o, li in (e[L] for e in EDUCATION))
    P = PUB[L]
    def chips(cs): return "".join(f'<span class="chip">{esc(c)}</span>' for c in cs)
    skills = "".join(f'<div class="skill-cat"><h3>{t}</h3><div class="chips">{chips(cs)}</div></div>'
                     for t, cs in (s[L] for s in SKILLS))
    body = page_hero(L, a["kk"], a["h1"], crumbs=[(u["home"], url("index", L)), (a["kk"], None)]) + f"""
<section class="block" id="about"><div class="wrap">
  <div class="about">
    <div class="reveal">{"".join(f"<p>{x}</p>" for x in a["paras"])}
      <div class="btns" style="margin-top:8px"><a class="btn btn-gold" href="/Resume.pdf" download>{u["resume"]}</a></div></div>
    <div class="facts reveal">{facts}</div>
  </div>
</div></section>
<section class="block honors" id="honors"><div class="wrap">
  {head_block(a["kk"], a["hon_h"])}
  <div class="h-grid">{hons}</div>
</div></section>
<section class="block" id="experience"><div class="wrap">
  {head_block(a["kk"], a["exp_h"])}
  <div class="timeline">{tl}</div>
</div></section>
<section class="block soft" id="education"><div class="wrap">
  {head_block(a["kk"], a["edu_h"])}
  <div class="edu">{edu}</div>
  <p class="edu-note">{EDU_NOTE[L]}</p>
</div></section>
<section class="block" id="publications"><div class="wrap">
  {head_block(a["kk"], a["pub_h"])}
  <div class="pub reveal">
    <span class="jbadge">{P["badge"]}</span>
    <div class="ptitle">{PUB["title"]}</div>
    <p class="pfa">{P["abstract"]}</p>
    <div class="authors">{PUB["authors"]}</div>
    <div class="prole">{P["role"]}</div>
    <div class="pmeta">{"".join(f"<span>{x}</span>" for x in P["meta"])}</div>
    <a class="plink" href="{DOI}" target="_blank" rel="noopener">{P["link"]}</a>
  </div>
</div></section>
<section class="block soft" id="skills"><div class="wrap">
  {head_block(a["kk"], a["skills_h"])}
  <div class="reveal">{skills}</div>
</div></section>
"""
    write(path, head(L, a["title"], a["desc"], path, alt, nodes, og_type="profile") + nav(L, "about", alt) + body + contact_section(L) + footer(L))


def build_media(L):
    s, u = MEDIA_PAGE[L], UI[L]
    path, alt = url("media", L), url("media", "en" if L == "fa" else "fa")
    nodes = [person_ref(L),
             {"@type": "CollectionPage", "@id": absu(path) + "#page", "url": absu(path), "name": s["title"], "description": s["desc"], "inLanguage": L,
              "about": {"@id": PERSON_ID}, "mainEntity": {"@type": "ItemList", "itemListElement": [
                  {"@type": "ListItem", "position": i + 1, "item": media_ld(m, L)} for i, m in enumerate(MEDIA)]}},
             breadcrumbs(L, [(u["home"], url("index", L)), (s["h1"], path)])]
    cards = "".join(media_card(m, L) for m in MEDIA)
    body = page_hero(L, s["kk"], s["h1"], s["lead"], crumbs=[(u["home"], url("index", L)), (s["h1"], None)]) + f"""
<section class="block media"><div class="wrap"><div class="m-grid">{cards}</div></div></section>
"""
    write(path, head(L, s["title"], s["desc"], path, alt, nodes) + nav(L, "media", alt) + body + contact_section(L) + footer(L))


# ---------------------------------------------------------------- فایل‌های جانبی
def build_extras():
    # en.html قدیمی → /en/
    open(os.path.join(ROOT, "en.html"), "w", encoding="utf-8").write(
        f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>{NAME["en"]}</title>'
        f'<link rel="canonical" href="{BASE}/en/"><meta name="robots" content="noindex, follow">'
        f'<meta http-equiv="refresh" content="0; url=/en/"></head><body><a href="/en/">{NAME["en"]}</a></body></html>\n')
    # 404
    open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(
        head("fa", "صفحه پیدا نشد | " + NAME["fa"], "این صفحه وجود ندارد.", "/404.html", "/404.html", [person_ref("fa")]).replace(
            '<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
        + nav("fa", None, "/en/") + page_hero("fa", "۴۰۴", "این صفحه پیدا نشد", "Page not found.")
        + f'<section class="block"><div class="wrap center"><div class="btns center"><a class="btn btn-gold" href="/">خانه</a>'
          f'<a class="btn btn-gold" href="/projects.html">پروژه‌ها</a><a class="btn btn-gold" href="/en/">English</a></div></div></section>'
        + footer("fa"))
    # sitemap
    alt_of = {}
    for pth in PAGES:
        if pth.startswith("/en/"): alt_of[pth] = pth[3:] or "/"
        else: alt_of[pth] = "/en" + pth
    rows = []
    for pth in PAGES:
        fa_p = pth if not pth.startswith("/en/") else alt_of[pth]
        en_p = alt_of[pth] if not pth.startswith("/en/") else pth
        pri = "1.0" if pth in ("/", "/en/") else ("0.9" if "services" in pth or "projects.html" in pth else "0.8")
        rows.append(f'  <url><loc>{absu(pth)}</loc><lastmod>{TODAY.isoformat()}</lastmod><priority>{pri}</priority>\n'
                    f'    <xhtml:link rel="alternate" hreflang="fa" href="{absu(fa_p)}"/><xhtml:link rel="alternate" hreflang="en" href="{absu(en_p)}"/>'
                    f'<xhtml:link rel="alternate" hreflang="x-default" href="{absu(fa_p)}"/></url>')
    for f in ("Resume.pdf", "bmn14-paper.pdf"):
        rows.append(f"  <url><loc>{BASE}/{f}</loc><lastmod>{TODAY.isoformat()}</lastmod><priority>0.5</priority></url>")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(rows) + "\n</urlset>\n")
    # robots
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot", "PerplexityBot", "Google-Extended", "Applebot-Extended", "Bingbot", "Googlebot"]
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(
        "User-agent: *\nAllow: /\n\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {BASE}/sitemap.xml\n")
    # llms.txt
    lines = [f"# {NAME['en']} ({NAME['fa']})", "",
             f"> {DISAMBIG['en']} He designs custom machinery and industrial robots and follows them through fabrication, assembly and commissioning; he also offers quality-controlled batch production of industrial parts and consulting. Based in Tehran, Iran.", "",
             f"> {DISAMBIG['fa']}", "",
             "## Key facts", "",
             "- MSc in Mechanical Engineering (Applied Design), Sharif University of Technology (supervisor: Prof. Mohammad Durali); BSc, Iran University of Science and Technology.",
             "- Led the mechanical design of Iran National Post's postal sorting robots (Tensor Intelligent Machines) across three generations: 80 robots in Tehran and Kermanshah; third generation produced as a 200-unit series (1.8 m/s, ~10 kg, 55×55 cm).",
             "- Built a 6-DOF knee prosthesis constraint and stability test apparatus per ASTM F1223 — the first of its kind in Iran.",
             "- Awards: Laureate, 64th Alborz Prize (2026); 2nd Place, 26th Khwarizmi Youth Award (2025); 2nd Place, 24th Khwarizmi Youth Award (2023).",
             f"- Publication: “{PUB['title']}”, Scientific Reports, 2025 ({DOI}).",
             "- Current role: Senior Mechanical Engineer at Karun HiTech Solutions (8,000+ industrial parts delivered).",
             "- Open to: design-and-build projects, multi-robot mobile fleets, batch production of parts with QC, automation/PLC, test rigs, career and award-application consulting. Not seeking employment.", "",
             "## Pages", "",
             f"- [Home (English)]({BASE}/en/): overview", f"- [Services]({BASE}/en/services.html): what he offers, process and FAQ",
             f"- [Projects]({BASE}/en/projects.html): all design-and-build projects", f"- [About]({BASE}/en/about.html): experience, education, awards, publication, skills",
             f"- [Media]({BASE}/en/media.html): TV interviews, documentary and news", f"- [Persian home / صفحه‌ی اصلی فارسی]({BASE}/)", ""]
    lines += ["## Projects", ""] + [f"- [{p['en']['title']}]({absu(url('project', 'en', p['slug']))}): {p['en']['short']}" for p in PROJECTS] + [""]
    lines += ["## Contact", "", f"- Email: {EMAIL}", f"- Phone: {PHONE_EN}", f"- LinkedIn: {LINKEDIN}", f"- Telegram: {TELEGRAM}", f"- Bale: {BALE}", f"- Instagram: {INSTAGRAM}", ""]
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write("\n".join(lines))


def build_og_images():
    try:
        from PIL import Image
    except ImportError:
        print("Pillow not installed: skipping og images (pip install pillow)"); return
    def fit(src, dst, bg=(255, 255, 255), cover=False):
        if os.path.exists(dst): return
        im = Image.open(src).convert("RGB")
        W, H = 1200, 630
        if cover:
            r = max(W / im.width, H / im.height); im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
            x, y = (im.width - W) // 2, (im.height - H) // 2; im = im.crop((x, y, x + W, y + H)); out = im
        else:
            r = min(W / im.width, H / im.height); im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
            out = Image.new("RGB", (W, H), bg); out.paste(im, ((W - im.width) // 2, (H - im.height) // 2))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        out.save(dst, quality=82, optimize=True, progressive=True)
    fit(os.path.join(ROOT, "cover.jpg"), os.path.join(ROOT, "og-image.jpg"), cover=True)
    for p in PROJECTS:
        if p["imgs"]: fit(os.path.join(ROOT, p["imgs"][0][0]), os.path.join(ROOT, "og", p["slug"] + ".jpg"))


def check():
    bad = {"ٔ": "همزه‌ی روی ه", "ۀ": "ۀ", "ي": "ي عربی", "ك": "ك عربی"}
    for pth in PAGES:
        s = open(out_path(pth), encoding="utf-8").read()
        for ch, n in bad.items():
            assert ch not in s, f"{pth}: forbidden char {n}"
        for ref in re.findall(r'(?:src|href|data-full)="(/[^"#?]*)"', s):
            if ref.endswith("/") or ref.startswith("//"): continue
            assert os.path.exists(os.path.join(ROOT, ref.lstrip("/"))), f"{pth}: missing {ref}"


if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    shutil.copy(os.path.join(SRC, "site.css"), os.path.join(ROOT, "assets", "site.css"))
    shutil.copy(os.path.join(SRC, "site.js"), os.path.join(ROOT, "assets", "site.js"))
    build_og_images()
    for L in LANGS:
        build_home(L); build_services(L); build_projects_index(L); build_about(L); build_media(L)
        for i, p in enumerate(PROJECTS): build_project(p, i, L)
    build_extras()
    check()
    print(f"built {len(PAGES)} pages")
