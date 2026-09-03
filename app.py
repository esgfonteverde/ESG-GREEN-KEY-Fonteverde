import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# CONFIG
# ==========================================================

st.set_page_config(
    page_title="Fonteverde Green Key Manager",
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

st.sidebar.image("logo_ftv.webp", width=180)

st.sidebar.title("Green Key Manager")

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

except Exception as e:

    st.error("Errore caricamento Excel")

    st.stop()

# ==========================================================
# DASHBOARD
# ==========================================================

if menu == "🏠 Dashboard":

    # HERO
    st.image(
        "fonteverde_cover.jpg",
        use_container_width=True
    )

    st.title("Fonteverde Thermal Spa Resort")

    st.markdown(
        "### Green Key Audit Manager"
    )

    st.caption(
        "Programma Green Key 2026-2027"
    )

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
    imperative = 84
    evidences = int(total_rows * 0.1)
    gap = max(criteria - evidences, 0)

    st.markdown("<br>", unsafe_allow_html=True)

    # KPI

    c1,c2,c3,c4 = st.columns(4)

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
            <div class="metric-label">Criteri Totali</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{evidences}</div>
            <div class="metric-label">Evidenze</div>
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

        st.subheader("Conformità complessiva")

        df_donut = pd.DataFrame({
            "Stato":[
                "Validati",
                "Parziali",
                "Da verificare",
                "Assenti"
            ],
            "Valore":[54,21,15,10]
        })

        fig = px.pie(
            df_donut,
            values="Valore",
            names="Stato",
            hole=0.65,
            color="Stato",
            color_discrete_map={
                "Validati":"#2C6E49",
                "Parziali":"#D4AF37",
                "Da verificare":"#DCCDB3",
                "Assenti":"#C94C4C"
            }
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("Performance per Area")

        df_bar = pd.DataFrame({

            "Area":[
                "Gestione",
                "Energia",
                "Acqua",
                "Rifiuti",
                "Acquisti",
                "Ospiti"
            ],

            "Score":[
                92,
                86,
                81,
                88,
                63,
                74
            ]
        })

        fig2 = px.bar(
            df_bar,
            x="Score",
            y="Area",
            orientation="h",
            color="Score",
            color_continuous_scale="Greens"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # AZIONI

    st.markdown("##")

    a1,a2 = st.columns(2)

    with a1:

        st.subheader("🔥 Azioni Prioritarie")

        st.warning("Caricare evidenze criterio 4.3")
        st.warning("Aggiornare Policy Acquisti")
        st.warning("Completare informazione ospiti")
        st.warning("Aggiornare Green Team")

    with a2:

        st.subheader("📄 Evidenze Recenti")

        st.success("Sustainability_Policy.pdf")
        st.success("Green_Team_Meeting.pdf")
        st.success("Consumi_Acqua.xlsx")
        st.success("Monitoraggio_Energia.xlsx")

# ==========================================================
# EXCEL
# ==========================================================

elif menu == "📊 Esplora Excel":

    sheet = st.selectbox(
        "Seleziona foglio",
        sheet_names
    )

    df = pd.read_excel(
        FILE,
        sheet_name=sheet
    )

    search = st.text_input(
        "Ricerca"
    )

    if search:

        mask = df.astype(str).apply(
            lambda x:
            x.str.contains(
                search,
                case=False,
                na=False
            )
        ).any(axis=1)

        df = df[mask]

    st.dataframe(
        df,
        use_container_width=True,
        height=700
    )
