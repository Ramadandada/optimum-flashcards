# Deployment Guide

How to get a public web URL for the flashcards.

The file `flashcards/index.html` is **already named correctly** for clean deployment — when you upload it, the bare URL will load the flashcards directly (no `/optimum-flashcards.html` needed at the end).

## Option 1: GitHub Pages (recommended — permanent, free)

**Best for:** a permanent URL you control. Your link will be `https://YOUR-USERNAME.github.io/REPO-NAME`.

```bash
# From inside the optimum-project folder
cd flashcards
git init
git add index.html
git commit -m "Initial flashcard deploy"

# Create a new public repo on github.com first, then:
git remote add origin https://github.com/YOUR-USERNAME/optimum-flashcards.git
git branch -M main
git push -u origin main
```

Then in GitHub:
1. Go to your repo → **Settings** → **Pages** (left sidebar)
2. Source: **Deploy from a branch**
3. Branch: `main`, folder: `/ (root)`
4. Save
5. Wait ~1 minute. Your URL appears at the top of the Pages settings.

Result: `https://YOUR-USERNAME.github.io/optimum-flashcards`

## Option 2: Netlify (easiest, with account)

**Best for:** drag-and-drop simplicity, custom subdomain.

1. Sign in at [app.netlify.com](https://app.netlify.com) (Google sign-in is fastest)
2. Click **"Sites"** → **"Add new site"** → **"Deploy manually"**
3. Drag `flashcards/index.html` onto the upload area
4. Get a URL like `https://random-name.netlify.app`
5. **Optional:** click **"Domain settings"** → **"Options"** → **"Edit site name"** to rename it to something like `optimum-drills.netlify.app`

⚠️ Anonymous Netlify Drop deploys (without signing in) **expire after 24 hours**. Always sign in first.

## Option 3: Vercel (similar to Netlify)

```bash
# Install Vercel CLI
npm install -g vercel

# From inside the flashcards folder
cd flashcards
vercel

# Follow prompts. First deploy creates the project, subsequent deploys update it.
```

## Option 4: Cloudflare Pages (fastest CDN globally)

1. Go to [pages.cloudflare.com](https://pages.cloudflare.com) → sign up
2. **Create a project** → **Direct Upload**
3. Upload `index.html`
4. Get a `*.pages.dev` URL

## Option 5: Local sharing only (no internet)

If your manager is in the same room, just **double-click** `flashcards/index.html` on your laptop. Opens in your default browser, fully functional, no setup needed. Show it directly.

## After deploying

Your link works on:
- Any browser, any device
- iPhone, Android, desktop
- No app install needed
- Progress saves per-device (each user has their own progress)

## Updating the deployed version

Whenever you change `flashcards/index.html`:

- **GitHub Pages:** `git add . && git commit -m "update" && git push` — auto-deploys
- **Netlify:** drag the new `index.html` to your existing site's deploys page
- **Vercel:** run `vercel --prod` from the flashcards folder
- **Cloudflare Pages:** upload the new file to the same project

## Troubleshooting

**"Page not found" on bare URL** → file must be named `index.html` (it already is in this project). If you renamed it, the bare URL will 404.

**Flashcards load but progress doesn't save** → some browsers block `localStorage` in private/incognito mode. Open in normal browsing mode.

**Custom domain (yourdomain.com)** → all 4 hosts above support custom domains in their dashboard. Cheapest domain registrar is Cloudflare (~$10/yr).
