import streamlit as st

# Page Configuration
st.set_page_config(page_title="Melaka Cataract Guide 2026", layout="wide")

# --- CUSTOM CSS FOR MINIMALIST LOOK ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_index=True)

st.title("👁️ Melaka Cataract Surgery Guide & Estimator")
st.write("A comprehensive guide for elderly cataract treatment in Melaka (Updated 2026).")

# --- SIDEBAR ESTIMATOR ---
st.sidebar.header("💰 Cost Estimator")
num_eyes = st.sidebar.radio("Number of Eyes", [1, 2])
tech = st.sidebar.selectbox("Surgical Technique", 
    ["Standard Phacoemulsification", "Laser-Assisted (FLACS)", "Extracapsular (ECCE)"])
lens = st.sidebar.selectbox("Intraocular Lens (IOL) Type", 
    ["Monofocal (Standard)", "Toric (Astigmatism)", "Multifocal/Trifocal", "EDOF"])

# Pricing Logic
base_costs = {"Standard Phacoemulsification": 4200, "Laser-Assisted (FLACS)": 7500, "Extracapsular (ECCE)": 3200}
lens_add = {"Monofocal (Standard)": 0, "Toric (Astigmatism)": 2000, "Multifocal/Trifocal": 4500, "EDOF": 3500}

total_est = (base_costs[tech] + lens_add[lens]) * num_eyes

st.sidebar.metric("Estimated Total (RM)", f"RM {total_est:,}")
st.sidebar.info("Note: Prices are estimates based on private hospital averages in Melaka.")

# --- MAIN CONTENT ---
tab1, tab2, tab3 = st.tabs(["🏥 Recommended Hospitals", "📋 Cost Breakdown", "💡 Tips for Elderly"])

with tab1:
    st.subheader("Top Eye Specialists & Centers")
    hospitals = [
        {"Name": "ISEC Melaka (SSEC)", "Doctor": "Dr. Robert Yeo / Dr. Ang Wen Jeat", "Rating": "4.9/5", "Notes": "Dedicated eye center. High patient satisfaction."},
        {"Name": "Pantai Hospital Ayer Keroh", "Doctor": "Dr. Liu Han Seng", "Rating": "4.8/5", "Notes": "Full-service hospital. Excellent post-op nursing."},
        {"Name": "OMSMC (Oriental)", "Doctor": "Dr. Peter Ang", "Rating": "4.7/5", "Notes": "Modern facilities, popular for medical tourism."},
        {"Name": "Putra Specialist Hospital", "Doctor": "Datin Dr. Kasthuri", "Rating": "4.8/5", "Notes": "Highly experienced with elderly patients."}
    ]
    for h in hospitals:
        with st.expander(f"{h['Name']} - ⭐ {h['Rating']}"):
            st.write(f"**Lead Specialist:** {h['Doctor']}")
            st.write(f"**Sentiment:** {h['Notes']}")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 1. Technique Costs")
        st.table({
            "Technique": ["Standard Phaco", "Laser-Assisted", "ECCE"],
            "Avg. Cost (RM)": ["4,200", "7,500", "3,200"]
        })
    with col2:
        st.markdown("### 2. Lens Upgrades")
        st.table({
            "Lens Type": ["Monofocal", "Toric", "Multifocal", "EDOF"],
            "Add-on (RM)": ["+0", "+2,000", "+4,500", "+3,500"]
        })
    
    st.markdown("### 3. Typical 'Hidden' Costs")
    st.write("""
    *   **Pre-op Biometry:** RM 200 - RM 400 (Eye measurement)
    *   **Post-op Meds:** RM 100 - RM 250 (Eye drops)
    *   **Follow-up visits:** RM 150 per session (Usually 3 visits needed)
    *   **Anesthesia:** Usually local/topical is included; 'Sleep' sedation adds RM 800+.
    """)

with tab3:
    st.success("**Elderly Care Checklist:**\n1. Ensure the patient has a caregiver for the first 24 hours.\n2. Avoid traditional 'jamu' or herbal eye drops post-surgery.\n3. Request a 'Global Package' quote to avoid surprise bills.")
