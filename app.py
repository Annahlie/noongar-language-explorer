import streamlit as st

from src.data_loader import load_data
from src.search import search_noongar


# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(
    page_title="Noongar Language Explorer",
    page_icon="📖",
    layout="centered"
)


# -----------------------------
# Load data
# -----------------------------
try:
    data = load_data()

except FileNotFoundError:
    st.error("The dataset could not be found.")
    st.stop()

except ValueError as error:
    st.error(f"Dataset error: {error}")
    st.stop()


# -----------------------------
# Page heading
# -----------------------------
st.title("📖 Noongar Language Explorer")

st.write(
    "Search a published Noongar wordlist and view the English meaning."
)


# -----------------------------
# Search input
# -----------------------------
query = st.text_input(
    "Enter a Noongar word",
    placeholder="Example: Kaya"
)


# -----------------------------
# Search button
# -----------------------------
if st.button("Search"):

    # Check for blank input
    if query.strip() == "":
        st.warning("Please enter a word before searching.")

    else:
        # Run our own search algorithm
        results = search_noongar(query, data)

        # If no matches were found
        if len(results) == 0:
            st.error("No matching words were found.")

        # If matches were found
        else:
            st.subheader("Search results")

            for result in results:
                st.write(
                    f"**{result['noongar']}** — {result['english']}"
                )

                st.caption(
                    f"Source: {result['source_url']}"
                )