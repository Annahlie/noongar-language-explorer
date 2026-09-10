from src.data_loader import load_data
from src.search import search_noongar


# Load the dataset
data = load_data()

# Ask the user for a search word
query = input("Enter a Noongar word: ")

# Search the dataset
results = search_noongar(query, data)

# Display results
if len(results) == 0:
    print("No matches found.")
else:
    print("\nMatches:")

    for result in results:
        print(result["noongar"], "->", result["english"])