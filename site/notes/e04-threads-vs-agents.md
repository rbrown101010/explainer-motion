# Threads vs agents

- Id: e04 · Kind: Explainer · Tags: Riley1
- Topic: Claude Code Projects treat work as threads in a project; Grok Bot treats it as agents.
- Keywords: threads, agents, projects, claude code, grok bot, compare, mental model, folders vs agents
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/e04-threads-vs-agents.mp4
- Composition: /source/e04-threads-vs-agents/index.html (live: /play.html?id=e04-threads-vs-agents)
- Assets: /source/e04-threads-vs-agents/assets/Geist-Variable.woff2, /source/e04-threads-vs-agents/assets/claude_code_wordmark.png, /source/e04-threads-vs-agents/assets/grokbot.png
- Style guide: /style.md

## Notes
Compares two mental models: a project folder of threads (Claude Code) vs a team of personified agents (Grok Bot). Use it when comparing how Claude Projects and Grok Bot organise work. Beats: Claude Code wordmark + folder panel, thread rows slide in (0.75s), live dot pulses → Grok Bot wordmark + agent avatars pop in (2.25s) → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 comparison on #212120 in Geist. Two 600x520 #2B2B29 panels. Left, under the official Claude Code wordmark: a white folder icon and four thread rows (dark pill rows with a dot and a grey bar) sliding in; the first row's dot is coral and pulses. Label 'Threads'. Right, under the Grok Bot wordmark: a 2x2 grid of round robot-face avatars popping in, the first one white. Label 'Agents'. Fade out at 5.4s. No captions.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
