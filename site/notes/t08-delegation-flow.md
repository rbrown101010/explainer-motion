# Delegation flow

- Id: t08 · Kind: Template · Tags: Riley1
- Topic: Show which product hands work to which.
- Keywords: flow, delegation, arrow, hands off, a to b, pairs, pipeline, sends work, connects
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/t08-delegation-flow.mp4
- Composition: /source/t08-delegation-flow/index.html (live: /play.html?id=t08-delegation-flow)
- Assets: /source/t08-delegation-flow/assets/Geist-Variable.woff2, /source/t08-delegation-flow/assets/codex_mono.png, /source/t08-delegation-flow/assets/cursor.png, /source/t08-delegation-flow/assets/dots.png, /source/t08-delegation-flow/assets/grokbot.png
- Style guide: /style.md

## Notes
Two rows of A → B pairs joined by coral arrows: Grok Bot → Cursor, dots → Codex. Beats: row one (0.2–1.35s), row two (1.7–2.85s) → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 flow on #212120 in Geist. Two rows, each a source wordmark, a 4px coral (#F07A5A) arrow that draws on, and a target logo with a grey 36px label: Grok Bot → Cursor, then dots → Codex. Each row animates source, arrow, target in order. Fade out at 5.4s. No captions.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
