from src.data_loader import load_data
from src.quiz import generate_question


# Load the published dataset.
data = load_data()


print("QUIZ QUESTION TEST")
print("------------------")


# Generate one quiz question.
question = generate_question(data)


# Display the generated question.
print("English meaning:", question["english"])
print("Correct answer:", question["correct_answer"])


# Display all four answer options.
print("\nOptions:")

for option in question["options"]:
    print("-", option)


# Check that the quiz question was generated correctly.
print("\nChecks:")

print(
    "Four options:",
    len(question["options"]) == 4
)

print(
    "Correct answer included:",
    question["correct_answer"] in question["options"]
)

print(
    "Options are unique:",
    len(question["options"]) == len(set(question["options"]))
)