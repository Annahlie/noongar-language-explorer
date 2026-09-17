import streamlit as st


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Noongar Language Explorer",
    page_icon="📖",
    layout="wide"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background:
        radial-gradient(circle at 95% 7%, #FFE5A0 0%, #FFE5A0 9%, transparent 9.2%),
        radial-gradient(circle at 88% 36%, #C9E9FF 0%, #C9E9FF 12%, transparent 12.2%),
        radial-gradient(circle at 16% 5%, #BCEDE7 0%, #BCEDE7 10%, transparent 10.2%),
        linear-gradient(
            135deg,
            #FFFDF8 0%,
            #F1FBF9 55%,
            #FFF8E7 100%
        );
}


/* MAIN CONTENT WIDTH */
.block-container {
    max-width: 1200px;
    padding-top: 2.5rem;
    padding-bottom: 4rem;
}


/* SIDEBAR */
[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #DDF5F2 0%,
            #EFFAF8 100%
        );

    border-right: 1px solid #CAE5E1;
}


/* HEADINGS */
h1 {
    color: #092F63 !important;
    font-size: 4rem !important;
    font-weight: 850 !important;
    letter-spacing: -2px !important;
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
    line-height: 1.65;
}


/* ==================================================
   BORDERED STREAMLIT CONTAINERS
   ================================================== */

[data-testid="stVerticalBlockBorderWrapper"] {

    border-radius: 25px !important;

    border: 1px solid
        rgba(195, 225, 221, 0.9) !important;

    background:
        rgba(255, 255, 255, 0.88);

    box-shadow:
        0 12px 30px
        rgba(20, 70, 85, 0.08);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        border-color 0.25s ease;
}


[data-testid="stVerticalBlockBorderWrapper"]:hover {

    transform: translateY(-4px);

    border-color:
        #8ACFC8 !important;

    box-shadow:
        0 18px 38px
        rgba(20, 70, 85, 0.14);
}


/* ==================================================
   PAGE LINKS
   ================================================== */

[data-testid="stPageLink"] {

    background:
        linear-gradient(
            90deg,
            #087F8C,
            #08A095
        );

    border-radius: 50px;

    padding:
        0.65rem
        1rem;

    margin-top:
        0.5rem;

    text-align:
        center;

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}


[data-testid="stPageLink"]:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 7px 16px
        rgba(8, 127, 140, 0.23);
}


[data-testid="stPageLink"] a {

    color:
        white !important;

    font-weight:
        750 !important;

    text-decoration:
        none !important;
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


/* ==================================================
   METRICS / TEXT
   ================================================== */

[data-testid="stCaptionContainer"] {
    color: #536A78;
}


/* ==================================================
   MOBILE
   ================================================== */

@media (max-width: 800px) {

    h1 {
        font-size:
            2.8rem !important;
    }

}

</style>
""", unsafe_allow_html=True)


# ==================================================
# HERO
# ==================================================

with st.container(border=True):

    st.caption("●  ●  ●  ●  ●")

    st.title(
        "Noongar Language Explorer"
    )

    st.subheader(
        "Explore language through data "
        "and interactive learning"
    )

    st.write(
        "Search a published Noongar wordlist, "
        "explore patterns in the dataset, and "
        "test your knowledge through an "
        "interactive quiz."
    )

    st.write("")

    st.page_link(
        "pages/1_Dictionary.py",
        label="Start exploring  →"
    )


# ==================================================
# EXPLORE SECTION
# ==================================================

st.write("")
st.divider()

st.header(
    "✨ Explore the app"
)

st.write(
    "Choose a section below to start exploring."
)

st.write("")


col1, col2, col3 = st.columns(
    3,
    gap="medium"
)


# ==================================================
# DICTIONARY
# ==================================================

with col1:

    with st.container(
        border=True,
        height=330
    ):

        st.markdown(
            "# 🔎"
        )

        st.subheader(
            "Dictionary"
        )

        st.write(
            "Search the published wordlist "
            "and view English meanings."
        )

        st.write("")

        st.page_link(
            "pages/1_Dictionary.py",
            label="Open Dictionary  →"
        )


# ==================================================
# DATA EXPLORER
# ==================================================

with col2:

    with st.container(
        border=True,
        height=330
    ):

        st.markdown(
            "# 📊"
        )

        st.subheader(
            "Data Explorer"
        )

        st.write(
            "Explore patterns, statistics, "
            "and information in the dataset."
        )

        st.write("")

        st.page_link(
            "pages/2_Data_Explorer.py",
            label="Explore Data  →"
        )


# ==================================================
# QUIZ
# ==================================================

with col3:

    with st.container(
        border=True,
        height=330
    ):

        st.markdown(
            "# 🧠"
        )

        st.subheader(
            "Quiz"
        )

        st.write(
            "Test your knowledge with "
            "an interactive quiz."
        )

        st.write("")

        st.page_link(
            "pages/3_Quiz.py",
            label="Start Quiz  →"
        )


# ==================================================
# QUICK OVERVIEW
# ==================================================

st.write("")
st.divider()

st.header(
    "💡 What can you do?"
)

info1, info2, info3 = st.columns(3)


with info1:

    st.metric(
        label="Search",
        value="Dictionary"
    )


with info2:

    st.metric(
        label="Discover",
        value="Data"
    )


with info3:

    st.metric(
        label="Learn",
        value="Quiz"
    )


# ==================================================
# ABOUT
# ==================================================

st.write("")
st.divider()

st.header(
    "🌿 About this project"
)


with st.container(border=True):

    st.subheader(
        "Learn more about the project"
    )

    st.write(
        "This application uses a published "
        "Noongar wordlist to provide search, "
        "data exploration, and interactive "
        "learning tools."
    )

    st.write("")

    st.page_link(
        "pages/4_About.py",
        label=(
            "Learn about the dataset "
            "and its source  →"
        )
    )


# ==================================================
# FOOTER
# ==================================================

st.write("")
st.write("")

st.caption(
    "Noongar Language Explorer"
)