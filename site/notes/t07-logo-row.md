# Logo row

- Id: t07 · Kind: Template · Tags: Riley1
- Topic: Show the players in a space, one by one.
- Keywords: logos, logo row, companies, players, competitors, list, market, labs, lineup
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/t07-logo-row.mp4
- Composition: /source/t07-logo-row/index.html (live: /play.html?id=t07-logo-row)
- Assets: /source/t07-logo-row/assets/Geist-Variable.woff2, /source/t07-logo-row/assets/anthropic.png, /source/t07-logo-row/assets/google.png, /source/t07-logo-row/assets/meta_logo.png, /source/t07-logo-row/assets/openai.png, /source/t07-logo-row/assets/spacex.png
- Style guide: /style.md

## Notes
Five official logos in a row with names on one baseline, each popping in as it's named. Beats: logo every 0.4s from 0.3s, labels follow → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 logo row on #212120 in Geist. Five official logos (Google, OpenAI, SpaceX, Anthropic, Meta), each in a 280px column with its name in Geist Medium 36px #9C9B96 on a shared baseline. Each logo pops in from 86% with back.out every 0.4s, its label fading up just after. Fade out at 5.4s. No captions.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
