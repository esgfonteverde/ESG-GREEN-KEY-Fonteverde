import streamlit as st

st.set_page_config(
    page_title="Test",
    layout="wide"
)

st.title("TEST")

st.write("App avviata correttamente")

try:
    st.image(
        "banner_fonteverde_esg.jpg",
        use_container_width=True
    )

    st.success("Banner OK")

except Exception as e:

    st.error(f"Banner errore: {e}")

try:

    st.image(
        "logo_ftv.webp",
        width=200
    )

    st.success("Logo OK")

except Exception as e:

    st.error(f"Logo errore: {e}")
