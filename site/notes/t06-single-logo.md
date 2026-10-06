# Single logo reveal

- Id: t06 · Kind: Template · Tags: Riley1
- Topic: Name one product with its official logo.
- Keywords: logo, single logo, reveal, brand, product name, mention, wordmark, intro
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/t06-single-logo.mp4
- Composition: /source/t06-single-logo/index.html (live: /play.html?id=t06-single-logo)
- Assets: /source/t06-single-logo/assets/Geist-Variable.woff2, /source/t06-single-logo/assets/gemini_wordmark_white.png
- Style guide: /style.md

## Notes
One official logo, centered on #212120, popping in on the word and slowly pushing in. Beats: pop 86→100% (0.25s) → slow push to 104% → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 logo reveal on #212120. The official Gemini wordmark (white text, color sparkle) at 150px tall, centered, pops in from 86% scale with back.out, then slowly pushes in to 104% over 4.5s. Nothing else on screen. Fade out at 5.4s.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
