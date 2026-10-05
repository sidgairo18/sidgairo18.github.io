# -*- coding: utf-8 -*-
"""
Content for sidgairo18.github.io.  Edit this file, then run  python3 site/build.py

Publications: bibliographic data (authors, title, venue, year, url) comes from the
CV's BibTeX file  assets/cv/SiddharthaGairola_CV_latex/publications.bib  so the CV
and the website never drift apart.  PUBS below only adds website extras (images,
links, blurb, featured flag) keyed by the BibTeX key.

To add a paper:   1) add it to publications.bib (top of the file, newest first)
                  2) add an entry to PUBS below with the same key
                  3) drop its figure(s) into images/ and run the build.
To add news:      prepend a tuple to NEWS.
"""

ME = "Siddhartha Gairola"
EMAIL = "sgairola@mpi-inf.mpg.de"
SITE_URL = "https://sidgairo18.github.io"
UPDATED = "October 2026"
GA_ID = "UA-120374008-1"          # Google Analytics property, emitted first in every page head
IMG = "images/"

TAGLINE = "PhD student in computer vision &amp; machine learning · MPI for Informatics &amp; ISTA"

# Links used in the icon row.  (label, icon, href)
LINKEDIN = "https://www.linkedin.com/in/siddharthagairola"
SCHOLAR = "https://scholar.google.co.in/citations?user=4tInxbgAAAAJ&hl=en"
CV_PDF = "assets/cv/SiddharthaGairola_CV.pdf"
TOPLINKS = [
    ("CV", "cv", CV_PDF),
    ("Short bio (text)", "idcard", "assets/cv/SidGairola-bio.txt"),
    ("Email", "mail", "mailto:" + EMAIL),
    ("Google Scholar", "scholar", SCHOLAR),
    ("GitHub", "github", "https://www.github.com/sidgairo18"),
    ("LinkedIn", "linkedin", LINKEDIN),
    ("Twitter / X", "x", "https://twitter.com/sidgairo18"),
    ("Personal page", "user", "personal.html"),
]

# People who get a hyperlink wherever they appear in an author list.
BS = "https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/people/bernt-schiele"
FL = "https://www.francescolocatello.com/"
PJN = "https://faculty.iiit.ac.in/~pjn/"
AUTHOR_LINKS = {
    "Bernt Schiele": BS,
    "Francesco Locatello": FL,
    "P. J. Narayanan": PJN,
    "Rajvi Shah": "https://cvit.iiit.ac.in/people/phd/phd-students/rajvi-shah",
    "Nipun Kwatra": "https://www.microsoft.com/en-us/research/people/nkwatra/",
    "Mohit Jain": "https://mohitjaindr.github.io/",
    "Sukrut Rao": "https://sukrutrao.github.io/",
    "Adam Wróbel": "https://www.linkedin.com/in/adamvrobel/",
    "Bartosz Zieliński": "https://bartoszzielinski.github.io/",
    "Dawid Rymarczyk": "https://dawrym.github.io/",
    "Adam Pardyl": "https://adam.pardyl.com/",
    "Jiahao Xie": "https://jiahao000.github.io/",
    "Anna Kukleva": "https://annusha.github.io/",
    "Moritz Böhle": "https://moboehle.github.io/",
    "Jacek Tabor": "https://jacek-tabor.u.matinf.uj.edu.pl/",
    "Vaibhav Ganatra": "https://ganatra-v.github.io/",
    "Vasudeva Varma": "https://faculty.iiit.ac.in/~vv/Home.html",
}

BIO = [
    'I am an <a href="https://ellis.eu/phd-postdoc">ELLIS PhD student</a> at the <a href="https://www.mpi-inf.mpg.de/home">Max Planck Institute for Informatics</a> and <a href="https://ist.ac.at/en/home/">ISTA</a>, advised by <a href="' + BS + '">Bernt Schiele</a> and <a href="' + FL + '">Francesco Locatello</a>. My research centres on representation learning for vision and vision-language foundation models. I am especially interested in how these models can be used for visual understanding tasks such as detection, segmentation and localisation, and in making deep networks interpretable.',
    'Before the PhD I was a Research Fellow at <a href="https://www.microsoft.com/en-us/research/lab/microsoft-research-india/">Microsoft Research India</a>, building low-cost smartphone diagnostics for eye care, and a research intern at <a href="https://www.adobe.com/in/">Adobe</a>. I did my MS and B.Tech at <a href="http://iiit.ac.in">IIIT Hyderabad</a> with <a href="' + PJN + '">P.&thinsp;J. Narayanan</a>.',
]
# Topic tags.  The publication list has a subtle filter row built from these;
# every PUBS entry lists the tag ids that apply to it.
TAGS = [("repr", "Representation learning"), ("vlm", "Vision-language models"),
        ("understanding", "Visual understanding"), ("interp", "Interpretability"), ("misc", "Misc")]
