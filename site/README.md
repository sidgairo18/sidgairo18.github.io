# Site source

The website is static HTML generated from this folder. Edit the source, run the
build, commit the generated files together with the source.

    python3 site/build.py

| What | Where |
|---|---|
| Homepage text, news, experience, service, resources | `site/content.py` |
| Publications (authors, title, venue, year, url) | `assets/cv/SiddharthaGairola_CV_latex/publications.bib` (shared with the CV) |
| Publication extras (figures, links, blurbs, featured flag) | `PUBS` in `site/content.py`, keyed by BibTeX key |
| Secondary pages (personal, guides, project page) | `site/pages/<slug>.html` (body only; title and back link in the header comments) |
| Styles | `css/style.css` (hand-maintained, not generated) |
| Templates / HTML assembly | `site/build.py` |
| Generated on build | `index.html`, the secondary pages, `404.html`, `assets/bib/*.bib`, `sitemap.xml`, `robots.txt` |

## Common edits

**Add a paper.** Add the entry at the top of `publications.bib` (the CV prints file
order). Then add a `dict(key=..., badge=..., img=..., img2=..., links=[...])` to `PUBS`
in `content.py` with the same key. Use two different figure files for `img`/`img2`
to get the hover swap; set `featured=True` (and a one-line `blurb`) to show it before
"Show all" in the Selected publications view. If the real author order differs from the CV's (the CV lists
S. Gairola first for equal-contribution papers), give the true order in `authors`.
The build writes a clean `assets/bib/<key>.bib` for every paper and embeds the same
text in the page's copy/download panel.

**Publication section layout.** `PUB_MODE` in `content.py`: `selected` (default; the list
opens on featured papers under "Selected publications" with a "Show all" button, and the
topic filters appear once expanded), `latest` (newest `LATEST_N` first), or `all`.
`python3 site/build.py --variants` writes `index_<mode>.html` previews for comparison.

**Add news.** Prepend a `(date, venue tag or "", html)` tuple to `NEWS`. The first
`NEWS_SHOWN` items are visible; the rest fold behind "Older news".

**Add a talk, course, reviewer year.** Edit `TALKS`, `TEACHING`, `REVIEWING` in
`content.py`. Years in `REVIEWING` are compressed into ranges automatically.

**Add a secondary page.** Create `site/pages/<slug>.html` starting with
`<!-- title: ... -->` and `<!-- back: href | label -->`, add the slug to `PAGES`,
and link it from `RESOURCES`.

**Logos.** `images/logos/*.svg`. Single-colour marks (`MASK_LOGOS`) are applied as
CSS masks so they recolour in dark mode; set their colours in `.lg.<name>` rules in
`css/style.css`.

## Notes

* Figures in `images/` are served as JPEGs at most 1000–1200 px wide (full-resolution originals
  live in `archive/images/originals/`). When adding a figure, downscale it similarly.

* Fonts: Geist from Google Fonts, with system sans fallbacks.
* Dark mode follows the system and can be toggled; the choice is stored in
  `localStorage`.
* Masked logos do not render when a page is opened from disk in Firefox
  (file:// is cross-origin for mask images). They render on the live site and in
  Chrome.
