import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Smhs Tech | Mubashir",
    page_icon="🧬",
    layout="wide"
)

# Hide Streamlit default UI chrome
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
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@500;700&display=swap" rel="stylesheet"/>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: #060d1a;
    color: #c9d6e3;
    font-family: 'Rajdhani', sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* Grid background */
  .grid-bg {
    position: fixed; inset: 0; z-index: 0;
    background-image:
      linear-gradient(rgba(0,200,255,0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,200,255,0.04) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
  }

  /* Animated scanline */
  .scanline {
    position: fixed; top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(0,200,255,0.6), transparent);
    z-index: 10;
    animation: scan 4s linear infinite;
  }
  @keyframes scan { from { top: 0; } to { top: 100vh; } }

  .wrap {
    position: relative; z-index: 1;
    max-width: 960px; margin: 0 auto;
    padding: 2.5rem 1.5rem 3rem;
  }

  /* ── HERO ── */
  .hero { padding: 3rem 0 2rem; }

  .hero-logo {
    font-family: 'Share Tech Mono', monospace;
    font-size: clamp(2.8rem, 7vw, 4.5rem);
    font-weight: 400;
    color: transparent;
    background: linear-gradient(135deg, #00c8ff 0%, #0057c2 55%, #00c8ff 100%);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 3s ease infinite, fadeDown 0.8s ease both;
    letter-spacing: 0.12em;
  }
  @keyframes shimmer {
    0%,100% { background-position: 0% 50%; }
    50%      { background-position: 100% 50%; }
  }
  @keyframes fadeDown {
    from { opacity: 0; transform: translateY(-24px); }
    to   { opacity: 1; transform: none; }
  }

  .terminal-box {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.82rem;
    background: rgba(0,0,0,0.6);
    border: 1px solid rgba(0,200,255,0.25);
    border-left: 3px solid #00c8ff;
    border-radius: 4px;
    padding: 1rem 1.25rem;
    margin-top: 1.5rem;
    line-height: 2.1;
    animation: fadeDown 0.8s 0.3s ease both;
    opacity: 0;
    animation-fill-mode: forwards;
  }
  .terminal-box .prompt { color: #00ff88; }
  .terminal-box .val    { color: #00c8ff; }

  .pulse-dot {
    display: inline-block;
    width: 8px; height: 8px;
    background: #00ff88;
    border-radius: 50%;
    margin-right: 6px;
    vertical-align: middle;
    animation: pulse 2s infinite;
  }
  @keyframes pulse {
    0%,100% { box-shadow: 0 0 0 0 rgba(0,255,136,0.6); }
    50%     { box-shadow: 0 0 0 7px rgba(0,255,136,0); }
  }

  /* ── SECTION LABEL ── */
  .section-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    color: #00c8ff;
    text-transform: uppercase;
    margin: 2.8rem 0 1rem;
    opacity: 0.7;
  }

  /* ── PROJECT CARDS ── */
  .cards-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
  }
  @media (max-width: 580px) {
    .cards-grid { grid-template-columns: 1fr; }
  }

  .card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(0,200,255,0.15);
    border-radius: 10px;
    padding: 1.3rem 1.5rem;
    cursor: default;
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    opacity: 0;
    transform: translateY(22px);
    animation: riseIn 0.6s ease forwards;
  }
  .card:hover {
    transform: translateY(-6px) !important;
    border-color: rgba(0,200,255,0.6);
    box-shadow: 0 8px 32px rgba(0,200,255,0.12),
                inset 0 0 0 1px rgba(0,200,255,0.08);
  }
  @keyframes riseIn {
    to { opacity: 1; transform: translateY(0); }
  }
  .card:nth-child(1) { animation-delay: 0.5s; }
  .card:nth-child(2) { animation-delay: 0.65s; }
  .card:nth-child(3) { animation-delay: 0.8s; }
  .card:nth-child(4) { animation-delay: 0.95s; }

  .card-icon  { font-size: 1.4rem; margin-bottom: 0.5rem; }
  .card-title {
    font-size: 1.05rem; font-weight: 700;
    color: #e0f4ff; margin-bottom: 0.4rem;
    letter-spacing: 0.02em;
  }
  .card-desc {
    font-size: 0.88rem; color: #7a96af;
    line-height: 1.55; margin-bottom: 0.75rem;
  }
  .badge {
    display: inline-block;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.68rem;
    padding: 3px 10px;
    border-radius: 3px;
    border: 1px solid rgba(0,255,136,0.3);
    background: rgba(0,255,136,0.07);
    color: #00ff88;
  }
  .badge.blue {
    border-color: rgba(0,200,255,0.3);
    background: rgba(0,200,255,0.07);
    color: #00c8ff;
  }

  /* ── TECH STACK ── */
  .stack-row {
    display: flex; flex-wrap: wrap; gap: 0.6rem;
    margin-top: 0.5rem;
    animation: fadeDown 0.8s 1.1s ease both;
    opacity: 0;
    animation-fill-mode: forwards;
  }
  .tag {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.73rem;
    padding: 5px 14px;
    border: 1px solid rgba(0,200,255,0.22);
    border-radius: 4px;
    color: #7ab8cf;
    background: rgba(0,200,255,0.04);
    letter-spacing: 0.05em;
    transition: border-color 0.2s, color 0.2s, background 0.2s;
  }
  .tag:hover {
    border-color: #00c8ff;
    color: #00c8ff;
    background: rgba(0,200,255,0.1);
  }

  /* ── DIVIDER ── */
  .divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,200,255,0.3), transparent);
    margin: 2rem 0;
  }

  /* ── FOOTER ── */
  .footer { text-align: center; padding: 1rem 0; }
  .footer p {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.7rem;
    color: rgba(122,150,175,0.45);
    letter-spacing: 0.1em;
  }
