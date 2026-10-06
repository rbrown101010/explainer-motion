# Explainer Motion

Motion graphics for Riley Brown's videos, built with [HyperFrames](https://hyperframes.heygen.com) (HTML + GSAP) and rendered to 1920×1080 MP4.

**Live gallery:** https://explainer-motion.vercel.app

- **10 topic explainers** (`videos/e01…e10`): chatbot → agent, one point of contact, primary agent, threads vs agents, lowest level, interface × model, local vs cloud, delegate from your phone, an agent with its own tools, the race.
- **14 B-roll templates** (`videos/t01…t14`): concept card, hot take, launch video on grey, launch video on blurred A-roll, side-by-side compare, single logo, logo row, delegation flow, website, benchmark, official post card, and three name labels over A-roll.

Every entry is tagged `Riley1` (the dark `#212120` + Geist + coral `#F07A5A` style) and ships notes, a recreation prompt, search keywords and its full composition source.

## For agents

Start at https://explainer-motion.vercel.app/llms.txt. It links the style guide (`/style.md`), the JSON index (`/data/explainers.json`), a notes page per entry (`/notes/<slug>.md`) and the composition source (`/source/<slug>/index.html`). `/play.html?id=<slug>` plays any composition live in a normal browser.

## Layout

```
videos/<slug>/        one HyperFrames project per motion graphic (index.html + assets/)
shared/               Geist font and official logos used by the explainers
shared-media/         launch-video clips, A-roll clips and stills used by the templates
build_templates.py    generates the 14 template compositions
site/                 the static gallery deployed to Vercel
```

## Make or change one

```bash
cd videos/<slug>
npx hyperframes check .                                  # 0 errors, 0 warnings
npx hyperframes render . -q high -o renders/video.mp4    # 6s, 1920x1080, 30fps
```

Copy the new render to `site/media/<slug>.mp4`, update `site/data/explainers.json`, then deploy from `site/`:

```bash
vercel deploy --prod --yes
```

Style rules for new pieces live in [`site/style.md`](site/style.md).

Launch-video clips, product logos and screenshots belong to their respective companies and are included for commentary and reference.
