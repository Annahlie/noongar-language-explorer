import streamlit as st


# ---------------------------------------------------------
# Page heading
# ---------------------------------------------------------

st.title("ℹ️ About")

st.write(
    "Learn about the Noongar Language Explorer, its published "
    "language-data source, and the development of the application."
)


# ---------------------------------------------------------
# About tabs
# ---------------------------------------------------------

data_tab, cultural_tab, project_tab = st.tabs(
    [
        "📖 Data & Source",
        "Cultural Considerations",
        "🎓 Project"
    ]
)


# ---------------------------------------------------------
# Data and source
# ---------------------------------------------------------

with data_tab:
    st.subheader("Language Data")

    st.write(
        "The Noongar entries and English meanings displayed in this "
        "application come from the published Wirlomin Noongar Language "
        "and Stories Word List."
    )

    st.write(
        "The dataset used by this application contains "
        "**275 records** derived from the published wordlist."
    )

    st.link_button(
        "View the Wirlomin Word List",
        "https://www.wirlomin.com.au/language-list/",
        icon="🔗"
    )

    st.caption(
        "This student application is not affiliated with or endorsed by "
        "Wirlomin Noongar Language and Stories Inc."
    )


# ---------------------------------------------------------
# Cultural and language considerations
# ---------------------------------------------------------

with cultural_tab:
    st.subheader("Cultural and Language Considerations")

    st.write(
        "Noongar language content in this application is not generated "
        "by artificial intelligence. The application uses the published "
        "wordlist as its source for Noongar entries and English meanings."
    )

    st.write(
        "AI has been used to assist with programming, debugging, testing, "
        "and application development, but not to create Noongar words, "
        "translations, cultural information, or historical information."
    )

    st.warning(
        "The related-word groups used by the Data Explorer are created "
        "by the application for data exploration. They are not official "
        "Noongar linguistic or cultural categories."
    )


# ---------------------------------------------------------
# Project information
# ---------------------------------------------------------

with project_tab:
    st.subheader("Educational Purpose")

    st.write(
        "This application was created as a university programming project "
        "to demonstrate Python programming, data processing, algorithms, "
        "interactive interface design, testing, and data visualisation."
    )

    st.info(
        "The dictionary searches the published dataset and should not be "
        "treated as an AI translation service or as a replacement for "
        "authoritative language resources."
    )