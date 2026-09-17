import pandas as pd
import streamlit as st

from src.data_loader import load_data
from src.analysis import group_entries, count_groups


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Data Explorer | Noongar Language Explorer",
    page_icon="📊",
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
                #CBE9FF 0%,
                #CBE9FF 9%,
                transparent 9.2%
            ),
            radial-gradient(
                circle at 84% 35%,
                #DDEEFF 0%,
                #DDEEFF 12%,
                transparent 12.2%
            ),
            linear-gradient(
                135deg,
                #FFFDF8 0%,
                #F1F8FE 60%,
                #F8FBFF 100%
            );
    }


    /* Main content */
    .block-container {
        max-width: 1100px;
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
        color: #176A96 !important;
        font-weight: 750 !important;
    }


    /* Paragraphs */
    p {
        line-height: 1.65;
    }


    /* ==================================================
       CONTAINERS
       ================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 22px !important;

        background:
            rgba(255, 255, 255, 0.92);

        border:
            1px solid #D3E5F1 !important;

        box-shadow:
            0 10px 28px
            rgba(26, 80, 110, 0.07);
    }


    /* ==================================================
       METRICS
       ================================================== */

    [data-testid="stMetric"] {
        background:
            linear-gradient(
                135deg,
                #FFFFFF,
                #EAF6FF
            );

        border:
            1px solid #CFE5F4;

        border-radius:
            18px;

        padding:
            1.3rem;

        box-shadow:
            0 7px 20px
            rgba(26, 80, 110, 0.07);
    }


    [data-testid="stMetricValue"] {
        color:
            #087F8C;

        font-weight:
            800;
    }


    /* ==================================================
       SELECT BOX
       ================================================== */

    [data-testid="stSelectbox"] > div > div {
        border-radius:
            14px;
    }


    /* ==================================================
       DATAFRAME
       ================================================== */

    [data-testid="stDataFrame"] {
        border-radius:
            16px;

        overflow:
            hidden;

        border:
            1px solid #D5E7F2;
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
                #52BEB3,
                #62AEE8,
                transparent
            ) !important;
    }


    /* Captions */
    [data-testid="stCaptionContainer"] {
        color:
            #5D737E;
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

    st.caption("DATA EXPLORER")

    st.title("📊 Explore the Wordlist")

    st.write(
        "Explore patterns in the published wordlist by grouping "
        "entries according to keywords found in their English meanings."
    )

    st.info(
        "These groups are created by the application for exploration "
        "and are not official Noongar linguistic or cultural categories."
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
# DATASET SUMMARY
# ==================================================

st.write("")
st.divider()

st.header("Dataset summary")

st.write(
    "A quick overview of the records contained in the published wordlist."
)


# Calculate summary values

total_records = len(data)

unique_noongar_entries = data[
    "noongar"
].nunique()

unique_english_meanings = data[
    "english"
].nunique()


# Display metrics

column1, column2, column3 = st.columns(
    3,
    gap="medium"
)


with column1:

    st.metric(
        label="📚 Total Records",
        value=total_records
    )


with column2:

    st.metric(
        label="🔤 Unique Noongar Entries",
        value=unique_noongar_entries
    )


with column3:

    st.metric(
        label="💬 Unique English Meanings",
        value=unique_english_meanings
    )


# ==================================================
# RELATED WORD GROUP ANALYSIS
# ==================================================

st.write("")
st.divider()

st.header("Related word groups")

st.write(
    "The chart below shows how many records were matched "
    "to each application-defined group."
)


# Calculate group counts

group_counts = count_groups(data)


# Convert results into a DataFrame for Streamlit charting

group_counts_df = pd.DataFrame(
    {
        "Category": group_counts.keys(),
        "Number of Entries": group_counts.values()
    }
)


group_counts_df = group_counts_df.set_index(
    "Category"
)


# ==================================================
# CHART
# ==================================================

with st.container(border=True):

    st.subheader(
        "📈 Entries by group"
    )

    st.bar_chart(
        group_counts_df,
        color="#299DB2"
    )


# ==================================================
# MOST COMMON MATCHED GROUP
# ==================================================

defined_groups = {
    category: count
    for category, count in group_counts.items()
    if category != "Other"
}


# Only calculate the maximum if defined groups exist
if len(defined_groups) > 0:

    most_common_group = max(
        defined_groups,
        key=defined_groups.get
    )

    most_common_count = defined_groups[
        most_common_group
    ]


    st.success(
        f"📌 The largest defined group is "
        f"**{most_common_group}**, with "
        f"**{most_common_count} matched records**."
    )

else:

    st.info(
        "No application-defined groups contained matching records."
    )


# ==================================================
# INTERACTIVE GROUP BROWSER
# ==================================================

st.write("")
st.divider()

st.header("🔍 Explore a group")

st.write(
    "Select a group to see the English meanings and "
    "Noongar entries that were matched to it."
)


# Generate grouped entries

groups = group_entries(
    data
)


# Group selection

selected_group = st.selectbox(
    "Choose a related-word group",
    list(groups.keys())
)


# Retrieve selected entries

selected_entries = groups[
    selected_group
]


# ==================================================
# GROUP SUMMARY
# ==================================================

st.write("")

st.metric(
    label=f"Entries matched to {selected_group}",
    value=len(selected_entries)
)


# ==================================================
# DISPLAY MATCHING ENTRIES
# ==================================================

if len(selected_entries) == 0:

    st.info(
        "No entries were found in this group."
    )


else:

    display_data = pd.DataFrame(
        selected_entries
    )


    with st.container(border=True):

        st.subheader(
            f"{selected_group} entries"
        )

        st.dataframe(
            display_data[
                [
                    "english",
                    "noongar"
                ]
            ],
            use_container_width=True,
            hide_index=True
        )


# ==================================================
# EXPLANATION
# ==================================================

st.write("")
st.divider()

st.subheader("💡 How are these groups created?")

with st.container(border=True):

    st.write(
        "The application examines English meanings in the "
        "wordlist and matches entries to predefined groups "
        "using keywords."
    )

    st.write(
        "The groups are provided as a way to explore patterns "
        "in the dataset. They should not be interpreted as "
        "official Noongar linguistic or cultural classifications."
    )


# ==================================================
# FOOTER
# ==================================================

st.write("")

st.caption(
    "Noongar Language Explorer • Data Explorer"
)