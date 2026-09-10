from src.data_loader import load_data
from src.analysis import find_categories, count_groups


data = load_data()


print("CATEGORY TESTS")
print("--------------")

test_meanings = [
    "kangaroo berries",
    "sweat",
    "feathers",
    "spirit creature/little man",
    "beneath",
    "many (emphatically)",
    "Frenchman's Peak",
    "earth, sand, country",
    "hear, understand",
    "seal (lit. 'dog his head')",
    "firestick (lit. fire-leg)",
    "very sweet to ear when ripe, grows on the ground of prickly bushes",
    "hunt, search, track",
    "searching",
]

for meaning in test_meanings:
    print(
        meaning,
        "->",
        find_categories(meaning)
    )


print("\nGROUP COUNTS")
print("------------")

counts = count_groups(data)

for category, count in counts.items():
    print(
        category,
        ":",
        count
    )