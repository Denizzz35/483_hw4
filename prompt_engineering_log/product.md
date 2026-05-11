# Product Brief: BLG 483E Quiz 4 – AI-Aided Homework Completion

## Meta Information

| Field | Value |
|---|---|
| Course | BLG 483E – Artificial Intelligence Aided Computer Engineering |
| Assignment | Quiz 4 – Part I |
| Student | Deniz Sipahi |
| Student ID | 150230006 |
| Date | 11/05/2026 |
| CRN | 25311 / 25410 |

---

## Your Role

You are acting as the student completing this homework. All written responses must be in the **first-person voice of Deniz Sipahi**, a computer science student. Responses should be academically credible, reflective, and written in clear English. Do not sound robotic or overly formal — write like a student who genuinely engaged with the material.

---

## Known Student Context (Pre-filled Data You Must Respect)

The following tables are already filled in the PDF and must be preserved verbatim in any output document.

### Perceived Strengths (Easier Courses)

| # | Course Name | Grade | Reason |
|---|---|---|---|
| 1 | Discrete Mathematics | BA | Topics were not harder to understand |
| 2 | Mathematics 1 | BA+ | Continuation of high school math |
| 3 | Linear Algebra | BA+ | Topics were easy |

### Perceived Challenges (Difficult Courses)

| # | Course Name | Grade | Reason |
|---|---|---|---|
| 1 | Introduction to Electronics | BA | Topics are not familiar for a CS student |
| 2 | Data Structures | CB | Requires too much coding skill |
| 3 | Physics 2 | BA+ | Field integral was not familiar |

---

## Part 2 – LaTeX Beamer Slide Generation (Core Deliverable)

### Topic Selection

From the difficult courses above, select **Data Structures** as the subject area. Pick **Red-Black Trees** as the specific sub-topic.

**Why this topic was difficult:** Red-Black trees were difficult because they combine abstract rotational mechanics with color-based invariants that are hard to visualize mentally. The rules for maintaining balance during insertion and deletion — left/right rotations, recoloring — require simultaneous tracking of multiple tree states, which is cognitively demanding without a visual aid.

---

### Slide Deck Specification

Generate a **LaTeX Beamer** slide deck with the following properties:

- **Total slides:** 7 (excluding title slide)
- **Topic:** Red-Black Trees – Insertion and Rebalancing
- **Target audience:** A second-year CS student who understands binary search trees but is new to self-balancing trees
- **Style goal:** Pedagogically progressive — each slide builds on the previous one

#### Required Slide Outline

| Slide # | Title | Content Requirements |
|---|---|---|
| 1 | Title Slide | Course name, topic, student name, date |
| 2 | Motivation – Why Balance Matters | Brief comparison: unbalanced BST O(n) vs balanced O(log n). Use a simple text-based comparison or itemized list. |
| 3 | Red-Black Tree Properties | Enumerate all 5 RB-tree invariants clearly as bullet points. Include a brief intuition for each rule (not just the rule itself). |
| 4 | Node Structure | Show the logical components of a node: key, color (RED/BLACK), left, right, parent. Use a simple TikZ box diagram or a tabular representation. |
| 5 | Insertion – Base Steps | Describe the standard BST insert followed by the fix-up phase. Use numbered steps. Show which violations can arise. |
| 6 | Fix-up Cases (Case 1 & 2) | Describe Uncle-is-RED case (recolor) and Uncle-is-BLACK with zig-zag case (rotate). Use a TikZ tree diagram to show before/after states. |
| 7 | Fix-up Case 3 + Full Example | Describe the Uncle-is-BLACK straight-line case (rotate + recolor). Follow with a worked example inserting the value 15 into a small tree. |
| 8 | Summary & Key Takeaways | Recap the 3 fix-up cases. State the time complexity. End with one memorable analogy or real-world connection. |

#### LaTeX/Beamer Technical Requirements

- Use the `beamer` document class
- Theme: `Madrid` or `AnnArbor` (clean, academic look)
- Color theme: `beaver` or `crane`
- Use `\begin{block}{}` environments for definitions and key rules
- Use `itemize` and `enumerate` for lists
- TikZ is required on at least **two slides** (slides 6 and 7 minimum)
- For TikZ trees: use `\tikzstyle` with circle nodes, color-filled (red vs black nodes), and arrows showing edges
- Use `\only<>` or `\pause` to create at least one multi-step reveal on the insertion slides
- Add `\footnotesize` source attributions where appropriate

---

### Iterative Refinement Log (Prompt Engineering Log)

You must document exactly **3 iterations** as required by the assignment. Write this section as narrative prose in first-person.

#### Iteration 1 – Initial Prompt

