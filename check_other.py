from src.data_loader import load_data
from src.analysis import group_entries


# Load the dataset
data = load_data()

# Group all dataset entries
groups = group_entries(data)

# Get entries currently classified as Other
other_entries = groups["Other"]


print("ENTRIES CLASSIFIED AS OTHER")
print("---------------------------")
print("Total:", len(other_entries))
print()


# Print the English meaning of every Other entry
for number, entry in enumerate(other_entries, start=1):
    print(
        number,
        "-",
        entry["english"]
    )