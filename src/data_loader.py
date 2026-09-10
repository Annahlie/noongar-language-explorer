import pandas as pd
from pathlib import Path


REQUIRED_COLUMNS = {"noongar", "english", "source_url"}


def load_data():
    """Load and validate the Noongar language dataset."""

    file_path = Path(__file__).parent.parent / "data" / "noongar_words.csv"

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    data = pd.read_csv(file_path)

    # Clean column names
    data.columns = data.columns.str.strip()

    # Check required columns
    if not REQUIRED_COLUMNS.issubset(data.columns):
        raise ValueError(
            "Dataset must contain noongar, english, and source_url columns."
        )

    # Remove completely empty rows
    data = data.dropna(how="all")

    # Clean whitespace from text columns
    for column in REQUIRED_COLUMNS:
        data[column] = data[column].astype(str).str.strip()

    # Check minimum dataset size
    if len(data) < 200:
        raise ValueError(
            "Dataset must contain at least 200 records."
        )

    return data