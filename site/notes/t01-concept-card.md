# Concept card

- Id: t01 · Kind: Template · Tags: Riley1
- Topic: Introduce a concept with the companies behind it.
- Keywords: text card, concept, intro, two lines, logos, title, statement, definition, idea
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/t01-concept-card.mp4
- Composition: /source/t01-concept-card/index.html (live: /play.html?id=t01-concept-card)
- Assets: /source/t01-concept-card/assets/Geist-Variable.woff2, /source/t01-concept-card/assets/anthropic.png, /source/t01-concept-card/assets/openai.png, /source/t01-concept-card/assets/spacex.png
- Style guide: /style.md

## Notes
A text card for introducing a concept: one logo group, then two same-size lines (white, then grey). Use it only when naming a new idea. Beats: logos pop in (0.2s) → line 1 fades up (0.85s) → line 2 (2.2s) → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 text card on #212120 in Geist Medium. Centered: a row of three official logos (OpenAI, Anthropic, SpaceX) that pop in one by one, then 64px below two lines at the same 72px size, tracking -2%: 'A single point of contact.' in #F4F3EF and 'Agent orchestrator.' in #9C9B96, each fading up as it is said. No other text. Fade out at 5.4s.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
