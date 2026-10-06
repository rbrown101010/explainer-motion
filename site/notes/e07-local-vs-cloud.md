# Local vs cloud agent

- Id: e07 · Kind: Explainer · Tags: Riley1
- Topic: Agents that run on your own computer keep your logins, files and footage.
- Keywords: local, cloud, computer, laptop, files, logins, privacy, compare, where agents run
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/e07-local-vs-cloud.mp4
- Composition: /source/e07-local-vs-cloud/index.html (live: /play.html?id=e07-local-vs-cloud)
- Assets: /source/e07-local-vs-cloud/assets/Geist-Variable.woff2
- Style guide: /style.md

## Notes
Compares an agent on your computer (logins, files, video) with one in the cloud. Local is the focal side. Use it when explaining why local agents matter, such as for video editing. Beats: laptop draws (0.45s), key, folder and video icons pop (1.2s) → cloud draws (2.15s) and floats → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 comparison on #212120 in Geist. Left 560x480 panel with a light border: a white outline laptop draws on, then grey key, folder and play-button icons pop in beneath it; label 'Local' in white. Right panel with a hairline border: a grey outline cloud draws on and gently floats; label 'Cloud' in grey. Fade out at 5.4s. No captions.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
