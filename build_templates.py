"""Writes the 14 B-roll template compositions (style-board frames → HyperFrames motion)."""
import os, re, shutil

ROOT = "/Users/rileybrown/Downloads/explainer-motion"
SRC = [f"{ROOT}/shared", f"{ROOT}/shared-media"]

HEAD = """<!doctype html>
<html lang="en" data-resolution="landscape">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>{title}</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      @font-face {{ font-family: "Geist"; src: url("assets/Geist-Variable.woff2") format("woff2"); font-weight: 100 900; }}
      :root {{ --ground: #212120; --panel: #2b2b29; --text: #f4f3ef; --muted: #9c9b96; --accent: #f07a5a; --line: rgba(255,255,255,0.10); --focus: rgba(244,243,239,0.55); }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: var(--ground); }}
      #root {{ position: relative; width: 100%; height: 100%; font-family: "Geist", ui-sans-serif, system-ui, sans-serif; color: var(--text); }}
      #scene {{ position: absolute; inset: 0; }}
      .fill {{ display: block; width: 100%; height: 100%; object-fit: cover; }}
      .inset {{ position: absolute; overflow: hidden; border: 1px solid var(--line); }}
{css}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="6" data-width="1920" data-height="1080">
{body}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
{script}
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
"""
FADE = '      tl.to("#scene", { opacity: 0, duration: 0.5, ease: "power2.in" }, 5.4);'

def vid(id_, file, track=1):
    return f'<video id="{id_}" class="clip fill" src="assets/{file}" muted playsinline data-start="0" data-duration="6" data-track-index="{track}"></video>'

T = {}

T["t01-concept-card"] = dict(title="Concept card", css="""
      #scene { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 64px; }
      .logos { display: flex; align-items: center; gap: 72px; height: 120px; }
      .logos img { display: block; width: auto; }
      .lines { display: flex; flex-direction: column; align-items: center; gap: 6px; text-align: center; }
      .line { font-size: 72px; font-weight: 500; letter-spacing: -0.02em; line-height: 1.12; }
      .muted { color: var(--muted); }""", body="""
      <div id="scene">
        <div class="logos">
          <img class="logo" src="assets/openai.png" alt="OpenAI" style="height: 116px" />
          <img class="logo" src="assets/anthropic.png" alt="Anthropic" style="height: 92px" />
          <img class="logo" src="assets/spacex.png" alt="SpaceX" style="height: 72px" />
        </div>
        <div class="lines">
          <div id="line-1" class="line">A single point of contact.</div>
          <div id="line-2" class="line muted">Agent orchestrator.</div>
        </div>
      </div>""", script="""
      tl.fromTo(".logo", { opacity: 0, y: 18, scale: 0.86 }, { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "back.out(1.8)", stagger: 0.15 }, 0.2);
      tl.fromTo("#line-1", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 0.85);
      tl.fromTo("#line-2", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 2.2);
""" + FADE)

T["t02-hot-take"] = dict(title="Hot take card", css="""
      #scene { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 64px; }
      #mark { display: block; height: 120px; width: auto; image-rendering: pixelated; }
      .lines { display: flex; flex-direction: column; align-items: center; gap: 6px; text-align: center; }
      .line { font-size: 72px; font-weight: 500; letter-spacing: -0.02em; line-height: 1.12; }
      .muted { color: var(--muted); }""", body="""
      <div id="scene">
        <img id="mark" src="assets/claude_code.png" alt="Claude Code" />
        <div class="lines">
          <div id="line-1" class="line muted">Nobody should be using Claude.</div>
          <div id="line-2" class="line">Everyone should be using Claude Code.</div>
        </div>
      </div>""", script="""
      tl.fromTo("#mark", { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(2)" }, 0.2);
      tl.fromTo("#line-1", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 0.7);
      tl.fromTo("#line-2", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 1.9);
      tl.fromTo("#mark", { y: 0 }, { immediateRender: false, y: -8, duration: 0.18, ease: "power2.out", yoyo: true, repeat: 1 }, 1.95);
""" + FADE)

