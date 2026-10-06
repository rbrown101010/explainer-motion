# Hot take card

- Id: t02 · Kind: Template · Tags: Riley1
- Topic: Land a contrarian opinion with one logo.
- Keywords: hot take, opinion, contrast, text card, two lines, punchline, claim, controversial
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/t02-hot-take.mp4
- Composition: /source/t02-hot-take/index.html (live: /play.html?id=t02-hot-take)
- Assets: /source/t02-hot-take/assets/Geist-Variable.woff2, /source/t02-hot-take/assets/claude_code.png
- Style guide: /style.md

## Notes
A text card for a hot take: one logo above a grey setup line and a white punchline, both the same size. Beats: logo pops (0.2s) → grey line (0.7s) → white line (1.9s) with a small logo bounce → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 hot-take card on #212120 in Geist Medium. Centered: the Claude Code pixel mascot pops in, then two 72px lines: 'Nobody should be using Claude.' in grey #9C9B96, then 'Everyone should be using Claude Code.' in white, with the mascot bouncing once as the second line lands. Fade out at 5.4s. No captions.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
