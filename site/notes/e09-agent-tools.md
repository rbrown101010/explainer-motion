# An agent with its own tools

- Id: e09 · Kind: Explainer · Tags: Riley1
- Topic: I gave GrokBot its own email and credit card.
- Keywords: tools, integrations, email, credit card, hub, spokes, connectors, apps, accounts
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/e09-agent-tools.mp4
- Composition: /source/e09-agent-tools/index.html (live: /play.html?id=e09-agent-tools)
- Assets: /source/e09-agent-tools/assets/Geist-Variable.woff2, /source/e09-agent-tools/assets/gmail.png, /source/e09-agent-tools/assets/googlecalendar.png, /source/e09-agent-tools/assets/notion.png, /source/e09-agent-tools/assets/slack.png
- Style guide: /style.md

## Notes
A hub-and-spoke: one agent in the centre connects to its own email, card, Slack, calendar, Notion and the web. Use it when an agent gets its own accounts or tools. Beats: hub pops and blinks (0.2s) → six coral spokes draw and tools pop clockwise (1.1s) → hub glows → second blink → fade (5.4s).

## Prompt
Make a 6-second 1920x1080 hub-and-spoke motion graphic on #212120 in Geist. Centre: a 260px round #2B2B29 node with a light border and a white robot-face icon that blinks. Around it at 60° steps, six 150px rounded tiles: Gmail, a credit card icon, Slack, Google Calendar, Notion and a globe. 4px coral spokes draw from the hub to each tile in turn as each tile pops in, then the hub glows coral. Fade out at 5.4s. No captions.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
