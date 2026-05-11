# BLG 483E – Quiz 4 Part I: Written Responses

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

## Part 1 – Perceived Strengths and Challenges

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

## Part 2 – LaTeX Beamer Slide Generation

### Topic Selection

**Course:** Data Structures  
**Sub-topic:** Red-Black Trees – Insertion and Rebalancing

**Why this topic was difficult:** Red-Black trees were difficult because they combine abstract rotational mechanics with color-based invariants that are hard to visualize mentally. The rules for maintaining balance during insertion and deletion — left/right rotations, recoloring — require simultaneous tracking of multiple tree states, which is cognitively demanding without a visual aid.

### Iterative Refinement Log (Prompt Engineering Log)

#### Iteration 1 – Initial Prompt

I started by asking the AI for a straightforward set of 6–8 Beamer slides explaining Red-Black tree insertion. My design choice was to mirror the numbered-title convention I observed in the instructor's example slides — each content slide is labeled "1. Title", "2. Title", and so on — because it creates a clear sequential progression the audience can follow. I chose Beamer with the Madrid theme and beaver color scheme because it produces a clean, academic look without distracting decorations, similar to the instructor's own Convolution and Rice's Theorem slide sets. The output I received was functional but flat. The fix-up cases were all crammed onto a single slide, making it nearly impossible to distinguish Case 1 from Case 2 from Case 3. The properties slide listed the five RB-tree invariants as bare rules without any explanation of why each rule exists. There were no TikZ diagrams at all — everything was text-based, which defeated the purpose of explaining a fundamentally visual data structure. Comparing this to the instructor's Convolution visual slides, where every single slide has a diagram paired with explanatory text, my v1 felt like a wall of words.

#### Iteration 2 – Refinement Prompt

For the second iteration, I asked the AI to split the fix-up cases across two separate slides and to add a TikZ diagram showing a before/after view of the zig-zag rotation on the Case 2 slide. I also asked it to add a one-sentence intuition after each of the five RB-tree properties. My reasoning here was inspired by the instructor's visual Convolution deck, where slide 4 ("The Visual Math") pairs an image patch, a kernel, and a summation result side-by-side — the dual representation forces understanding. I wanted to replicate that dual-channel approach for rotations. The improvement was significant. The properties now read as understandable rules with clear motivation, not just formal constraints copied from a textbook. The TikZ diagram on slide 5 made the zig-zag rotation visually trackable — I could see exactly which node moves where and why the configuration changes from a zig-zag to a straight line. However, the worked example on the last slide was still too abstract. It used placeholder variables like A, B, and C instead of concrete numeric values, which reduced the pedagogical value of the example.

#### Iteration 3 – Final Refinement

In the third iteration, I asked the AI to replace the abstract worked example with a concrete step-by-step insertion of the value 15 into a specific seven-node tree. I also asked for a `\pause`-based reveal so that the tree transformation would play out step by step during a presentation, rather than showing the final state all at once. This was inspired by how the instructor's Convolution visual slides progressively build from "The Image as a Grid" through "The Sliding Process" to "The Output: Feature Map" — each slide adds one layer of understanding. The improvement was clear. The final version now has a concrete, traceable example where you can follow each step and verify the RB-tree properties at every stage. The pause mechanism makes the slide genuinely usable in a live teaching context. I also refined the summary slide to include a mnemonic for each of the three fix-up cases, making the material more memorable — similar to how the instructor's Convolution real-life deck ends with a "Hierarchical Perception" conclusion that ties the analogy back to the technical concept.

#### Before vs After Comparison

| Dimension | Initial Version (v1) | Final Version (v3) |
|---|---|---|
| Visual aids | None | TikZ diagrams on 3 slides |
| Fix-up explanation | All cases on one slide | Spread across slides 5 and 6 |
| Property slide | Rules only | Rules + one-line intuition each |
| Worked example | Abstract/placeholder | Concrete insertion of value 15 |
| Interactivity | Static | `\pause` reveals on insertion slide |
| Pedagogical flow | Flat | Progressive, story-like structure |

---

## Part 3 – Comparative Performance Analysis

### 3.1 Communication Strategy

The most effective instructor sample was the Convolution visual slide set. It worked because it used a strict one-concept-per-slide structure: first the image grid, then the kernel, then the sliding process, then the dot product, then the output — each building on the previous. Slide 4 ("The Visual Math") is particularly effective because it places the image patch, the ⊗ operator, the kernel, and the Σ value on a single horizontal line, making the abstract operation feel like a physical assembly. My slides on Red-Black Trees attempt a similar strategy on slides 5 and 6 by pairing rotation rules with a TikZ before/after diagram. However, the instructor's Convolution slides use a richer visual vocabulary: the kernel literally overlays the image grid on slide 3, the stride arrow physically shows movement on slide 5, and the padding zeros are drawn as a visible border on slide 6. My TikZ diagrams rely only on node fill colors (red vs. black) without additional annotation cues like dashed arrows indicating the direction of rotation or highlighted borders showing which subtree is being restructured. The instructor's approach of making every spatial relationship explicit through the diagram — rather than expecting the reader to infer it from text — is what makes their communication so effective.