OFFHOURS = ('When not working on my research, I like to play the piano 🎹 and guitar 🎸, listen to music 🎧, read non-fiction 📚, '
            'drive motorcycles 🏍️, and go for a run 🏃 or hike 🥾. I am also really fascinated by paradoxes ♾️ '
            '(you can find some <a href="https://en.wikipedia.org/wiki/List_of_paradoxes">here</a>), and I wish I had Hermione\'s '
            '<a href="https://harrypotter.fandom.com/wiki/Time-Turner">Time-Turner</a> ⏳ to do much more in a day. '
            'See more at <a href="personal.html">Personal</a>.')

# (date, venue tag or "", html).  Newest first; the first NEWS_SHOWN are visible, the rest fold away.
NEWS_SHOWN = 4

# Publication section layout: "all" = selected-work cards + full list;
# "latest" = cards + only the newest LATEST_N in the list, rest behind "Show all";
# "selected" = no cards, list shows featured papers (with thumbnails), rest behind "Show all".
PUB_MODE = "selected"
LATEST_N = 5
NEWS = [
    ("Sep 2026", "NeurIPS", '<em>Stranger Things</em> accepted at NeurIPS 2026.'),
    ("May 2026", "ICML", '<em>DAVE</em> accepted at ICML 2026 as a <b>Spotlight</b> (top 2.2%).'),
    ("Feb 2026", "CVPR", '<em>ALOE</em> accepted at CVPR 2026.'),
    ("Feb 2026", "", 'DAVE pre-print on distribution-aware attribution for ViTs on <a href="https://arxiv.org/abs/2602.06613">arXiv</a>.'),
    ("Aug 2025", "WACV", '<em>SmartKC++</em> accepted at WACV 2025.'),
    ("Jan 2025", "ICLR", '<a href="https://openreview.net/forum?id=57NfyYxh5f"><em>How to Probe</em></a> accepted at ICLR 2025.'),
    ("Oct 2024", "", 'Invited talk at the <a href="https://gmum.net/">GMUM Workshop, Jagiellonian University</a> on XAI in visual models.'),
    ("Sep 2022", "", 'Started my PhD at MPI for Informatics as part of the <a href="https://ellis.eu/phd-postdoc">ELLIS PhD program</a>.'),
    ("2022", "", 'Auto-retinoscopy and keratoconus classifier papers published at IMWUT and EMBC.'),
    ("2021", "", 'SmartKC published at IMWUT; RespireNet at EMBC 2021.'),
]

