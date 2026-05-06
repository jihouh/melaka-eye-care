import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Melaka Cataract Guide 2026", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .stAlert { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("👁️ Melaka Cataract Guide & Cost Estimator")

# --- DATA DEFINITIONS ---

# Hospital Pricing Multipliers (Base Cost for Standard Care)
hospital_data = {
    "ISEC Melaka (SSEC)": {"base": 3800, "rating": "4.9/5", "dr": "Dr. Robert Yeo"},
    "Pantai Hospital Ayer Keroh": {"base": 4500, "rating": "4.8/5", "dr": "Dr. Liu Han Seng"},
    "Oriental Melaka Straits": {"base": 4000, "rating": "4.7/5", "dr": "Dr. Ang Wen Jeat"},
    "Putra Specialist Hospital": {"base": 3900, "rating": "4.8/5", "dr": "Datin Dr. Kasthuri"},
    "Mahkota Medical Centre": {"base": 4600, "rating": "4.6/5", "dr": "Dr. Liau Kok Liang"}
}

# Technique Definitions & Costs
tech_info = {
    "Standard Phaco": {
        "price": 0, 
        "def": "The gold standard. Uses ultrasound to break up the cataract. Requires a small manual incision."
    },
    "Laser-Assisted (FLACS)": {
        "price": 3000, 
        "def": "Uses a femtosecond laser for incisions and softening the cataract. Offers higher precision and faster healing."
    }
}

# Lens Definitions & Costs
lens_info = {
    "Monofocal (Standard)": {
        "price": 0, 
        "def": "Provides clear vision at one distance (usually far). Reading glasses will still be needed."
    },
    "Toric (Astigmatism)": {
        "price": 1800, 
        "def": "Designed for patients with astigmatism to ensure distance vision is sharp without glasses."
    },
    "Multifocal / Trifocal": {
        "price": 4000, 
        "def": "Provides clear vision at near, intermediate, and far distances. Aim is to be glasses-free."
    },
    "EDOF (Extended Depth)": {
        "price": 3200, 
        "def": "Provides a continuous range of high-quality vision from distance to intermediate (computer) work."
    }
}

# --- SIDEBAR ESTIMATOR ---
st.sidebar.header("📊 Personalized Estimator")

selected_hosp = st.sidebar.selectbox("Select Hospital/Doctor", list(hospital_data.keys()))
num_eyes = st.sidebar.radio("Number of Eyes", [1, 2], index=0)
selected_tech = st.sidebar.selectbox("Surgical Technique", list(tech_info.keys()))
selected_lens = st.sidebar.selectbox("Lens Type", list(lens_info.keys()))

# --- CALCULATION ---
h_base = hospital_data[selected_hosp]["base"]
t_extra = tech_info[selected_tech]["price"]
l_extra = lens_info[selected_lens]["price"]

total_per_eye = h_base + t_extra + l_extra
grand_total = total_per_eye * num_eyes

st.sidebar.markdown("---")
st.sidebar.metric("Estimated Total", f"RM {grand_total:,}")
st.sidebar.caption(f"Based on {selected_hosp} typical rates.")

# --- MAIN INTERFACE ---
tab1, tab2, tab3 = st.tabs(["📋 Selection Details", "🏥 Hospital Directory", "💡 Definitions Guide"])

with tab1:
    st.subheader("Your Selection Breakdown")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Hospital:** {selected_hosp}")
        st.write(f"**Lead Specialist:** {hospital_data[selected_hosp]['dr']}")
        st.write(f"**Technique:** {selected_tech}")
    with col2:
        st.write(f"**Lens Choice:** {selected_lens}")
        st.write(f"**Total Eyes:** {num_eyes}")
        st.write(f"**Est. Price per Eye:** RM {total_per_eye:,}")
    
    st.info("**Standard Package Inclusions:** Most Melaka hospitals include the surgeon fee, basic OT charges, and the first follow-up in this price.")

with tab2:
    st.subheader("Hospital & Specialist Overview")
    h_df = pd.DataFrame([
        {"Hospital": k, "Primary Specialist": v["dr"], "Rating": v["base"], "Base Price (Est)": f"RM {v['base']}"} 
        for k, v in hospital_data.items()
    ])
    st.table(h_df)

with tab3:
    st.subheader("Understanding Your Options")
    
    st.markdown("### 💉 Surgical Techniques")
    for k, v in tech_info.items():
        st.write(f"**{k}**: {v['def']}")
        
    st.markdown("---")
    
    st.markdown("### 👓 Lens Types (IOL)")
    for k, v in lens_info.items():
        st.write(f"**{k}**: {v['def']}")

    st.warning("Note: The best lens for you depends on your eye health (cornea and retina). Always consult the specialist before finalizing a lens type.")