T["t03-video-on-grey"] = dict(title="Launch video on grey", css="""
      #frame { left: 160px; top: 90px; width: 1600px; height: 900px; border-radius: 28px; box-shadow: 0 28px 80px rgba(0,0,0,0.5); }""", body=f"""
      <div id="scene">
        <div id="frame" class="inset">{vid("launch", "dots_launch.mp4")}</div>
      </div>""", script="""
      tl.fromTo("#frame", { opacity: 0, scale: 0.955 }, { opacity: 1, scale: 1, duration: 0.45, ease: "power3.out" }, 0);
""" + FADE)

T["t04-video-on-blur"] = dict(title="Launch video on blurred A-roll", css="""
      #bg { position: absolute; inset: 0; }
      #frame { left: 200px; top: 112px; width: 1520px; height: 855px; border-radius: 28px; border-color: rgba(255,255,255,0.14); box-shadow: 0 28px 90px rgba(0,0,0,0.55); }""", body=f"""
      <div id="scene">
        <div id="bg">{vid("aroll-blur", "riley_blur_bg.mp4", 0)}</div>
        <div id="frame" class="inset">{vid("launch", "grok_primary.mp4")}</div>
      </div>""", script="""
      tl.fromTo("#frame", { opacity: 0, scale: 0.955 }, { opacity: 1, scale: 1, duration: 0.45, ease: "power3.out" }, 0.1);
""" + FADE)

T["t05-side-by-side"] = dict(title="Side-by-side compare", css="""
      #scene { display: flex; align-items: center; justify-content: center; gap: 64px; }
      .col { display: flex; flex-direction: column; align-items: center; gap: 44px; width: 800px; }
      .logo { height: 64px; display: flex; align-items: center; }
      .logo img { display: block; width: auto; }
      .card { position: relative; width: 800px; height: 450px; border-radius: 24px; overflow: hidden; border: 1px solid var(--line); box-shadow: 0 24px 70px rgba(0,0,0,0.45); }""", body=f"""
      <div id="scene">
        <div class="col">
          <div id="logo-a" class="logo"><img src="assets/claude_code_wordmark.png" alt="Claude Code" style="height: 52px" /></div>
          <div id="card-a" class="card">{vid("clip-a", "claude_projects.mp4")}</div>
        </div>
        <div class="col">
          <div id="logo-b" class="logo"><img src="assets/grokbot.png" alt="Grok Bot" style="height: 56px" /></div>
          <div id="card-b" class="card">{vid("clip-b", "grok_launch.mp4", 2)}</div>
        </div>
      </div>""", script="""
      tl.fromTo(["#card-a", "#card-b"], { opacity: 0, y: 30, scale: 0.96 }, { opacity: 1, y: 0, scale: 1, duration: 0.55, ease: "power3.out", stagger: 0.18 }, 0.15);
      tl.fromTo(["#logo-a", "#logo-b"], { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.45, ease: "power3.out", stagger: 0.18 }, 0.4);
""" + FADE)

T["t06-single-logo"] = dict(title="Single logo reveal", css="""
      #scene { display: flex; align-items: center; justify-content: center; }
      #mark { display: block; height: 150px; width: auto; }""", body="""
      <div id="scene">
        <img id="mark" src="assets/gemini_wordmark_white.png" alt="Gemini" />
      </div>""", script="""
      tl.fromTo("#mark", { opacity: 0, scale: 0.86, y: 12 }, { opacity: 1, scale: 1, y: 0, duration: 0.6, ease: "back.out(1.6)" }, 0.25);
      tl.fromTo("#mark", { scale: 1 }, { immediateRender: false, scale: 1.04, duration: 4.5, ease: "sine.inOut" }, 0.85);
""" + FADE)

def logo_item(file, alt, label, style):
    return f'<div class="item"><div class="mark"><img src="assets/{file}" alt="{alt}" style="{style}" /></div><div class="label">{label}</div></div>'

