import streamlit as st

st.set_page_config(
    page_title="ESG Audit Manager",
    page_icon="🌿",
    layout="wide"
)

st.title("ESG AUDIT MANAGER")

try:
    st.image(
        "banner_fonteverde_esg.jpg",
        use_container_width=True
    )
except:
    st.warning("Banner non trovato")

st.success("Dashboard in costruzione")
