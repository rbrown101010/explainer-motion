# Pick an agent vs primary agent

- Id: e03 · Kind: Explainer · Tags: Riley1
- Topic: Grok Bot added a primary bot so you stop choosing which agent to talk to.
- Keywords: primary agent, chief of staff, choose agent, before after, grok bot, sub agents, routing
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/e03-primary-agent.mp4
- Composition: /source/e03-primary-agent/index.html (live: /play.html?id=e03-primary-agent)
- Assets: /source/e03-primary-agent/assets/Geist-Variable.woff2
- Style guide: /style.md

## Notes
Before/after: on the left you pick from six agents (dashed grey choice lines); on the right one primary agent fans work out to six sub-agents with coral lines. Use it when a product adds a 'main', 'primary' or 'chief of staff' agent. Beats: left grid (0.4s) → divider (1.4s) → right: you → primary (2.25s) → fan (2.75s) → sub-agents (3.05s) → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 before/after motion graphic on #212120 in Geist, split by a faint vertical divider. Left: a small person node with dashed grey lines to a 3x2 grid of grey robot-face tiles, labelled 'Pick an agent' in grey. Right: a person node, a short coral arrow down into one larger robot tile with a light border, then six coral lines fan down to six small robot tiles; label 'Primary agent' in white. Animate left first, then right. Fade out at 5.4s. No captions.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
