import random


def is_suitable_quiz_meaning(english_meaning):
    """
    Check whether an English meaning is suitable
    to use as a quiz question.
    """

    if not isinstance(english_meaning, str):
        return False

    meaning = english_meaning.strip()

    if meaning == "":
        return False

    unsuitable_phrases = [
        "(emphasis)",
        "(emphatically)",
        "?",
    ]

    for phrase in unsuitable_phrases:
        if phrase in meaning.lower():
            return False

    return True


def generate_question(data):
    """
    Generate one multiple-choice quiz question.

    The English meaning is used as the question.
    One correct Noongar entry and three incorrect Noongar
    entries are selected from the published dataset.
    """

    # A quiz needs at least four records.
    if len(data) < 4:
        raise ValueError(
            "The dataset must contain at least 4 records "
            "to generate a quiz question."
        )

    # Only use English meanings that have one unique Noongar entry.
    # This prevents the quiz from treating another valid equivalent
    # as an incorrect answer.
    meaning_counts = data.groupby("english")["noongar"].nunique()

    unambiguous_meanings = meaning_counts[
        meaning_counts == 1
    ].index

    suitable_rows = data[
        data["english"].isin(unambiguous_meanings)
        & data["english"].apply(is_suitable_quiz_meaning)
    ]
    
    # Make sure at least one suitable question exists.
    if len(suitable_rows) == 0:
        raise ValueError(
            "No suitable quiz meanings were found in the dataset."
        )

    # Randomly select the correct question.
    correct_row = suitable_rows.sample(n=1).iloc[0]

    english_meaning = correct_row["english"]
    correct_answer = correct_row["noongar"]

    # Build a list of possible incorrect answers.
    possible_distractors = []

    for _, row in data.iterrows():
        noongar_entry = row["noongar"]

        # Do not include the correct answer as a distractor.
        if noongar_entry != correct_answer:
            possible_distractors.append(noongar_entry)

    # Remove duplicate Noongar entries.
    possible_distractors = list(
        set(possible_distractors)
    )

    # Make sure three unique distractors are available.
    if len(possible_distractors) < 3:
        raise ValueError(
            "The dataset does not contain enough unique Noongar "
            "entries to generate quiz options."
        )

    # Randomly choose three incorrect answers.
    distractors = random.sample(
        possible_distractors,
        3
    )

    # Combine correct answer and distractors.
    options = distractors + [
        correct_answer
    ]

    # Shuffle the answers so the correct one
    # is not always in the same position.
    random.shuffle(options)

    return {
        "english": english_meaning,
        "correct_answer": correct_answer,
        "options": options
    }