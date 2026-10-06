# Name label · plain

- Id: t12 · Kind: Template · Tags: Riley1
- Topic: Put your name on screen over your own footage.
- Keywords: name, lower third, label, intro, person, speaker, overlay, on video, name tag, introduction
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/t12-label-plain.mp4
- Composition: /source/t12-label-plain/index.html (live: /play.html?id=t12-label-plain)
- Assets: /source/t12-label-plain/assets/Geist-Variable.woff2, /source/t12-label-plain/assets/riley_150.mp4
- Style guide: /style.md

## Notes
Your A-roll with 'Riley Brown' bottom-left (96px in, 84px up) in Geist Semibold 60px over a soft corner shade. Name only, never a subtitle. Beats: shade (0.4s) → name fades up (0.55s) → hold ~4s → out (4.6s).

## Prompt
Make a 6-second 1920x1080 name label over the speaker's own footage. Bottom-left, 96px from the left and 84px from the bottom, the name 'Riley Brown' in Geist Semibold 60px white with a soft text shadow, over a subtle radial dark shade in that corner. The shade and name fade up at about 0.5s and fade out at 4.6s. One line only, no title or subtitle.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