# ---------------------------------------------------------------------------
# Publications: website extras keyed by BibTeX key (see docstring).
#   badge        short venue label shown as a tag
#   featured     True -> shown before "Show all" (and in the cards, in the card modes)
#   img / img2   figure shown normally / on hover (use two different files)
#   links        [(label, href or None)]; None renders as a greyed placeholder
#   soon         True -> "(coming soon)" after the links
#   blurb        one sentence for the card (featured papers only)
#   notes        extra lines under the entry (workshop acceptances etc.)
#   tags         topic tag ids from TAGS (drives the filter row)
#   authors      optional true author order when it differs from the CV (which
#                lists S. Gairola first for equal-contribution papers)
# ---------------------------------------------------------------------------
PUBS = [
    dict(key="gairola2026disparq", tags=['interp', 'repr'], badge="Preprint", featured=True, img="dpq_1.jpg", img2="dpq_2.jpg",
         links=[("arxiv", None), ("code", None)], soon=True,
         authors=["Adam Pardyl", "Siddhartha Gairola", "Sukrut Rao", "Adam Wróbel", "Bartosz Zieliński", "Bernt Schiele", "Dawid Rymarczyk"]),
    dict(key="gairola2026stranger", tags=['understanding', 'repr'], badge="NeurIPS", featured=True, img="sb_1.jpg", img2="sb_2.jpg",
         links=[("arxiv", None), ("code", None), ("dataset", None)], soon=True,
         blurb="Do vision models still recognise an object once its usual neighbours are gone? A dataset and study of context reliance."),
    dict(key="gairola2026dave", tags=['interp'], badge="ICML", featured=True, img="dave_1.jpg", img2="dave_2.jpg",
         links=[("arxiv", "https://arxiv.org/abs/2602.06613"), ("code", "https://github.com/a-vrobell/DAVE"), ("slides", "assets/presentations/dave_ppt.pdf")],
         blurb="Distribution-aware attribution for ViTs: stable, high-resolution saliency maps without patch-grid artifacts.",
         authors=["Adam Wróbel", "Siddhartha Gairola", "Jacek Tabor", "Bernt Schiele", "Bartosz Zieliński", "Dawid Rymarczyk"]),
    dict(key="gairola2026aloe", tags=['interp', 'repr', 'vlm'], badge="CVPR", featured=True, img="aloe_1.jpg", img2="aloe_2.jpg",
         links=[("abstract", "https://cvpr.thecvf.com/virtual/2026/poster/40400"), ("arxiv", None), ("code", None), ("project page", None)],
         blurb="One label-free alignment step turns DINOv3 or SigLIP2 into an inherently interpretable B-cos model.",
         notes=['Spotlight at the <a href="https://sites.google.com/view/how-cvpr-workshop">HOW Workshop</a> and poster at the <a href="https://xai4cv-workshop.github.io/xai4cv2026/">XAI4CV Workshop</a>, CVPR 2026.'],
         authors=["Raphael Maser", "Siddhartha Gairola", "Sukrut Rao", "Bernt Schiele"]),
    dict(key="gairola2025probe", tags=['interp', 'repr'], badge="ICLR", featured=True, img="probe_1.jpg", img2="probe_2.jpg",
         links=[("openreview", "https://openreview.net/forum?id=57NfyYxh5f"), ("arxiv", "https://arxiv.org/pdf/2503.00641"), ("code", "https://github.com/sidgairo18/how-to-probe")],
         blurb="How the final layer is trained (&lt;10% of parameters) shapes post-hoc explanations; simple fixes improve them markedly."),
    dict(key="ganatra2025smartkcpp", tags=['misc'], badge="WACV", img="smartkc_plusplus.png", img2="smartkc_plusplus.png",
         links=[("paper", "https://openaccess.thecvf.com/content/WACV2025/html/Ganatra_SmartKC_Improving_Performance_of_Smartphone-Based_Corneal_Topographers_WACV_2025_paper.html"), ("code", "https://github.com/microsoft/SmartKC-A-Smartphone-based-Corneal-Topographer")]),
    dict(key="gairola2022keratoconus", tags=['misc'], badge="EMBC", img="device_and_setup.png", img2="device_and_setup.png",
         links=[("arxiv", "https://arxiv.org/abs/2205.03702"), ("pdf", "https://arxiv.org/pdf/2205.03702.pdf")]),
    dict(key="aggarwal2022retinoscopy", tags=['misc'], badge="IMWUT", img="auto_retinoscopy.jpeg", img2="auto_retinoscopy.jpeg",
         links=[("pdf", "https://arxiv.org/pdf/2208.05552.pdf"), ("code", "https://github.com/microsoft/Auto-retinoscopy"), ("project page", "https://www.microsoft.com/en-us/research/project/auto-retinoscopy-automating-retinoscopy-for-refractive-error-diagnosis/")]),
    dict(key="gairola2021smartkc", tags=['misc'], badge="IMWUT", img="corneal_topographer.png", img2="corneal_topographer.png",
         links=[("pdf", "assets/papers/smartkc.pdf"), ("code", "https://github.com/microsoft/SmartKC-A-Smartphone-based-Corneal-Topographer"), ("project page", "https://www.microsoft.com/en-us/research/project/smartkc-a-smartphone-based-corneal-topographer/"), ("video", "https://www.youtube.com/watch?v=rp4uyzf6e2Q")]),
    dict(key="gairola2021respirenet", tags=['misc'], badge="EMBC", img="respirenet.png", img2="respirenet.png",
         links=[("arxiv", "https://arxiv.org/abs/2011.00196"), ("pdf", "assets/papers/respirenet.pdf"), ("code", "https://github.com/microsoft/RespireNet")]),
    dict(key="gairola2020simpropnet", tags=['understanding'], badge="IJCAI", img="fss.png", img2="fss.png",
         links=[("proceedings", "https://www.ijcai.org/Proceedings/2020/80"), ("pdf", "https://www.ijcai.org/Proceedings/2020/0080.pdf")]),
    dict(key="gairola2020style", tags=['repr'], badge="WACV", img="gram.png", img2="b-tri.png",
         links=[("paper", "https://openaccess.thecvf.com/content_WACV_2020/html/Gairola_Unsupervised_Image_Style_Embeddings_for_Retrieval_and_Recognition_Tasks_WACV_2020_paper.html"), ("code", "https://github.com/sidgairo18/unsupervised-style-learning"), ("project page", "style.html"), ("supplementary", "assets/papers/style_supp.pdf")]),
    dict(key="kumar2018clickbait", tags=['vlm', 'misc'], badge="SIGIR", img="clickbait_before.png", img2="clickbait_after.png",
         links=[("arxiv", "https://arxiv.org/abs/1710.01507"), ("acm", "https://dl.acm.org/citation.cfm?id=3210144"), ("code", "https://github.com/vaibhav4595/Clickbait_Detection")]),
    dict(key="rawat2018sky", tags=['misc'], badge="MMM", img="sky_before.png", img2="sky_after.png",
         links=[("project page", "https://cvit.iiit.ac.in/research/projects/cvit-projects/findmeasky"), ("pdf", "assets/papers/sky.pdf"), ("springer", "https://link.springer.com/chapter/10.1007/978-3-319-73603-7_18")]),
]

