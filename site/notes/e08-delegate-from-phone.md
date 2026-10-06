# Delegate from your phone

- Id: e08 · Kind: Explainer · Tags: Riley1
- Topic: Calling your dot with AirPods in and having it spin up Codex sessions on your computer.
- Keywords: phone, voice, delegate, airpods, dots, codex, remote, flow, mobile
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/e08-delegate-from-phone.mp4
- Composition: /source/e08-delegate-from-phone/index.html (live: /play.html?id=e08-delegate-from-phone)
- Assets: /source/e08-delegate-from-phone/assets/Geist-Variable.woff2, /source/e08-delegate-from-phone/assets/codex_mono.png, /source/e08-delegate-from-phone/assets/dots.png
- Style guide: /style.md

## Notes
A three-step flow: voice on your phone → your agent (dots) → work on your computer (Codex). Use it for delegating by voice. Beats: phone with an animated waveform (0.2s) → arrow (1.2s) → dots panel (1.5s) → arrow (2.3s) → monitor draws and Codex pops in (2.8s) → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 flow on #212120 in Geist: three 400x440 #2B2B29 panels joined by 4px coral arrows that draw on in sequence. Panel 1: a grey phone outline with a five-bar voice waveform that bounces; label 'Voice'. Panel 2 (light border): the official dots wordmark rises in; label 'Agent'. Panel 3: a grey monitor outline draws on and the Codex logo pops onto the screen; label 'Computer'. Fade out at 5.4s. No captions.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
