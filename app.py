import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Fonteverde Green Key Manager",
    page_icon="🌿",
    layout="wide"
)

FILE = "Green_Key_Master_Audit_File_Fonteverde_2026_2027.xlsx"

# ===== LOGO E HEADER =====

col1, col2 = st.columns([1,4])

with col1:
    st.image("logo_fonteverde.webp", width=180)

with col2:
    st.title("🌿 Fonteverde Thermal Spa Resort")
    st.markdown("### Green Key Audit Manager")

st.divider()

try:

    xls = pd.ExcelFile(FILE)

    sheets = xls.sheet_names

    st.sidebar.title("🌿 Green Key Manager")

    page = st.sidebar.radio(
        "Menu",
        [
            "🏠 Dashboard",
            "📊 Esplora Excel"
        ]
    )

    if page == "🏠 Dashboard":

        total_rows = 0

        for sheet in sheets:
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

        st.subheader("Audit Readiness")

        c1,c2,c3,c4 = st.columns(4)

        c1.metric(
            "📄 Fogli",
            len(sheets)
        )

        c2.metric(
            "📋 Record",
            total_rows
        )

        c3.metric(
            "✅ Repository",
            "Attivo"
        )

        c4.metric(
            "🎯 Readiness",
            f"{readiness}%"
        )

        st.divider()

        left,right = st.columns([1,1])

        with left:

            if readiness >= 85:
                st.success("🟢 Ready for Audit")

            elif readiness >= 60:
                st.warning("🟡 In Preparazione")

            else:
                st.error("🔴 Da Completare")

            st.progress(readiness/100)

        with right:

            chart = pd.DataFrame({
                "Stato":[
                    "Completato",
                    "Da verificare"
                ],
                "Valore":[
                    readiness,
                    100-readiness
                ]
            })

            fig = px.pie(
                chart,
                values="Valore",
                names="Stato",
                hole=0.65,
                color="Stato",
                color_discrete_map={
                    "Completato":"#2C6E49",
                    "Da verificare":"#D9D9D9"
                }
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.divider()

        st.subheader("📂 Aree disponibili")

        cols = st.columns(3)

        for i, sheet in enumerate(sheets):
            cols[i % 3].info(sheet)

        st.divider()

        st.subheader("🚀 Roadmap")

        st.markdown("""
        - Repository PDF
        - Google Drive Integration
        - Evidenze Green Key
        - KPI ESG
        - Gap Analysis
        - Gestione Audit
        - Workflow Validazione
        """)

    if page == "📊 Esplora Excel":

        sheet = st.selectbox(
            "Foglio",
            sheets
        )

        df = pd.read_excel(
            FILE,
            sheet_name=sheet
        )

        c1,c2 = st.columns(2)

        c1.metric(
            "Righe",
            len(df)
        )

        c2.metric(
            "Colonne",
            len(df.columns)
        )

        ricerca = st.text_input(
            "🔍 Cerca"
        )

        if ricerca:

            mask = df.astype(str).apply(
                lambda x: x.str.contains(
                    ricerca,
                    case=False,
                    na=False
                )
            ).any(axis=1)

            df = df[mask]

        st.dataframe(
            df,
            use_container_width=True,
            height=600
        )

except Exception as e:

    st.error(str(e))
