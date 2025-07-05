import streamlit as st
import pandas as pd
from PIL import Image

# ---------------------------
# GEO-VEDA THEME CONFIG (auto applied from .streamlit/config.toml)
# ---------------------------
st.set_page_config(
    page_title="GEO-VEDA Dashboard",
    page_icon="🛰️",
    layout="wide"
)

# ---------------------------
# HEADER
# ---------------------------
st.markdown("""
<style>
.header-title {
    font-size:36px;
    color:#F57C00;
    font-weight:bold;
    margin-bottom:0px;
}
.sub-header {
    font-size:18px;
    color:#FFFFFF;
    margin-top:-10px;
    margin-bottom:10px;
}
.section-title {
    font-size:20px;
    color:#FFB74D;
    margin-top:30px;
    margin-bottom:10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="header-title">🛰️ GEO-VEDA: Unified Geospatial AI Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Automated Detection of Glacial Lakes, Road Networks & Urban Drainage using Satellite Imagery</p>', unsafe_allow_html=True)

# ---------------------------
# SIDEBAR - Input Options
# ---------------------------
with st.sidebar:
    st.header("🚀 Upload Satellite Image")
    uploaded_file = st.file_uploader("Choose an image (JPEG/PNG/TIF):", type=["jpg", "png", "tif"])
    st.markdown("📌 Supported: Sentinel-1/2, LISS-IV, CartoDEM")

    st.header("🗂️ Options")
    detect_glacial = st.checkbox("Detect Glacial Lakes", value=True)
    detect_roads = st.checkbox("Detect Roads", value=True)
    detect_drainage = st.checkbox("Detect Urban Drainage", value=True)

    st.header("🔁 Temporal Analysis")
    temporal_mode = st.radio("Enable time-series change detection?", ("No", "Yes"))

    st.header("🗣 Ask GEO-Astra")
    user_query = st.text_input("Type your question (e.g., 'Show lake change in Ladakh')")

# ---------------------------
# MAIN AREA
# ---------------------------
if uploaded_file:
    st.markdown('<p class="section-title">📷 Uploaded Image Preview</p>', unsafe_allow_html=True)
    st.image(uploaded_file, use_column_width=True, caption="Satellite Input Image")

    st.markdown('<p class="section-title">🧠 GEO-VEDA is Processing...</p>', unsafe_allow_html=True)
    with st.spinner("Extracting geospatial features..."):
        st.success("✅ Analysis complete!")

    st.markdown('<p class="section-title">📍 Detected Features Map</p>', unsafe_allow_html=True)
    st.image("output_map_placeholder.jpg", caption="Simulated Output Overlay", use_column_width=True)

    st.markdown('<p class="section-title">📊 Feature Detection Summary</p>', unsafe_allow_html=True)
    results_df = pd.DataFrame({
        "Feature": ["Glacial Lake", "Road Centerline", "Drainage Path"],
        "Detected": ["Yes" if detect_glacial else "No",
                     "Yes" if detect_roads else "No",
                     "Yes" if detect_drainage else "No"],
        "Confidence Score": ["0.94", "0.89", "0.91"]
    })
    st.dataframe(results_df, use_container_width=True)

    if temporal_mode == "Yes":
        st.markdown('<p class="section-title">📈 Temporal Change Map</p>', unsafe_allow_html=True)
        st.image("temporal_change_placeholder.jpg", caption="Simulated Change Detection", use_column_width=True)

    if user_query:
        st.markdown('<p class="section-title">🗣 GEO-Astra Says:</p>', unsafe_allow_html=True)
        st.info(f"‘{user_query}’ → This is a placeholder response. Change detection will be available in your final model.")

else:
    st.warning("📥 Please upload a satellite image from the sidebar to begin.")

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")
st.markdown('<center><small style="color:gray;">© 2025 | Team GEO-VEDA | Bharatiya Antariksh Hackathon</small></center>', unsafe_allow_html=True)
