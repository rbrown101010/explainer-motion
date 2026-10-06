# Explainer Motion — style guide

How every motion explainer in this collection is built, so another agent can replicate the look for a different video.

## Canvas
- 1920×1080, 6 seconds, 30 fps, rendered to MP4 with HyperFrames (`npx hyperframes render`).
- One idea per frame, built from official logos, simple line icons and arrows.
- Loops cleanly: start on an empty frame, build in over about 0–3.4s, hold, and fade the whole scene out from 5.4s to 5.9s.

## Color
- Background `#212120` (the agentnative.inc grey). Panels `#2B2B29`.
- Text and focal strokes `#F4F3EF`. Secondary text and strokes `#9C9B96`.
- Accent `#F07A5A`, only for arrows, wires and soft glows.
- Hairline borders `rgba(255,255,255,0.10)`. Focal node border `2px rgba(244,243,239,0.55)`.

## Type
- Geist, one family, bundled locally as a variable woff2.
- Node labels: Geist Medium 36–40px. One or two words only.
- No titles, captions, subtitles or source tags on the frame.

## Shapes
- Panels: 28px radius, 1px hairline. Small tiles: 18–24px radius.
- Icons are inline SVG strokes at 5–7px, round caps and joins.
- Official logos as transparent PNGs, never boxed in a colored badge.

## Motion
- Panels enter with `opacity 0→1, y 30→0, scale 0.96→1`, 0.55s, `power3.out`.
- Arrows and outlines draw on with `pathLength="1"` + `stroke-dasharray="1"` and `strokeDashoffset 1→0`, 0.45–0.7s, `power2.inOut`.
- Logos and tiles pop with `scale 0.6→1`, 0.4s, `back.out(2)`, staggered 0.12–0.22s.
- Labels fade up `y 12→0`, 0.4s.
- One gentle secondary loop during the hold (a pulse, blink, float or glow), never more.
- Exit: one `opacity → 0` on the whole scene at 5.4s, 0.5s, `power2.in`.

## HyperFrames rules that matter
- One paused GSAP timeline registered at `window.__timelines["main"]`, matching the root `data-composition-id`.
- Root carries `data-duration="6" data-width="1920" data-height="1080"`.
- Deterministic only: no `Math.random`, clocks or network.
- When a second `fromTo` targets the same element, give it `immediateRender: false`.
- Run `npx hyperframes check .` before rendering; it should report 0 errors and 0 warnings.
