# Continuing in Claude Code

Quick guide to picking up this project in Claude Code.

## Install Claude Code (if you haven't yet)

```bash
# Requires Node.js 18+
npm install -g @anthropic-ai/claude-code
```

Sign in:
```bash
claude
# Follow the auth prompt — uses your existing claude.ai account
```

## Open this project

1. **Unzip** `optimum-project.zip` to wherever you keep code projects (e.g. `~/Projects/`)
2. **Open the folder in your terminal:**
   ```bash
   cd ~/Projects/optimum-project
   ```
3. **Start Claude Code:**
   ```bash
   claude
   ```

That's it. Claude Code will automatically read `CLAUDE.md` on startup and pick up exactly where the chat left off — including knowing your name, preferences, and the deployment status.

## What to try first

Once you're in Claude Code, try one of these prompts to confirm it has full context:

- *"Where did we leave off with deployment?"*
- *"Add 5 new flashcards about handling gatekeepers"*
- *"Make the PDF print-friendly in black and white"*
- *"Help me set up GitHub Pages for the flashcards"*
- *"Review the playbook for any gaps"*

## File map cheat sheet

| When you want to... | Edit this file |
|---|---|
| Add or change a flashcard | `flashcards/index.html` (search for `CARDS = [`) |
| Modify the cheat sheet PDF | `pdf/build_pdf.py` then run `python build_pdf.py` |
| Update the playbook | `docs/playbook.md` |
| Deploy the flashcards | follow `deploy/DEPLOY.md` |

## Useful Claude Code commands

- `/init` — re-read project context
- `/clear` — clear conversation, keep project context
- `/cost` — see how many tokens you've used
- Ctrl+C twice — exit

## If Claude Code doesn't seem to have context

Just say: *"Read CLAUDE.md and tell me what this project is about."*

That forces it to load the project memory if it didn't auto-load.
