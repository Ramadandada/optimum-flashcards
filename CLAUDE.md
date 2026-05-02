# Project context for Claude Code

This file gets read automatically by Claude Code on startup. It contains the full context of what this project is, how it's organized, and where the work left off.

## Project summary

Sales training toolkit for **Ahmad**, a new sales rep at **Optimum Water Solutions** in Toronto. The company sells reverse-osmosis water/ice systems on long-term rental contracts (typically 60 months) to commercial customers. Ahmad needs to memorize a large set of scripts, processes, and product specs before formal training in Pittsburgh.

The project was built from a single training transcript (an audio-recorded ride-along training session) and turned into three artifacts:

1. **A markdown playbook** — the master reference document
2. **A printable PDF cheat sheet** — for handing out / studying
3. **A flashcard web app** — for active drilling on phone/laptop

## Where the previous chat left off

The user was attempting to **deploy the flashcard app to a public URL** so they could share it with their manager. They had:

- Successfully uploaded `optimum-flashcards.html` to Netlify Drop (anonymous deploy)
- Got the URL `https://comfy-sunflower-e2ed24.netlify.app/`
- The bare URL was returning "Page not found" because the file isn't named `index.html`
- The fix: rename the file to `index.html` and redeploy, OR access via `https://comfy-sunflower-e2ed24.netlify.app/optimum-flashcards.html`

The user is now switching to Claude Code to continue iterating with proper file management. The HTML file in this project is **already named `index.html`** so deployment should work cleanly going forward.

## Key facts about Ahmad (the user)

- New sales rep at Optimum Water Solutions, Toronto branch
- Lives in Mississauga
- Going to formal training in Pittsburgh in ~4 weeks
- Has a colleague named Belan/Belen (also a sales rep) who introduced him
- Manager is **Paul** (VP of Sales, based in the US)
- Toronto technician is **Sean**, telemarketer is **Leon**
- Prefers practical learning over abstract theory

## Tone preferences

When helping Ahmad:
- Keep responses concise and action-oriented
- Use clear file deliverables when appropriate
- Don't over-explain — he's figuring things out fast
- Prioritize "what to do right now" over "how it works conceptually"
- He's on mobile a lot — keep that in mind for any UI work

## File organization

```
optimum-project/
├── README.md                       Project overview
├── CLAUDE.md                       This file
├── flashcards/
│   ├── index.html                  The deployable flashcard app (single HTML file)
│   └── optimum-flashcards.jsx      Original React source (kept for reference)
├── pdf/
│   ├── build_pdf.py                Python/reportlab script
│   └── optimum-cheat-sheet.pdf     Generated 10-page PDF
├── docs/
│   ├── playbook.md                 Full markdown reference
│   └── source-transcript.txt       Raw training transcript
└── deploy/
    └── DEPLOY.md                   Deployment instructions
```

## How the flashcard app works

- Pure HTML/CSS/vanilla-JS, single file, no dependencies
- 90 cards across 9 categories: Cold Call, Phone, 10-Step Pitch, Closing, Comp Plan, Products, Water Science, Process, Mindset
- Cards have three types: `script` (memorize verbatim), `list` (memorize sequence), `concept` (understand)
- Progress saves to `localStorage` keyed by card ID with values `mastered` | `drill` | undefined
- Modes: All / Drill (only flagged) / New (only untouched)
- Keyboard shortcuts: Space=reveal, 1=mastered, 2=drill, 3=skip, arrows=navigate
- Aesthetic: dark navy/gold sales-bible feel, Fraunces serif for headlines, Manrope for body, JetBrains Mono for labels

To add a card, edit the `CARDS` array in `flashcards/index.html`. Each card is:
```js
{ id: 91, cat: 'Closing', q: 'question text', a: 'answer text', type: 'script' }
```

## How the PDF is built

`pdf/build_pdf.py` uses `reportlab`. Run with:
```bash
cd pdf && python build_pdf.py
```
Outputs `pdf/optimum-cheat-sheet.pdf`. Cover page is custom-drawn on canvas with navy/gold blocks. All other pages use Platypus flowables.

## Common tasks the user might ask for

- **"Add a card about X"** → edit `CARDS` array in `flashcards/index.html`
- **"Update the PDF"** → modify `pdf/build_pdf.py`, rerun
- **"Deploy this somewhere"** → see `deploy/DEPLOY.md`
- **"Add audio playback for scripts"** → would need Web Speech API integration in the HTML
- **"Make a quiz mode where it tests me without showing the answer"** → add a new mode that hides the reveal until user types/speaks something
- **"Print only one category as a handout"** → modify `build_pdf.py` to filter by category

## Deployment paths (in order of preference)

1. **GitHub Pages** — permanent, free, custom URL. See `deploy/DEPLOY.md`
2. **Netlify (with account)** — permanent free deploys, drag-and-drop
3. **Vercel** — same as Netlify, slightly different UI
4. **Cloudflare Pages** — fastest CDN
5. ❌ Netlify Drop (anonymous) — expires in 24 hours, **don't use**

## Source material

The original training transcript is in `docs/source-transcript.txt`. It's a real recorded ride-along covering an entire training day. Use it as the canonical source if any extracted content seems off or incomplete.