THESIS = dict(tags=["repr"], title="Image Representations for Style Retrieval, Recognition and Background Replacement Tasks",
              venue="Master's Thesis, IIIT Hyderabad", year="2020", badge="MS Thesis",
              links=[("abstract", "https://web2py.iiit.ac.in/research_centres/publications/view_publication/mastersthesis/828"), ("pdf", "assets/papers/IIIT_Thesis_Siddhartha_Gairola.pdf")])

# ---------------------------------------------------------------------------
# Background.  Logos live in images/logos/; "mask" logos are single-colour SVGs
# recoloured by CSS (see .lg.<name> rules), the others are plain <img>.
# ---------------------------------------------------------------------------
EXPERIENCE = [  # (organisation, role, dates, logo)
    ("Microsoft Research India", "Research Fellow, Technology for Emerging Markets", "Aug 2020 &ndash; Aug 2022", "microsoft"),
    ("Microsoft Research India", "Research Intern", "Jan 2020 &ndash; Jul 2020", "microsoft"),
    ("Adobe Inc.", "Research Intern, Media and Data Science Research", "Jun 2019 &ndash; Jan 2020", "adobe"),
]
EDUCATION = [  # (institution, href, [degree lines], dates, logo)
    ("Max Planck Institute for Informatics &amp; Saarland University", "https://www.mpi-inf.mpg.de/home", ["PhD student, Computer Science"], "Sep 2022 &ndash; present", "mpi"),
    ("Institute of Science and Technology Austria (ISTA)", "https://ist.ac.at/en/home/", ["Visiting PhD student, Locatello group"], "Aug 2024 &ndash; Feb 2025", "ista"),
    ("IIIT Hyderabad", "https://www.iiit.ac.in/", ["MS by Research, Computer Science (2018 &ndash; 2020)", "B.Tech with Honours, Computer Science (2014 &ndash; 2018)"], "2014 &ndash; 2020", "iiit"),
]
MASK_LOGOS = {"mpi", "saarland", "iiit"}

# ---------------------------------------------------------------------------
# Academic service & more
# ---------------------------------------------------------------------------
ORGANIZING = [("Computer Vision for Developing Countries (CV4DC) Workshop", "https://cv4dc.github.io/", "co-organizer",
               [("ICCV 2025", "https://cv4dc.github.io/2025/"), ("ACCV 2024", "https://cv4dc.github.io/2024/")])]
REVIEWING = [("ICML", "2023, 2024, 2025, 2026"), ("NeurIPS", "2022, 2023, 2025"), ("ICLR", "2022, 2023, 2024"),
             ("CVPR", "2024, 2025, 2026"), ("ECCV", "2024"), ("ICCV", "2025"), ("IHCI", "2021")]
