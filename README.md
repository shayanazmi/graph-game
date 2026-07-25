# Graph Theory — Introduction & Basics

An interactive, self-paced educational module covering **Unit 1** of Graph Theory. Built as a single-page web app with zero dependencies beyond two optional CDN libraries for certificate export.

🔗 **Live Site:** [https://shayanazmi.github.io/graph-game/](https://shayanazmi.github.io/graph-game/)

---

## What's Inside

| Section | Description |
|---------|-------------|
| **History & Origin** | The Königsberg Bridges problem — try the interactive puzzle yourself, then read how Euler proved it impossible in 1736. Includes a filterable timeline from 1736 to the modern web. |
| **Applications of Graphs** | Four real-world applications (networks, molecules, GPS, task scheduling) each shown as both an abstract graph and a real-life illustration. Includes an interactive social network explorer. |
| **Master Graphs** | Six progressive missions covering graph vocabulary, order & size, degree, connectivity, subgraphs, complements, bipartite/regular graphs, and more — each with interactive builders and quizzes. |
| **Articles & Videos** | Curated external resources from Wikipedia, MIT OCW, Khan Academy, Numberphile, and freeCodeCamp. |

<!-- RECENT_UPDATES_START -->
> 💡 **Latest Repo Updates:**
> * Initialized AI README auto-summarizer powered by NVIDIA NIM API (`meta/llama-3.3-70b-instruct`).
<!-- RECENT_UPDATES_END -->

## Features

- 🎮 **Gamified learning** — 6 missions + a 12-question final challenge
- 🧩 **Interactive puzzles** — Königsberg bridge walk, K₄ builder, spanning tree challenge, social network explorer
- 🏅 **Badges & progress** — persistent progress via `localStorage`
- 🔊 **Text-to-speech** — listen to any definition read aloud
- 📜 **Certificate** — downloadable PNG/PDF completion certificate
- 📱 **Responsive** — works on desktop, tablet, and mobile
- ♿ **Accessible** — respects `prefers-reduced-motion`, semantic HTML

## Tech Stack

- **Pure HTML/CSS/JS** — single file, no build step, no framework
- **Inline SVG** — all graph visualizations are generated client-side
- **html2canvas + jsPDF** (CDN) — only used for certificate download

## Running Locally

Just open `index.html` in any modern browser. No server required.

```bash
open index.html          # macOS
xdg-open index.html      # Linux
start index.html         # Windows
```

## Project Structure

```
.
├── index.html        # The entire application (HTML + CSS + JS)
├── .nojekyll         # Tells GitHub Pages to skip Jekyll processing
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## Course Context

This module was built as an **e-content module** for **Semester 5 — Graph Theory** coursework. It covers:

- **CO1:** Introduction, history, and origins of graph theory
- Graph definitions: order, size, adjacency, incidence, degree
- Graph types: simple, null, trivial, multigraph, pseudograph
- Connectivity and complete graphs (Kₙ)
- Subgraphs, spanning subgraphs, induced subgraphs, complements
- Bipartite graphs, regular graphs, degree sequences
- Directed graphs, weighted graphs, classes of graphs

## References

1. Euler, L. (1736). *Solutio problematis ad geometriam situs pertinentis*
2. West, D. B. *Introduction to Graph Theory*, 2nd ed., Pearson
3. Deo, N. *Graph Theory with Applications to Engineering and Computer Science*, PHI Learning
4. Diestel, R. *Graph Theory*, 5th ed., Springer

## License

Educational use. Built for coursework at university level.