### 3.2 Information Density

The densest slide in my deck is Slide 5 (Fix-up Cases 1 & 2). Without a TikZ diagram, the zig-zag rotation case is nearly impossible to understand from text alone because it requires tracking three nodes — the inserted node, its parent, and its grandparent — plus a directionality constraint simultaneously. The instructor's Rice's Theorem visual slides handle a similar density problem on slide 6 ("The Impossible Reduction") by drawing a flow diagram with labeled boxes: an input M enters a "Transformer" box, producing M′, which feeds into a "Magic Analyzer (A)" that outputs either HALTS or LOOPS. This transforms a multi-step logical argument into a single visual pipeline. A prompt to generate an analogous diagram for my slide would be: "Draw a TikZ binary tree showing a right-left zig-zag case before rotation: node Z is inserted as the right child of a left child P of grandparent G. Both Z and P are RED, uncle U is BLACK. Show the tree before the left-rotation on P and after, with RED nodes filled red and BLACK nodes filled black. Label the rotation arrow 'Left-rotate(P)' between the two states." The diagram resolves the spatial ambiguity that the text description fundamentally cannot convey.

### 3.3 Efficiency

The AI-generated slides explain the recoloring case (Case 1) more clearly than a typical textbook. Textbooks tend to present it as a formal proof obligation: "if the uncle is red, recolor parent and uncle to black and grandparent to red." This framing treats the operation as a rule to memorize rather than an action to understand. The AI reformulated this as an intuitive strategy: "push the redness problem up the tree by recoloring, because adding redness at a higher level creates fewer local violations." This matches the pedagogical approach in the instructor's Rice's Theorem real-life slides, where the concept of undecidability is introduced through the baking analogy — "you cannot predict the cake's taste by reading the recipe" — before the formal statement is given. The AI similarly provides an intuition-first, rule-second structure that makes the action feel motivated rather than arbitrary. It reframes the recoloring as a goal-directed strategy (escalation) rather than a mechanical rule, which is more cognitively accessible for a second-year student.

### 3.4 Slide Improvement Challenge

The Chinese Room real-life instructor slide set ("The Illusion of Understanding: From a Call Center to the Chinese Room") is conceptually strong but would benefit from a more explicit visual mapping between the analogy and the formal argument. The set uses a call center metaphor effectively on slides 2–4, but slide 5 ("The Reveal") simply states the connection in text without a side-by-side visual mapping. By contrast, the Convolution real-life set has a dedicated "Mapping the Analogy" slide that visually places "Giant Mural (Input Pixels)", "Flashlight (The Kernel)", and "Blank Map (Feature Map)" in a three-column layout, making the correspondence unmissable. A refined prompt for the Chinese Room slide would be:

"Add a 'Mapping the Analogy' slide between the call center story and the philosophical conclusion. Use a three-column TikZ layout: Column 1 shows 'Call Center Operator (The Person)' with an icon, Column 2 shows 'Phonetic Manual (The Rulebook)' with a book icon, and Column 3 shows 'Perfect Response (The Output)' with a speech bubble icon. Below the three columns, draw an arrow labeled 'Appears fluent from outside' pointing upward, and a contrasting label below stating 'No understanding exists inside'. Use visual specification prompting to define the exact layout, and chain-of-thought structuring to first present the visual, then state the conclusion."

Prompting techniques used: **visual specification prompting** (explicitly describing the three-column layout, icons, and spatial relationships) and **chain-of-thought structuring** (asking the AI to first describe the visual mapping, then derive the philosophical conclusion, which produces more logically organized output).

### 3.5 Missing Piece

Both the instructor slides and my own slides lack failure cases and boundary conditions. For Red-Black Trees specifically, no slide addresses what happens when you insert into an already-balanced tree (the no-fix-up case, where the parent is BLACK and no property is violated) or what happens when fix-up propagates all the way to the root, requiring the root to be recolored from RED back to BLACK. This omission creates a false impression that fix-up is always a local operation — which it is not. Similarly, the instructor's Rice's Theorem slides never show an example of a trivial property being successfully decided, which would ground the definition of "non-trivial" more concretely. In the Convolution visual slides, there is no mention of what happens when stride > 1 causes information loss, or when a kernel is larger than the input. These omissions are pedagogically dangerous: without seeing the edge cases, a student may fail to understand why the O(log n) worst-case bound applies to the fix-up phase itself (for RB-trees), or why convolution output shrinks without padding. The missing piece, across all slide sets, is the explicit treatment of degenerate or boundary scenarios that reveal the limits of the presented algorithms.

---

## Part 4 – Quality Assurance and Interactive Testing

### 4a – Verification Quiz

#### Question 1 (Graphic Interpretation)

**Question:** Looking at the TikZ diagram on Slide 5, node P is the left child of grandparent G and node Z is the right child of P. Both Z and P are RED, while uncle U is BLACK. After the left-rotation on P, which node becomes the new left child of G, and what color must it take after the subsequent right-rotation on G and recoloring?

