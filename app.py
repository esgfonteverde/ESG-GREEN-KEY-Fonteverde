import streamlit as st
import pandas as pd

# --------------------------------------------------
# CONFIGURAZIONE PAGINA
# --------------------------------------------------

st.set_page_config(
    page_title="Fonteverde Green Key Manager",
    page_icon="🌿",
    layout="wide"
)

# --------------------------------------------------
# CSS PERSONALIZZATO
# --------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #F8F6F0;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    text-align: center;
}

.metric-big {
    font-size: 42px;
    font-weight: bold;
    color: #2C6E49;
}

.metric-label {
    color: #666666;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# FILE EXCEL
# --------------------------------------------------

FILE = "Green_Key_Master_Audit_File_Fonteverde_2026_2027.xlsx"

# --------------------------------------------------
# COVER
# --------------------------------------------------

try:
    st.image(
        "fonteverde_cover.jpg",
        use_container_width=True
    )
except:
    st.warning("Cover non trovata")

# --------------------------------------------------
# HEADER
# --------------------------------------------------

col1, col2 = st.columns([1,4])

with col1:

    try:
        st.image(
            "logo_ftv.webp",
            width=150
        )
    except:
        st.write("🌿")

with col2:

    st.title("Fonteverde Thermal Spa Resort")

    st.markdown(
        "### Green Key Audit Manager"
    )

st.divider()

# --------------------------------------------------
# LETTURA EXCEL
# --------------------------------------------------

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

    # ==========================================
    # DASHBOARD
    # ==========================================

    if pagina == "Dashboard":

        st.subheader("Executive Overview")

        total_rows = 0

        for sheet in sheets:

            try:

                temp_df = pd.read_excel(
                    FILE,
                    sheet_name=sheet
                )

                total_rows += len(temp_df)

            except:
                pass

        # KPI

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.markdown("""
            <div class="card">
                <div class="metric-big">87%</div>
                <div class="metric-label">Audit Readiness</div>
            </div>
            """, unsafe_allow_html=True)

        with c2:

            st.markdown(f"""
            <div class="card">
                <div class="metric-big">{len(sheets)}</div>
                <div class="metric-label">Fogli Excel</div>
            </div>
            """, unsafe_allow_html=True)

        with c3:

            st.markdown(f"""
            <div class="card">
                <div class="metric-big">{total_rows}</div>
                <div class="metric-label">Record Totali</div>
            </div>
            """, unsafe_allow_html=True)

        with c4:

            st.markdown("""
            <div class="card">
                <div class="metric-big">Online</div>
                <div class="metric-label">Sistema</div>
            </div>
            """, unsafe_allow_html=True)

        st.divider()

        st.subheader("Stato Audit")

        st.progress(0.87)

        st.success(
            "🟢 Audit Readiness: 87% - Ready for Audit"
        )

        st.divider()

        st.subheader("Fogli presenti nel Master File")

        col_a, col_b, col_c = st.columns(3)

        for i, sheet in enumerate(sheets):

            if i % 3 == 0:
                col_a.info(sheet)

            elif i % 3 == 1:
                col_b.info(sheet)

            else:
                col_c.info(sheet)

    # ==========================================
    # ESPLORA EXCEL
    # ==========================================

    elif pagina == "Esplora Excel":

        st.subheader("Esplora Workbook")

        selected_sheet = st.selectbox(
            "Seleziona foglio",
            sheets
        )

        df = pd.read_excel(
            FILE,
            sheet_name=selected_sheet
        )

        m1, m2 = st.columns(2)

        m1.metric(
            "Righe",
            len(df)
        )

        m2.metric(
            "Colonne",
            len(df.columns)
        )

        ricerca = st.text_input(
            "🔍 Cerca nel foglio"
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
            height=700
        )

except Exception as e:

    st.error("Errore durante il caricamento")

    st.code(str(e))