T["t07-logo-row"] = dict(title="Logo row", css="""
      #scene { display: flex; align-items: center; justify-content: center; gap: 56px; }
      .item { display: flex; flex-direction: column; align-items: center; gap: 36px; width: 280px; }
      .mark { height: 170px; display: flex; align-items: center; justify-content: center; }
      .mark img { display: block; }
      .label { font-size: 36px; font-weight: 500; color: var(--muted); }""", body="""
      <div id="scene">
        """ + "\n        ".join([
            logo_item("google.png", "Google", "Google", "height: 150px; width: auto"),
            logo_item("openai.png", "OpenAI", "OpenAI", "height: 156px; width: auto"),
            logo_item("spacex.png", "SpaceX", "SpaceX", "width: 250px; height: auto"),
            logo_item("anthropic.png", "Anthropic", "Anthropic", "height: 140px; width: auto"),
            logo_item("meta_logo.png", "Meta", "Meta", "width: 230px; height: auto")]) + """
      </div>""", script="""
      tl.fromTo(".mark", { opacity: 0, scale: 0.86, y: 18 }, { opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.8)", stagger: 0.4 }, 0.3);
      tl.fromTo(".label", { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.35, ease: "power2.out", stagger: 0.4 }, 0.45);
""" + FADE)

ARROW = '<svg width="150" height="40" viewBox="0 0 150 40" fill="none" aria-hidden="true"><path class="arrow-{n}" d="M4 20 H140 M120 6 L140 20 L120 34" pathLength="1" stroke-dasharray="1" stroke="#f07a5a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
T["t08-delegation-flow"] = dict(title="Delegation flow", css="""
      #scene { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 120px; }
      .row { display: grid; grid-template-columns: 520px 220px 320px; align-items: center; justify-items: center; }
      .to { display: flex; flex-direction: column; align-items: center; gap: 24px; }
      .row img { display: block; width: auto; }
      .label { font-size: 36px; font-weight: 500; color: var(--muted); }""", body=f"""
      <div id="scene">
        <div class="row">
          <img id="from-1" src="assets/grokbot.png" alt="Grok Bot" style="height: 92px" />
          {ARROW.format(n=1)}
          <div id="to-1" class="to"><img src="assets/cursor.png" alt="Cursor" style="height: 150px" /><div class="label">Cursor</div></div>
        </div>
        <div class="row">
          <img id="from-2" src="assets/dots.png" alt="dots" style="height: 120px" />
          {ARROW.format(n=2)}
          <div id="to-2" class="to"><img src="assets/codex_mono.png" alt="Codex" style="height: 150px" /><div class="label">Codex</div></div>
        </div>
      </div>""", script="""
      tl.fromTo("#from-1", { opacity: 0, x: -24 }, { opacity: 1, x: 0, duration: 0.45, ease: "power3.out" }, 0.2);
      tl.fromTo(".arrow-1", { strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 0.45, ease: "power2.inOut" }, 0.55);
      tl.fromTo("#to-1", { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.45, ease: "back.out(2)" }, 0.9);
      tl.fromTo("#from-2", { opacity: 0, x: -24 }, { opacity: 1, x: 0, duration: 0.45, ease: "power3.out" }, 1.7);
      tl.fromTo(".arrow-2", { strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 0.45, ease: "power2.inOut" }, 2.05);
      tl.fromTo("#to-2", { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.45, ease: "back.out(2)" }, 2.4);
""" + FADE)