</style>
</head>
<body>

<div class="grid-bg"></div>
<div class="scanline"></div>

<div class="wrap">

  <!-- HERO -->
  <div class="hero">
    <div class="hero-logo">SMHS TECH</div>
    <div class="terminal-box">
      <span class="prompt">&gt;</span> INITIALIZING INTERFACE...<br>
      <span class="prompt">&gt;</span> ENGINEER: <span class="val">MUBASHIR — ERP &amp; AI</span><br>
      <span class="prompt">&gt;</span> LOCATION: <span class="val">KARACHI_PK</span><br>
      <span class="prompt">&gt;</span> STATUS:&nbsp;<span class="pulse-dot"></span><span class="val">ONLINE</span>
    </div>
  </div>

  <!-- PROJECTS -->
  <div class="section-label">// Featured Projects</div>
  <div class="cards-grid">

    <div class="card">
      <div class="card-icon">🛡️</div>
      <div class="card-title">AI Authenticity Detector</div>
      <div class="card-desc">B2B API for synthetic media detection. High-concurrency FastAPI backend with dual PyTorch / TensorFlow models and explainability features.</div>
      <span class="badge">Production Ready</span>
    </div>

    <div class="card">
      <div class="card-icon">🏎️</div>
      <div class="card-title">F1 2026 Visualizer</div>
      <div class="card-desc">Mission Control style telemetry dashboard. Active aero animations &amp; live timing tables built in Python / Streamlit.</div>
      <span class="badge blue">Python / Streamlit</span>
    </div>

    <div class="card">
      <div class="card-icon">📊</div>
      <div class="card-title">Spinning Mill Dashboard</div>
      <div class="card-desc">Automated waste mapping &amp; Oracle ERP data sync for Alkaram Textile Mills. Reduced manual entry by 90%.</div>
      <span class="badge">−90% Manual Entry</span>
    </div>

    <div class="card">
      <div class="card-icon">📍</div>
      <div class="card-title">Precision Geo-Timing</div>
      <div class="card-desc">High-precision Aladhan API integration delivering sub-second accuracy for prayer time calculation. Deployed on Streamlit Cloud.</div>
      <span class="badge blue">Deployed: Cloud</span>
    </div>

  </div>

  <!-- TECH STACK -->
  <div class="section-label">// Tech Stack &amp; Capabilities</div>
  <div class="stack-row">
    <div class="tag">Python</div>
    <div class="tag">FastAPI</div>
    <div class="tag">PyTorch</div>
    <div class="tag">TensorFlow</div>
    <div class="tag">Oracle ERP</div>
    <div class="tag">Streamlit</div>
    <div class="tag">Deep Learning</div>
    <div class="tag">Cloud Deploy</div>
  </div>

  <div class="divider"></div>

  <!-- FOOTER -->
  <div class="footer">
    <p>SMHS TECH &copy; 2026 &nbsp;|&nbsp; KARACHI, SINDH, PAKISTAN</p>
  </div>

</div>
</body>
</html>
"""

components.html(HTML, height=900, scrolling=False)

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

st.markdown("---")
st.caption("© 2026 Smhs Tech | Built with Python")
