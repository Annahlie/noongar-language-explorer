import streamlit as st

from src.data_loader import load_data
from src.search import search_english


# -----------------------------
# Page heading
# -----------------------------
st.title("🔎 English to Noongar Dictionary")

st.write(
    "Enter an English word or meaning to find matching Noongar entries."
)


# -----------------------------
# Load dataset
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
# Search input
# -----------------------------
query = st.text_input(
    "Enter an English word",
    placeholder="Example: water"
)


# -----------------------------
# Search button
# -----------------------------
if st.button("Search"):

    # Prevent blank searches
    if query.strip() == "":
        st.warning("Please enter an English word before searching.")

    else:
        # Run our English-to-Noongar search algorithm
        results = search_english(query, data)

        # No results found
        if len(results) == 0:
            st.error("No matching entries were found.")

        # Results found
        else:
            st.subheader("Matching Noongar entries")

            for result in results:
                st.write(
                    f"**{result['noongar']}**"
                )

                st.write(
                    f"English meaning: {result['english']}"
                )

                st.caption(
                    f"Source: {result['source_url']}"
                )

                st.divider()