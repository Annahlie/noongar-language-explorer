import streamlit as st

from src.data_loader import load_data


# -----------------------------
# Page heading
# -----------------------------
st.title("📊 Data Explorer")

st.write(
    "Explore statistics and patterns in the published Noongar wordlist."
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

unique_noongar_words = data["noongar"].nunique()

unique_english_meanings = data["english"].nunique()


# Display the statistics in three columns
column1, column2, column3 = st.columns(3)

column1.metric(
    "Total Records",
    total_records
)

column2.metric(
    "Unique Noongar Entries",
    unique_noongar_words
)

column3.metric(
    "Unique English Meanings",
    unique_english_meanings
)
# -----------------------------
# Dataset browser
# -----------------------------
st.subheader("Browse the Wordlist")

st.write(
    "View the Noongar words and English meanings contained in the dataset."
)

st.dataframe(
    data[["noongar", "english"]],
    use_container_width=True,
    hide_index=True
)
# -----------------------------
# Word length analysis
# -----------------------------
st.subheader("Word Length Analysis")

# Create a new column containing the number of characters
# in each Noongar entry.
data["word_length"] = data["noongar"].str.len()

# Calculate the average word length.
average_length = data["word_length"].mean()

# Find the shortest and longest entries.
shortest_length = data["word_length"].min()
longest_length = data["word_length"].max()


# Display summary statistics.
col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Length",
    f"{average_length:.1f} characters"
)

col2.metric(
    "Shortest Entry",
    f"{shortest_length} characters"
)

col3.metric(
    "Longest Entry",
    f"{longest_length} characters"
)
# Count how many entries have each word length.
length_counts = (
    data["word_length"]
    .value_counts()
    .sort_index()
)

# Display the distribution as a bar chart.
st.bar_chart(length_counts)
st.write(
    "This chart shows how frequently different Noongar entry lengths "
    "occur in the dataset."
)