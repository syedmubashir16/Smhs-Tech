import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Smhs Tech | Mubashir",
    page_icon="🧬",
    layout="wide"
)

st.markdown("""
    <style>
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    </style>
""", unsafe_allow_html=True)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Exo+2:wght@300;400;500&family=Share+Tech+Mono&display=swap" rel="stylesheet"/>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }

  :root {
    --cyan:    #00e5ff;
    --blue:    #0066ff;
    --green:   #00ff9d;
    --dim:     #4a6580;
    --text:    #cde0f0;
    --bg:      #04080f;
    --card-bg: rgba(0, 20, 45, 0.6);
  }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Exo 2', sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* ── BACKGROUND LAYERS ── */
  .bg-layer { position: fixed; inset: 0; z-index: 0; pointer-events: none; }
  .bg-grid {
    background-image:
      linear-gradient(rgba(0,229,255,0.035) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,229,255,0.035) 1px, transparent 1px);
    background-size: 48px 48px;
  }
  .bg-radial {
    background:
      radial-gradient(ellipse 70% 50% at 80% 10%, rgba(0,102,255,0.12) 0%, transparent 70%),
      radial-gradient(ellipse 50% 40% at 10% 80%, rgba(0,229,255,0.07) 0%, transparent 60%);
  }

  /* ── SCANLINE ── */
  .scanline {
    position: fixed; left: 0; right: 0; top: -3px;
    height: 3px; z-index: 20; pointer-events: none;
    background: linear-gradient(90deg, transparent, var(--cyan) 40%, rgba(0,229,255,0.4) 60%, transparent);
    filter: blur(1px);
    animation: scan 5s linear infinite;
  }
  @keyframes scan { from { top: -3px; } to { top: 100vh; } }

  /* ── CORNER BRACKETS ── */
  .corner { position: fixed; width: 55px; height: 55px; z-index: 5; pointer-events: none; }
  .corner::before, .corner::after { content: ''; position: absolute; background: rgba(0,229,255,0.5); }
  .corner::before { width: 100%; height: 1px; top: 0; }
  .corner::after  { width: 1px; height: 100%; top: 0; }
  .corner.tl { top: 14px; left: 14px; }
  .corner.tr { top: 14px; right: 14px; transform: scaleX(-1); }
  .corner.bl { bottom: 14px; left: 14px; transform: scaleY(-1); }
  .corner.br { bottom: 14px; right: 14px; transform: scale(-1); }

  /* ── LAYOUT ── */
  .wrap {
    position: relative; z-index: 1;
    max-width: 980px; margin: 0 auto;
    padding: 3rem 2rem 4rem;
  }

  /* ── HERO ── */
  .hero { padding: 3.5rem 0 2.5rem; }

  .hero-eyebrow {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.67rem;
    letter-spacing: 0.35em;
    color: var(--cyan);
    opacity: 0.55;
    margin-bottom: 0.9rem;
    animation: fadeUp 0.6s ease both;
  }

  .hero-logo {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(2.6rem, 8vw, 5rem);
    font-weight: 900;
    letter-spacing: 0.06em;
    line-height: 1;
    color: transparent;
    background: linear-gradient(135deg, #ffffff 0%, var(--cyan) 38%, var(--blue) 72%, var(--cyan) 100%);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 4s ease infinite, fadeUp 0.7s 0.1s ease both;
  }
  @keyframes shimmer {
    0%,100% { background-position: 0% 50%; }
    50%      { background-position: 100% 50%; }
  }
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: none; }
  }

  .hero-sub {
    font-family: 'Exo 2', sans-serif;
    font-size: 0.95rem;
    font-weight: 300;
    color: var(--dim);
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-top: 0.65rem;
    animation: fadeUp 0.7s 0.2s ease both;
  }
  .hero-sub span { color: var(--cyan); font-weight: 400; }

  /* ── TERMINAL ── */
  .terminal-box {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.79rem;
    background: rgba(0,0,0,0.55);
    border: 1px solid rgba(0,229,255,0.16);
    border-left: 2px solid var(--cyan);
    border-radius: 6px;
    padding: 1.1rem 1.4rem;
    margin-top: 2rem;
    line-height: 2.2;
    opacity: 0;
    animation: fadeUp 0.7s 0.4s ease forwards;
    position: relative;
  }
  .terminal-box::before {
    content: '\25CF  \25CF  \25CF';
    display: block;
    font-size: 0.45rem;
    letter-spacing: 0.4em;
    color: rgba(0,229,255,0.25);
    margin-bottom: 0.8rem;
  }
  .terminal-box .prompt { color: var(--green); }
  .terminal-box .val    { color: var(--cyan); }
  .terminal-box .muted  { color: var(--dim); }

  .pulse-dot {
    display: inline-block; width: 7px; height: 7px;
    background: var(--green); border-radius: 50%;
    margin: 0 6px 1px 0; vertical-align: middle;
    animation: pulse 2s infinite;
  }
  @keyframes pulse {
    0%,100% { box-shadow: 0 0 0 0 rgba(0,255,157,0.7); }
    50%      { box-shadow: 0 0 0 8px rgba(0,255,157,0); }
  }

  /* ── SECTION LABEL ── */
  .section-label {
    display: flex; align-items: center; gap: 0.8rem;
    font-family: 'Orbitron', sans-serif;
    font-size: 0.58rem;
    font-weight: 600;
    letter-spacing: 0.3em;
    color: var(--cyan);
    text-transform: uppercase;
    margin: 3rem 0 1.25rem;
    opacity: 0.6;
  }
  .section-label::after {
    content: '';
    flex: 1; height: 1px;
    background: linear-gradient(90deg, rgba(0,229,255,0.2), transparent);
  }

  /* ── STATS ── */
  .stats-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    opacity: 0;
    animation: fadeUp 0.7s 0.5s ease forwards;
  }
  @media (max-width: 520px) { .stats-row { grid-template-columns: 1fr 1fr; } }

  .stat-box {
    border: 1px solid rgba(0,229,255,0.1);
    border-radius: 6px;
    padding: 1.1rem 1rem;
    background: rgba(0,229,255,0.03);
    text-align: center;
    transition: border-color 0.3s, box-shadow 0.3s;
  }
  .stat-box:hover {
    border-color: rgba(0,229,255,0.35);
    box-shadow: 0 4px 20px rgba(0,229,255,0.07);
  }
  .stat-val {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.7rem;
    font-weight: 700;
    color: var(--cyan);
    line-height: 1;
  }
  .stat-val sup {
    font-size: 0.9rem;
    color: rgba(0,229,255,0.45);
    vertical-align: super;
  }
  .stat-label {
    font-family: 'Exo 2', sans-serif;
    font-size: 0.7rem;
    font-weight: 300;
    color: var(--dim);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-top: 0.4rem;
  }

  /* ── PROJECT CARDS ── */
  .cards-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
  }
  @media (max-width: 600px) { .cards-grid { grid-template-columns: 1fr; } }

  .card {
    background: var(--card-bg);
    border: 1px solid rgba(0,229,255,0.1);
    border-radius: 8px;
    padding: 1.4rem 1.6rem;
    position: relative;
    overflow: hidden;
    cursor: default;
    transition: transform 0.35s ease, border-color 0.35s ease, box-shadow 0.35s ease;
    opacity: 0;
    transform: translateY(24px);
    animation: riseIn 0.7s ease forwards;
  }
  .card::before {
    content: '';
    position: absolute; top: 0; left: 0;
    width: 28px; height: 28px;
    border-top: 2px solid rgba(0,229,255,0.35);
    border-left: 2px solid rgba(0,229,255,0.35);
    border-radius: 8px 0 0 0;
    transition: border-color 0.3s;
  }
  .card:hover {
    transform: translateY(-7px) !important;
    border-color: rgba(0,229,255,0.4);
    box-shadow: 0 14px 40px rgba(0,229,255,0.09), inset 0 0 0 1px rgba(0,229,255,0.05);
  }
  .card:hover::before { border-color: var(--cyan); }

  @keyframes riseIn { to { opacity: 1; transform: translateY(0); } }
  .card:nth-child(1) { animation-delay: 0.6s; }
  .card:nth-child(2) { animation-delay: 0.75s; }
  .card:nth-child(3) { animation-delay: 0.9s; }
  .card:nth-child(4) { animation-delay: 1.05s; }

  .card-num {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.52rem;
    font-weight: 700;
    color: rgba(0,229,255,0.22);
    letter-spacing: 0.22em;
    margin-bottom: 0.7rem;
  }
  .card-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.82rem;
    font-weight: 700;
    color: #dff0ff;
    margin-bottom: 0.6rem;
    letter-spacing: 0.03em;
    line-height: 1.35;
  }
  .card-desc {
    font-family: 'Exo 2', sans-serif;
    font-size: 0.84rem;
    font-weight: 300;
    color: #4e6e88;
    line-height: 1.65;
    margin-bottom: 1rem;
  }
  .badge {
    display: inline-block;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.62rem;
    padding: 3px 10px;
    border-radius: 2px;
    border: 1px solid rgba(0,255,157,0.25);
    background: rgba(0,255,157,0.05);
    color: var(--green);
    letter-spacing: 0.06em;
  }
  .badge.blue {
    border-color: rgba(0,229,255,0.25);
    background: rgba(0,229,255,0.05);
    color: var(--cyan);
  }

  /* ── TECH STACK ── */
  .stack-row {
    display: flex; flex-wrap: wrap; gap: 0.55rem;
    margin-top: 0.5rem;
    opacity: 0;
    animation: fadeUp 0.7s 1.2s ease forwards;
  }
  .tag {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.69rem;
    padding: 5px 14px;
    border: 1px solid rgba(0,229,255,0.16);
    border-radius: 3px;
    color: #506a80;
    background: rgba(0,229,255,0.025);
    letter-spacing: 0.07em;
    transition: all 0.22s;
  }
  .tag:hover {
    border-color: var(--cyan);
    color: var(--cyan);
    background: rgba(0,229,255,0.08);
    box-shadow: 0 0 14px rgba(0,229,255,0.1);
  }

  /* ── DIVIDER ── */
  .divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,229,255,0.18), transparent);
    margin: 2.5rem 0;
  }

  /* ── FOOTER ── */
  .footer { text-align: center; padding: 0.5rem 0 1rem; }
  .footer p {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.58rem;
    font-weight: 400;
    color: rgba(74,101,128,0.45);
    letter-spacing: 0.22em;
  }
