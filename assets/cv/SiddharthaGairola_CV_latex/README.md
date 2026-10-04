# CV sources

    SiddharthaGairola_CV.tex   main style (sans-serif, navy accent)  -> ../SiddharthaGairola_CV.pdf
    cv_content.tex             all CV content except publications, written with semantic macros
    publications.bib           publications as BibTeX; rendered by biblatex, newest first, numbered in reverse
    cv_bib.tex                 biblatex configuration (name highlighting, equal-contribution stars, layout)
    build.sh                   pdflatex -> biber -> pdflatex x2
    alt/                       two alternate styles that render the same content
    legacy/                    the previous resume.cls based CV, kept for reference

## Editing

* **Content** (education, experience, projects, ...): edit `cv_content.tex`.
* **A new paper**: add an entry at the TOP of `publications.bib`.  Mark yourself
  with `author+an = {1=me}` (bold) and equal contributors with `;1=eq;2=eq`
  (superscript star).  `url` makes the title a link; `addendum` adds a short
  highlighted note such as a spotlight.  Use `@unpublished` with
  `note = {Under submission}` for papers in review.
* **Look**: edit `SiddharthaGairola_CV.tex`.  Publication styling hooks are
  `\pubnumfmt`, `\pubtitlefmt`, `\pubvenuefmt`, `\pubnotefmt`.

## Build

    ./build.sh                          # main CV, also updates ../SiddharthaGairola_CV.pdf
    ./build.sh alt/variant_a_classic    # Charter serif, small caps, centered name
    ./build.sh alt/variant_c_timeline   # Palatino, burgundy, dates in a left column

Needs TeX Live with biber and the packages sourcesanspro, XCharter, newpxtext,
fontawesome5, biblatex, titlesec, enumitem, needspace, lastpage, microtype.
The user-local TinyTeX is missing some of these, so the script uses /usr/bin.

## Content macros (cv_content.tex)

    \cvheader                                      name + contact block
    \begin{cvsection}{Title} ... \end{cvsection}
    \cventry{Org}{Location}{Role}{Dates}{Body}
    \cvsubentry{Role}{Dates}{Body}                 second role at same org
    \begin{cvbullets} \item ... \end{cvbullets}
    \cvpublications                                prints publications.bib
    \cvproject{Title}{Dates}{Body}
    \cvline{Label}{Text}
    \cvtalk{Text}                                  plain bullet
    \begin{cvskills} \cvskill{Label}{Text} ... \end{cvskills}
    \cvnote{Text}                                  small right-aligned note
