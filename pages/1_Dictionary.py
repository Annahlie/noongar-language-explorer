import streamlit as st

from src.data_loader import load_data
from src.search import search_english


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Dictionary | Noongar Language Explorer",
    page_icon="🔎",
    layout="wide"
)


# ==================================================
# CUSTOM STYLING
# ==================================================

st.markdown(
    """
    <style>

    /* Page background */
    .stApp {
        background:
            radial-gradient(
                circle at 92% 8%,
                #BCEDE7 0%,
                #BCEDE7 9%,
                transparent 9.2%
            ),
            radial-gradient(
                circle at 84% 35%,
                #D6F3EF 0%,
                #D6F3EF 12%,
                transparent 12.2%
            ),
            linear-gradient(
                135deg,
                #FFFDF8 0%,
                #F0FBF9 60%,
                #F7FCFB 100%
            );
    }


    /* Main content */
    .block-container {
        max-width: 1050px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }


    /* Sidebar */
    [data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #DDF5F2 0%,
                #EFFAF8 100%
            );

        border-right: 1px solid #CAE5E1;
    }


    /* Headings */
    h1 {
        color: #092F63 !important;
        font-weight: 850 !important;
        letter-spacing: -1.5px;
    }

    h2,
    h3 {
        color: #08747D !important;
        font-weight: 750 !important;
    }


    /* Normal text */
    p {
        line-height: 1.65;
    }


    /* Containers */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 22px !important;

        background:
            rgba(255, 255, 255, 0.92);

        border:
            1px solid #CFE8E4 !important;

        box-shadow:
            0 10px 28px
            rgba(20, 70, 85, 0.07);
    }


    /* Text input */
    [data-testid="stTextInput"] input {
        border-radius: 14px;

        border:
            1px solid #B9DCD7;

        padding:
            0.75rem;
    }


    [data-testid="stTextInput"] input:focus {
        border-color:
            #07828C;

        box-shadow:
            0 0 0 1px #07828C;
    }


    /* Search button */
    .stButton > button {
        width: 100%;

        background:
            linear-gradient(
                90deg,
                #087F8C,
                #08A095
            );

        color: white;

        border: none;

        border-radius: 50px;

        padding:
            0.7rem 1.4rem;

        font-weight: 750;

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }


    .stButton > button:hover {
        color: white;

        transform:
            translateY(-2px);

        box-shadow:
            0 8px 18px
            rgba(8, 127, 140, 0.22);
    }


    /* Dividers */
    hr {
        border: none !important;

        height: 1px !important;

        background:
            linear-gradient(
                90deg,
                #7DCFC6,
                #D8EEEB,
                transparent
            ) !important;
    }


    /* Captions */
    [data-testid="stCaptionContainer"] {
        color: #60777C;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# PAGE HEADER
# ==================================================

with st.container(border=True):

    st.caption("DICTIONARY")

    st.title("🔎 English to Noongar Dictionary")

    st.write(
        "Search the published wordlist by entering an English "
        "word or meaning below."
    )


# ==================================================
# LOAD DATASET
# ==================================================

try:
    data = load_data()

except FileNotFoundError:
    st.error(
        "The dataset could not be found."
    )
    st.stop()

except ValueError as error:
    st.error(
        f"Dataset error: {error}"
    )
    st.stop()


# ==================================================
# SEARCH AREA
# ==================================================

st.write("")

st.subheader("Search the wordlist")

with st.container(border=True):

    query = st.text_input(
        "Enter an English word or meaning",
        placeholder="Example: water"
    )

    search_clicked = st.button(
        "🔎 Search Dictionary"
    )


# ==================================================
# SEARCH RESULTS
# ==================================================

if search_clicked:

    # Remove unnecessary spaces from the query
    cleaned_query = query.strip()

    # ----------------------------------------------
    # BLANK SEARCH
    # ----------------------------------------------

    if cleaned_query == "":

        st.warning(
            "Please enter an English word before searching."
        )


    # ----------------------------------------------
    # VALID SEARCH
    # ----------------------------------------------

    else:

        results = search_english(
            cleaned_query,
            data
        )


        # ------------------------------------------
        # NO RESULTS
        # ------------------------------------------

        if len(results) == 0:

            st.error(
                f'No matching entries were found for '
                f'"{cleaned_query}".'
            )

            st.info(
                "Try another English word or a shorter search term."
            )


        # ------------------------------------------
        # RESULTS FOUND
        # ------------------------------------------

        else:

            st.write("")

            st.subheader(
                "Matching Noongar entries"
            )

            st.success(
                f"Found {len(results)} matching "
                f"{'entry' if len(results) == 1 else 'entries'}."
            )


            # Display every matching entry
            for result in results:

                with st.container(border=True):

                    st.subheader(
                        result["noongar"]
                    )

                    st.write(
                        f"**English meaning:** "
                        f"{result['english']}"
                    )

                    st.caption(
                        f"Source: {result['source_url']}"
                    )


# ==================================================
# HELP SECTION
# ==================================================

st.write("")
st.divider()

st.subheader("💡 Search tips")

with st.container(border=True):

    st.write(
        "Enter an English word or part of a meaning "
        "to search the published wordlist."
    )

    st.write(
        "For example, you could search for **water** "
        "to find entries whose English meaning matches "
        "your search."
    )


# ==================================================
# FOOTER
# ==================================================

st.write("")
st.caption(
    "Noongar Language Explorer • Dictionary"
)