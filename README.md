# purplinator.github.io

Personal site for Saxon Stockton — astrophysics research, teaching resources,
and CV. Built with [Quarto](https://quarto.org), published to GitHub Pages by
the workflow in `.github/workflows/quarto.yml` on every push to `main`.

## Working on it locally

```bash
quarto preview      # live-reloading local server
quarto render       # one-off build into _site/
```

`_site/` is the build output and is not committed — GitHub Actions rebuilds it.

## Where things live

```
index.qmd                 splash page
about.qmd                 longer bio
cv.qmd                    curriculum vitae
404.qmd                   not-found page

research/                 HELD BACK: on disk, ignored by git, not rendered (see .gitignore)
  index.qmd               hub; the project grid fills itself from this folder
  01-30dor-emission-lines.qmd   one file per project
  code/
    index.qmd             hub for code documentation
    01-30dor-pipeline.qmd

notes/                    HELD BACK: personal blog listing, no posts yet (see .gitignore)
  posts/_template.qmd     copy this to start a note

teaching/
  index.qmd               hub
  philosophy.qmd
  labs/                   Lab Help — short answers for the physics labs
    _metadata.yml         loads the wizard and checklist scripts on every lab page
    _notes/               reference notes behind the lab pages (not rendered)
    01-uncertainty.qmd    click-through guide to the two uncertainty rows
    02-lab-report-format.qmd   what goes on each whiteboard (QPD / UDA / CON)
    lab-guides/           one page per lab; copy _template.qmd to add one
  python/                 "Python from Scratch" — interactive lessons
    _template.qmd         copy this to start a new lesson
    00-what-is-a-programming-language.qmd
    01-how-computers-work.qmd
    02-choosing-a-language.qmd
    03-python-basics.qmd
  math/                   mathematics lessons (empty, ready for content)
  physics/                worked physics problems (empty, ready for content)

assets/
  theme-light.scss        light palette and Bootstrap variables
  theme-dark.scss         dark palette
  mathjax-config.html     MathJax 4 setup: STIX Two Math font and site-wide LaTeX macros
  wizard.html             click-through question-and-answer used on lab pages
  checklist.html          makes task-list checkboxes tickable on lab pages
  spacing-head.html       applies the saved "wider spacing" preference before paint
  spacing-toggle.html     adds the wider-spacing toggle next to the dark-mode toggle
styles.css                shared component styles, reads --sx-* tokens
images/                   hero, portrait, favicon, og-card.jpg (link previews)
files/                    CV PDFs (lab templates kept here are ignored by git)
```

## Adding a page

Drop a `.qmd` file into the right folder with a two-digit number prefix:

```
teaching/math/01-vectors-and-coordinates.qmd
```

The number sets its position. Nothing else needs editing — both the sidebar
(`auto:` globs in `_quarto.yml`) and the section's card listing pick it up
automatically. Give it front matter like:

```yaml
---
title: "Vectors and Coordinate Systems"
subtitle: "One line on what the reader can do afterwards"
description: "One or two sentences. Shows on the section index card."
order: 1
categories: [Linear Algebra]
---
```

`order` should match the filename number. `description` is what appears on the
listing card and in search results, so it is worth writing properly.

## Adding an interactive Python lesson

Copy `teaching/python/_template.qmd`. It already carries the one setting that
cannot be inherited:

```yaml
engine: markdown
```

**Every page with `{pyodide}` cells needs that line in its own front matter.**
Quarto decides a document's execution engine from its own front matter before
folder metadata is merged, so it cannot come from `_metadata.yml` or
`_quarto.yml`. Without it, Quarto assumes the cells need running, tries to start
a Jupyter kernel, and the GitHub Actions build fails.

The Pyodide runtime itself is switched on per folder, in
`teaching/python/_metadata.yml`. To make another folder interactive, copy the
`filters:` and `ojs-engine:` keys from that file.

## Writing content

Available on any page:

| What | How |
|------|-----|
| Math | `$inline$`, `$$display$$`. Macros such as `\msun`, `\halpha`, `\ebv`, `\deriv{x}{t}` are defined in `assets/mathjax-config.html`. |
| Figures | `![Caption.](figures/thing.png){#fig-thing width=80%}`, referenced as `@fig-thing`. Click to enlarge is automatic. |
| Callouts | `::: {.callout-note}` — also `-tip`, `-warning`, `-caution`, `-important`. Add `collapse="true"` to fold. |
| Footnotes | `text[^tag]` then `[^tag]: definition`. They appear as hover popups. |
| Tabs | `::: {.panel-tabset}` with `###` headings inside. |
| Cards | Card grids are raw HTML in a ` ```{=html} ` block — Pandoc splits `<a>` elements otherwise. See `index.qmd`. |

## Design

Colour is defined once, in `assets/theme-light.scss` and `assets/theme-dark.scss`,
as a set of `--sx-*` custom properties. `styles.css` never hard-codes a colour —
it reads those tokens, so a single rule covers both themes. To re-skin the site,
change the purple scale at the top of both SCSS files.