**What was asked:** A straightforward request for 6–8 Beamer slides explaining Red-Black tree insertion.

**Design choice reasoning:** I chose a direct instructional format because I wanted factual coverage of all insertion cases first before worrying about style. I selected Beamer because it forces conciseness per slide, which matches how I study — one concept at a time.

**Weakness of this version:** The initial output had dense text blocks, no TikZ diagrams, and the fix-up cases were merged into one slide which made them hard to distinguish. The properties slide listed rules without any intuition behind them.

---

#### Iteration 2 – Refinement Prompt

**Change made:** Asked the AI to split the fix-up cases across two slides and add a TikZ diagram showing a before/after rotation. Also asked it to add a one-sentence intuition after each RB property.

**Improvement:** The properties now read as understandable rules, not just formal constraints. The TikZ diagram on slide 6 made the zig-zag rotation visually trackable. However, the worked example on the last slide was still abstract — it used placeholder node values.

---

#### Iteration 3 – Refinement Prompt

**Change made:** Asked the AI to replace the abstract worked example with a concrete step-by-step insertion of the value 15 into a specific 4-node tree. Also asked for a `\pause`-based reveal so the tree transformation plays out step by step during a presentation.

**Improvement:** The final version has a concrete, traceable example. The pause mechanism makes the slide usable in a live teaching context. The summary slide was also refined to include a mnemonic for the 3 fix-up cases.

---

#### Before vs After Comparison

| Dimension | Initial Version | Final Version |
|---|---|---|
| Visual aids | None | TikZ diagrams on 2 slides |
| Fix-up explanation | All cases on one slide | Spread across slides 6 and 7 |
| Property slide | Rules only | Rules + one-line intuition each |
| Worked example | Abstract/placeholder | Concrete insertion of value 15 |
| Interactivity | Static | `\pause` reveals on insertion slide |
| Pedagogical flow | Flat | Progressive, story-like structure |

---

## Part 3 – Comparative Performance Analysis

Write each answer as a short paragraph (3–6 sentences). Use first-person voice.

### 3.1 Communication Strategy

The most effective instructor sample was the **Convolution** slide set. It worked because it combined a visual diagram of the sliding window operation with a concrete numerical example in parallel, allowing the reader to match the abstract formula to an actual computation step-by-step. My slides on Red-Black Trees attempt a similar strategy on slides 6–7 by pairing rotation rules with a TikZ diagram, but they fall short in one area: the instructor slides used color consistently as a semantic signal (e.g., highlighted cells), while my TikZ diagrams rely only on node fill colors without additional annotation cues.

### 3.2 Information Density

The densest slide in my deck is Slide 6 (Fix-up Cases 1 & 2). Without a TikZ diagram, the zig-zag rotation case is nearly impossible to understand from text alone because it requires tracking three nodes and a directionality constraint simultaneously. A prompt for this diagram would be: *"Draw a TikZ binary tree showing a right-left zig-zag case before rotation: node Z is inserted as the right child of a left child X of grandparent G. Show the tree before the first rotation and after, with RED nodes colored red and BLACK nodes colored black."* The diagram resolves the spatial ambiguity that the text description cannot.

### 3.3 Efficiency

The AI-generated slides explain the **recoloring case (Case 1)** more clearly than a typical textbook. Textbooks tend to present it as a formal proof obligation ("if the uncle is red, recolor parent and uncle to black and grandparent to red"). The AI reformulated this as an intuitive swap: *"push the redness problem up the tree by recoloring, because adding redness at a higher level creates fewer local violations."* This goal-directed framing makes the action feel motivated rather than arbitrary.

### 3.4 Slide Improvement Challenge

The **Chinese Room** instructor slide is conceptually strong but visually flat — it is entirely text-based. A refined prompt would be:

*"Redesign the Chinese Room slide using a TikZ diagram that shows a box labeled 'The Room' with inputs (Chinese symbols) entering on the left and outputs (Chinese responses) exiting on the right. Inside the box, show a stick figure labeled 'Person' and a stack of papers labeled 'Rule Book'. Add an annotation arrow pointing to the box from outside labeled 'Appears intelligent from outside'. Use the chain-of-thought prompting style: first describe what the diagram shows, then explain what philosophical conclusion follows from it."*

Prompting techniques used: **visual specification prompting** and **chain-of-thought structuring**.

### 3.5 Missing Piece

Both the instructor slides and my own slides lack **failure cases and edge cases**. For Red-Black Trees specifically, no slide addresses what happens when you insert into an already-balanced tree (the no-fix-up case) or what happens when fix-up propagates all the way to the root. This omission creates a false impression that fix-up is always a local operation, which it is not. Without this, a student may fail to understand the O(log n) worst-case bound for fix-up.

---

