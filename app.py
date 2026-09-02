import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -------------------------------------------------
# CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="ESG Audit Manager",
    page_icon="🌿",
    layout="wide"
)

# -------------------------------------------------
# CSS
# -------------------------------------------------

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
}

.kpi-card{
    background:white;
    padding:24px;
    border-radius:18px;
    box-shadow:0px 4px 18px rgba(0,0,0,0.08);
    text-align:center;
}

.kpi-number{
    font-size:42px;
    font-weight:700;
    color:#1f4d3a;
}

.kpi-label{
    color:#555;
    font-size:15px;
}

.section-box{
    background:white;
    padding:20px;
    border-radius:18px;
    box-shadow:0px 4px 18px rgba(0,0,0,0.08);
}

.action-item{
    padding:10px;
    border-bottom:1px solid #eee;
}

div[data-testid="stSidebar"]{
    background-color:#143225;
}

div[data-testid="stSidebar"] *{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.image(
    "logo_ftv.webp",
    width=180
)

page = st.sidebar.radio(
    "Navigazione",
    [
        "🏠 Dashboard",
        "📋 Certifications",
        "📁 Evidence Repository",
        "📊 Gap Analysis",
        "📈 ESG KPI",
        "✅ Corrective Actions",
        "📑 Reports"
    ]
)

# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------

if page == "🏠 Dashboard":

    st.image(
        "banner_fonteverde_esg.jpg",
        use_container_width=True
    )

    st.write("")

    # KPI CARDS

    c1, c2, c3, c4 = st.columns(4)

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

    col1, col2, col3 = st.columns([1.2,1,1])

    # ---------------------------------------------
    # GAUGE
    # ---------------------------------------------

    with col1:

        st.markdown(
            '<div class="section-box">',
            unsafe_allow_html=True
        )

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=87,
                number={"suffix":"%"},
                title={"text":"Audit Readiness"},
                gauge={
                    "axis":{"range":[0,100]},
                    "bar":{"color":"#1f4d3a"},
                    "steps":[
                        {"range":[0,60],"color":"#e74c3c"},
                        {"range":[60,85],"color":"#f1c40f"},
                        {"range":[85,100],"color":"#2ecc71"}
                    ]
                }
            )
        )

        fig.update_layout(
            height=350,
            margin=dict(l=10,r=10,t=50,b=10)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

    # ---------------------------------------------
    # DONUT
    # ---------------------------------------------

    with col2:

        donut = pd.DataFrame({
            "Status":[
                "Validati",
                "Parziali",
                "Da verificare",
                "Assenti"
            ],
            "Value":[54,21,15,10]
        })

        fig2 = px.pie(
            donut,
            values="Value",
            names="Status",
            hole=0.65
        )

        fig2.update_layout(
            title="Conformità Complessiva",
            height=350
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # ---------------------------------------------
    # PERFORMANCE
    # -------------