T["t09-website"] = dict(title="Website screenshot", css="""
      #scene { display: flex; align-items: center; justify-content: center; }
      #browser { width: 1440px; border-radius: 24px; overflow: hidden; background: var(--panel); border: 1px solid rgba(255,255,255,0.12); box-shadow: 0 28px 80px rgba(0,0,0,0.5); display: flex; flex-direction: column; }
      .chrome { height: 56px; display: flex; align-items: center; gap: 10px; padding: 0 22px; border-bottom: 1px solid rgba(255,255,255,0.08); }
      .dot { width: 13px; height: 13px; border-radius: 50%; background: #5a5a57; }
      .url { margin: 0 auto; padding: 8px 28px; border-radius: 999px; background: var(--ground); font-size: 20px; color: #c9c8c3; }
      .spacer { width: 63px; }
      .page { width: 1440px; height: 900px; overflow: hidden; }
      #shot { display: block; width: 1440px; height: 900px; object-fit: cover; object-position: top; }""", body="""
      <div id="scene">
        <div id="browser">
          <div class="chrome"><div class="dot"></div><div class="dot"></div><div class="dot"></div><div class="url">agentnative.inc</div><div class="spacer"></div></div>
          <div class="page"><img id="shot" src="assets/agentnative_site.jpg" alt="agentnative.inc homepage" /></div>
        </div>
      </div>""", script="""
      tl.fromTo("#browser", { opacity: 0, y: 40, scale: 0.96 }, { opacity: 1, y: 0, scale: 1, duration: 0.6, ease: "power3.out" }, 0.15);
      tl.fromTo("#shot", { scale: 1 }, { scale: 1.05, duration: 5.2, ease: "sine.inOut", transformOrigin: "50% 30%" }, 0.3);
""" + FADE)

T["t10-benchmark"] = dict(title="Benchmark chart", css="""
      #card { position: absolute; left: 160px; top: 155px; width: 1600px; height: 770px; border-radius: 24px; overflow: hidden; border: 1px solid var(--line); box-shadow: 0 28px 80px rgba(0,0,0,0.5); }
      #chart { display: block; width: 1600px; height: 770px; object-fit: cover; object-position: top; }
      #highlight { position: absolute; left: 550px; top: 341px; }""", body="""
      <div id="scene">
        <div id="card"><img id="chart" src="assets/opus_chart.jpg" alt="Claude Opus 5.5 benchmark table" /></div>
        <svg id="highlight" width="248" height="596" viewBox="0 0 248 596" fill="none" aria-hidden="true"><rect id="box" x="2" y="2" width="244" height="592" rx="14" pathLength="1" stroke-dasharray="1" stroke="#f07a5a" stroke-width="4"></rect></svg>
      </div>""", script="""
      tl.fromTo("#card", { opacity: 0, y: 40, scale: 0.96 }, { opacity: 1, y: 0, scale: 1, duration: 0.6, ease: "power3.out" }, 0.15);
      tl.fromTo("#box", { strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 0.9, ease: "power2.inOut" }, 1.1);
      tl.fromTo("#box", { opacity: 1 }, { immediateRender: false, opacity: 0.55, duration: 0.45, ease: "sine.inOut", yoyo: true, repeat: 3 }, 2.3);
""" + FADE)

T["t11-post-card"] = dict(title="Official post card", css="""
      #scene { display: flex; align-items: center; justify-content: center; }
      #post { width: 1120px; padding: 56px 64px; border-radius: 28px; background: var(--panel); border: 1px solid var(--line); box-shadow: 0 28px 80px rgba(0,0,0,0.45); display: flex; flex-direction: column; gap: 32px; }
      .head { display: flex; align-items: center; gap: 22px; }
      .avatar { width: 84px; height: 84px; border-radius: 50%; background: var(--text); display: flex; align-items: center; justify-content: center; }
      .avatar img { display: block; width: 50px; height: 50px; }
      .name { font-size: 34px; font-weight: 600; }
      .handle { font-size: 22px; color: var(--muted); margin-top: 4px; }
      #text { font-size: 40px; font-weight: 400; line-height: 1.32; letter-spacing: -0.01em; }
      #media { position: relative; width: 100%; height: 420px; border-radius: 18px; overflow: hidden; border: 1px solid rgba(255,255,255,0.08); }""", body=f"""
      <div id="scene">
        <div id="post">
          <div id="head" class="head"><div class="avatar"><img src="assets/claude_symbol.png" alt="" /></div><div><div class="name">Claude</div><div class="handle">@claudeai</div></div></div>
          <div id="text">Projects now run from one conversation, starting in Claude Code. You describe what needs doing, and Claude directs parallel threads that keep working after you close your laptop.</div>
          <div id="media">{vid("post-video", "claude_projects.mp4")}</div>
        </div>
      </div>""", script="""
      tl.fromTo("#post", { opacity: 0, y: 40, scale: 0.96 }, { opacity: 1, y: 0, scale: 1, duration: 0.6, ease: "power3.out" }, 0.15);
      tl.fromTo("#head", { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" }, 0.45);
      tl.fromTo("#text", { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }, 0.65);
      tl.fromTo("#media", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, 1.0);
""" + FADE)

