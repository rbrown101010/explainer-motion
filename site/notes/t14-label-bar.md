# Name label · accent bar

- Id: t14 · Kind: Template · Tags: Riley1
- Topic: Name label with a coral bar over your footage.
- Keywords: name, lower third, accent bar, label, intro, person, speaker, overlay, on video, coral
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/t14-label-bar.mp4
- Composition: /source/t14-label-bar/index.html (live: /play.html?id=t14-label-bar)
- Assets: /source/t14-label-bar/assets/Geist-Variable.woff2, /source/t14-label-bar/assets/riley_560.mp4
- Style guide: /style.md

## Notes
Your A-roll with a 6px coral bar that grows up, then 'Riley Brown' sliding in beside it, bottom-left over a soft shade. Beats: shade (0.35s) → bar grows (0.5s) → name slides (0.72s) → out (4.6s).

## Prompt
Make a 6-second 1920x1080 name label over the speaker's own footage. Bottom-left (96px in, 84px up): a 6x58px coral (#F07A5A) rounded bar that grows upward, then 'Riley Brown' in Geist Semibold 56px slides in beside it, over a subtle dark corner shade. Fade out at 4.6s. One line only, no subtitle.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