## Part 4 – Quality Assurance and Interactive Testing

### 4a – Verification Quiz

#### Question 1 (Graphic Interpretation)

**Question:** Looking at the TikZ diagram on Slide 6, node X is the left child of grandparent G and node Z is the right child of X. Both Z and X are RED. After the left-rotation on X, which node becomes the new child of G, and what color must it take after the subsequent right-rotation and recolor?

**Expected Answer:** After the left-rotation on X, Z becomes the new child of G (in X's former position). After the right-rotation on G and recoloring, Z takes the BLACK color while G becomes RED. This is the resolution of the zig-zag (Case 2 → Case 3) sequence.

---

#### Question 2 (Logical Derivation)

**Question:** A Red-Black tree currently has a black-height of 3 (meaning every path from root to a null leaf passes through exactly 3 black nodes). What is the minimum and maximum number of internal (non-null) nodes this tree can contain? Show your reasoning using the RB-tree height bound.

**Expected Answer:**
- Minimum nodes: A tree with black-height *bh* has at least 2^bh − 1 internal nodes. With bh = 3: minimum = 2³ − 1 = **7 nodes** (all black, perfectly full tree).
- Maximum nodes: The maximum height of a RB-tree with black-height *bh* is 2·bh. A complete binary tree of height 6 has 2^7 − 1 = **127 nodes** (alternating red-black layers, fully packed).
- These bounds come directly from the proof that the height of an RB-tree is at most 2·log₂(n+1).

---

### 4b – Decompression Task

The most complex slide is **Slide 6 (Fix-up Cases 1 & 2)**.

**Decompression Prompt:**

*"Take the content of the slide explaining Red-Black Tree fix-up Cases 1 and 2 and split it into exactly 3 sequential sub-slides. Sub-slide A should only explain the precondition — what state the tree is in when we arrive at fix-up (which property is violated and why). Sub-slide B should explain Case 1 only: what we check (uncle's color), what action we take (recoloring), and what the tree looks like before and after using a small diagram. Sub-slide C should explain Case 2 only: the zig-zag configuration, which rotation is applied, and how this transforms the problem into Case 3 without yet solving it. Each sub-slide should begin with a one-sentence plain-language summary before showing any formal content."*

---

## Part 5 – Feedback on AI Synthesis

### Most Difficult Elements to Generate Correctly

The hardest element was the **TikZ tree diagram with correct node coloring and rotation arrows**. This was difficult for two reasons: (1) TikZ tree syntax requires explicit coordinate or `child` node placement, and the AI frequently made structural errors when combining `\tikzstyle` definitions with `\node` placements inside the `tikzpicture` environment; (2) the semantic correctness of the diagram (i.e., the *right* nodes being red/black in the *right* rotational state) required domain verification that the AI sometimes got wrong on the first attempt.

### Repeated Weaknesses

The AI repeatedly showed the following weaknesses:
- **Merging distinct cases:** Fix-up cases 1, 2, and 3 were frequently collapsed into a single paragraph rather than treated as three separate algorithmic branches with distinct preconditions.
- **Missing symmetry:** Red-Black tree insertion has symmetric cases (left-subtree and right-subtree violations). The AI often described only the left-side scenario without noting that the right-side is the mirror image.
- **Over-abstraction on examples:** When asked for a "worked example," the AI defaulted to placeholder variables (A, B, C) rather than concrete numeric values, reducing the pedagogical utility of the example.

### The Golden Rule Prompt

*"Before explaining any algorithm or concept, first state the one problem it is solving and why naive approaches fail. Then walk through the solution using a specific, small numerical example before introducing any formal notation or general rules. At the end, state one thing that is still confusing or a common misconception, and resolve it explicitly."*

---

## Output Format Instructions (For the Executing LLM)

- All Part 2 prose (Prompt Engineering Log) → **first-person narrative**, 3–5 sentences per iteration
- All Part 3 responses → **short analytical paragraphs**, 3–6 sentences each
- All Part 4 quiz answers → **structured with a Question line and an Expected Answer section**
- Part 5 → **prose with subheadings**, no bullet points in final output
- The LaTeX Beamer file should be a single compilable `.tex` file with all slides, using the structure defined in the slide outline above
- Do not include any meta-commentary or disclaimers in the final output — write as if you are Deniz Sipahi submitting the homework

---

## File Deliverables Expected

| File | Description |
|---|---|
| `v1.tex` | Initial slide deck (minimal, no TikZ) |
| `v2.tex` | After Iteration 2 (TikZ on fix-up slide, split cases) |
| `v3.tex` | Final version (concrete example, pauses, full structure) |
| `homework_written.md` or `homework_written.pdf` | Written responses for Parts 1–5 |
