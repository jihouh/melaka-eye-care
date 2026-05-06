import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Melaka Eye Care", layout="wide")

# Custom CSS for Mobile Optimization
st.markdown("""
    <style>
    /* Make tables more readable on small screens */
    .stTable { font-size: 0.9rem; overflow-x: auto; }
    /* Improve button and sidebar spacing for touch */
    .st-emotion-cache-16idsys p { font-size: 1.1rem; }
    </style>
    """, unsafe_allow_html=True)

st.title("👁️ Melaka Cataract Guide")

# Updated Hospital Data
hospital_data = {
    "ISEC Melaka (SSEC)": {"base": 3800, "rating": "4.9/5", "dr": "Dr. Robert Yeo", "contact": "+606-283 3510", "just": "Specialized eye-only facility; short wait times."},
    "Pantai Hospital Ayer Keroh": {"base": 4500, "rating": "4.8/5", "dr": "Dr. Liu Han Seng", "contact": "+606-231 9999", "just": "Strong post-op support and 24/7 ER facility."},
    "Oriental Melaka Straits": {"base": 4000, "rating": "4.8/5", "dr": "Dr. Ang Wen Jeat", "contact": "+606-315 8888", "just": "Modern equipment and highly rated for transparency."},
    "Putra Specialist Hospital": {"base": 3900, "rating": "4.7/5", "dr": "Datin Dr. Kasthuri", "contact": "+606-283 5888", "just": "Experienced consultants; trusted local reputation."},
    "Mahkota Medical Centre": {"base": 4600, "rating": "4.6/5", "dr": "Dr. Liau Kok Liang", "contact": "+606-285 2999", "just": "High surgical volume; comprehensive medical hub."}
}

# (Surgical and Lens definitions remain as before)
# ... [Insert tech_info and lens_info from previous code] ...

# --- SIDEBAR ---
st.sidebar.header("💰 Cost Estimator")
selected_hosp = st.sidebar.selectbox("Hospital", list(hospital_data.keys()))
num_eyes = st.sidebar.radio("Eyes", [1, 2])
# ... [Insert selection logic from previous code] ...

# --- MAIN CONTENT ---
tab1, tab2 = st.tabs(["🏥 Directory", "💡 Definitions"])

with tab1:
    st.subheader("Hospital Directory & Reviews")
    # Mapping for the table display
    h_list = []
    for k, v in hospital_data.items():
        h_list.append({
            "Hospital": k,
            "Contact": v["contact"],
            "Rating": v["rating"],
            "Why this rating?": v["just"]
        })
    st.table(pd.DataFrame(h_list))

    st.success(f"**Quick Call:** You can contact {selected_hosp} at **{hospital_data[selected_hosp]['contact']}** for a consultation.")

with tab2:
    st.markdown("### 💉 Surgical Techniques")
    # Simple list for mobile readability
    for k, v in tech_info.items():
        st.write(f"**{k}**: {v['def']}")
    
    st.markdown("---")
    st.markdown("### 👓 Lens Types")
    for k, v in lens_info.items():
        st.write(f"**{k}**: {v['def']}")