LABEL_CSS = """
      #shade { position: absolute; left: 0; bottom: 0; width: 1100px; height: 420px; background: radial-gradient(ellipse at 0% 100%, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0) 70%); }
      .name { font-size: 60px; font-weight: 600; letter-spacing: -0.02em; text-shadow: 0 2px 18px rgba(0,0,0,0.45); }
      #label { position: absolute; left: 96px; bottom: 84px; }"""
LABEL_OUT = '      tl.to("#label", { opacity: 0, y: 8, duration: 0.3, ease: "power2.in" }, 4.6);'

T["t12-label-plain"] = dict(title="Name label plain", css=LABEL_CSS, body=f"""
      <div id="scene">
        {vid("aroll", "riley_150.mp4", 0)}
        <div id="shade"></div>
        <div id="label" class="name">Riley Brown</div>
      </div>""", script="""
      tl.fromTo("#shade", { opacity: 0 }, { opacity: 1, duration: 0.4 }, 0.4);
      tl.fromTo("#label", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.45, ease: "power3.out" }, 0.55);
""" + LABEL_OUT + '\n      tl.to("#shade", { opacity: 0, duration: 0.3 }, 4.65);')

T["t13-label-pill"] = dict(title="Name label pill", css="""
      #label { position: absolute; left: 96px; bottom: 84px; padding: 18px 34px; border-radius: 999px; background: rgba(33,33,32,0.88); border: 1px solid rgba(255,255,255,0.12); box-shadow: 0 12px 40px rgba(0,0,0,0.35); font-size: 44px; font-weight: 500; letter-spacing: -0.01em; }""", body=f"""
      <div id="scene">
        {vid("aroll", "riley_245.mp4", 0)}
        <div id="label">Riley Brown</div>
      </div>""", script="""
      tl.fromTo("#label", { opacity: 0, x: -30 }, { opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }, 0.55);
""" + LABEL_OUT)

T["t14-label-bar"] = dict(title="Name label accent bar", css=LABEL_CSS + """
      #label { display: flex; align-items: center; gap: 22px; }
      #bar { display: block; width: 6px; height: 58px; border-radius: 3px; background: var(--accent); }
      #name { font-size: 56px; }""", body=f"""
      <div id="scene">
        {vid("aroll", "riley_560.mp4", 0)}
        <div id="shade"></div>
        <div id="label"><div id="bar"></div><div id="name" class="name">Riley Brown</div></div>
      </div>""", script="""
      tl.fromTo("#shade", { opacity: 0 }, { opacity: 1, duration: 0.4 }, 0.35);
      tl.fromTo("#bar", { scaleY: 0, transformOrigin: "50% 100%" }, { scaleY: 1, duration: 0.35, ease: "power3.out" }, 0.5);
      tl.fromTo("#name", { opacity: 0, x: -20 }, { opacity: 1, x: 0, duration: 0.45, ease: "power3.out" }, 0.72);
""" + LABEL_OUT + '\n      tl.to("#shade", { opacity: 0, duration: 0.3 }, 4.65);')

for slug, t in T.items():
    d = f"{ROOT}/videos/{slug}"
    html = HEAD.format(title=t["title"], css=t["css"], body=t["body"], script=t["script"])
    open(f"{d}/index.html", "w").write(html)
    needed = set(re.findall(r'assets/([\w.\-]+)', html))
    for n in needed:
        for s in SRC:
            if os.path.exists(f"{s}/{n}"):
                shutil.copy(f"{s}/{n}", f"{d}/assets/{n}"); break
        else:
            raise SystemExit(f"missing asset {n} for {slug}")
    print("wrote", slug, sorted(needed))
