import streamlit as st

from src.data_loader import load_data
from src.search import search_noongar


st.title("🔎 Dictionary")

st.write(
    "Search the published Noongar wordlist and view English meanings."
)


# Load the dataset
try:
    data = load_data()

except FileNotFoundError:
    st.error("The dataset could not be found.")
    st.stop()

except ValueError as error:
    st.error(f"Dataset error: {error}")
    st.stop()


# Search box
query = st.text_input(
    "Enter a Noongar word",
    placeholder="Example: Kaya"
)


if st.button("Search"):

    if query.strip() == "":
        st.warning("Please enter a word before searching.")

    else:
        results = search_noongar(query, data)

        if len(results) == 0:
            st.error("No matching words were found.")

        else:
            st.subheader("Search results")

            for result in results:
                st.write(
                    f"**{result['noongar']}** — {result['english']}"
                )

                st.caption(
                    f"Source: {result['source_url']}"
                )