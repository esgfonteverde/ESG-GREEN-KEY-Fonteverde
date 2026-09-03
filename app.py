import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
    background: white;
    padding: 28px;
    border-radius: 22px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.08);
    text-align: left;
    transition: all 0.3s ease;
    height: 190px;
}

.metric-card:hover {
    transform: translateY(-6px);
    box-shadow: 0px 16px 35px rgba(0,0,0,0.15);
}

.card-green {
    border-top: 5px solid #2C6E49;
}

.card-gold {
    border-top: 5px solid #D4AF37;
}

.card-blue {
    border-top: 5px solid #3B82F6;
}

.card-red {
    border-top: 5px solid #C94C4C;
}

.metric-icon {
    font-size: 30px;
    margin-bottom: 12px;
}

.metric-number {
    font-size: 52px;
    font-weight: 700;
    color: #1F4D3A;
    line-height: 1;
}

.metric-label {
    margin-top: 12px;
    font-size: 14px;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #666;
}

.metric-sub {
    margin-top: 8px;
    font-size: 12px;
    color: #999;
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

    try:
        st.image(
            "banner_fonteverde_esg.jpg",
            use_container_width=True
        )
    except:
        st.warning("Banner non disponibile")

    total_rows = 0

    for sheet in sheet_names:

        try:
            temp = pd.read_excel(
                FILE,
                sheet_name=sheet
            )

            total_rows += len(temp)

        except:
            pass

    readiness = min(
        round((total_rows / 1000) * 100
             )
