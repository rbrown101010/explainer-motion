# Benchmark chart

- Id: t10 · Kind: Template · Tags: Riley1
- Topic: Point at the one number that matters.
- Keywords: benchmark, chart, table, stats, numbers, highlight, data, model comparison, scores, proof
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/t10-benchmark.mp4
- Composition: /source/t10-benchmark/index.html (live: /play.html?id=t10-benchmark)
- Assets: /source/t10-benchmark/assets/Geist-Variable.woff2, /source/t10-benchmark/assets/opus_chart.jpg
- Style guide: /style.md

## Notes
An official benchmark table in a rounded card with a single coral highlight box drawn around the column that matters. Beats: card rises (0.15s) → box draws on (1.1s) → box pulses → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 benchmark shot on #212120. A 1600x770 rounded card showing the official Claude Opus 5.5 benchmark table. A 4px coral (#F07A5A) rounded rectangle draws itself around the Opus 5.5 column, then gently pulses. One highlight only. Fade out at 5.4s.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
