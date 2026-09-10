AI Use Log
Project

Noongar Language Explorer — CITS1501 Introduction to Programming with Python

This document records significant uses of AI tools during the development of the Noongar Language Explorer.

AI tools are being used to assist with programming explanations, debugging, project planning, code suggestions, and documentation. All AI-generated suggestions are reviewed, tested, and modified where necessary by the development team.

AI is not being used to generate Noongar language, cultural, or historical content. Language data used by the application comes from the published dataset identified in the project documentation.

AI Use 1 — Project Structure and Planning

AI tool: ChatGPT

Purpose:
Asked for assistance planning an appropriate Python and Streamlit project structure based on the CITS1501 project requirements.

AI assistance:
Suggested separating the project into components including:

data/ for the CSV dataset
src/ for application logic
pages/ for Streamlit pages
tests/ for automated tests
README.md
AI-LOG.md
requirements.txt

How the output was used:
The suggested structure was reviewed and used as the starting structure for the application. The team created and managed the files in VS Code and GitHub.

AI Use 2 — Git and GitHub Setup

AI tool: ChatGPT

Purpose:
Requested assistance setting up Git and connecting the local VS Code project to the shared GitHub repository.

AI assistance:
Provided explanations and commands for:

identifying an incorrectly initialised Git repository
initialising Git in the correct project directory
staging files
creating commits
connecting the shared GitHub repository
pulling and rebasing changes
resolving non-fast-forward push errors

How the output was verified:
Git commands were run individually in the VS Code terminal. git status, git log, and the GitHub repository were checked to confirm that commits and files were correctly tracked.

AI Use 3 — Loading the Dataset

AI tool: ChatGPT

Purpose:
Requested assistance writing Python code to load the Noongar CSV dataset.

AI assistance:
Suggested a load_data() function using Pandas and pathlib to locate and load data/noongar_words.csv.

How the output was tested:
A check_data.py script was created and run manually.

The test confirmed:

275 records were loaded
the expected columns were present:
noongar
english
source_url
AI Use 4 — Dataset Validation

AI tool: ChatGPT

Purpose:
Requested assistance validating the dataset before using it in the application.

AI assistance:
Suggested checks for:

required columns
missing dataset file
minimum 200-record requirement
empty rows
whitespace
duplicate rows
duplicate Noongar entries

How the output was tested:
check_data.py was run against the dataset.

Results:

275 records
0 missing values
0 duplicate full rows
1 duplicate Noongar entry

The duplicate Noongar entry was not automatically removed because different records may contain different meanings for the same word.

AI Use 5 — Noongar Word Search Algorithm

AI tool: ChatGPT

Purpose:
Requested assistance designing the application's Noongar word search functionality.

AI assistance:
Suggested implementing a search algorithm that:

normalises the user's input
removes surrounding whitespace
performs case-insensitive comparison
checks for exact matches
checks for words beginning with the query
checks for words containing the query
ranks the results by match type

How the output was modified/used:
The algorithm was placed in src/search.py rather than directly in the Streamlit interface so that the search logic is separated from the user interface.

Comments were added to the code to assist with understanding and explanation.

How the output was tested:
A manual check_search.py script was used to test searches including:

exact matches
uppercase input
input containing extra spaces
partial matches
unknown words

The search algorithm was confirmed to return results without crashing for these cases.

AI Use 6 — Streamlit Interface

AI tool: ChatGPT

Purpose:
Requested assistance connecting the existing Python search functionality to a Streamlit user interface.

AI assistance:
Suggested:

a search text input
a Search button
result display
warnings for blank input
feedback when no results are found
handling dataset loading errors

How the output was tested:
The application was run locally using:

python -m streamlit run Home.py

The search interface was manually tested in the browser.

AI Use 7 — Multi-Page Application Structure

AI tool: ChatGPT

Purpose:
Requested assistance meeting the requirement for at least three distinct application views.

AI assistance:
Suggested a Streamlit multi-page structure containing:

Home
Dictionary
Data Explorer
Quiz
About

How the output was used:
A pages/ directory was created and the existing dictionary functionality was moved into the Dictionary page. Placeholder pages were created for functionality still under development.

The original app.py entry point was renamed to Home.py so that the Streamlit navigation displays "Home".

Verification and Responsibility

AI-generated code is not accepted automatically.

The development team is responsible for:

reading and understanding suggested code
running and testing the code
checking that it satisfies the project requirements
modifying code where necessary
identifying errors and limitations
ensuring that submitted work can be explained during the demonstration and Q&A

AI is used as a development assistance tool rather than as a source of Noongar language or cultural knowledge.