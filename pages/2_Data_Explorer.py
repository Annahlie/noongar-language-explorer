import pandas as pd
import streamlit as st

from src.data_loader import load_data
from src.analysis import group_entries, count_groups


# -----------------------------
# Page heading
# -----------------------------
st.title("📊 Data Explorer")

st.write(
    "Explore groups of related entries based on keywords "
    "in their published English meanings."
)

st.caption(
    "These groups are created by the application for exploration "
    "and are not official Noongar linguistic or cultural categories."
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
# Dataset summary
# -----------------------------
st.subheader("Dataset Summary")

total_records = len(data)
unique_noongar_entries = data["noongar"].nunique()
unique_english_meanings = data["english"].nunique()

column1, column2, column3 = st.columns(3)

column1.metric(
    "Total Records",
    total_records
)

column2.metric(
    "Unique Noongar Entries",
    unique_noongar_entries
)

column3.metric(
    "Unique English Meanings",
    unique_english_meanings
)


# -----------------------------
# Related-word group analysis
# -----------------------------
st.subheader("Related Word Groups")

st.write(
    "The application analyses the published English meanings "
    "and groups entries when they contain selected keywords."
)

group_counts = count_groups(data)

# Convert the dictionary into a DataFrame so Streamlit
# can display it as a chart.
group_counts_df = pd.DataFrame(
    {
        "Category": group_counts.keys(),
        "Number of Entries": group_counts.values()
    }
)

group_counts_df = group_counts_df.set_index("Category")

st.bar_chart(group_counts_df)


# -----------------------------
# Interactive group browser
# -----------------------------
st.subheader("Explore a Group")

groups = group_entries(data)

selected_group = st.selectbox(
    "Choose a related-word group",
    list(groups.keys())
)

selected_entries = groups[selected_group]

st.write(
    f"**{len(selected_entries)} entries** were matched "
    f"to the {selected_group} group."
)


# -----------------------------
# Display matching entries
# -----------------------------
if len(selected_entries) == 0:

    st.info(
        "No entries were found in this group."
    )

else:

    display_data = pd.DataFrame(selected_entries)

    st.dataframe(
        display_data[["english", "noongar"]],
        use_container_width=True,
        hide_index=True
    )