import streamlit as st
import pandas as pd

# 1. Page Config - SET TO WIDE BUT MOBILE WILL AUTO-STACK
st.set_page_config(page_title="Melaka Eye Guide", layout="wide")

# 2. DATA DEFINITIONS (Always define at the top)
hospital_data = {
    "ISEC Melaka (SSEC)": {
        "specialist": "Dr. Robert Yeo",
        "rating": 4.9,
        "contact": "+606-283 3510",
        "base": 3800,
        "just": "Dedicated eye center with specialized surgical teams."
    },
    "Pantai Hospital": {
        "specialist": "Dr. Liu Han Seng",
        "rating": 4.8,
        "contact": "+606-231 9999",
        "base": 4500,
        "just": "Full-service hospital backup with 24/7 emergency support."
    },
    "Oriental Melaka Straits": {
        "specialist": "Dr. Ang Wen Jeat",
        "rating": 4.8,
        "contact": "+606-315 8888",
        "base": 4000,
        "just": "Modern facilities and transparent medical tourism packages."
    }
}

tech_info = {
    "Standard Phaco": {"price": 0, "def": "Standard ultrasound surgery."},
    "Laser-Assisted": {"price": 3000, "def": "Femtosecond laser precision."}
}

lens_info = {
    "Monofocal": {"price": 0, "def": "Clear distance vision; need reading glasses."},
    "Multifocal": {"price": 4000, "def": "Clear vision at all distances; less glasses."}
}

# --- SIDEBAR (Auto-collapses on mobile) ---
st.sidebar.header("💰 Estimator")
selected_hosp = st.sidebar.selectbox("Hospital", list(hospital_data.keys()))
num_eyes = st.sidebar.radio("Eyes", [1, 2])
selected_tech = st.sidebar.selectbox("Technique", list(tech_info.keys()))
selected_lens = st.sidebar.selectbox("Lens", list(lens_info.keys()))

# Pricing Calculation
total = (hospital_data[selected_hosp]["base"] + tech_info[selected_tech]["price"] + lens_info[selected_lens]["price"]) * num_eyes

st.sidebar.divider()
st.sidebar.metric("Total Estimate", f"RM {total:,}")

# --- MAIN CONTENT ---
st.title("👁️ Melaka Cataract Guide")

tab1, tab2 = st.tabs(["🏥 Directory", "💡 Definitions"])

with tab1:
    st.subheader("Recommended Specialists")
    
    # MOBILE-FRIENDLY CARD LAYOUT
    # Instead of one big table that cuts off, we use a loop to create "cards"
    for name, info in hospital_data.items():
        with st.container(border=True):
            col_a, col_b = st.columns([1, 3])
            with col_a:
                st.write(f"⭐ **{info['rating']}**")
            with col_b:
                st.markdown(f"### {info['specialist']}")
                st.write(f"📍 {name}")
                st.write(f"📞 [Call {info['contact']}](tel:{info['contact'].replace(' ', '')})")
                st.caption(info['just'])

with tab2:
    st.write("### Surgical Techniques")
    for k, v in tech_info.items():
        st.write(f"**{k}**: {v['def']}")
    
    st.divider()
    
    st.write("### Lens Types")
    for k, v in lens_info.items():
        st.write(f"**{k}**: {v['def']}")
