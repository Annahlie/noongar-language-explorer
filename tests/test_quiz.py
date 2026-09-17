import pandas as pd
import pytest

from src.quiz import is_suitable_quiz_meaning, generate_question


def make_quiz_data():
    """
    Create simple placeholder data for testing the quiz algorithm.
    """

    return pd.DataFrame(
        [
            {
                "english": "water",
                "noongar": "test_entry_1",
                "source_url": "test"
            },
            {
                "english": "fire",
                "noongar": "test_entry_2",
                "source_url": "test"
            },
            {
                "english": "tree",
                "noongar": "test_entry_3",
                "source_url": "test"
            },
            {
                "english": "bird",
                "noongar": "test_entry_4",
                "source_url": "test"
            },
            {
                "english": "running",
                "noongar": "test_entry_5",
                "source_url": "test"
            }
        ]
    )


def test_is_suitable_quiz_meaning_accepts_normal_meaning():
    result = is_suitable_quiz_meaning("water")

    assert result is True


def test_is_suitable_quiz_meaning_rejects_blank_meaning():
    result = is_suitable_quiz_meaning("   ")

    assert result is False


def test_generate_question_has_four_unique_options():
    data = make_quiz_data()

    question = generate_question(data)

    assert len(question["options"]) == 4
    assert len(set(question["options"])) == 4


def test_generate_question_contains_correct_answer():
    data = make_quiz_data()

    question = generate_question(data)

    assert question["correct_answer"] in question["options"]


def test_generate_question_rejects_dataset_with_fewer_than_four_records():
    data = make_quiz_data().head(3)

    with pytest.raises(ValueError):
        generate_question(data)
def test_generate_question_avoids_ambiguous_english_meanings():
    data = pd.DataFrame(
        [
            {
                "english": "water",
                "noongar": "test_entry_1",
                "source_url": "test"
            },
            {
                "english": "water",
                "noongar": "test_entry_2",
                "source_url": "test"
            },
            {
                "english": "fire",
                "noongar": "test_entry_3",
                "source_url": "test"
            },
            {
                "english": "tree",
                "noongar": "test_entry_4",
                "source_url": "test"
            },
            {
                "english": "bird",
                "noongar": "test_entry_5",
                "source_url": "test"
            }
        ]
    )

    question = generate_question(data)

    assert question["english"] != "water"