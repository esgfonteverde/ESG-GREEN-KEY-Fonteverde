import streamlit as st
import pandas as pd
st.markdown("""
<style>

.main {
    background-color: #F8F6F0;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
}

.metric-big {
    font-size: 42px;
    font-weight: bold;
    color: #2C6E49;
}

.metric-label {
    color: #666;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)
st.set_page_config(
    page_title="Fonteverde Green Key Manager",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 Fonteverde Thermal Spa Resort")
st.subheader("Green Key Audit Manager")

try:
    st.image("logo_ftv.webp", width=250)
except:
    st.info("Logo non disponibile")

FILE = "Green_Key_Master_Audit_File_Fonteverde_2026_2027.xlsx"

try:

    xls = pd.ExcelFile(FILE)

    sheets = xls.sheet_names

    page = st.sidebar.selectbox(
        "Menu",
        [
            "Dashboard",
            "Esplora Excel"
        ]
    )

    if page == "Dashboard":

        st.header("Dashboard")

        total_rows = 0

        for sheet in sheets:

            try:
                df_temp = pd.read_excel(
                    FILE,
                    sheet_name=sheet
                )

                total_rows += len(df_temp)

            except:
                pass

        col1, col2 = st.columns(2)

        col1.metric(
            "Numero Fogli",
            len(sheets)
        )

        col2.metric(
            "Totale Record",
            total_rows
        )

        st.subheader("Fogli disponibili")

        for sheet in sheets:
            st.write("✅", sheet)

    elif page == "Esplora Excel":

        selected_sheet = st.selectbox(
            "Seleziona foglio",
            sheets
        )

        df = pd.read_excel(
            FILE,
            sheet_name=selected_sheet
        )

        st.write(f"Righe: {len(df)}")

        search = st.text_input(
            "Ricerca"
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

    st.error(str(e))
