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
    text-align: center;
}

.metric-number {
    font-size: 42px;
    font-weight: 700;
    color: #2C6E49;
}

.metric-label {
    font-size: 16px;
    color: #666;
}

.section-card {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 2px 12px rgba(0,0,0,0.08);
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

    try:
        st.image(
            "banner_fonteverde_esg.jpg",
            use_container_width=True
        )
    except:
        st.warning("Banner non disponibile")

    # CALCOLI BASE

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
        round((total_rows / 1000) * 100),
        100
    )

    criteria = 132
    evidences = int(total_rows * 0.1)
    gap = max(criteria - evidences, 0)

    st.markdown("<br>", unsafe_allow_html=True)

    # KPI

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{readiness}%</div>
            <div class="metric-label">Audit Readiness</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{criteria}</div>
            <div class="metric-label">Certification Criteria</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{evidences}</div>
            <div class="metric-label">Evidence</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{gap}</div>
            <div class="metric-label">Gap</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("##")

    # GRAFICI

    left, right = st.columns(2)

    with left:

        st.subheader("Compliance Overview")

        df_donut = pd.DataFrame({
            "Status": [
                "Validated",
                "Partial",
                "Review",
                "Missing"
            ],
            "Value": [54, 21, 15, 10]
        })

        fig = px.pie(
            df_donut,
            values="Value",
            names="Status",
            hole=0.65,
            color="Status",
            color_discrete_map={
                "Validated": "#2C6E49",
                "Partial": "#D4AF37",
                "Review": "#DCCDB3",
                "Missing": "#C94C4C"
            }
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("Performance by Area")

        df_bar = pd.DataFrame({

            "Area": [
                "Management",
                "Energy",
                "Water",
                "Waste",
                "Procurement",
                "Guest Awareness"
            ],

            "Score": [
                92,
