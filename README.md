# BLG 483E – Quiz 4 Part I: Red-Black Trees Beamer Slides

## Meta Information

| Field | Value |
|---|---|
| **Student** | Deniz Sipahi |
| **Student ID** | 150230006 |
| **Course** | BLG 483E – Artificial Intelligence Aided Computer Engineering |
| **Assignment** | Quiz 4 – Part I |
| **Date** | 11/05/2026 |
| **CRN** | 25311 / 25410 |

## GitHub Repository

🔗 **[https://github.com/Denizzz35/BLG483](https://github.com/Denizzz35/BLG483)**

## Project Overview

This project contains an iteratively refined LaTeX Beamer slide deck on **Red-Black Tree Insertion and Rebalancing**, along with written responses covering comparative analysis, quality assurance, and reflections on AI-assisted content generation.

## File Structure

```
hw4/
├── v1.tex                      # Iteration 1 – Minimal slides, no TikZ, all cases on one slide
├── v2.tex                      # Iteration 2 – TikZ diagrams, split fix-up cases, intuitions added
├── v3.tex                      # Iteration 3 – Step-by-step example with \pause, mnemonics, analogy
├── homework_written.md         # Written responses for Parts 1–5
├── homework_written.html       # HTML version (for PDF conversion via browser print)
├── chat_log.md                 # Prompt engineering log – 3 iteration chat history
├── product.md                  # Product requirements document (PRD)
├── generated_course_slides.zip # Zip of v1.tex, v2.tex, v3.tex (Ninova upload)
├── prompt_engineering_log.zip  # Zip of chat_log.md + .tex files (Ninova upload)
├── README.md                   # This file
├── recommendation.md           # Recommendations for AI-aided slide generation
└── Example Slides/             # Instructor-provided example slide sets
    ├── Convolution/            # 4 variants: visual, math, code, real-life
    ├── Rice_s Theorem/         # 4 variants: visual, math, code, real-life
    └── The Chinese Room/       # 4 variants: visual, math, code, real-life
```

## How to Compile the LaTeX Files

### Requirements

- A LaTeX distribution with `pdflatex` (e.g., TeX Live, MiKTeX)
- Required packages: `beamer`, `tikz`, `amsmath`

### Compilation

```bash
pdflatex v1.tex
pdflatex v2.tex
pdflatex v3.tex
```

Or use [Overleaf](https://www.overleaf.com) — upload any `.tex` file and compile online.

> **Note:** `v3.tex` uses `\pause` and `\only<>` overlays, so its compiled PDF will contain multiple sub-slides (frames) per content slide.

## Slide Deck Topic

**Subject:** Data Structures (BLG 202E)  
**Topic:** Red-Black Trees – Insertion and Rebalancing  
**Target Audience:** Second-year CS students familiar with BSTs but new to self-balancing trees

## Iterative Refinement Summary

| Version | Key Changes |
|---|---|
| `v1.tex` | Baseline: text-only, no TikZ, all fix-up cases on one slide |
| `v2.tex` | Added TikZ diagrams, split fix-up cases, property intuitions, node structure diagram |
| `v3.tex` | Concrete worked example with `\pause` reveals, mnemonics, real-world analogy, symmetry notes |

## AI Tool Used

- **Model:** GPT-4o (ChatGPT)
- **Iterations:** 3
- **Full chat log:** See `chat_log.md`
