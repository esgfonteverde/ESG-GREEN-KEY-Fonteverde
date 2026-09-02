import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Green Key Audit Manager",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 Green Key Audit Manager")
st.subheader("Fonteverde 2026-2027")

FILE = "Green_Key_Master_Audit_File_Fonteverde_2026_2027.xlsx"

try:

    xls = pd.ExcelFile(FILE)

    st.success("Excel caricato correttamente")

    st.write("Fogli trovati:")

    for sheet in xls.sheet_names:
        st.write("✅", sheet)

    selected_sheet = st.selectbox(
        "Seleziona foglio",
        xls.sheet_names
    )

    df = pd.read_excel(
        FILE,
        sheet_name=selected_sheet
    )

    st.metric(
        "Righe",
        len(df)
    )

    st.dataframe(
        df,
        use_container_width=True
    )

except Exception as e:

    st.error("Errore")

    st.code(str(e))