GOLD_REVIEWS = {"ICML": ["2026"]}      # venue -> years with the gold-reviewer star
GOLD_LEGEND = "gold reviewer, ICML 2026"
TALKS = [  # (title, venue html, when, (link kind, href))
    ("Intriguing Applications and Overlooked Pitfalls of XAI in Visual Models", '<a href="https://gmum.net/">GMUM Workshop</a>, Jagiellonian University · invited talk', "Oct 2024", ("slides", "assets/presentations/GMUM_Talk_Sharing.pptx")),
    ("RespireNet: Detecting Abnormal Lung Sounds in Limited Data Settings", "EMBC 2021 · paper talk", "2021", ("video", "https://www.youtube.com/watch?v=XoAF3fCAqq4")),
    ("SimPropNet: Improved Similarity Propagation for Few-shot Segmentation", "IJCAI 2020 · paper talk", "2020", ("video", "https://www.ijcai.org/proceedings/2020/video/24830")),
    ("Unsupervised Image Style Embeddings for Retrieval and Recognition Tasks", "WACV 2020 · paper talk", "2020", ("video", "https://www.youtube.com/watch?v=EbUOg1gVcFw&t=909s")),
]
TEACHING = [  # (institution, href, role, period, [(course, terms)], logo)
    ("Saarland University", "https://www.uni-saarland.de/en/home.html", "Teaching assistant", "2023 &ndash; 2026",
     [("Elements of Data Science and Artificial Intelligence", "Winter 2023–26")], "saarland"),
    ("IIIT Hyderabad", "https://iiit.ac.in/", "Teaching assistant", "2016 &ndash; 2019",
     [("Computer Graphics", "Spring 2019"), ("Digital Image Processing", "Monsoon 2017, 2018"), ("Computer Vision", "Spring 2018"),
      ("Artificial Intelligence", "Spring 2017"), ("Digital Logic and Processors", "Monsoon 2016")], "iiit"),
]
OPENSOURCE = [  # (title, href, detail)
    ("Google Summer of Code 2018 · Scilab", "https://www.scilab.org/en/projects/gsoc/2018", "Working MEX-library demo in C/C++ and Scilab"),
    ("Google Summer of Code 2017 · Scilab", "https://summerofcode.withgoogle.com/archive/2017/projects/4882600426471424/", "C/C++ wrapper for the Matlab MEX API on the Scilab API"),
]
VOLUNTEERING = [("ICVGIP 2018", "https://cvit.iiit.ac.in/icvgip18/index.php", "student volunteer")]

# ---------------------------------------------------------------------------
# Writing & resources: (icon, group title, [(title, href, description)])
# ---------------------------------------------------------------------------
RESOURCES = [
    ("pen", "Guides I maintain", [
        ("How to Do Research", "notes_and_resources_on_how_to_do_research.html", "notes and resources for young researchers"),
        ("Writing Academic Papers", "how_to_write_academic_papers.html", "structure, clarity and process"),
        ("Reviewing Scientific Papers", "how_to_review_scientific_papers.html", "how to review well and fairly"),
        ("PhD Applications", "grad_school_resources.html", "writings, resources and FAQs on applying to grad school"),
    ]),
    ("layout", "Templates &amp; checklists", [
        ("MPI-INF poster templates", "assets/templates/MPI-INF_Poster_Templates/CVPR_2026_Poster.key",
         'Keynote · <a href="assets/templates/MPI-INF_Poster_Templates/CVPR_2026_Poster.key">CVPR 2026</a> · <a href="assets/templates/MPI-INF_Poster_Templates/ICLR_2025_Poster.key">ICLR 2025</a>'),
        ("Reproducibility checklist", "assets/presentations/ReproducibilityChecklist.pdf", "by Joelle Pineau"),
    ]),
    ("rss", "Elsewhere", [
        ("Medium", "https://medium.com/@siddhartha.gairola18", "occasional posts on research, general thoughts, and personal things"),
        ("Personal page", "personal.html", "some personal, impersonal, and random stuff"),
    ]),
]

# Secondary pages: slug -> fragment in site/pages/<slug>.html (title/back link in the fragment header).
PAGES = ["personal", "grad_school_resources", "how_to_review_scientific_papers",
         "how_to_write_academic_papers", "notes_and_resources_on_how_to_do_research", "style"]
# Links in the slim top bar of secondary pages.
SUBNAV = [("Home", "index.html"), ("Publications", "index.html#publications"), ("Resources", "index.html#resources")]

