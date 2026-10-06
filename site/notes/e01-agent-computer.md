# Chatbot → agent with a computer

- Id: e01 · Kind: Explainer · Tags: Riley1
- Topic: ChatGPT was a chatbot. Now it has its own computer.
- Keywords: chatbot, agent, computer, apps, chatgpt, own computer, tools, gmail, slack, notion, upgrade, before after
- Duration: 6s · 1920x1080 · 30 fps
- Built with: HyperFrames (HTML + GSAP), Geist
- Video: /media/e01-agent-computer.mp4
- Composition: /source/e01-agent-computer/index.html (live: /play.html?id=e01-agent-computer)
- Assets: /source/e01-agent-computer/assets/Geist-Variable.woff2, /source/e01-agent-computer/assets/gmail.png, /source/e01-agent-computer/assets/googlecalendar.png, /source/e01-agent-computer/assets/notion.png, /source/e01-agent-computer/assets/slack.png
- Style guide: /style.md

## Notes
Explains the jump from a chat window to an agent that owns a computer and can use your apps. Use it when a video says a model now 'has its own computer' or 'works in your apps'. Beats: chatbot panel (0.2s) → arrow draws (1.35s) → computer draws on screen (1.95s) → Gmail, Slack, Calendar, Notion pop in (2.75s) → hold → fade out (5.4s).

## Prompt
Make a 6-second 1920x1080 motion graphic on a flat #212120 background in Geist. Left: a #2B2B29 rounded panel (500px, 28px radius, 1px hairline) with two grey outline chat bubbles that pop in, labelled 'Chatbot' in #9C9B96. A 4px coral (#F07A5A) arrow draws left to right. Right: a matching panel with a 2px light border; a white outline monitor draws itself on, a terminal prompt and blinking caret appear, then Gmail, Slack, Google Calendar and Notion logos pop in one by one. Label it 'Agent' in white. Hold, then fade everything out at 5.4s so it loops on an empty frame. No titles, captions or subtitles.

## Recreate it for another video
1. `npx hyperframes init <name> --example blank --non-interactive --skill motion-graphics`
2. Copy the composition to `index.html` and the files above into `assets/`.
3. Swap the logos, footage, words and timing for what you want to show. Keep the palette, type and motion rules from /style.md.
4. `npx hyperframes check .` (aim for 0 errors, 0 warnings), then `npx hyperframes render . -q high -o renders/video.mp4`.
