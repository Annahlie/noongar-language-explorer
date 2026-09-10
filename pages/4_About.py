import streamlit as st

st.title("ℹ️ About")

st.write(
    "The Noongar Language Explorer is a student project developed "
    "for CITS1501 Introduction to Programming with Python."
)

st.write(
    "The application allows users to explore a published Noongar "
    "wordlist through dictionary search, data exploration, and an "
    "interactive quiz."
)

st.subheader("Language Data")

st.write(
    "The Noongar entries and English meanings displayed in this "
    "application come from the published Wirlomin Noongar Language "
    "and Stories Word List."
)

st.link_button(
    "View the Wirlomin Word List",
    "https://www.wirlomin.com.au/language-list/"
)

st.write(
    "The dataset used by this application contains 275 records "
    "derived from the published word list."
)

st.subheader("About the Source")

st.write(
    "Wirlomin Noongar Language and Stories Inc. works to reclaim "
    "and support Wirlomin stories and dialect, maintain Noongar "
    "language, and support Wirlomin Noongar cultural heritage."
)

st.write(
    "This student application is not affiliated with or endorsed by "
    "Wirlomin Noongar Language and Stories Inc."
)

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

st.subheader("Application-Defined Analysis")

st.write(
    "The Data Explorer groups some records according to keywords "
    "found in their published English meanings."
)

st.warning(
    "These groups are created by the application for data exploration. "
    "They are not official Noongar linguistic or cultural categories."
)

st.subheader("Educational Purpose")

st.write(
    "This application was created as a university programming project "
    "to demonstrate Python programming, data processing, algorithms, "
    "interactive interface design, testing, and data visualisation."
)

st.write(
    "The dictionary searches the published dataset and should not be "
    "treated as an AI translation service or as a replacement for "
    "authoritative language resources."
)