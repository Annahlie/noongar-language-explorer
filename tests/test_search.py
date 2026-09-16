from src.search import normalise_text, search_english


def test_normalise_text_converts_to_lowercase():
    result = normalise_text("WATER")

    assert result == "water"


def test_normalise_text_removes_surrounding_whitespace():
    result = normalise_text("   water   ")

    assert result == "water"


def test_normalise_text_handles_non_string_input():
    result = normalise_text(None)

    assert result == ""
def test_search_english_finds_exact_match():
    data = [
        {
            "english": "water",
            "noongar": "test_noongar_1",
            "source_url": "test"
        },
        {
            "english": "waterhole",
            "noongar": "test_noongar_2",
            "source_url": "test"
        }
    ]

    import pandas as pd
    data = pd.DataFrame(data)

    results = search_english("water", data)

    assert results[0]["english"] == "water"


def test_search_english_is_case_insensitive():
    data = [
        {
            "english": "water",
            "noongar": "test_noongar",
            "source_url": "test"
        }
    ]

    import pandas as pd
    data = pd.DataFrame(data)

    results = search_english("WATER", data)

    assert len(results) == 1
    assert results[0]["english"] == "water"


def test_search_english_returns_empty_list_for_blank_query():
    data = [
        {
            "english": "water",
            "noongar": "test_noongar",
            "source_url": "test"
        }
    ]

    import pandas as pd
    data = pd.DataFrame(data)

    results = search_english("   ", data)

    assert results == []