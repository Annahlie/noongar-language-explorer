Noongar Language Explorer
Project Overview

Noongar Language Explorer is a CITS1501 group project built using Python and Streamlit.

The application is designed to help users explore a published Noongar wordlist and view English meanings.

The language data used in the application comes from a published source and is loaded from a CSV file rather than being written directly into the Python code.

Current Features
Home page
Multi-page Streamlit navigation
Noongar word search
Case-insensitive searching
Partial word searching
Ranked search results
English meanings displayed for matching words
Dataset validation
Error handling for invalid or empty searches
Planned Features
Data analysis and visualisations
Interactive quiz
About and source information
Automated tests
Deployment
Project Structure
noongar-language-explorer/
│
├── Home.py
├── check_data.py
├── check_search.py
│
├── data/
│   └── noongar_words.csv
│
├── pages/
│   ├── 1_Dictionary.py
│   ├── 2_Data_Explorer.py
│   ├── 3_Quiz.py
│   └── 4_About.py
│
├── src/
│   ├── data_loader.py
│   └── search.py
│
├── tests/
├── README.md
├── AI-LOG.md
├── requirements.txt
└── .gitignore
Dataset

The application currently uses a dataset containing 275 records.

The dataset contains the following columns:

noongar
english
source_url

The published source is:

Wirlomin Noongar Language and Stories
https://www.wirlomin.com.au/language-list/

The source and its usage conditions will be documented fully before final submission.

Running the Application

Install the required packages:

python -m pip install -r requirements.txt

Run the Streamlit application:

python -m streamlit run Home.py
Testing

Manual test scripts are currently included:

python check_data.py
python check_search.py

Automated tests using pytest will be added during development.

Development

GitHub is used throughout development for version control and team collaboration.

Both team members are expected to make meaningful commits and understand all submitted code.

AI Use

Significant AI assistance is documented in AI-LOG.md.

AI is not used to generate Noongar language or cultural content.
