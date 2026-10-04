#!/usr/bin/env bash
# Build the CV.  Run from this directory.
#   ./build.sh                       -> builds SiddharthaGairola_CV.tex and
#                                       copies the PDF to ../SiddharthaGairola_CV.pdf
#   ./build.sh alt/variant_a_classic -> builds an alternate style into build/
# Runs pdflatex -> biber -> pdflatex x2.  Uses the system TeX Live.
set -u
cd "$(dirname "$0")"
export PATH=/usr/bin:$PATH
v=${1:-SiddharthaGairola_CV}; out=${2:-build}
name=$(basename "$v")
mkdir -p "$out"
pdflatex -interaction=nonstopmode -output-directory="$out" "$v.tex" >/dev/null 2>&1
biber --quiet --output-directory "$out" "$name" >/dev/null 2>&1 || echo "!! biber failed (see $out/$name.blg)"
for i in 1 2; do pdflatex -interaction=nonstopmode -output-directory="$out" "$v.tex" >/dev/null 2>&1; done
errs=$(grep -c '^!' "$out/$name.log")
echo "== $name: $errs errors, $(pdfinfo "$out/$name.pdf" 2>/dev/null | awk '/Pages/{print $2}') pages, $(grep -c 'Overfull' "$out/$name.log") overfull, $(grep -c 'WARN' "$out/$name.blg" 2>/dev/null) biber warnings"
grep -A3 '^!' "$out/$name.log" | head -20
if [ $# -eq 0 ] && [ "$errs" -eq 0 ]; then cp "$out/$name.pdf" ../SiddharthaGairola_CV.pdf && echo "-> ../SiddharthaGairola_CV.pdf updated"; fi
