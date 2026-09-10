def normalise_text(text):
    """Prepare text for case-insensitive searching."""

    if not isinstance(text, str):
        return ""

    return text.strip().lower()


def search_noongar(query, data):
    """
    Search for Noongar words and rank the results.

    Ranking order:
    1. Exact matches
    2. Words that start with the query
    3. Words that contain the query
    """

    # Clean the user's input
    query = normalise_text(query)

    # Empty input should return no results
    if query == "":
        return []

    # Store results in separate groups
    exact_matches = []
    starts_with_matches = []
    contains_matches = []

    # Search through every row in the dataset
    for _, row in data.iterrows():

        noongar_word = normalise_text(row["noongar"])

        # Highest priority: exact match
        if noongar_word == query:
            exact_matches.append(row.to_dict())

        # Second priority: word starts with the query
        elif noongar_word.startswith(query):
            starts_with_matches.append(row.to_dict())

        # Third priority: query appears somewhere else in the word
        elif query in noongar_word:
            contains_matches.append(row.to_dict())

    # Combine the lists in ranking order
    results = (
        exact_matches
        + starts_with_matches
        + contains_matches
    )

    return results