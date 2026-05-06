import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Melaka Cataract Guide 2026", layout="wide")

# --- CUSTOM CSS FOR MINIMALIST LOOK ---
# Fixed the 'unsafe_allow_html' argument here
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    h1 { color: #2c3e50; }
    </style>
    """, unsafe_allow_html=True)

st.title("👁️ Melaka Cataract Surgery Guide & Estimator")
st.write("A comprehensive guide for elderly cataract treatment in Melaka.")

# --- DATA DEFINITIONS ---
tech_options = {
    "Standard Phacoemulsification": 4200,
    "Laser-Assisted (FLACS)": 7500,
    "Extracapsular (ECCE)": 3200
}

lens_options = {
    "Monofocal (Standard)": 0,
    "Toric (Astigmatism)": 2000,
    "Multifocal/Trifocal": 4500,
    "EDOF": 3500
}

# --- SIDEBAR ESTIMATOR ---
st.sidebar.header("💰 Cost Estimator")
num_eyes = st.sidebar.radio("Number of Eyes", [1, 2], index=0)
selected_tech = st.sidebar.selectbox("Surgical Technique", list(tech_options.keys()))
selected_lens = st.sidebar.selectbox("Intraocular Lens (IOL) Type", list(lens_options.keys()))

# Calculation logic
base_price = tech_options[selected_tech]
lens_price = lens_options[selected_lens]
total_est = (base_price + lens_price) * num_eyes

st.sidebar.markdown("---")
st.sidebar.metric("Estimated Total", f"RM {total_est:,}")
st.sidebar.info("Prices are estimates. Request a 'Global Package' from the hospital for exact figures.")

# --- MAIN INTERFACE ---
tab1, tab2, tab3 = st.tabs(["🏥 Recommended Specialists", "📋 Detailed Costs", "🕒 Recovery & Tips"])

with tab1:
    st.subheader("Top Eye Specialists in Melaka")
    doctors_df = pd.DataFrame([
        {"Hospital": "ISEC Melaka", "Specialist": "Dr. Robert Yeo", "Rating": "4.9/5", "Notes": "Highly experienced, dedicated eye center."},
        {"Hospital": "Pantai Ayer Keroh", "Specialist": "Dr. Liu Han Seng", "Rating": "4.8/5", "Notes": "Great facilities, excellent post-op care."},
        {"Hospital": "Oriental Melaka", "Specialist": "Dr. Ang Wen Jeat", "Rating": "4.7/5", "Notes": "Modern medical center with all-in packages."},
        {"Hospital": "Putra Specialist", "Specialist": "Datin Dr. Kasthuri", "Rating": "4.8/5", "Notes": "Very thorough with elderly patients."}
    ])
    st.table(doctors_df)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 1. Technique Costs (Per Eye)")
        st.dataframe(pd.DataFrame(tech_options.items(), columns=["Technique", "Price (RM)"]))
    with col2:
        st.markdown("### 2. Lens Upgrades")
        st.dataframe(pd.DataFrame(lens_options.items(), columns=["Lens Type", "Add-on (RM)"]))
    
    st.markdown("### 3. Typical 'Hidden' Costs")
    st.write("""
    - **Pre-op Biometry (Measurement):** RM 200 - RM 400
    - **Post-op Medication (Drops):** RM 100 - RM 250
    - **Follow-up Consultations:** Usually RM 150 per visit (typically 3 visits needed).
    """)

with tab3:
    st.subheader("Post-Surgery Checklist")
    st.write("Important steps for elderly patients:")
    st.checkbox("Use eye shield during sleep for the first week.")
    st.checkbox("Avoid getting tap water in the eye for 1 month.")
    st.checkbox("Strictly follow the antibiotic/steroid eye drop schedule.")
    st.checkbox("No heavy lifting or intense exercise for at least 2 weeks.")
    st.warning("Contact the doctor immediately if there is sudden pain or loss of vision.")
