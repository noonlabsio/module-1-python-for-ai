# NoonLabs Slidev theme — ink

Ported from the NoonLabs platform design system.

## Surfaces, in the site's own proportion

| Layout | Surface | Use |
|---|---|---|
| `default` | ink-900 `#061A2E` | **the default.** Nine of eleven site sections are ink. |
| `cover` | ink-950 `#04121F` | title cards |
| `section` | ink-800 `#0B2742` | dividers |
| `center` | ink-900, centred | statements |
| `paper` | white | **the exception** — dense notation only (Module II) |

Opt into paper with `layout: paper` in the slide frontmatter.

## What came across from the site

- The **28px + 140px double grid**, at 5% on ink
- A **softened vignette** (gentler than the site's — heavy dark gradients band under YouTube compression)
- The **bronze eyebrow with its leading rule** (`.nl-eyebrow`)
- The **code well** at ink-950 with the site's exact syntax tones
- **IBM Plex Sans / Serif / JetBrains Mono**

## Contrast, measured

Everything on ink-900:

| | ratio | |
|---|---|---|
| headings `#F4F7FA` | 16.34:1 | AAA |
| body `#A8BACF` | 8.86:1 | AAA |
| bronze `#C58B5A` | 6.04:1 | AA |
| muted `#8195AD` | 5.72:1 | AA |

Code well on ink-950: plain 12.7:1, string 8.2:1, keyword 6.5:1, comment 4.9:1.

## Components

`.nl-eyebrow` `.nl-label` `.nl-statement` `.nl-math` `.nl-card` `.nl-cols`
`.nl-chars` `.nl-char` `.nl-box` `.nl-type` `.nl-kv` `.nl-recap` `.nl-verify` `.nl-brand`

## Install

```
themes/noonlabs/          ← replace the whole folder
npx slidev 01-premier-script/slides.md
```

Slide 1 must come up deep navy with IBM Plex. If it is white with Inter, the
theme did not load — check `theme: ./themes/noonlabs` on line 2 of slides.md.
