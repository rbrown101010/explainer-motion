# Interface × model

- Id: e06 · Kind: Explainer · Tags: Riley1
- Topic: A great interface only takes you so far; the model matters as much.
- Keywords: interface, model, multiply, ui, quality, equation, compare, product vs model
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/e06-interface-x-model.mp4
- Composition: /source/e06-interface-x-model/index.html (live: /play.html?id=e06-interface-x-model)
- Assets: /source/e06-interface-x-model/assets/Geist-Variable.woff2
- Style guide: /style.md

## Notes
Shows that results come from interface times model. Use it when a video says 'the best interface but a weak model' or vice versa. Beats: app window draws on (0.45s), layout blocks fill in → the × spins in (1.55s) → chip outline draws, die pops (2.2s), die pulses → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 motion graphic on #212120 in Geist. Two 480px #2B2B29 panels with a large grey '×' between them. Left: a white outline app window that draws itself on, three title-bar dots and three translucent layout blocks fill in; label 'Interface'. Right: a white outline chip with pins draws on and its centre die pops in and pulses; label 'Model'. The × spins in between them. Fade out at 5.4s. No captions.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
