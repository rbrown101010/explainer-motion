# Learn the lowest level

- Id: e05 · Kind: Explainer · Tags: Riley1
- Topic: Learn Claude Code / Codex / Cursor so you can direct the agents built on top of them.
- Keywords: stack, layers, lowest level, learn, claude code, codex, cursor, hierarchy, foundation
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/e05-lowest-level.mp4
- Composition: /source/e05-lowest-level/index.html (live: /play.html?id=e05-lowest-level)
- Assets: /source/e05-lowest-level/assets/Geist-Variable.woff2, /source/e05-lowest-level/assets/claude_code.png, /source/e05-lowest-level/assets/codex_mono.png, /source/e05-lowest-level/assets/cursor.png, /source/e05-lowest-level/assets/dots.png, /source/e05-lowest-level/assets/grokbot.png
- Style guide: /style.md

## Notes
A three-layer stack: You → Agent (dots, Grok Bot) → Code (Claude Code, Codex, Cursor). A coral arrow travels down to the lowest level, which glows. Use it for 'learn the hardest level' or 'the base layer'. Beats: You slab (0.2s) → Agent slab (0.55s) → arrow travels down (1.2s) → Code slab and logos (1.75s) → glow pulse (2.9s) → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 motion graphic on #212120 in Geist: three stacked 1340px-wide #2B2B29 slabs. Top 'You' with a person icon, middle 'Agent' with the dots and Grok Bot wordmarks, bottom (taller, light border) 'Code' with the Claude Code, Codex and Cursor logos. A 4px coral arrow draws down the left side from top to bottom as the slabs drop in, then the Code slab softly glows coral twice. Fade out at 5.4s. No captions.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
