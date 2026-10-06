# Launch video on blurred A-roll

- Id: t04 · Kind: Template · Tags: Riley1
- Topic: Show launch footage over a blurred copy of your own shot.
- Keywords: video, blur, blurred background, a-roll, launch video, insert, footage, depth, overlay
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/t04-video-on-blur.mp4
- Composition: /source/t04-video-on-blur/index.html (live: /play.html?id=t04-video-on-blur)
- Assets: /source/t04-video-on-blur/assets/Geist-Variable.woff2, /source/t04-video-on-blur/assets/grok_primary.mp4, /source/t04-video-on-blur/assets/riley_blur_bg.mp4
- Style guide: /style.md

## Notes
A full-screen video insert over your own footage: the A-roll scaled up 15%, blurred and dimmed to 50% fills the frame, and the launch clip plays in a 1520x855 rounded frame on top. Beats: frame scales in (0.1s) → both play → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 video insert. Background: the speaker's own footage scaled up 15%, Gaussian blurred heavily and darkened to 50% brightness. On top, a 1520x855 frame with 28px radius, a light hairline and a deep shadow, playing an official launch clip muted (here Grok Bot's Primary Bot). Scale the frame in from 95.5% over 0.45s. No captions. Fade out at 5.4s.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
