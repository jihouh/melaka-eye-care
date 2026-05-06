import streamlit as st
import pandas as pd

# 1. PAGE SETUP
st.set_page_config(page_title="Melaka Cataract Guide 2026", layout="wide")

# Custom CSS to ensure visibility on mobile (Android)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    /* Fix for mobile text scaling */
    div[data-testid="stMetricValue"] { font-size: 1.8rem; color: #2c3e50; }
    .stTabs [data-baseweb="tab"] { font-size: 1.1rem; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. COMPLETE DATASET (Restored Selection)
hospital_data = {
    "ISEC Melaka (SSEC)": {
        "dr": "Dr. Robert Yeo / Dr. Ang Wen Jeat",
        "rating": "⭐ 4.9/5",
        "contact": "+606-283 3510",
        "base": 3800,
        "just": "Dedicated eye center with 15 consultation rooms and specialized OT. Best for focused care."
    },
    "Pantai Hospital Ayer Keroh": {
        "dr": "Dr. Liu Han Seng",
        "rating": "⭐ 4.8/5",
        "contact": "+606-231 9999",
        "base": 4500,
        "just": "JCI accredited. Excellent for elderly with underlying health issues (heart/diabetes) needing full ER backup."
    },
    "Oriental Melaka Straits (OMSMC)": {
        "dr": "Dr. Ang Wen Jeat (Peter)",
        "rating": "⭐ 4.8/5",
        "contact": "+606-315 8888",
        "base": 4000,
        "just": "Modern beachside facility. Highly transparent with 'Fixed Price' cataract packages."
    },
    "Putra Specialist Hospital": {
        "dr": "Datin Dr. Kasthuri Nagaratnam",
        "rating": "⭐ 4.7/5",
        "contact": "+606-283 5888",
        "base": 3900,
        "just": "Very popular with local seniors; known for high-touch, compassionate bedside manner."
    },
    "Mahkota Medical Centre": {
        "dr": "Dr. Sendhil Kumar Somasundaram",
        "rating": "⭐ 4.6/5",
        "contact": "+606-285 2999",
        "base": 4600,
        "just": "High-volume center. Dr. Sendhil is also a Vitreo-Retinal specialist (ideal for complex retina issues)."
    }
}

tech_info = {
    "Standard Phaco": {"price": 0, "def": "Manual incision + ultrasound. Most common and highly successful."},
    "Laser-Assisted (FLACS)": {"price": 3000, "def": "Uses laser for precise incisions; gentler on the cornea."}
}

lens_info = {
    "Monofocal (Distance)": {"price": 0, "def": "Focuses at one distance. Reading glasses will be needed."},
    "Toric (Astigmatism)": {"price": 2000, "def": "Corrects astigmatism. Crisp distance vision without glasses."},
    "EDOF (Extended Range)": {"price": 3500, "def": "Great for distance + computer work. Few visual halos."},
    "Multifocal / Trifocal": {"price": 4500, "def": "Near, mid, and far vision. Goal: No glasses at all."}
}

# --- SIDEBAR: PERSONALIZED ESTIMATOR ---
st.sidebar.header("💰 Cost Estimator")
hosp_choice = st.sidebar.selectbox("Choose Hospital & Doctor", list(hospital_data.keys()))
num_eyes = st.sidebar.radio("Number of Eyes", [1, 2], horizontal=True)
tech_choice = st.sidebar.selectbox("Surgery Technique", list(tech_info.keys()))
lens_choice = st.sidebar.selectbox("Lens Technology", list(lens_info.keys()))

# Calculation logic
total_cost = (hospital_data[hosp_choice]["base"] + tech_info[tech_choice]["price"] + lens_info[lens_choice]["price"]) * num_eyes

st.sidebar.divider()
st.sidebar.metric("Estimated Total", f"RM {total_cost:,}")
st.sidebar.write(f"📞 Contact: {hospital_data[hosp_choice]['contact']}")

# --- MAIN CONTENT: MOBILE CARDS ---
st.title("👁️ Melaka Cataract Guide")

tab1, tab2 = st.tabs(["🏥 Specialist Directory", "💡 Understanding Choices"])

with tab1:
    st.info("Tap a card to see doctor details. Ratings are based on 2026 patient satisfaction scores.")
    for name, info in hospital_data.items():
        with st.expander(f"{info['rating']} - {info['dr']} ({name})"):
            st.markdown(f"**Specialist:** {info['dr']}")
            st.markdown(f"**Justification:** {info['just']}")
            st.markdown(f"**Contact:** [Call {info['contact']}](tel:{info['contact'].replace(' ', '')})")
            st.write(f"**Est. Base Price:** RM {info['base']:,}")

with tab2:
    st.subheader("What are you paying for?")
    st.markdown("### Surgical Techniques")
    for k, v in tech_info.items():
        st.write(f"**{k}**: {v['def']}")
    
    st.divider()
    
    st.markdown("### Lens (IOL) Types")
    for k, v in lens_info.items():
        st.write(f"**{k}**: {v['def']}")
