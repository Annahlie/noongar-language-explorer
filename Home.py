import streamlit as st


st.set_page_config(
    page_title="Noongar Language Explorer",
    page_icon="📖",
    layout="centered"
)


# ---------------------------------------------------------
# Page introduction
# ---------------------------------------------------------

st.title("📖 Noongar Language Explorer")

st.write(
    "Explore a published Noongar wordlist through dictionary search, "
    "data exploration, and interactive learning."
)


# ---------------------------------------------------------
# Navigation
# ---------------------------------------------------------

st.subheader("Explore the application")

left_col, right_col = st.columns(2)

with left_col:
    with st.container(border=True):
        st.page_link(
            "pages/1_Dictionary.py",
            label="🔎  Dictionary",
            use_container_width=True
        )

    with st.container(border=True):
        st.page_link(
            "pages/3_Quiz.py",
            label="🧠  Quiz",
            use_container_width=True
        )

with right_col:
    with st.container(border=True):
        st.page_link(
            "pages/2_Data_Explorer.py",
            label="📊  Data Explorer",
            use_container_width=True
        )

    with st.container(border=True):
        st.page_link(
            "pages/4_About.py",
            label="ℹ️  About",
            use_container_width=True
        )