# Website screenshot

- Id: t09 · Kind: Template · Tags: Riley1
- Topic: Show a website in a clean browser frame.
- Keywords: website, browser, screenshot, url, landing page, web page, site, homepage, link
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/t09-website.mp4
- Composition: /source/t09-website/index.html (live: /play.html?id=t09-website)
- Assets: /source/t09-website/assets/Geist-Variable.woff2, /source/t09-website/assets/agentnative_site.jpg
- Style guide: /style.md

## Notes
A 1440px browser frame (traffic-light dots and a URL pill) holding a full-page screenshot that slowly pushes in. Beats: browser rises (0.15s) → screenshot pushes 100→105% → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 website shot on #212120. A 1440px-wide browser window (#2B2B29, 24px radius, hairline, shadow) with three grey traffic-light dots and a centered URL pill reading 'agentnative.inc', showing the site's screenshot. The window rises in, then the screenshot slowly pushes in to 105%. Fade out at 5.4s.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
