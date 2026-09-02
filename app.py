import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Green Key Audit Manager",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 Green Key Audit Manager")
st.subheader("Fonteverde 2026-2027")

file_excel = "Green_Key_Evidence_Pack_Fonteverde_2026_2027.xlsx"

try:

    criteria = pd.read_excel(
        file_excel,
        sheet_name="02_CRITERION_EVIDENCE"
    )

    total = len(criteria)

    mapped = len(
        criteria[
            criteria["Evidence Count"] > 0
        ]
    )

    gap = total - mapped

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "Totale criteri",
        total
    )

    c2.metric(
        "Con evidenze",
        mapped
    )

    c3.metric(
        "Gap",
        gap
    )

    st.dataframe(
        criteria,
        use_container_width=True
    )

except Exception as e:

    st.error(str(e))
