# Launch video on grey

- Id: t03 · Kind: Template · Tags: Riley1
- Topic: Show official launch footage, full screen, on the brand grey.
- Keywords: video, launch video, footage, b-roll, official, insert, product demo, announcement, framed video
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/t03-video-on-grey.mp4
- Composition: /source/t03-video-on-grey/index.html (live: /play.html?id=t03-video-on-grey)
- Assets: /source/t03-video-on-grey/assets/Geist-Variable.woff2, /source/t03-video-on-grey/assets/dots_launch.mp4
- Style guide: /style.md

## Notes
A full-screen video insert: the official launch clip plays inside a 1600x900 rounded frame (28px radius, hairline, soft shadow) on #212120. Never picture-in-picture over the A-roll. Beats: frame scales 96→100% (0–0.45s) → clip plays → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 video insert on #212120. Center a 1600x900 frame with 28px rounded corners, a 1px rgba(255,255,255,0.10) border and a soft drop shadow, playing an official launch video muted (here OpenAI's dots launch film). The frame scales in from 95.5% to 100% over 0.45s with power3.out. No captions or source tags. Fade out at 5.4s.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
