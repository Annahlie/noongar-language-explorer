import streamlit as st


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="About | Noongar Language Explorer",
    page_icon="ℹ️",
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
                circle at 86% 35%,
                #FFE8A8 0%,
                #FFE8A8 10%,
                transparent 10.2%
            ),
            linear-gradient(
                135deg,
                #FFFDF8 0%,
                #F1FBF9 58%,
                #FFF9EA 100%
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

    h2 {
        color: #092F63 !important;
        font-weight: 800 !important;
    }

    h3 {
        color: #08747D !important;
        font-weight: 750 !important;
    }


    p {
        line-height: 1.7;
    }


    /* ==================================================
       CONTAINERS
       ================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 24px !important;

        background:
            rgba(255, 255, 255, 0.92);

        border:
            1px solid #D3E8E4 !important;

        box-shadow:
            0 10px 28px
            rgba(20, 70, 85, 0.07);
    }


    /* ==================================================
       LINK BUTTON
       ================================================== */

    [data-testid="stLinkButton"] a {
        background:
            linear-gradient(
                90deg,
                #087F8C,
                #08A095
            ) !important;

        color:
            white !important;

        border:
            none !important;

        border-radius:
            50px !important;

        font-weight:
            750 !important;

        padding:
            0.65rem 1.2rem !important;
    }


    /* ==================================================
       DIVIDERS
       ================================================== */

    hr {
        border:
            none !important;

        height:
            2px !important;

        background:
            linear-gradient(
                90deg,
                #FFC83D,
                #52BEB3,
                transparent
            ) !important;
    }


    /* Captions */
    [data-testid="stCaptionContainer"] {
        color: #60777C;
    }


    /* Mobile */
    @media (max-width: 800px) {

        h1 {
            font-size:
                2.8rem !important;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# PAGE HEADER
# ==================================================

with st.container(border=True):

    st.caption("ABOUT THE PROJECT")

    st.title("ℹ️ About")

    st.subheader(
        "Noongar Language Explorer"
    )

    st.write(
        "The Noongar Language Explorer is a student project "
        "developed for CITS1501 Introduction to Programming "
        "with Python."
    )

    st.write(
        "The application allows users to explore a published "
        "Noongar wordlist through dictionary search, data "
        "exploration, and an interactive quiz."
    )


# ==================================================
# LANGUAGE DATA
# ==================================================

st.write("")
st.divider()

st.header("📚 Language Data")


with st.container(border=True):

    st.write(
        "The Noongar entries and English meanings displayed "
        "in this application come from the published Wirlomin "
        "Noongar Language and Stories Word List."
    )

    st.write(
        "The dataset used by this application contains "
        "**275 records** derived from the published word list."
    )

    st.write("")

    st.link_button(
        "View the Wirlomin Word List  →",
        "https://www.wirlomin.com.au/language-list/"
    )


# ==================================================
# ABOUT THE SOURCE
# ==================================================

st.write("")
st.divider()

st.header("🌿 About the Source")


with st.container(border=True):

    st.write(
        "Wirlomin Noongar Language and Stories Inc. works to "
        "reclaim and support Wirlomin stories and dialect, "
        "maintain Noongar language, and support Wirlomin "
        "Noongar cultural heritage."
    )

    st.info(
        "This student application is not affiliated with or "
        "endorsed by Wirlomin Noongar Language and Stories Inc."
    )


# ==================================================
# CULTURAL AND LANGUAGE CONSIDERATIONS
# ==================================================

st.write("")
st.divider()

st.header("🤝 Cultural and Language Considerations")


with st.container(border=True):

    st.write(
        "Noongar language content in this application is not "
        "generated by artificial intelligence. The application "
        "uses the published wordlist as its source for Noongar "
        "entries and English meanings."
    )

    st.write(
        "AI has been used to assist with programming, debugging, "
        "testing, and application development, but not to create "
        "Noongar words, translations, cultural information, or "
        "historical information."
    )


# ==================================================
# APPLICATION-DEFINED ANALYSIS
# ==================================================

st.write("")
st.divider()

st.header("📊 Application-Defined Analysis")


with st.container(border=True):

    st.write(
        "The Data Explorer groups some records according to "
        "keywords found in their published English meanings."
    )

    st.warning(
        "These groups are created by the application for data "
        "exploration. They are not official Noongar linguistic "
        "or cultural categories."
    )


# ==================================================
# EDUCATIONAL PURPOSE
# ==================================================

st.write("")
st.divider()

st.header("🎓 Educational Purpose")


with st.container(border=True):

    st.write(
        "This application was created as a university programming "
        "project to demonstrate Python programming, data processing, "
        "algorithms, interactive interface design, testing, and "
        "data visualisation."
    )

    st.write(
        "The dictionary searches the published dataset and should "
        "not be treated as an AI translation service or as a "
        "replacement for authoritative language resources."
    )


# ==================================================
# PROJECT FEATURES
# ==================================================

st.write("")
st.divider()

st.header("✨ Explore the Project")


column1, column2, column3 = st.columns(
    3,
    gap="medium"
)


with column1:

    with st.container(
        border=True,
        height=210
    ):

        st.subheader("🔎 Dictionary")

        st.write(
            "Search English meanings and explore "
            "matching entries from the dataset."
        )


with column2:

    with st.container(
        border=True,
        height=210
    ):

        st.subheader("📊 Data Explorer")

        st.write(
            "Explore dataset statistics and "
            "application-defined word groups."
        )


with column3:

    with st.container(
        border=True,
        height=210
    ):

        st.subheader("🧠 Quiz")

        st.write(
            "Test recognition using questions "
            "generated from the published dataset."
        )


# ==================================================
# FOOTER
# ==================================================

st.write("")
st.divider()

st.caption(
    "Noongar Language Explorer • "
    "CITS1501 Introduction to Programming with Python"
)