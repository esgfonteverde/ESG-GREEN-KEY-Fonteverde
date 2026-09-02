import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Green Key Audit Manager",
    page_icon="🌿",
    layout="wide"
)

FILE = "Green_Key_Master_Audit_File_Fonteverde_2026_2027.xlsx"

# HEADER

st.title("🌿 Green Key Audit Manager")
st.caption("Fonteverde Thermal Spa Resort | Green Key 2026-2027")

try:

    xls = pd.ExcelFile(FILE)

    sheet_names = xls.sheet_names

    st.sidebar.title("Navigazione")

    page = st.sidebar.radio(
        "Seleziona sezione",
        [
            "Dashboard",
            "Esplora Excel"
        ]
    )

    if page == "Dashboard":

        st.markdown("---")

        total_sheets = len(sheet_names)

        total_rows = 0

        for sheet in sheet_names:

            try:
                df_tmp = pd.read_excel(
                    FILE,
                    sheet_name=sheet
                )

                total_rows += len(df_tmp)

            except:
                pass

        readiness = min(
            round((total_rows / 1000) * 100),
            100
        )

        col1,col2,col3,col4 = st.columns(4)

        col1.metric(
            "Fogli Excel",
            total_sheets
        )

        col2.metric(
            "Righe Totali",
            total_rows
        )

        col3.metric(
            "Repository",
            "Attivo"
        )

        col4.metric(
            "Audit Readiness",
            f"{readiness}%"
        )

        st.markdown("---")

        left,right = st.columns([1,1])

        with left:

            st.subheader("Audit Readiness")

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
                    "Documentazione disponibile",
                    "Documentazione da verificare"
                ],
                "Valore":[
                    readiness,
                    100-readiness
                ]
            })

            fig = px.pie(
                chart,
                names="Stato",
                values="Valore",
                hole=0.6,
                color="Stato",
                color_discrete_map={
                    "Documentazione disponibile":"green",
                    "Documentazione da verificare":"lightgrey"
                }
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.markdown("---")

        st.subheader("📄 Fogli disponibili")

        for sheet in sheet_names:
            st.write("✅", sheet)

        st.markdown("---")

        st.subheader("🚀 Prossimi sviluppi")

        st.info("""
        Versione futura:

        • Repository documentale PDF

        • Collegamento Google Drive

        • Evidenze Green Key

        • KPI ESG

        • Gap Analysis

        • Gestione criteri

        • Workflow Audit
        """)

    elif page == "Esplora Excel":

        st.subheader("Esplora Workbook")

        selected_sheet = st.selectbox(
            "Seleziona foglio",
            sheet_names
        )

        df = pd.read_excel(
            FILE,
            sheet_name=selected_sheet
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

        search = st.text_input(
            "Cerca nel foglio"
        )

        if search:

            mask = df.astype(str).apply(
                lambda x: x.str.contains(
                    search,
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

    st.error("Errore durante il caricamento")

    st.code(str(e))
