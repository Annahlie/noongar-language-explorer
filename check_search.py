from src.data_loader import load_data
from src.search import search_english


# Load the dataset
data = load_data()

# Ask the user for an English word
query = input("Enter an English word: ")

# Run the search algorithm
results = search_english(query, data)


# Display results
if len(results) == 0:
    print("No matches found.")

else:
    print("\nMatches:")

    for result in results:
        print(
            result["english"],
            "->",
            result["noongar"]
        )