**Expected Answer:** After the left-rotation on P, Z becomes the new left child of G (in P's former position). P moves down to become Z's left child. At this point, the configuration is a straight line: Z is the left child of G, and P is the left child of Z — both RED. This is now Case 3. After the right-rotation on G and recoloring, Z takes the BLACK color while G becomes RED. The result is a locally balanced subtree rooted at Z. This is the complete resolution of the zig-zag (Case 2 → Case 3) sequence.

---

#### Question 2 (Logical Derivation)

**Question:** A Red-Black tree currently has a black-height of 3 (meaning every path from root to a null leaf passes through exactly 3 black nodes). What is the minimum and maximum number of internal (non-null) nodes this tree can contain? Show your reasoning using the RB-tree height bound.

**Expected Answer:**
- **Minimum nodes:** A tree with black-height *bh* has at least 2^bh − 1 internal nodes. With bh = 3: minimum = 2³ − 1 = **7 nodes** (all black, a perfectly full binary tree of height 3).
- **Maximum nodes:** The maximum height of an RB-tree with black-height *bh* is 2·bh. A complete binary tree of height 6 has 2⁷ − 1 = **127 nodes** (alternating red-black layers, fully packed). In this configuration, every other level is red, which satisfies Property 4 while maximizing the total number of nodes.
- These bounds come directly from the proof that the height of an RB-tree is at most 2·log₂(n+1), which implies n ≥ 2^bh − 1.

---

### 4b – Decompression Task

The most complex slide is **Slide 5 (Fix-up Cases 1 & 2)**.

**Decompression Prompt:**

"Take the content of the slide explaining Red-Black Tree fix-up Cases 1 and 2 and split it into exactly 3 sequential sub-slides, following the instructor's convention of one concept per slide. Sub-slide A should only explain the precondition — what state the tree is in when we arrive at fix-up (which property is violated and why). Include a small TikZ diagram showing a grandparent-parent-child chain with two consecutive RED nodes to make the violation visually obvious. Sub-slide B should explain Case 1 only: what we check (uncle's color), what action we take (recoloring), and what the tree looks like before and after using a side-by-side TikZ diagram — similar to how the Convolution visual slides pair an image patch with its output on slide 4. Sub-slide C should explain Case 2 only: the zig-zag configuration, which rotation is applied, and how this transforms the problem into Case 3 without yet solving it. Each sub-slide should begin with a one-sentence plain-language summary before showing any formal content, mirroring how the Rice's Theorem real-life slides always lead with the analogy before introducing the formal concept."

---

## Part 5 – Feedback on AI Synthesis

### Most Difficult Elements to Generate Correctly

The hardest element to generate correctly was the TikZ tree diagram with correct node coloring and rotation arrows. This difficulty had two distinct causes. First, TikZ tree syntax requires explicit coordinate or child-node placement, and the AI frequently made structural errors when combining `\tikzstyle` definitions with `\node` placements inside the `tikzpicture` environment — for example, producing overlapping nodes or edges that pointed to the wrong targets. This contrasts sharply with the instructor's example slides, where TikZ is used fluently: the Rice's Theorem visual slides contain clean flow diagrams with labeled boxes and arrows on nearly every slide, and the Chinese Room visual slides use nested boxes with input/output slots that render correctly. Second, the semantic correctness of the diagram — meaning the right nodes being red or black in the right rotational state — required domain-specific verification that the AI sometimes got wrong on the first attempt. It would, for instance, show the uncle as RED in a Case 2 diagram where the uncle must be BLACK by definition. These errors are subtle because the LaTeX compiles without warnings, so the only way to catch them is to manually verify each diagram against the algorithm specification.

### Repeated Weaknesses

The AI repeatedly exhibited three specific weaknesses across iterations. First, it had a tendency to merge distinct cases: fix-up Cases 1, 2, and 3 were frequently collapsed into a single paragraph rather than treated as three separate algorithmic branches with distinct preconditions. This is the opposite of what the instructor slides demonstrate — for example, the Rice's Theorem math slides dedicate separate slides to "Trivial vs. Non-Trivial Properties", "The Assumption", "The Mapping Reduction", and "Analyzing the Reduction", giving each logical step its own space. Second, the AI consistently missed the symmetry of Red-Black tree insertion. The algorithm has symmetric cases for left-subtree and right-subtree violations, and a complete explanation must at least acknowledge that the right-side case is a mirror image. The AI often described only the left-side scenario without any mention of the symmetric counterpart. Third, when asked for a "worked example," the AI defaulted to placeholder variables (A, B, C) or generic labels rather than concrete numeric values. The instructor's Convolution code slides use specific numbers — a 5×5 image with values like 10, 10, 10, 0, 0 — and show the actual computed output (30, 30, 0), making the operation verifiable by hand. My early iterations lacked this concreteness, reducing the pedagogical utility.

### The Golden Rule Prompt

"Before explaining any algorithm or concept, first state the one problem it is solving and why naive approaches fail. Then walk through the solution using a specific, small numerical example before introducing any formal notation or general rules. At the end, state one thing that is still confusing or a common misconception, and resolve it explicitly."
