import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# CONFIG
# ==========================================================

st.set_page_config(
    page_title="ESG Audit Manager",
    page_icon="🌿",
    layout="wide"
)

FILE = "Green_Key_Master_Audit_File_Fonteverde_2026_2027.xlsx"

# ==========================================================
# CSS CUSTOM
# ==========================================================

st.markdown("""
<style>

.main {
    background-color: #F8F6F0;
}

.metric-card {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 2px 12px rgba(0,0,0,0.08);
    text-align:center;
}

.metric-number {
    font-size:42px;
    font-weight:700;
    color:#2C6E49;
}

.metric-label {
    font-size:16px;
    color:#666;
}

.section-card {
    background-color:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 2px 12px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

try:
    st.sidebar.image("logo_ftv.webp", width=180)
except:
    pass

st.sidebar.title("ESG Audit Manager")

menu = st.sidebar.radio(
    "Menu",
    [
        "🏠 Dashboard",
        "📊 Esplora Excel"
    ]
)

# ==========================================================
# LOAD EXCEL
# ==========================================================

try:

    xls = pd.ExcelFile(FILE)

    sheet_names = xls.sheet_names

except Exception:

    st.error("Errore caricamento Excel")

    st.stop()

# ==========================================================
# DASHBOARD
# ==========================================================

if menu == "🏠 Dashboard":

    # HERO BANNER
