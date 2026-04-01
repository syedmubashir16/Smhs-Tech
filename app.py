import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Mubashir | Smhs Tech", page_icon="⚡", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #00d4ff; color: black; }
    .project-box {
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 15px;
        background-color: #161b22;
        margin-bottom: 20px;
        height: 250px;
    }
    .service-card {
        text-align: center;
        padding: 15px;
        border-radius: 10px;
        background: #1f2937;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🚀 Smhs Tech")
    st.markdown("---")
    page = st.radio("Navigation", ["Identity", "Portfolio", "Services", "Inquiry"])
    st.markdown("---")
    st.caption("Based in Karachi, Pakistan")

# --- PAGE 1: IDENTITY (HOME) ---
if page == "Identity":
    col1, col2 = st.columns([2, 1], gap="large")
    with col1:
        st.title("Mubashir")
        st.subheader("ERP Executive & AI Developer")
        st.write("""
            I bridge the gap between industrial operations and intelligent automation. 
            By day, I manage complex inventory and ERP workflows at **Alkaram Textile Mills**; 
            by night, I lead **Smhs Tech**, developing deployable AI systems that solve 
            real-world business friction.
        """)
        st.markdown("---")
        st.write("📍 **Location:** Karachi, Sindh")
        st.write("🎓 **Education:** BBA (IT) | Specialist in Deep Learning")

# --- PAGE 2: PORTFOLIO ---
elif page == "Portfolio":
    st.title("Solutions & Deployments")
    st.write("A showcase of scalable, formula-driven applications.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('''<div class="project-box">
            <h3>🛡️ AI Authenticity Detector</h3>
            <p>A B2B API framework designed to detect synthetic media and deepfakes. 
            Built with a FastAPI backend for high-concurrency social media monitoring.</p>
        </div>''', unsafe_allow_html=True)

        st.markdown('''<div class="project-box">
            <h3>🏎️ F1 Mission Control</h3>
            <p>A 2026-regulation compliant visualizer. Features active aero animations 
            and real-time telemetry tables using custom Python logic.</p>
        </div>''', unsafe_allow_html=True)

    with c2:
        st.markdown('''<div class="project-box">
            <h3>📊 Textile Analytics Hub</h3>
            <p>Eliminated manual data entry at A Large textile mill by automating waste mapping 
            and production sync using dynamic Python-to-Excel pipelines.</p>
        </div>''', unsafe_allow_html=True)

        st.markdown('''<div class="project-box">
            <h3>📍 Precision Geolocation</h3>
            <p>Deployed Streamlit app utilizing Aladhan API for sub-second 
            location-based timing accuracy.</p>
        </div>''', unsafe_allow_html=True)

# --- PAGE 3: SERVICES ---
elif page == "Services":
    st.title("What Smhs Tech Does")
    s1, s2, s3 = st.columns(3)
    
    with s1:
        st.markdown('<div class="service-card"><h3>Inventory Auto</h3><p>Oracle ERP sync & automation</p></div>', unsafe_allow_html=True)
    with s2:
        st.markdown('<div class="service-card"><h3>Custom AI</h3><p>Deep Learning & Object Detection</p></div>', unsafe_allow_html=True)
    with s3:
        st.markdown('<div class="service-card"><h3>Web Tech</h3><p>FastAPI, Streamlit & SEO</p></div>', unsafe_allow_html=True)
    
    st.markdown("---")

# --- PAGE 4: INQUIRY ---
elif page == "Inquiry":
    st.title("Get a Quotation")
    st.write("Typical project delivery: 40-60 days.")
    with st.form("smhs_form"):
        name = st.text_input("Business Name")
        needs = st.multiselect("Service Needed", ["ERP Automation", "AI/ML Integration", "Web Dev", "SEO"])
        details = st.text_area("Project Context")
        if st.form_submit_button("Submit to Smhs Tech"):
            st.success("Proposal request received. We will align our workflow and contact you.")

st.markdown("---")
st.caption("© 2026 Smhs Tech | Built with Python")