# ---------------------------------------------------------------------------
# Inline SVG icons (24px viewBox).  Stroke icons are Lucide-style; brand marks are
# the official simple-icons paths.
# ---------------------------------------------------------------------------
_S = 'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"'
ICONS = {
    "star": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="m12 2.5 2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4l-5.9 3.1 1.2-6.5L2.5 9.4l6.6-.9z"/></svg>',
    "mail": f'<svg {_S}><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    "cv": f'<svg {_S}><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/></svg>',
    "idcard": f'<svg {_S}><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M6 16c.6-1.5 1.8-2 3-2s2.4.5 3 2M14 10h4M14 13h4"/></svg>',
    "user": f'<svg {_S}><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
    "sun": f'<svg {_S}><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
    "moon": f'<svg {_S}><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>',
    "mic": f'<svg {_S}><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3M8 21h8"/></svg>',
    "users": f'<svg {_S}><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 13.5a6.5 6.5 0 0 1 3.5 6.5"/></svg>',
    "clipboard": f'<svg {_S}><rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v2H9zM8.5 13l2.5 2.5 4.5-4.5"/></svg>',
    "heart": f'<svg {_S}><path d="M12 21s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.6-7 10-7 10z"/></svg>',
    "code": f'<svg {_S}><path d="m8 8-4 4 4 4M16 8l4 4-4 4M14 4l-4 16"/></svg>',
    "pen": f'<svg {_S}><path d="M12 20h9M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/></svg>',
    "layout": f'<svg {_S}><rect x="3" y="3" width="18" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>',
    "rss": f'<svg {_S}><path d="M4 11a9 9 0 0 1 9 9M4 4a16 16 0 0 1 16 16"/><circle cx="5" cy="19" r="1.5" fill="currentColor"/></svg>',
    "chalk": f'<svg {_S}><rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M7 20h10M12 16v4M7 8h6M7 11h4"/></svg>',
    "video": f'<svg {_S}><rect x="3" y="6" width="13" height="12" rx="2"/><path d="m16 10 5-3v10l-5-3z"/></svg>',
    "slides": f'<svg {_S}><rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M12 16v4M8 20h8M3 8h18"/></svg>',
    "football": f'<svg {_S}><circle cx="12" cy="12" r="9"/><path d="m12 7.5 3.8 2.8-1.5 4.4h-4.6L8.2 10.3z"/><path d="M12 7.5V3.2M15.8 10.3l4.1-1.4M14.3 14.7l2.6 3.5M9.7 14.7l-2.6 3.5M8.2 10.3 4.1 8.9"/></svg>',
    "quote": f'<svg {_S}><path d="M4 16c0-4.4 2.2-7.4 6-9v3c-2 1-3.2 2.6-3.4 4H10v6H4z"/><path d="M14 16c0-4.4 2.2-7.4 6-9v3c-2 1-3.2 2.6-3.4 4H20v6h-6z"/></svg>',
    "dumbbell": f'<svg {_S}><rect x="4" y="7.5" width="3" height="9" rx="1"/><rect x="17" y="7.5" width="3" height="9" rx="1"/><path d="M7 12h10M2 10v4M22 10v4"/></svg>',
    "globe": f'<svg {_S}><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a13.5 13.5 0 0 1 0 18M12 3a13.5 13.5 0 0 0 0 18"/></svg>',
    "toolbox": f'<svg {_S}><rect x="3" y="8" width="18" height="12" rx="2"/><path d="M8 8V6a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18M10 13v2M14 13v2"/></svg>',
    "help": f'<svg {_S}><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.7.4-1 1-1 1.7M12 17h.01"/></svg>',
    "briefcase": f'<svg {_S}><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 12h18"/></svg>',
    "cap": f'<svg {_S}><path d="m2 9 10-5 10 5-10 5z"/><path d="M6 11.5V16c0 1.5 3 3 6 3s6-1.5 6-3v-4.5M22 9v6"/></svg>',
    "copy": f'<svg {_S}><rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg>',
    "download": f'<svg {_S}><path d="M12 3v12M6 11l6 6 6-6M4 21h16"/></svg>',
    "github": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>',
    "x": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"/></svg>',
    "scholar": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M5.242 13.769 0 9.5 12 0l12 9.5-5.242 4.269C17.548 11.249 14.978 9.5 12 9.5c-2.977 0-5.548 1.748-6.758 4.269zM12 10a7 7 0 1 0 0 14 7 7 0 0 0 0-14z"/></svg>',
}