</style>
</head>
<body>

<div class="bg-layer bg-grid"></div>
<div class="bg-layer bg-radial"></div>
<div class="scanline"></div>
<div class="corner tl"></div>
<div class="corner tr"></div>
<div class="corner bl"></div>
<div class="corner br"></div>

<div class="wrap">

  <!-- HERO -->
  <div class="hero">
    <div class="hero-eyebrow">// PORTFOLIO SYSTEM v2.6 — INITIALIZED</div>
    <div class="hero-logo">SMHS TECH</div>
    <div class="hero-sub">ERP &amp; AI Engineering &nbsp;&middot;&nbsp; <span>Karachi, PK</span></div>
    <div class="terminal-box">
      <span class="prompt">&gt;</span> <span class="muted">BOOT SEQUENCE COMPLETE</span><br>
      <span class="prompt">&gt;</span> ENGINEER: <span class="val">MUBASHIR &mdash; ERP &amp; AI SYSTEMS</span><br>
      <span class="prompt">&gt;</span> LOCATION: <span class="val">KARACHI_PK &nbsp;/&nbsp; 24.8607&deg;N 67.0011&deg;E</span><br>
      <span class="prompt">&gt;</span> STACK: <span class="val">PYTHON &middot; FASTAPI &middot; PYTORCH &middot; ORACLE</span><br>
      <span class="prompt">&gt;</span> STATUS: <span class="pulse-dot"></span><span class="val">ONLINE &amp; AVAILABLE</span>
    </div>
  </div>

  <!-- STATS -->
  <div class="section-label">Metrics</div>
  <div class="stats-row">
    <div class="stat-box">
      <div class="stat-val">90<sup>%</sup></div>
      <div class="stat-label">Manual Entry Reduced</div>
    </div>
    <div class="stat-box">
      <div class="stat-val">4+</div>
      <div class="stat-label">Live Deployments</div>
    </div>
    <div class="stat-box">
      <div class="stat-val">2</div>
      <div class="stat-label">AI Model Backends</div>
    </div>
  </div>

  <!-- PROJECTS -->
  <div class="section-label">Featured Projects</div>
  <div class="cards-grid">

    <div class="card">
      <div class="card-num">PROJECT // 01</div>
      <div class="card-title">AI Authenticity Detector</div>
      <div class="card-desc">B2B API for synthetic media detection. High-concurrency FastAPI backend with dual PyTorch / TensorFlow models and explainability layer.</div>
      <span class="badge">Production Ready</span>
    </div>

    <div class="card">
      <div class="card-num">PROJECT // 02</div>
      <div class="card-title">F1 2026 Visualizer</div>
      <div class="card-desc">Mission Control telemetry dashboard with active aero animations, live timing tables, and real-time data pipelines.</div>
      <span class="badge blue">Python / Streamlit</span>
    </div>

    <div class="card">
      <div class="card-num">PROJECT // 03</div>
      <div class="card-title">Spinning Mill Dashboard</div>
      <div class="card-desc">Automated waste mapping &amp; Oracle ERP sync for Alkaram Textile Mills. Eliminated 90% of manual data entry across production lines.</div>
      <span class="badge">&minus;90% Manual Entry</span>
    </div>

    <div class="card">
      <div class="card-num">PROJECT // 04</div>
      <div class="card-title">Precision Geo-Timing</div>
      <div class="card-desc">High-precision Aladhan API integration delivering sub-second prayer time accuracy. Live on Streamlit Cloud with geolocation support.</div>
      <span class="badge blue">Deployed: Cloud</span>
    </div>

  </div>

  <!-- TECH STACK -->
  <div class="section-label">Tech Stack</div>
  <div class="stack-row">
    <div class="tag">Python</div>
    <div class="tag">FastAPI</div>
    <div class="tag">PyTorch</div>
    <div class="tag">TensorFlow</div>
    <div class="tag">Oracle ERP</div>
    <div class="tag">Streamlit</div>
    <div class="tag">Deep Learning</div>
    <div class="tag">Cloud Deploy</div>
    <div class="tag">REST APIs</div>
    <div class="tag">Pandas</div>
  </div>

  <div class="divider"></div>

  <!-- FOOTER -->
  <div class="footer">
    <p>SMHS&nbsp;TECH &nbsp;&middot;&nbsp; &copy;&nbsp;2026 &nbsp;&middot;&nbsp; KARACHI,&nbsp;SINDH,&nbsp;PAKISTAN</p>
  </div>

</div>
</body>
</html>
"""

components.html(HTML, height=1050, scrolling=False)

st.markdown("---")
st.subheader("📬 Get in Touch")

with st.form("contact_form"):
    name = st.text_input("Business Name")
    details = st.text_area("Project Context")
    submit = st.form_submit_button("Send Requirement")

if submit:
    if name and details:
        st.success(f"Requirement logged for {name}. Smhs Tech will reach out shortly.")
    else:
        st.error("Please provide a Business Name and Project Context.")

st.caption("© 2026 Smhs Tech | Built with Python")
