def normalise_text(text):
    """Prepare text for case-insensitive searching."""

    # Return an empty string if the input is not text
    if not isinstance(text, str):
        return ""

    # Remove surrounding spaces and convert to lowercase
    return text.strip().lower()


def search_english(query, data):
    """
    Search English meanings and return matching Noongar entries.

    Results are ranked:
    1. Exact English meaning
    2. English meaning starts with the query
    3. English meaning contains the query
    """

    # Clean the user's search input
    query = normalise_text(query)

    # Prevent an empty search from matching every record
    if query == "":
        return []

    # Create separate lists for each type of match
    exact_matches = []
    starts_with_matches = []
    contains_matches = []

    # Go through every record in the dataset
    for _, row in data.iterrows():

        # Get and clean the English meaning
        english_meaning = normalise_text(row["english"])

        # Highest priority: exact match
        if english_meaning == query:
            exact_matches.append(row.to_dict())

        # Second priority: meaning begins with the query
        elif english_meaning.startswith(query):
            starts_with_matches.append(row.to_dict())

        # Third priority: query appears elsewhere in the meaning
        elif query in english_meaning:
            contains_matches.append(row.to_dict())

    # Combine the results in ranking order
    results = (
        exact_matches
        + starts_with_matches
        + contains_matches
    )

    return results