import streamlit as st


st.set_page_config(
    page_title="Noongar Language Explorer",
    page_icon="📖",
    layout="centered"
)


st.title("📖 Noongar Language Explorer")

st.write(
    "Explore a published Noongar wordlist through search, "
    "data analysis, and interactive learning."
)

st.subheader("What you can do")

st.write("🔎 Search Noongar words and view English meanings.")
st.write("📊 Explore patterns and statistics in the dataset.")
st.write("🧠 Test your knowledge with a quiz.")
st.write("ℹ️ Learn about the dataset and source.")