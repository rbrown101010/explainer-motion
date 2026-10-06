# The race

- Id: e10 · Kind: Explainer · Tags: Riley1
- Topic: Every lab is racing to build the single point of contact agent.
- Keywords: timeline, race, launches, dates, history, grok bot, muse, dots, gemini, claude
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/e10-the-race.mp4
- Composition: /source/e10-the-race/index.html (live: /play.html?id=e10-the-race)
- Assets: /source/e10-the-race/assets/Geist-Variable.woff2, /source/e10-the-race/assets/claude_code_wordmark.png, /source/e10-the-race/assets/dots.png, /source/e10-the-race/assets/gemini_wordmark_white.png, /source/e10-the-race/assets/grokbot.png, /source/e10-the-race/assets/meta_logo.png
- Style guide: /style.md

## Notes
A launch timeline from Aug to Oct 2026: Grok Bot (Aug 11), Muse (Sep 8), Claude Code Projects (Sep 17), dots (Sep 29), then Gemini on a dashed, still-moving coral line. Use it for 'the great race'. Beats: line draws Aug → Oct (0.2s) with each launch landing as it reaches its date → future line marches (2.2s) → Gemini lands (2.6s) → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 timeline on #212120 in Geist. A faint white horizontal line draws from Aug to Oct with grey month ticks and labels. As it passes each date a white dot pops and an official logo rises in, alternating above and below: Grok Bot (Aug 11), Meta/Muse (Sep 8), Claude Code (Sep 17), dots (Sep 29). Then a dashed coral line marches on past today to a hollow dot where a dimmed Gemini wordmark appears. Fade out at 5.4s. No captions.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
