import streamlit as st
import time

# --- CONFIG & STYLING ---
st.set_page_config(page_title="Smhs Tech | Mubashir", page_icon="🧬", layout="wide")

st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
    <style>
    /* Main Background & Glassmorphism */
    .stApp {
        background: radial-gradient(circle at top right, #1a1a2e, #16213e, #0f3460);
        color: #e94560;
    }
    
    /* Animated Title */
    .hero-title {
        font-family: 'Courier New', Courier, monospace;
        font-size: 4rem;
        font-weight: 800;
        background: -webkit-linear-gradient(#00d4ff, #005f73);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: fadeInDown 1s;
    }

    /* Project Cards with Glow & Hover Animation */
    .card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 25px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 20px;
    }
    .card:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.3);
        border: 1px solid #00d4ff;
    }

    /* Terminal Text Effect */
    .terminal {
        background: #000;
        color: #00ff41;
        padding: 15px;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
        border-left: 4px solid #00ff41;
    }

    /* Status Pulse */
    .pulse {
        height: 10px;
        width: 10px;
        background-color: #00ff41;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 0 0 rgba(0, 255, 65, 0.7);
        animation: pulse-green 2s infinite;
    }
    @keyframes pulse-green {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 255, 65, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(0, 255, 65, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 255, 65, 0); }
    }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown('<h1 class="hero-title animate__animated animate__fadeInDown">SMHS TECH</h1>', unsafe_allow_html=True)
st.markdown("""
    <div class="terminal">
        > INITIALIZING INTERFACE... <br>
        > MUBASHIR: ERP & AI ENGINEER DETECTED <br>
        > LOCATION: KARACHI_PK <br>
        > STATUS: <span class="pulse"></span> ONLINE
    </div>
    """, unsafe_allow_html=True)

st.write("##")

# --- GRID LAYOUT ---
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 🛠️ Specialized Engineering")
    st.write("Building formula-driven automation for industrial scale.")
    
    # Project 1: AI Authenticity
    st.markdown('''
    <div class="card animate__animated animate__fadeInLeft">
        <h3 style="color:#00d4ff;">🛡️ AI Authenticity Detector</h3>
        <p>B2B API for synthetic media detection. High-concurrency FastAPI backend.</p>
        <code style="color:#00ff41;">Status: Production Ready</code>
    </div>
    ''', unsafe_allow_html=True)

    # Project 2: F1 Mission Control
    st.markdown('''
    <div class="card animate__animated animate__fadeInLeft" style="animation-delay: 0.2s;">
        <h3 style="color:#00d4ff;">🏎️ F1 2026 Visualizer</h3>
        <p>Mission Control style telemetry. Active aero animations & live timing tables.</p>
        <code style="color:#00ff41;">Engine: Python / Streamlit</code>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown("### 🏢 Industrial Impact")
    st.write("Modernizing the core of Pakistan's textile industry.")

    # Project 3: Alkaram ERP
    st.markdown('''
    <div class="card animate__animated animate__fadeInRight">
        <h3 style="color:#00d4ff;">📊 Spinning Mill Dashboard</h3>
        <p>Automated waste mapping & Oracle ERP data sync for Alkaram Textile Mills.</p>
        <code style="color:#00ff41;">Impact: -90% Manual Entry</code>
    </div>
    ''', unsafe_allow_html=True)

    # Project 4: Geolocation
    st.markdown('''
    <div class="card animate__animated animate__fadeInRight" style="animation-delay: 0.2s;">
        <h3 style="color:#00d4ff;">📍 Precision Geo-Timing</h3>
        <p>High-precision Aladhan API integration with sub-second accuracy.</p>
        <code style="color:#00ff41;">Deployed: Streamlit Cloud</code>
    </div>
    ''', unsafe_allow_html=True)

# --- SERVICES & TECH STACK ---
st.write("---")
st.markdown('<h2 style="text-align: center;">TECH STACK & CAPABILITIES</h2>', unsafe_allow_html=True)

tech_col1, tech_col2, tech_col3, tech_col4 = st.columns(4)
with tech_col1: st.button("🐍 Python / FastAPI")
with tech_col2: st.button("🤖 Deep Learning")
with tech_col3: st.button("🏢 Oracle ERP")
with tech_col4: st.button("☁️ Cloud Deploy")

# --- FOOTER ---
st.write("---")

# --- FOOTER SECTION ---
with st.container():
    # Professional Footer Branding
    st.markdown("""
        <div style="text-align: center; color: #8892b0; padding: 20px;">
            <p><b>Designed by Smhs Tech © 2026</b></p>
            <p>Karachi, Sindh, Pakistan</p>
        </div>
    """, unsafe_allow_html=True)

    # --- CONTACT FORM SECTION ---
    st.subheader("📩 Start a Project with Smhs Tech")
    
    # Crucial: Use st.form to group these inputs
    with st.form("inquiry_form", clear_on_submit=True):
        col_a, col_b = st.columns(2)
        
        with col_a:
            name = st.text_input("Business Name")
        with col_b:
            needs = st.multiselect("Services Required", ["ERP Automation", "AI/ML Integration", "Web Dev", "SEO"])
            
        details = st.text_area("Project Context & Goals")
        
        # The submit button MUST be the last item in the form block
        submit = st.form_submit_button("Submit Proposal")
        
        if submit:
            if name and details:
                st.success(f"Requirement logged for {name}. Smhs Tech will reach out shortly.")
            else:
                st.error("Please provide a Business Name and Project Context.")

st.markdown("---")
st.caption("© 2026 Smhs Tech | Built with Python")
