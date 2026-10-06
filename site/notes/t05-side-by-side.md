# Side-by-side compare

- Id: t05 · Kind: Template · Tags: Riley1
- Topic: Compare two products' footage at once.
- Keywords: compare, versus, vs, side by side, two videos, split screen, comparison, head to head
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/t05-side-by-side.mp4
- Composition: /source/t05-side-by-side/index.html (live: /play.html?id=t05-side-by-side)
- Assets: /source/t05-side-by-side/assets/Geist-Variable.woff2, /source/t05-side-by-side/assets/claude_code_wordmark.png, /source/t05-side-by-side/assets/claude_projects.mp4, /source/t05-side-by-side/assets/grok_launch.mp4, /source/t05-side-by-side/assets/grokbot.png
- Style guide: /style.md

## Notes
Two 800x450 video cards side by side, each under its product's wordmark, for direct comparisons. Beats: cards rise in, staggered (0.15s) → wordmarks fade in (0.4s) → both play → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 comparison on #212120. Two 800x450 video cards (24px radius, hairline, shadow) side by side with a 64px gap, each playing muted official footage: Claude Code Projects on the left, Grok Bot on the right. Above each, its official wordmark (Claude Code, Grok Bot) about 54px tall. Cards rise in staggered, then the wordmarks fade in. No captions. Fade out at 5.4s.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
