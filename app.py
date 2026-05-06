import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Melaka Eye Care", layout="wide")

# --- CUSTOM CSS FOR ANDROID FRIENDLINESS ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    /* Larger touch targets for mobile */
    .st-emotion-cache-16idsys p { font-size: 1.1rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. DATA DEFINITIONS (Must be defined before they are used) ---

hospital_data = {
    "ISEC Melaka (SSEC)": {
        "base": 3800, "rating": "4.9/5", "dr": "Dr. Robert Yeo", "contact": "+606-283 3510", 
        "just": "Specialized eye center; highly focused care and short wait times."
    },
    "Pantai Hospital Ayer Keroh": {
        "base": 4500, "rating": "4.8/5", "dr": "Dr. Liu Han Seng", "contact": "+606-231 9999", 
        "just": "Full-service hospital backup; excellent 24/7 post-op support."
    },
    "Oriental Melaka Straits": {
        "base": 4000, "rating": "4.8/5", "dr": "Dr. Ang Wen Jeat", "contact": "+606-315 8888", 
        "just": "Modern equipment; known for transparent billing packages."
    },
    "Putra Specialist Hospital": {
        "base": 3900, "rating": "4.7/5", "dr": "Datin Dr. Kasthuri", "contact": "+606-283 5888", 
        "just": "Strong local reputation; highly experienced senior consultants."
    },
    "Mahkota Medical Centre": {
        "base": 4600, "rating": "4.6/5", "dr": "Dr. Liau Kok Liang", "contact": "+606-285 2999", 
        "just": "Major medical hub; high success rates despite higher patient volume."
    }
}

tech_info = {
    "Standard Phaco": {
        "price": 0, 
        "def": "Standard ultrasound surgery. Safe, reliable, and uses a tiny manual incision."
    },
    "Laser-Assisted (FLACS)": {
        "price": 3000, 
        "def": "Uses a laser for extreme precision in incisions. Reduces ultrasound energy used on the eye."
    }
}

lens_info = {
    "Monofocal (Standard)": {
        "price": 0, 
        "def": "Fixed focus (usually for distance). You will likely still need reading glasses."
    },
    "Toric (Astigmatism)": {
        "price": 1800, 
        "def": "Corrects astigmatism. Ideal for patients wanting clear distance vision without glasses."
    },
    "Multifocal / Trifocal": {
        "price": 4000, 
        "def": "Provides near, intermediate, and far vision. The goal is to eliminate glasses entirely."
    },
    "EDOF (Extended Depth)": {
        "price": 3200, 
        "def": "Offers a continuous range of vision, particularly strong for computer and car dashboard distances."
    }
}

# --- 2. SIDEBAR ESTIMATOR ---
st.sidebar.header("💰 Cost Estimator")
selected_hosp = st.sidebar.selectbox("Hospital", list(hospital_data.keys()))
num_eyes = st.sidebar.radio("Eyes", [1, 2], index=0)
selected_tech = st.sidebar.selectbox("Technique", list(tech_info.keys()))
selected_lens = st.sidebar.selectbox("Lens Type", list(lens_info.keys()))

# Calculation
h_base = hospital_data[selected_hosp]["base"]
t_extra = tech_info[selected_tech]["price"]
l_extra = lens_info[selected_lens]["price"]
total_est = (h_base + t_extra + l_extra) * num_eyes

st.sidebar.markdown("---")
st.sidebar.metric("Estimated Total", f"RM {total_est:,}")
st.sidebar.caption(f"Contact {selected_hosp} at {hospital_data[selected_hosp]['contact']} for a firm quote.")

# --- 3. MAIN CONTENT ---
st.title("👁️ Melaka Cataract Guide")

tab1, tab2 = st.tabs(["🏥 Directory", "💡 Definitions"])

with tab1:
    st.subheader("Hospital Directory & Specialist Ratings")
    # Clean table for Android viewing
    h_list = []
    for k, v in hospital_data.items():
        h_list.append({
            "Hospital": k,
            "Contact": v["contact"],
            "Rating": v["rating"],
            "Justification": v["just"]
        })
    st.table(pd.DataFrame(h_list))

with tab2:
    st.subheader("Understand Your Options")
    
    st.markdown("### 💉 Surgical Techniques")
    for k, v in tech_info.items():
        st.write(f"**{k}**: {v['def']}")
    
    st.markdown("---")
    
    st.markdown("### 👓 Lens Types (IOL)")
    for k, v in lens_info.items():
        st.write(f"**{k}**: {v['def']}")
