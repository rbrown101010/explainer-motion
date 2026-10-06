# One point of contact

- Id: e02 · Kind: Explainer · Tags: Riley1
- Topic: The race for a single point of contact agent orchestrator.
- Keywords: orchestrator, main agent, delegate, single point of contact, codex, claude code, cursor, fan out, one agent
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/e02-one-point-of-contact.mp4
- Composition: /source/e02-one-point-of-contact/index.html (live: /play.html?id=e02-one-point-of-contact)
- Assets: /source/e02-one-point-of-contact/assets/Geist-Variable.woff2, /source/e02-one-point-of-contact/assets/claude_code.png, /source/e02-one-point-of-contact/assets/codex_mono.png, /source/e02-one-point-of-contact/assets/cursor.png
- Style guide: /style.md

## Notes
Explains talking to one main agent that delegates to coding agents. Use it for 'one point of contact', 'main agent' or 'orchestrator'. Beats: You (0.2s) → arrow → Main agent with rings (1.05s) → three curved coral wires fan out (1.9s) → Codex, Claude Code, Cursor slide in (2.35s) → outer ring breathes → fade out (5.4s).

## Prompt
Make a 6-second 1920x1080 motion graphic on #212120 in Geist. A round 'You' node on the left (grey person icon), a coral arrow into a 320x300 'Main agent' panel with a white hub icon whose rings scale in. From it, three curved 4px coral wires draw out to three 200px panels holding the official Codex, Claude Code and Cursor logos, each with a grey 36px label to its right. The outer hub ring gently pulses. Fade out at 5.4s for a clean loop. No captions.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
