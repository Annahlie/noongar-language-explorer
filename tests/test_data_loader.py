from src.data_loader import load_data


def test_load_data_returns_at_least_200_records():
    data = load_data()

    assert len(data) >= 200


def test_load_data_contains_required_columns():
    data = load_data()

    required_columns = {
        "noongar",
        "english",
        "source_url"
    }

    assert required_columns.issubset(data.columns)


def test_load_data_has_no_completely_empty_rows():
    data = load_data()

    empty_rows = data.isnull().all(axis=1)

    assert empty_rows.sum() == 0