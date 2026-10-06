# Official post card

- Id: t11 · Kind: Template · Tags: Riley1
- Topic: Quote a real launch post with its video.
- Keywords: tweet, post, x, twitter, announcement, quote, social, launch post, official post
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/t11-post-card.mp4
- Composition: /source/t11-post-card/index.html (live: /play.html?id=t11-post-card)
- Assets: /source/t11-post-card/assets/Geist-Variable.woff2, /source/t11-post-card/assets/claude_projects.mp4, /source/t11-post-card/assets/claude_symbol.png
- Style guide: /style.md

## Notes
A real post recreated as a clean card: avatar, name and handle, the post's real text, and its launch video playing below. Beats: card rises (0.15s) → header (0.45s) → text (0.65s) → video (1.0s) → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 post card on #212120 in Geist. A 1120px #2B2B29 card (28px radius) with a round avatar (the Claude mark on white), 'Claude' and '@claudeai', the post's real text at 40px: 'Projects now run from one conversation, starting in Claude Code. You describe what needs doing, and Claude directs parallel threads that keep working after you close your laptop.', and a 420px rounded media area playing the post's launch video muted. Parts fade up in order. Fade out at 5.4s.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
