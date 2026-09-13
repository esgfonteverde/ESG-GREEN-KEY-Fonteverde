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

FILE = "Green_Key_Criteria_Master_Fonteverde.xlsx"

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

.readiness-card {
    background: white;
    border-radius: 24px;
    padding: 50px;
    text-align: center;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.08);
    min-height: 430px;
}

.readiness-title {
    font-size: 16px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #888;
}

.readiness-score {
    font-size: 96px;
    font-weight: 700;
    color: #1F4D3A;
    line-height: 1;
    margin-top: 20px;
}

.readiness-status {
    font-size: 28px;
    font-weight: 600;
    margin-top: 20px;
}

.readiness-sub {
    margin-top: 20px;
    color: #888;
    font-size: 14px;
}

.repo-card {
    background:white;
    border-radius:14px;
    padding:14px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# LOAD EXCEL
# ==========================================================

try:

    df_master = pd.read_excel(
        FILE,
        sheet_name="01_CRITERI_GREEN_KEY"
    )

except Exception as e:

    st.error(f"Errore caricamento file Excel: {e}")
    st.stop()

# ==========================================================
# KPI REALI
# ==========================================================

criteria = len(df_master)

completed = len(
    df_master[
        df_master["Stato"]
        .astype(str)
        .str.upper()
        == "COMPLETATO"
    ]
)

in_progress = len(
    df_master[
        df_master["Stato"]
        .astype(str)
        .str.upper()
        == "IN CORSO"
    ]
)

not_started = len(
    df_master[
        df_master["Stato"]
        .astype(str)
        .str.upper()
        == "NON AVVIATO"
    ]
)

evidences = len(
    df_master[
        df_master["Evidenza Presente"]
        .astype(str)
        .str.upper()
        == "SI"
    ]
)

gap = criteria - completed

readiness = 0

if criteria > 0:
    readiness = round(
        (completed / criteria) * 100,
        1
    )

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
        "📁 Evidence Repository",
        "📊 Gap Analysis",
        "✅ Corrective Actions",
        "📊 Esplora Excel"
    ]
)

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

    st.markdown("##")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.markdown(f"""
        <div class="metric-card card-green">
            <div class="metric-icon">📊</div>
            <div class="metric-number">{readiness}%</div>
            <div class="metric-label">Audit Readiness</div>
            <div class="metric-sub">Real data</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown(f"""
        <div class="metric-card card-gold">
            <div class="metric-icon">✅</div>
            <div class="metric-number">{criteria}</div>
            <div class="metric-label">Criteria</div>
            <div class="metric-sub">Total criteria</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown(f"""
        <div class="metric-card card-blue">
            <div class="metric-icon">📁</div>
            <div class="metric-number">{evidences}</div>
            <div class="metric-label">Evidence</div>
            <div class="metric-sub">Evidence present</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:

        st.markdown(f"""
        <div class="metric-card card-red">
            <div class="metric-icon">⚠️</div>
            <div class="metric-number">{gap}</div>
            <div class="metric-label">Gap</div>
            <div class="metric-sub">Not completed</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("##")

    left, right = st.columns(2)

  with left:

    st.metric(
        label="Audit Readiness",
        value=f"{readiness}%"
    )

    if readiness >= 85:
        st.success("READY ✅")

    elif readiness >= 60:
        st.warning("ATTENTION ⚠️")

    else:
        st.error("CRITICAL 🔴")

        st.markdown(f"""
        <div class="readiness-card">

            <div class="readiness-title">
                Audit Readiness
            </div>

            <div class="readiness-score">
                {readiness}%
            </div>

            <div class="readiness-status"
                 style="color:{color};">
                {status}
            </div>

            <div class="readiness-sub">
                Based on completed criteria
            </div>

        </div>
        """, unsafe_allow_html=True)

    with right:

        donut = pd.DataFrame({
            "Status": [
                "Completed",
                "In Progress",
                "Not Started"
            ],
            "Value": [
                completed,
                in_progress,
                not_started
            ]
        })

        fig = px.pie(
            donut,
            values="Value",
            names="Status",
            hole=0.75
        )

        fig.update_layout(height=430)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# ==========================================================
# EVIDENCE REPOSITORY
# ==========================================================

elif menu == "📁 Evidence Repository":

    st.title("📁 Evidence Repository")

    search = st.text_input(
        "🔍 Search evidence"
    )

    evidenze = df_master[
        df_master["Nome Evidenza"]
        .notna()
    ]

    if search:

        evidenze = evidenze[
            evidenze["Nome Evidenza"]
            .astype(str)
            .str.contains(
                search,
                case=False,
                na=False
            )
        ]

    for _, row in evidenze.iterrows():

        nome = row["Nome Evidenza"]
        criterio = row["ID"]
        area = row["Area"]

        st.markdown(
            f"""
            <div class="repo-card">
            📄 <b>{nome}</b><br>
            Criterion: {criterio}<br>
            Area: {area}
            </div>
            """,
            unsafe_allow_html=True
        )

# ==========================================================
# GAP ANALYSIS
# ==========================================================

elif menu == "📊 Gap Analysis":

    st.title("📊 Gap Analysis")

    gaps = df_master[
        df_master["Stato"]
        .astype(str)
        .str.upper()
        != "COMPLETATO"
    ]

    st.metric(
        "Open Gaps",
        len(gaps)
    )

    st.dataframe(
        gaps[
            [
                "ID",
                "Area",
                "Criterio",
                "Stato",
                "Responsabile"
            ]
        ],
        use_container_width=True
    )

# ==========================================================
# CORRECTIVE ACTIONS
# ==========================================================

elif menu == "✅ Corrective Actions":

    st.title("✅ Corrective Actions")

    gaps = df_master[
        df_master["Stato"]
        .astype(str)
        .str.upper()
        != "COMPLETATO"
    ]

    for _, row in gaps.iterrows():

        st.warning(
            f"{row['ID']} - {row['Criterio']} "
            f"(Owner: {row['Responsabile']})"
        )

# ==========================================================
# EXPLORA EXCEL
# ==========================================================

elif menu == "📊 Esplora Excel":

    sheet = st.selectbox(
        "Seleziona foglio",
        ["01_CRITERI_GREEN_KEY"]
    )

    st.dataframe(
        df_master,
        use_container_width=True,
        height=700
    )
