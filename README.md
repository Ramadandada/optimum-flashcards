# Optimum Water Solutions — Sales Training Project

A complete sales training toolkit for Optimum Water Solutions reps in Toronto, built from a real on-the-job training transcript. Includes a deployable flashcard web app, a printable instructor cheat sheet, and a comprehensive playbook reference.

## What's in this project

```
optimum-project/
├── README.md                       ← you are here
├── CLAUDE.md                       ← context for Claude Code (read first)
│
├── flashcards/
│   ├── index.html                  ← deployable flashcard web app (90 cards)
│   └── optimum-flashcards.jsx      ← original React source (for reference)
│
├── pdf/
│   ├── build_pdf.py                ← Python script to regenerate the PDF
│   └── optimum-cheat-sheet.pdf     ← printable 10-page instructor handout
│
├── docs/
│   ├── playbook.md                 ← full playbook (master reference)
│   └── source-transcript.txt       ← original raw training transcript
│
└── deploy/
    └── DEPLOY.md                   ← step-by-step deployment instructions
```

## Quick start

### To use the flashcards locally
Open `flashcards/index.html` in any browser. Works offline. Progress saves to your browser's local storage.

### To deploy the flashcards as a public web link
See `deploy/DEPLOY.md`. Easiest path is dragging `flashcards/index.html` to [app.netlify.com](https://app.netlify.com) after signing in.

### To regenerate the PDF
```bash
cd pdf
pip install reportlab
python build_pdf.py
```

### To continue working with Claude Code
1. Open this folder in your terminal: `cd path/to/optimum-project`
2. Run: `claude`
3. Claude Code reads `CLAUDE.md` automatically and picks up where the chat left off

## Project status

| Asset | Status |
|---|---|
| Playbook (markdown) | ✅ Complete |
| Cheat sheet (PDF) | ✅ Complete |
| Flashcard app (HTML) | ✅ Complete · 90 cards |
| Deployment | ⏳ In progress (Netlify drop) |

## Common next tasks

- Deploy the flashcards to a permanent URL (GitHub Pages, Netlify with account, Vercel)
- Add new cards as new sales scripts emerge
- Create category-specific PDFs for handouts
- Build a progress-sharing feature (right now progress is local-only)
- Add an audio mode for drilling scripts hands-free in the car

## Source

Built from a real Optimum Water Solutions training transcript covering:
- The 10-step sales pitch
- Cold calling and phone scripts
- Comp plan, bonus tiers, term multipliers
- Five core machines and water science
- Closing rituals and objection handling
