from src.analysis import find_categories, group_entries

import pandas as pd


def test_find_categories_matches_clear_keyword():
    result = find_categories("running")

    assert "Actions" in result


def test_find_categories_avoids_substring_false_positive():
    result = find_categories("sweat")

    assert result == ["Other"]


def test_find_categories_uses_category_override():
    result = find_categories("back (anatomical)")

    assert result == ["Body"]


def test_group_entries_places_record_in_correct_group():
    data = pd.DataFrame(
        [
            {
                "english": "running",
                "noongar": "test_entry",
                "source_url": "test"
            }
        ]
    )

    groups = group_entries(data)

    assert len(groups["Actions"]) == 1
    assert groups["Actions"][0]["english"] == "running"