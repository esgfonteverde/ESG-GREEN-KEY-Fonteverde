import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Fonteverde Green Key Manager",
    page_icon="🌿",
    layout="wide"
)

# HEADER

col1, col2 = st.columns([1, 4])

with col1:
    try:
        st.image("logo_ftv.webp", width=180)
    except:
        st.write("🌿")

with col2:
    st.title("Fonteverde Thermal Spa Resort")
    st.subheader("Green Key Audit Manager")

st.divider()

FILE = "Green_Key_Master_Audit_File_Fonteverde_2026_2027.xlsx"

try:

    xls = pd.ExcelFile(FILE)

    sheets = xls.sheet_names

    pagina = st.sidebar.radio(
        "Menu",
        [
            "Dashboard",
            "Esplora Excel"
        ]
    )

    if pagina == "Dashboard":

        totale_righe = 0

        for foglio in sheets:
            try:
                df_temp = pd.read_excel(
                    FILE,
                    sheet_name=foglio
                )

                totale_righe += len(df_temp)

            except:
                pass

        st.subheader("Panoramica")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Fogli Excel",
            len(sheets)
        )

        c2.metric(
            "Record Totali",
            totale_righe
        )

        c3.metric(
            "Stato Sistema",
            "Online"
        )

        st.divider()

        st.subheader("Fogli disponibili")

        for foglio in sheets:
            st.success(foglio)

    elif pagina == "Esplora Excel":

       
