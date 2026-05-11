# Recommendations for AI-Aided Slide Generation

## Overview

This document summarizes my recommendations for using AI tools to generate LaTeX Beamer presentations, based on my experience creating a Red-Black Trees slide deck through 3 iterative refinement cycles.

---

## What Worked Well

### 1. Iterative Prompting Over One-Shot Requests

Asking for everything in a single prompt produced a flat, text-heavy deck with no visual elements. Splitting the task across 3 rounds — structure first, then visuals, then interactivity — yielded dramatically better results. Each iteration allowed me to evaluate the output and target specific weaknesses.

### 2. Explicit Visual Specifications

The AI only produced correct TikZ diagrams when I described the exact layout: which nodes are children of which, what colors they should be, and where labels go. Vague requests like "add a diagram" produced generic or incorrect trees. Being specific about the visual structure ("node Z is the right child of left child P of grandparent G, both RED, uncle U is BLACK") was essential.

### 3. Numbered Slide Titles

Matching the instructor's convention of "1. Title", "2. Title" helped maintain a clear pedagogical progression and made the slide deck feel consistent with course materials.

### 4. Block Environments for Key Concepts

Using `\begin{block}{}` for definitions, insights, and mnemonics made the slides visually distinct and scannable. The AI was good at generating these when asked.

---

## What Did Not Work Well

### 1. TikZ Semantic Correctness

The AI frequently produced TikZ trees that compiled without errors but had semantically incorrect node colorings or parent-child relationships. For example, it once showed the uncle as RED in a Case 2 diagram where the uncle must be BLACK by definition. **Lesson:** Always verify TikZ diagrams against the algorithm specification manually. LaTeX compilation does not catch logical errors.

### 2. Merging Distinct Cases

The AI repeatedly collapsed fix-up Cases 1, 2, and 3 into a single paragraph. This is a general tendency when asking AI to explain multi-branch algorithms — it optimizes for compactness over clarity. **Lesson:** Explicitly tell the AI how many slides or sections each case should get.

### 3. Over-Abstraction in Examples

When asked for "a worked example," the AI defaulted to placeholder variables (A, B, C) instead of concrete numbers. This happened consistently across iterations. **Lesson:** Always specify the exact values you want in the example (e.g., "insert value 15 into the tree {10, 5, 20, 3, 7, 17, 25}").

### 4. Missing Symmetric Cases

Red-Black tree operations have left-right symmetry. The AI consistently described only one side without acknowledging the mirror case. **Lesson:** Explicitly ask the AI to note symmetric cases, or add them yourself.

---

## Prompting Strategies That Helped

| Strategy | Example | Effect |
|---|---|---|
| **Constraint specification** | "Use exactly 7 content slides" | Prevented sprawl or compression |
| **Visual specification** | "Draw node Z as right child of P, both RED, uncle BLACK" | Produced correct TikZ |
| **Negative examples** | "Do NOT merge all fix-up cases on one slide" | Prevented known failure modes |
| **Step-by-step reveal** | "Use `\only<1>`, `\only<2>` for the insertion example" | Made slides interactive |
| **Analogy requests** | "End with a real-world analogy" | Made content memorable |
| **Format matching** | "Use numbered titles like '1. Title'" | Matched instructor style |

---

## The Golden Rule Prompt

After three iterations, I distilled the most effective general-purpose prompt structure:

> *"Before explaining any algorithm or concept, first state the one problem it is solving and why naive approaches fail. Then walk through the solution using a specific, small numerical example before introducing any formal notation or general rules. At the end, state one thing that is still confusing or a common misconception, and resolve it explicitly."*

This prompt structure forces the AI to be pedagogically progressive (problem → example → theory → misconception) rather than dumping definitions first.

---

## Tool Comparison Notes

| Aspect | AI-Generated Slides | Manual Slide Creation |
|---|---|---|
| **Speed** | Very fast (minutes) | Slow (hours for TikZ) |
| **Correctness** | Requires manual verification | Correct by construction |
| **Visual quality** | Good with explicit specs | Depends on LaTeX skill |
| **Pedagogical flow** | Often flat; needs iteration | Better with experience |
| **Best for** | First drafts, structure | Final polish, TikZ accuracy |

---

## Final Recommendation

Use AI as a **first-draft generator** and **structure organizer**, not as a final-output tool. The iterative cycle of prompt → evaluate → refine is essential. Expect to verify all visual elements manually and to make 2–3 passes before the output is submission-ready. The AI excels at generating LaTeX boilerplate, writing block definitions, and structuring bullet-point content — but it struggles with spatial reasoning (TikZ layouts) and algorithmic correctness (node colorings in specific cases).
