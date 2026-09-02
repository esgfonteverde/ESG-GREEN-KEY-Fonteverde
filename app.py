import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="ESG Audit Manager",
    page_icon="🌿",
    layout="wide"
)

# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

.block-container{
    padding-top:0rem;
}

.kpi-card{
    background:white;
    border-radius:20px;
    padding:25px;
    text-align:center;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
}

.kpi-number{
    font-size:42px;
    font-weight:700;
    color:#1F4D3A;
}

.kpi-label{
    font-size:14px;
    color:#666;
}

div[data-testid="stSidebar"]{
    background-color:#143225;
}

div[data-testid="stSidebar"] *{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR
# ==================================================

try:
    st.sidebar.image(
        "logo_ftv.webp",
        width=180
    )
except:
    st.sidebar.write("Fonteverde")

menu = st.sidebar.radio(
    "Navigazione",
    [
        "🏠 Dashboard",
        "📋 Certifications",
        "📁 Repository",
        "📊 Gap Analysis",
        "📈 ESG KPI",
        "📑 Reports"
    ]
)

# ==================================================
# DASHBOARD
# ==================================================

if menu == "🏠 Dashboard":

    try:
        st.image(
            "banner_fonteverde_esg.jpg",
            use_container_width=True
        )
    except:
        st.title("ESG AUDIT MANAGER")

    st.markdown("## ESG AUDIT 
