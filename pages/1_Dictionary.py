import streamlit as st

from src.data_loader import load_data
from src.search import search_english


# ---------------------------------------------------------
# Page heading
# ---------------------------------------------------------

st.title("English to Noongar Dictionary")

st.write(
    "Search an English word or meaning to find matching "
    "Noongar entries from the published wordlist."
)


# ---------------------------------------------------------
# Load dataset
# ---------------------------------------------------------

try:
    data = load_data()

except FileNotFoundError:
    st.error("The dataset could not be found.")
    st.stop()

except ValueError as error:
    st.error(f"Dataset error: {error}")
    st.stop()


# ---------------------------------------------------------
# Search
# ---------------------------------------------------------

with st.form("dictionary_search_form"):
    search_col, button_col = st.columns([5, 1])

    with search_col:
        query = st.text_input(
            "English word or meaning",
            placeholder="Example: water",
            label_visibility="collapsed"
        )

    with button_col:
        search_clicked = st.form_submit_button(
            "Search",
            icon="🔎",
            type="primary",
            use_container_width=True
        )


# ---------------------------------------------------------
# Search results
# ---------------------------------------------------------

if search_clicked:
    if query.strip() == "":
        st.warning(
            "Please enter an English word or meaning before searching."
        )

    else:
        results = search_english(query, data)

        if len(results) == 0:
            st.info(
                f'No matching entries were found for "{query.strip()}".'
            )

        else:
            st.markdown(
                f"#### {len(results)} matching "
                f"{'entry' if len(results) == 1 else 'entries'}"
            )

            for result in results:
                with st.container(border=True):
                    word_col, meaning_col = st.columns([1, 2])

                    with word_col:
                        st.markdown(f"**{result['noongar']}**")

                    with meaning_col:
                        st.write(result["english"])

                    st.caption(
                        f"Source: {result['source_url']}"
                    )