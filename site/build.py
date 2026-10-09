#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build sidgairo18.github.io from site/content.py + the CV's publications.bib.

    python3 site/build.py            # writes index.html, secondary pages, assets/bib/*.bib

Everything generated is plain static HTML; css/style.css is hand-maintained.
"""
import os, re, sys, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import *  # noqa

BIB_FILE = os.path.join(ROOT, "assets/cv/SiddharthaGairola_CV_latex/publications.bib")
BIB_OUT = os.path.join(ROOT, "assets/bib")


# ---------------------------------------------------------------------------
# BibTeX: parse the CV file, clean each entry for the website
# ---------------------------------------------------------------------------
def parse_bib(path):
    text = open(path, encoding="utf-8").read()
    entries = {}
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", text):
        etype, key = m.group(1).lower(), m.group(2)
        i, depth, j = m.end(), 1, m.end()
        while j < len(text) and depth:
            if text[j] == "{": depth += 1
            elif text[j] == "}": depth -= 1
            j += 1
        body = text[i:j - 1]
        fields = {}
        for fm in re.finditer(r"([\w+:\-]+)\s*=\s*\{", body):
            name = fm.group(1).lower()
            k, d = fm.end(), 1
            while k < len(body) and d:
                if body[k] == "{": d += 1
                elif body[k] == "}": d -= 1
                k += 1
            fields[name] = body[fm.end():k - 1].strip()
        entries[key] = dict(type=etype, key=key, fields=fields)
    return entries


LATEX_MAP = {r"{\'o}": "ó", r"{\'n}": "ń", r'{\"o}': "ö", r'{\"u}': "ü", r'{\"a}': "ä", r"{\'e}": "é", r"\&": "&amp;", "--": "–", "~": " "}


def latex_to_html(s):
    for a, b in LATEX_MAP.items():
        s = s.replace(a, b)
    s = re.sub(r"\$\{\\sim\}\$", "~", s)
    s = s.replace(r"\%", "%")
    s = re.sub(r"[{}]", "", s)
    return html.escape(s, quote=False).replace("&amp;amp;", "&amp;")


def split_authors(field):
    return [latex_to_html(a.strip()) for a in re.split(r"\s+and\s+", field)]


def eq_indices(fields):
    spec = fields.get("author+an:eq", "")
    return {int(x.split("=")[0]) - 1 for x in spec.split(";") if "=" in x}


def protect_title(t):
    """Brace words BibTeX would otherwise lower-case: acronyms (DAVE, ViT, CNN) and
    words with internal capitals (DisParQ, SmartKC++).  Hyphenated Title-Case words
    (Self-Supervised) are left alone; trailing punctuation stays outside the braces."""
    out = []
    for w in t.split(" "):
        m = re.match(r"^(\W*)(.*?)(\W*)$", w)
        lead, core, trail = m.groups()
        parts = [p for p in core.split("-") if p]
        needs = any(re.search(r"[A-Z]", p[1:]) for p in parts) or any(len(p) >= 2 and p.isupper() for p in parts)
        if needs and core and not (lead.startswith("{") or trail.endswith("}")):
            w = f"{lead}{{{core}}}{trail}"
        out.append(w)
    return " ".join(out)


def clean_bibtex(entry, authors):
    """Website BibTeX: standard fields only, consistent layout, true author order."""
    f = entry["fields"]
    etype = entry["type"]
    rows = [("author", " and ".join(authors)), ("title", protect_title(f["title"]))]
    if etype == "inproceedings":
        rows.append(("booktitle", f["booktitle"]))
    elif etype == "article":
        rows.append(("journal", f.get("journaltitle", f.get("journal", ""))))
        if f.get("volume"): rows.append(("volume", f["volume"]))
        if f.get("number"): rows.append(("number", f["number"]))
    elif etype == "unpublished":
        rows.append(("note", f.get("note", "Under submission")))
    elif etype == "misc":
        if f.get("note"): rows.append(("howpublished", f["note"]))
    rows.append(("year", f["year"]))
    if f.get("eprint"):
        rows.append(("eprint", f["eprint"]))
        rows.append(("archiveprefix", {"arxiv": "arXiv"}.get(f.get("eprinttype", "").lower(), f.get("eprinttype", ""))))
        if f.get("eprintclass"): rows.append(("primaryclass", f["eprintclass"]))
    if f.get("url"): rows.append(("url", f["url"]))
    w = max(len(k) for k, _ in rows)
    body = ",\n".join(f"  {k.ljust(w)} = {{{v}}}" for k, v in rows)
    return f"@{etype}{{{entry['key']},\n{body}\n}}\n"


def bib_authors_tex(entry, order_html):
    """Return the raw (LaTeX) author strings in the requested display order."""
    raw = [a.strip() for a in re.split(r"\s+and\s+", entry["fields"]["author"])]
    by_html = {latex_to_html(a): a for a in raw}
    return [by_html.get(a, a) for a in order_html]


# ---------------------------------------------------------------------------
# Small HTML helpers
# ---------------------------------------------------------------------------
def I(k):
    return f'<i class="ico">{ICONS[k]}</i>'


STAR = I("star")


def author_html(name, eq):
    s = f'<a href="{AUTHOR_LINKS[name]}">{name}</a>' if name in AUTHOR_LINKS else name
    if name == ME:
        s = f'<span class="me">{name}</span>'
    return s + ("<sup>*</sup>" if eq else "")


def links_html(links, soon=False, bibkey=None):
    out = []
    for lab, href in links:
        out.append(f'<a href="{href}">{lab}</a>' if href else f'<span class="soon">{lab}</span>')
    if bibkey:
        out.append(f'<a href="#bib-{bibkey}" class="bibtoggle" data-key="{bibkey}">bibtex</a>')
    s = " · ".join(out)
    if soon:
        s += ' <span class="soon-note">(coming soon)</span>'
    return s


def yrange(ys):
    ys = sorted(int(x) for x in ys)
    out, i = [], 0
    while i < len(ys):
        k = i
        while k + 1 < len(ys) and ys[k + 1] == ys[k] + 1:
            k += 1
        out.append(f"{ys[i]}–{str(ys[k])[2:]}" if k > i else str(ys[i]))
        i = k + 1
    return ", ".join(out)


def logo(name, label):
    if name in MASK_LOGOS:
        return f'<span class="lg mask {name}" role="img" aria-label="{label}"></span>'
    return f'<img class="lg {name}" src="images/logos/{name}.svg" alt="{label}">'


def blk(icon, title, body, small=""):
    return f'<div class="blk"><h3>{I(icon)}{title}{f"<small>{small}</small>" if small else ""}</h3>{body}</div>'


def bibpanel(key, bibtex):
    return (f'<div class="bibpanel" id="bib-{key}" hidden><pre>{html.escape(bibtex)}</pre>'
            f'<div class="bar"><button type="button" class="copybib">{I("copy")} Copy</button>'
            f'<a href="assets/bib/{key}.bib" download>{I("download")} Download .bib</a><span class="ok" aria-live="polite"></span></div></div>')


# ---------------------------------------------------------------------------
# Publications
# ---------------------------------------------------------------------------
def build_pubs():
    bib = parse_bib(BIB_FILE)
    os.makedirs(BIB_OUT, exist_ok=True)
    pubs = []
    for ex in PUBS:
        e = bib[ex["key"]]
        f = e["fields"]
        authors = ex.get("authors") or split_authors(f["author"])
        if ex.get("authors"):          # equal-contribution stars follow the CV spec
            cv_order = split_authors(f["author"])
            eq_names = {cv_order[i] for i in eq_indices(f) if i < len(cv_order)}
        else:
            eq_names = {authors[i] for i in eq_indices(f) if i < len(authors)}
        venue = latex_to_html(f.get("booktitle") or f.get("journaltitle") or f.get("note", ""))
        if e["type"] == "article" and f.get("volume"):
            venue += f", {f['volume']}({f.get('number', '')})".replace("()", "")
        addendum = f.get("addendum", "")
        p = dict(ex)
        p.update(title=latex_to_html(f["title"]), year=f["year"], venue=venue,
                 authors_html=", ".join(author_html(a, a in eq_names) for a in authors),
                 spotlight=addendum.lower().startswith("spotlight"),
                 bibtex=clean_bibtex(e, bib_authors_tex(e, authors)),
                 venue_short=f"{ex['badge']} {f['year']}")
        p.setdefault("featured", False); p.setdefault("notes", []); p.setdefault("soon", False)
        p["short"] = p["title"].split(":")[0]
        open(os.path.join(BIB_OUT, f"{p['key']}.bib"), "w", encoding="utf-8").write(p["bibtex"])
        pubs.append(p)
    return pubs


def pub_row(p, more=False, thumb=False, blurb=False):
    tags = f'<span class="tag{" soft" if p["badge"] in ("Preprint", "arXiv") else ""}">{p["badge"]}</span>'
    if p["spotlight"]:
        tags += f'<span class="tag spot">{STAR} Spotlight</span>'
    notes = "".join(f'<p class="nt">{n}</p>' for n in p["notes"])
    th = f'<div class="mini"><img src="{IMG}{p["img"]}" alt=""><img class="hov" src="{IMG}{p["img2"]}" alt=""></div>' if thumb else ""
    ab = f'<p class="ab">{p["blurb"]}</p>' if blurb and p.get("blurb") else ""
    return (f'<li class="pub" id="{p["key"]}" data-tags="{" ".join(p.get("tags", []))}"{" data-more" if more else ""}>{th}<div class="bd"><div class="t">{p["title"]}</div>'
            f'<div class="au">{p["authors_html"]}</div><div class="vn">{tags}<span>{p["venue"]}, {p["year"]}</span></div>{ab}'
            f'<div class="lk">{links_html(p["links"], p["soon"], p["key"])}</div>{notes}{bibpanel(p["key"], p["bibtex"])}</div></li>')


def pubs_by_year(pubs, visible=None, thumbs=False, blurbs=False):
    """visible: set of keys shown before 'Show all' (None = everything visible)."""
    years = sorted({p["year"] for p in pubs}, reverse=True)
    out = []
    for y in years:
        rows = "".join(pub_row(p, more=(visible is not None and p["key"] not in visible), thumb=thumbs, blurb=blurbs and p["featured"]) for p in pubs if p["year"] == y)
        out.append(f'<div class="yr"><div class="y">{y}</div><ul class="plist">{rows}</ul></div>')
    th = THESIS
    more = " data-more" if visible is not None else ""
    out.append(f'<div class="yr"><div class="y">Thesis</div><ul class="plist"><li class="pub" data-tags="{" ".join(th.get("tags", []))}"{more}><div class="bd"><div class="t">{th["title"]}</div>'
               f'<div class="au"><span class="me">{ME}</span></div><div class="vn"><span class="tag soft">{th["badge"]}</span><span>{th["venue"]}, {th["year"]}</span></div>'
               f'<div class="lk">{links_html(th["links"])}</div></div></li></ul></div>')
    return "".join(out)


def card(p):
    gs = f'<span class="gs">{STAR} Spotlight</span>' if p["spotlight"] else ""
    return (f'<article class="card"><a class="fig" href="#{p["key"]}" aria-label="{p["title"]}"><img src="{IMG}{p["img"]}" alt=""><img class="hov" src="{IMG}{p["img2"]}" alt=""></a>'
            f'<div class="bd"><div class="k">{p["venue_short"]}{gs}</div><div class="t"><a href="#{p["key"]}">{p["short"]}</a></div>'
            f'<p class="ab">{p.get("blurb", "")}</p><div class="lk">{links_html(p["links"], p["soon"], p["key"])}</div></div></article>')


# ---------------------------------------------------------------------------
# Page pieces
# ---------------------------------------------------------------------------
# Google Analytics, placed first in <head> as Google recommends; identical on every page.
ANALYTICS = f"""<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_ID}');
</script>"""


def head(title, description, extra="", url=None):
    url = url or SITE_URL + "/"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{ANALYTICS}
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{SITE_URL}/images/sid_beard_profile_paris.jpg">
<meta property="og:url" content="{url}">
<link rel="canonical" href="{url}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧙</text></svg>">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">{extra}
</head>'''


THEME_BTN = f'<button id="theme-btn" type="button" title="Toggle dark mode" aria-label="Toggle dark mode"><i class="ico moon">{ICONS["moon"]}</i><i class="ico sun">{ICONS["sun"]}</i></button>'

SCRIPTS = """<script>
(function(){var b=document.getElementById('theme-btn');if(!b)return;function cur(){var t=document.documentElement.getAttribute('data-theme');if(t)return t;return window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';}
b.addEventListener('click',function(){var n=cur()==='dark'?'light':'dark';document.documentElement.setAttribute('data-theme',n);try{localStorage.setItem('theme',n);}catch(e){}});})();
(function(){
document.querySelectorAll('.bibtoggle').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();var p=document.getElementById('bib-'+a.getAttribute('data-key'));if(!p)return;
var inCard=!!a.closest('.card');if(inCard){p.hidden=false;document.getElementById(a.getAttribute('data-key')).scrollIntoView({behavior:'smooth',block:'center'});}else{p.hidden=!p.hidden;}});});
document.querySelectorAll('.copybib').forEach(function(b){b.addEventListener('click',function(){var panel=b.closest('.bibpanel'),txt=panel.querySelector('pre').textContent,ok=panel.querySelector('.ok');
function done(){ok.textContent='Copied';setTimeout(function(){ok.textContent='';},1600);}
if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(done);}else{var r=document.createRange();r.selectNodeContents(panel.querySelector('pre'));var s=window.getSelection();s.removeAllRanges();s.addRange(r);try{document.execCommand('copy');done();}catch(e){}s.removeAllRanges();}});});
var sec=document.getElementById('publications'),fb=document.querySelectorAll('.filters button'),tb=document.getElementById('pubs-toggle'),tag='all',expanded=!tb;
function apply(){if(!sec)return;sec.querySelectorAll('.pub[data-tags]').forEach(function(li){var mt=(tag==='all'||(' '+li.getAttribute('data-tags')+' ').indexOf(' '+tag+' ')>=0);li.hidden=!(mt&&(expanded||!li.hasAttribute('data-more')));});
sec.querySelectorAll('.yr').forEach(function(y){y.hidden=!y.querySelector('.pub:not([hidden])');});if(tb){tb.textContent=expanded?'Show fewer ↑':tb.getAttribute('data-label');var ttl=document.getElementById('pubs-title'),fl=sec.querySelector('.filters');if(ttl)ttl.textContent=expanded?'Publications':'Selected publications';if(fl)fl.hidden=!expanded;}}
fb.forEach(function(b){b.addEventListener('click',function(){tag=b.getAttribute('data-tag');fb.forEach(function(x){x.classList.toggle('on',x===b);});if(tag!=='all')expanded=true;apply();});});
if(tb){tb.addEventListener('click',function(){expanded=!expanded;if(!expanded){tag='all';fb.forEach(function(x){x.classList.toggle('on',x.getAttribute('data-tag')==='all');});}apply();if(!expanded)sec.scrollIntoView({behavior:'smooth',block:'start'});});}
(function(){var c=document.getElementById('cover');if(!c)return;var s=[].slice.call(c.querySelectorAll('.slide')),cap=c.querySelector('figcaption'),i=0,n=s.length,t=null,iv=+c.getAttribute('data-interval')||7000,rm=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
function load(k){var im=s[(k+n)%n];if(im.getAttribute('data-src')){im.src=im.getAttribute('data-src');im.removeAttribute('data-src');}}
function go(k){i=(k+n)%n;load(i);load(i+1);s.forEach(function(im,j){im.classList.toggle('on',j===i);});cap.textContent=s[i].getAttribute('data-caption');}
function start(){if(rm||n<2)return;stop();t=setInterval(function(){go(i+1);},iv);}function stop(){if(t){clearInterval(t);t=null;}}
c.querySelector('.prev').addEventListener('click',function(){go(i-1);start();});c.querySelector('.next').addEventListener('click',function(){go(i+1);start();});
c.addEventListener('mouseenter',stop);c.addEventListener('mouseleave',start);c.addEventListener('focusin',stop);c.addEventListener('focusout',start);
c.addEventListener('keydown',function(e){if(e.key==='ArrowLeft'){go(i-1);}else if(e.key==='ArrowRight'){go(i+1);}});
document.addEventListener('visibilitychange',function(){document.hidden?stop():start();});
c.classList.add('init');go(Math.floor(Math.random()*n));var f=s[i];function ready(){requestAnimationFrame(function(){requestAnimationFrame(function(){c.classList.remove('init');});});}if(f.complete&&f.naturalWidth){ready();}else{f.addEventListener('load',ready,{once:true});f.addEventListener('error',ready,{once:true});}start();})();
var nm=document.getElementById('news-more'),nt=document.getElementById('news-toggle');if(nm&&nt){nt.addEventListener('click',function(){nm.hidden=!nm.hidden;nt.textContent=nm.hidden?nt.getAttribute('data-open'):nt.getAttribute('data-close');});}
if(location.hash){var tgt=document.getElementById(location.hash.replace(/^#(bib-)?/,''));if(tgt&&tgt.hasAttribute('data-more')){expanded=true;}}
apply();
if(location.hash&&location.hash.indexOf('#bib-')===0){var p=document.getElementById(location.hash.slice(1));if(p)p.hidden=false;}
})();
</script>"""


def build_index(pubs, mode="all"):
    """mode: "all" (cards + full list), "latest" (cards + first LATEST_N in list, rest behind Show all),
    "selected" (no cards; list shows featured papers with thumbnails, rest behind Show all)."""
    icons = "".join((f'<a class="pri" href="{h}" title="{l}">{I(ic)}<span>{l}</span></a>' if l == "CV"
                     else f'<a href="{h}" title="{l}" aria-label="{l}">{I(ic)}</a>') for l, ic, h in TOPLINKS)
    # news
    def nitem(d, b, t):
        t = t.replace("<b>Spotlight</b>", f'<b class="gs" style="font-size:inherit;letter-spacing:0;text-transform:none;margin:0">{STAR} Spotlight</b>')
        return f'<li><time>{d}</time><span>{f"<b>{b}</b>" if b else ""}{t}</span></li>'
    news = (f'<ul class="news">{"".join(nitem(*n) for n in NEWS[:NEWS_SHOWN])}</ul>'
            f'<ul class="news" id="news-more" hidden>{"".join(nitem(*n) for n in NEWS[NEWS_SHOWN:])}</ul>'
            f'<div class="showall"><button type="button" id="news-toggle" data-open="Older news ↓" data-close="Show fewer ↑">Older news ↓</button></div>')
    # background
    exp = "".join(f'<li>{logo(lg, c)}<div class="l"><b>{c}</b><span>{r}</span></div><div class="r">{d}</div></li>' for c, r, d, lg in EXPERIENCE)
    edu = "".join(f'<li>{logo(lg, n)}<div class="l"><b><a href="{h}">{n}</a></b>{"".join(f"<span>{x}</span>" for x in degs)}</div><div class="r">{d}</div></li>' for n, h, degs, d, lg in EDUCATION)
    exp_list = '<ul class="rows withlogo">' + exp + '</ul>'
    edu_list = '<ul class="rows withlogo">' + edu + '</ul>'
    background = '<div class="blocks">' + blk("briefcase", "Experience", exp_list) + blk("cap", "Education", edu_list) + '</div>'
    # service
    organizing = "".join(f'<li><div class="l"><b><a href="{h}">{t}</a></b><span>{r} · ' + " · ".join(f'<a href="{vh}"><span class="k" style="margin:0">{v}</span></a>' for v, vh in venues) + '</span></div></li>' for t, h, r, venues in ORGANIZING)
    def revitem(v, y):
        g = STAR.replace('class="ico"', 'class="gs ico"') if GOLD_REVIEWS.get(v) else ""
        return f'<span class="rv"><b>{v}</b> {yrange([x.strip() for x in y.split(",")])}{g}</span>'
    reviewing = f'<p class="revline">{"".join(revitem(v, y) for v, y in REVIEWING)}</p><div class="legend">{STAR} {GOLD_LEGEND}</div>'
    talks = '<ul class="rows">' + "".join(f'<li><div class="l"><b>{t}</b><span>{v} · <a class="lnk" href="{lk[1]}">{I(lk[0])} {lk[0]}</a></span></div><div class="r">{y}</div></li>' for t, v, y, lk in TALKS) + '</ul>'
    def teach(n, h, role, per, cs, lg):
        cl = "".join(f'<li><span>{c}</span><span>{t}</span></li>' for c, t in cs)
        return f'<li class="teach">{logo(lg, n)}<div class="l"><b><a href="{h}">{n}</a></b><span>{role}</span></div><div class="r">{per}</div><ul class="courses">{cl}</ul></li>'
    ncourses = sum(len(cs) for *_, cs, _ in TEACHING)
    teaching = '<ul class="rows withlogo">' + "".join(teach(*t) for t in TEACHING) + '</ul>'
    oss = '<ul class="rows">' + "".join(f'<li><div class="l"><b><a href="{h}">{t}</a></b><span>{d}</span></div></li>' for t, h, d in OPENSOURCE) + '</ul>'
    vol = '<ul class="rows">' + "".join(f'<li><div class="l"><b><a href="{h}">{t}</a></b><span>{r}</span></div></li>' for t, h, r in VOLUNTEERING) + '</ul>'
    service = ('<div class="blocks">' + blk("users", "Organizing", f'<ul class="rows">{organizing}</ul>') + blk("clipboard", "Reviewing", reviewing)
               + blk("mic", "Talks", talks, f"{len(TALKS)} talks") + blk("chalk", "Teaching", teaching, f"teaching assistant · {ncourses} courses")
               + blk("code", "Open source", oss) + blk("heart", "Volunteering", vol) + '</div>')
    resources = "".join(blk(ic, title, '<ul class="res">' + "".join(f'<li><a href="{h}">{t}</a><span>{d}</span></li>' for t, h, d in items) + '</ul>') for ic, title, items in RESOURCES)
    def slide(i, s):
        f, cap = s[0], s[1]
        pos = f' style="object-position:{s[2]}"' if len(s) > 2 else ""
        return f'<img class="slide" data-src="{IMG}{f}" alt="{cap}" data-caption="{cap}"{pos}>'
    cover = (f'<figure class="cover" id="cover" tabindex="0" aria-label="Travel photos" data-interval="{COVER_INTERVAL_MS}">'
             + "".join(slide(i, s) for i, s in enumerate(COVER))
             + f'<button type="button" class="cnav prev" aria-label="Previous photo">{I("chevron-left")}</button>'
             + f'<button type="button" class="cnav next" aria-label="Next photo">{I("chevron-right")}</button>'
             + f'<figcaption aria-live="polite"></figcaption><noscript><img class="slide on" src="{IMG}{COVER[0][0]}" alt="{COVER[0][1]}"></noscript></figure>')
    sel = [p for p in pubs if p["featured"]]
    selected_section = f'<section id="selected"><h2>Selected work<a href="#publications">all {len(pubs)} papers ↓</a></h2><div class="cards">{"".join(card(p) for p in sel)}</div></section>' if mode != "selected" else ""
    if mode == "latest":
        visible = {p["key"] for p in pubs[:LATEST_N]}
        publist = pubs_by_year(pubs, visible)
    elif mode == "selected":
        visible = {p["key"] for p in sel}
        publist = pubs_by_year(pubs, visible, thumbs=True, blurbs=True)
    else:
        visible, publist = None, pubs_by_year(pubs)
    showall = (f'<div class="showall"><button type="button" id="pubs-toggle" data-label="Show all {len(pubs)} papers ↓">Show all {len(pubs)} papers ↓</button></div>' if visible is not None else "")
    filters = (f'<div class="filters" role="group" aria-label="Filter publications by topic"{" hidden" if visible is not None else ""}><span class="flabel">Filter by topic</span>'
               '<button type="button" data-tag="all" class="on">All</button>'
               + "".join(f'<button type="button" data-tag="{t}">{l}</button>' for t, l in TAGS) + '</div>')
    desc = f"{ME} — ELLIS PhD student at the Max Planck Institute for Informatics and ISTA. Computer vision, representation learning, interpretability."
    jsonld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Person","name":"' + ME + '","url":"' + SITE_URL + '/",'
              '"jobTitle":"PhD student","affiliation":[{"@type":"Organization","name":"Max Planck Institute for Informatics"},{"@type":"Organization","name":"Institute of Science and Technology Austria"}],'
              '"sameAs":["' + SCHOLAR.replace("&amp;", "&") + '","https://github.com/sidgairo18","' + LINKEDIN + '","https://twitter.com/sidgairo18"]}</script>')
    return f'''{head(ME, desc, extra=jsonld, url=SITE_URL + "/")}
<body>{THEME_BTN}<div class="wrap">
{cover}
<header class="hdr"><img src="{IMG}sid_beard_profile_paris.jpg" alt="{ME}"><div><h1>{ME}</h1><p class="sub">{TAGLINE}</p><nav class="icons" aria-label="Links">{icons}</nav></div></header>
<section class="bio" id="about">{"".join(f"<p>{p}</p>" for p in BIO)}<p class="off">{OFFHOURS}</p></section>
<section id="news"><h2>News</h2>{news}</section>
{selected_section}
<section id="publications"><h2><span id="pubs-title">{"Selected publications" if visible is not None else "Publications"}</span><a href="{SCHOLAR}">Google Scholar ↗</a></h2>{filters}{publist}{showall}<p class="eqnote"><sup>*</sup>equal contribution · click <em>bibtex</em> on an entry to copy or download its citation</p></section>
<section id="background"><h2>Background<a href="{CV_PDF}">full CV (PDF) ↗</a></h2>{background}</section>
<section id="service"><h2>Academic service &amp; more</h2>{service}</section>
<section id="resources"><h2>Writing &amp; resources</h2><div class="rgroups">{resources}</div></section>
<footer style="margin-top:56px"><span>© 2026 {ME}</span><span>Updated {UPDATED}</span></footer>
</div>{SCRIPTS}</body></html>
'''


def build_page(slug, bibs=None):
    frag = open(os.path.join(ROOT, "site/pages", slug + ".html"), encoding="utf-8").read()
    meta = dict(re.findall(r"<!--\s*(\w+):\s*(.*?)\s*-->", frag))
    body = re.sub(r"^(<!--.*?-->\s*)+", "", frag, flags=re.S)
    body = re.sub(r'<(h[23])([^>]*?)\s+data-icon="(\w+)"([^>]*)>', lambda m: f'<{m.group(1)}{m.group(2)}{m.group(4)} class="hi">{I(m.group(3))}', body)
    body = re.sub(r'<i data-icon="(\w+)"></i>', lambda m: f'<i class="ico inl">{ICONS[m.group(1)]}</i>', body)
    # Links to files hosted on the site render as download pills, site-wide.
    def pill(m):
        attrs, label = m.group(1), m.group(2)
        attrs = re.sub(r'\s*class="[^"]*"', '', attrs)
        return f'<a class="dl file"{attrs} download>{I("download")}{label}</a>'
    body = re.sub(r'<a((?:(?!href=)[^>])*?href="(?:\./)?(?:assets|grad_school_resources)/[^"]+\.(?:pdf|zip|pptx|key|bib)"[^>]*)>(.*?)</a>', pill, body, flags=re.S)
    if bibs:
        body = re.sub(r'<!--\s*bibtex:\s*(\S+)\s*-->', lambda m: bibpanel(m.group(1), bibs[m.group(1)]).replace(' hidden>', '>', 1), body)
    title = meta["title"]
    back_href, back_label = [x.strip() for x in meta["back"].split("|")]
    wide = meta.get("wide") == "true"
    h1 = "" if meta.get("notitle") == "true" else f"<h1>{title}</h1>"
    nav = "".join(f'<a href="{h}">{l}</a>' for l, h in SUBNAV)
    extra = f'<base href="{SITE_URL}/">' if meta.get("base") == "true" else ""
    return f'''{head(f"{title} · {ME}", f"{title} — {ME}", extra=extra, url=f"{SITE_URL}/{slug}.html")}
<body>
<div class="topbar"><div class="in"><a class="nm" href="index.html">{ME}</a><nav>{nav}{THEME_BTN}</nav></div></div>
<main class="page{" wide" if wide else ""}"><a class="back" href="{back_href}">← {back_label}</a>{h1}
<div class="prose">
{body.strip()}
</div>
<footer style="margin-top:56px"><span>© 2026 {ME}</span><span><a href="index.html">sidgairo18.github.io</a></span></footer>
</main>{SCRIPTS}</body></html>
'''


def main():
    pubs = build_pubs()
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(build_index(pubs, PUB_MODE))
    if "--variants" in sys.argv:   # side-by-side previews of the publication-section modes
        for m in ("all", "latest", "selected"):
            open(os.path.join(ROOT, f"index_{m}.html"), "w", encoding="utf-8").write(build_index(pubs, m))
    bibs = {p["key"]: p["bibtex"] for p in pubs}
    for slug in PAGES:
        open(os.path.join(ROOT, slug + ".html"), "w", encoding="utf-8").write(build_page(slug, bibs))
    urls = [SITE_URL + "/"] + [f"{SITE_URL}/{p}.html" for p in PAGES if p != "404"]
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    print(f"built index.html, {len(PAGES)} pages, {len(pubs)} bib files, sitemap.xml, robots.txt")


if __name__ == "__main__":
    main()
