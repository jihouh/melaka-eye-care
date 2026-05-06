import streamlit as st
import pandas as pd

# 1. PAGE SETUP
st.set_page_config(page_title="Melaka Eye Guide 2026", layout="wide")

# Custom CSS for Mobile Visibility
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    /* Stylizing the Estimator Box */
    .estimator-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e0e0e0;
        margin-bottom: 20px;
    }
    div[data-testid="stMetricValue"] { font-size: 2rem !important; color: #1e88e5; }
    </style>
    """, unsafe_allow_html=True)

# 2. COMPLETE DATASET
hospital_data = {
    "ISEC Melaka (SSEC)": {
        "dr": "Dr. Robert Yeo / Dr. Ang Wen Jeat",
        "rating": "⭐ 4.9/5",
        "contact": "+606-283 3510",
        "base": 3800,
        "just": "Dedicated eye center. Best for focused surgical care."
    },
    "Pantai Hospital Ayer Keroh": {
        "dr": "Dr. Liu Han Seng",
        "rating": "⭐ 4.8/5",
        "contact": "+606-231 9999",
        "base": 4500,
        "just": "Full-service hospital backup; excellent for elderly with complex health needs."
    },
    "Oriental Melaka Straits (OMSMC)": {
        "dr": "Dr. Ang Wen Jeat (Peter)",
        "rating": "⭐ 4.8/5",
        "contact": "+606-315 8888",
        "base": 4000,
        "just": "Modern facility; transparent fixed-price packages."
    },
    "Putra Specialist Hospital": {
        "dr": "Datin Dr. Kasthuri Nagaratnam",
        "rating": "⭐ 4.7/5",
        "contact": "+606-283 5888",
        "base": 3900,
        "just": "Known for compassionate care and trusted local reputation."
    },
    "Mahkota Medical Centre": {
        "dr": "Dr. Sendhil Kumar Somasundaram",
        "rating": "⭐ 4.6/5",
        "contact": "+606-285 2999",
        "base": 4600,
        "just": "High-volume center with experienced retina specialists."
    }
}

tech_info = {
    "Standard Phaco": {"price": 0, "def": "Manual incision + ultrasound. Most common."},
    "Laser-Assisted (FLACS)": {"price": 3000, "def": "Laser precision; gentler on the eye."}
}

lens_info = {
    "Monofocal (Distance)": {"price": 0, "def": "Clear distance vision; reading glasses needed."},
    "Toric (Astigmatism)": {"price": 2000, "def": "Corrects astigmatism for sharp distance vision."},
    "EDOF (Extended Range)": {"price": 3500, "def": "Great for distance + computer; fewer halos."},
    "Multifocal / Trifocal": {"price": 4500, "def": "Near, mid, and far vision. Goal: No glasses."}
}

# --- 3. MAIN BODY ESTIMATOR (Visible by Default) ---
st.title("👁️ Melaka Cataract Guide")

with st.container():
    st.subheader("💰 Personalized Cost Estimator")
    
    # Selection inputs in the main body instead of sidebar
    col1, col2 = st.columns(2)
    with col1:
        hosp_choice = st.selectbox("Choose Hospital & Doctor", list(hospital_data.keys()))
        num_eyes = st.radio("Number of Eyes", [1, 2], horizontal=True)
    with col2:
        tech_choice = st.selectbox("Surgery Technique", list(tech_info.keys()))
        lens_choice = st.selectbox("Lens Technology", list(lens_info.keys()))

    # Calculation logic
    total_cost = (hospital_data[hosp_choice]["base"] + tech_info[tech_choice]["price"] + lens_info[lens_choice]["price"]) * num_eyes

    # Result Metric
    st.metric("Estimated Total Cost", f"RM {total_cost:,}")
    st.caption(f"📞 Contact {hosp_choice}: {hospital_data[hosp_choice]['contact']}")
    st.divider()

# --- 4. DIRECTORY & DEFINITIONS ---
tab1, tab2 = st.tabs(["🏥 Specialist Directory", "💡 Understanding Choices"])

with tab1:
    for name, info in hospital_data.items():
        with st.expander(f"{info['rating']} - {info['dr']} ({name})"):
            st.markdown(f"**Specialist:** {info['dr']}")
            st.markdown(f"**Justification:** {info['just']}")
            st.markdown(f"**Contact:** [Call {info['contact']}](tel:{info['contact'].replace(' ', '')})")
            st.write(f"**Est. Base Price:** RM {info['base']:,}")

with tab2:
    st.subheader("What are the options?")
    st.markdown("### Surgical Techniques")
    for k, v in tech_info.items():
        st.write(f"**{k}**: {v['def']}")
    st.divider()
    st.markdown("### Lens (IOL) Types")
    for k, v in lens_info.items():
        st.write(f"**{k}**: {v['def']}")
