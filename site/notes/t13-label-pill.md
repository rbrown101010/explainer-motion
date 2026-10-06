# Name label · pill

- Id: t13 · Kind: Template · Tags: Riley1
- Topic: Name label as a grey pill over your footage.
- Keywords: name, lower third, pill, label, intro, person, speaker, overlay, on video, chip
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/t13-label-pill.mp4
- Composition: /source/t13-label-pill/index.html (live: /play.html?id=t13-label-pill)
- Assets: /source/t13-label-pill/assets/Geist-Variable.woff2, /source/t13-label-pill/assets/riley_245.mp4
- Style guide: /style.md

## Notes
Your A-roll with 'Riley Brown' in a rounded #212120 pill at 88% opacity, bottom-left. Beats: pill slides in from the left (0.55s) → hold → out (4.6s).

## Prompt
Make a 6-second 1920x1080 name label over the speaker's own footage. Bottom-left (96px in, 84px up), a fully rounded pill in rgba(33,33,32,0.88) with a light hairline and soft shadow, holding 'Riley Brown' in Geist Medium 44px. It slides in from the left with a fade at 0.55s and fades out at 4.6s. One line only.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
