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
# CSS
# ==========================================================

st.markdown("""
<style>

.main {
    background-color:#F8F6F0;
}

.metric-card{
    background:white;
    padding:28px;
    border-radius:22px;
    box-shadow:0px 10px 25px rgba(0,0,0,0.08);
    text-align:left;
    transition:all .3s ease;
    height:190px;
}

.metric-card:hover{
    transform:translateY(-6px);
    box-shadow:0px 16px 35px rgba(0,0,0,0.15);
}

.card-green{
    border-top:5px solid #2C6E49;
}

.card-gold{
    border-top:5px solid #D4AF37;
}

.card-blue{
    border-top:5px solid #3B82F6;
}

.card-red{
    border-top:5px solid #C94C4C;
}

.metric-icon{
    font-size:30px;
    margin-bottom:12px;
}

.metric-number{
    font-size:52px;
    font-weight:700;
    color:#1F4D3A;
    line-height:1;
}

.metric-label{
    margin-top:12px;
    font-size:14px;
    letter-spacing:1px;
    text-transform:uppercase;
    color:#666;
}

.metric-sub{
    margin-top:8px;
    font-size:12px;
    color:#999;
}

.readiness-card{
    background:white;
    border-radius:24px;
    padding:50px;
    text-align:center;
    box-shadow:0px 10px 25px rgba(0,0,0,0.08);
    min-height:430px;
}

.readiness-title{
    font-size:18px;
    letter-spacing:2px;
    color:#777;
    text-transform:uppercase;
}

.readiness-score{
    font-size:90px;
    font-weight:700;
    color:#1F4D3A;
    margin-top:25px;
}

.readiness-status{
    font-size:24px;
    font-weight:600;
    margin-top:20px;
}

.readiness-sub{
    font-size:14px;
    color:#888;
    margin-top:25px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

try:
    st.sidebar.image(
        "logo_ftv.webp",
        width=180
    )
except:
    pass

st.sidebar.title("ESG Audit Manager")

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📋 Certifications",
        "📁 Evidence Repository",
        "📊 Gap Analysis",
        "📈 ESG KPI",
        "✅ Corrective Actions",
        "📑 Reports",
        "📊 Esplora Excel"
    ]
)

# ==========================================================
# LOAD EXCEL
# ==========================================================

try:
    xls = pd.ExcelFile(FILE)
    sheet_names = xls.sheet_names
except:
    st.error("Errore caricamento Excel")
    st.stop()

# ==========================================================
# DASHBOARD
# ============
