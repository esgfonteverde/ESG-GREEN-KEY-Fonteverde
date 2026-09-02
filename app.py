import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# CONFIGURAZIONE PAGINA
# =====================================================

st.set_page_config(
    page_title="ESG Audit Manager",
    page_icon="🌿",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}

.kpi-card{
    background:white;
    border-radius:20px;
    padding:20px;
    text-align:center;
    box-shadow:0 3px 12px rgba(0,0,0,0.08);
}

.kpi-number{
    font-size:42px;
    font-weight:700;
    color:#1f4d3a;
}

.kpi-label{
    color:#666;
    font-size:14px;
}

div[data-testid="stSidebar"]{
    background:#143225;
}

div[data-testid="stSidebar"] *{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

try:
    st.sidebar.image("logo_ftv.webp", width=180)
except:
    st.sidebar.write("Fonteverde")

pagina = st.sidebar.radio(
    "Menu",
    [
        "🏠 Dashboard",
        "📋 Certifications",
        "📁 Repository",
        "📊 Gap Analysis",
        "📈 KPI ESG",
        "📑 Reports"
    ]
)

# =====================================================
# DASHBOARD
# =====================================================

if pagina == "🏠 Dashboard":

    # Banner

    try:
        st.image(
            "banner_fonteverde_esg.jpg",
            use_container_width=True
        )
    except:
        st.title("ESG AUDIT MANAGER")
        st.caption("Fonteverde Thermal Spa Resort")

    st.write("")

    # KPI

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="kpi-card">
        <div class="kpi-number">87%</div>
        <div class="kpi-label">Audit Readiness</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="kpi-card">
        <div class="kpi-number">132</div>
        <div class="kpi-label">Criteria</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="kpi-card">
        <div class="kpi-number">95</div>
        <div class="kpi-label">Evidence</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="kpi-card">
        <div class="kpi-number">37</div>
        <div class="kpi-label">Gap</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    left,right = st.columns(2)

    # ==========================================
    # GAUGE
    # ==========================================

    with left:

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=87,
                number={"suffix":"%"},
                title={"text":"Audit Readiness"},
                gauge={
                    "axis":{"range":[0,100]},
                    "bar":{"color":"#1f4d3a"}
                }
            )
