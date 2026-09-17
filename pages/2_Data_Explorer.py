import pandas as pd
import streamlit as st

from src.analysis import count_groups, group_entries
from src.data_loader import load_data

# ---------------------------------------------------------
# Page heading
# ---------------------------------------------------------

st.title("📊 Data Explorer")

st.write(
    "Explore dataset statistics and application-defined "
    "related-word groups."
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
# Dataset summary
# ---------------------------------------------------------

st.subheader("Dataset Summary")

total_records = len(data)
unique_noongar_entries = data["noongar"].nunique()
unique_english_meanings = data["english"].nunique()

column1, column2, column3 = st.columns(3)

column1.metric("Total Records", total_records)
column2.metric("Unique Noongar Entries", unique_noongar_entries)
column3.metric("Unique English Meanings", unique_english_meanings)


# ---------------------------------------------------------
# Related-word groups
# ---------------------------------------------------------

st.divider()

st.subheader("Related-Word Groups")

st.write(
    "The chart shows how many dataset records were matched "
    "to each application-defined group."
)

group_counts = count_groups(data)

group_counts_df = pd.DataFrame(
    {
        "Category": group_counts.keys(),
        "Number of Entries": group_counts.values()
    }
)

group_counts_df = group_counts_df.set_index("Category")

st.bar_chart(
    group_counts_df,
    height=350,
    color="#C62828"
)


# ---------------------------------------------------------
# Largest defined group
# ---------------------------------------------------------

defined_groups = {
    category: count
    for category, count in group_counts.items()
    if category != "Other"
}

most_common_group = max(
    defined_groups,
    key=defined_groups.get
)

most_common_count = defined_groups[most_common_group]

st.warning(
    f"The largest defined group is **{most_common_group}**, "
    f"with **{most_common_count} matched records**."
)


# ---------------------------------------------------------
# Interactive group browser
# ---------------------------------------------------------

st.divider()

st.subheader("Explore a Group")

st.write(
    "Select a group to view the published entries matched to it."
)

groups = group_entries(data)

selected_group = st.selectbox(
    "Related-word group",
    list(groups.keys())
)

selected_entries = groups[selected_group]

st.write(
    f"**{len(selected_entries)} "
    f"{'entry' if len(selected_entries) == 1 else 'entries'}** "
    f"matched to **{selected_group}**."
)


# ---------------------------------------------------------
# Display matching entries
# ---------------------------------------------------------

if len(selected_entries) == 0:
    st.info("No entries were found in this group.")

else:
    display_data = pd.DataFrame(selected_entries)

    display_data = display_data[
        ["english", "noongar"]
    ].rename(
        columns={
            "english": "English Meaning",
            "noongar": "Noongar Entry"
        }
    )

    st.dataframe(
        display_data,
        use_container_width=True,
        hide_index=True,
        height=300
    )


# ---------------------------------------------------------
# Category information
# ---------------------------------------------------------

st.caption(
    "The related-word groups are created by the application for "
    "data exploration and are not official Noongar linguistic or "
    "cultural categories."
)