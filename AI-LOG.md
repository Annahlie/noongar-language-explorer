# AI Use Log

## Project

**Noongar Language Explorer**
**CITS1501 Introduction to Programming with Python**

## Purpose of This Log

This document records significant uses of generative AI during the development of the Noongar Language Explorer.

ChatGPT has been used as a development assistance tool for project planning, programming explanations, debugging, algorithm design, Streamlit development, Git/GitHub assistance, and documentation.

AI-generated suggestions are not automatically accepted into the project. The development team is responsible for reading, understanding, testing, modifying, and verifying suggested code before including it in the application.

AI is **not used to generate Noongar language, cultural, or historical content**. Noongar words and English meanings displayed by the application come from the published dataset used by the project.

---

## AI Use 1 — Project Planning and Application Design

**AI tool:** ChatGPT

**Purpose:**
Asked for assistance interpreting the CITS1501 project requirements and planning an application that would satisfy the technical, data, algorithm, user-interface, testing, and documentation requirements.

**AI assistance:**
ChatGPT suggested developing a Noongar language exploration application rather than a simple static word lookup.

Potential application features discussed included:

* English-to-Noongar dictionary search
* data exploration
* related-word analysis
* visualisations
* interactive quiz functionality
* source information
* multiple Streamlit views

ChatGPT also suggested separating the application into data, application logic, user-interface pages, and tests.

**How the output was used:**
The suggestions were reviewed and used to develop the initial application plan. Features are being implemented progressively rather than copying a complete generated application.

---

## AI Use 2 — Project File Structure

**AI tool:** ChatGPT

**Purpose:**
Asked for assistance organising the Python project in a way that would make the application easier to develop, test, and explain.

**AI assistance:**
ChatGPT suggested a structure including:

* `data/` for the CSV dataset
* `src/` for Python application logic
* `pages/` for Streamlit pages
* `tests/` for automated tests
* `README.md` for project documentation
* `AI-LOG.md` for AI-use documentation
* `requirements.txt` for dependencies
* `.gitignore` for files that should not be tracked

**How the output was used:**
The structure was created manually in VS Code and modified as the application developed.

The current application separates data loading and search logic from the Streamlit user interface.

---

## AI Use 3 — Git and GitHub Setup and Debugging

**AI tool:** ChatGPT

**Purpose:**
Requested assistance setting up Git and connecting the local project to the team's shared GitHub repository.

**Problem encountered:**
Git was initially configured at the Windows user-directory level rather than inside the Noongar Language Explorer project. This caused `git status` to identify unrelated directories and files such as Downloads, AppData, and OneDrive.

**AI assistance:**
ChatGPT explained how to:

* identify the Git repository root using `git rev-parse --show-toplevel`;
* remove the incorrectly located Git repository metadata;
* initialise Git inside the correct project directory;
* inspect repository status;
* stage files;
* create meaningful commits;
* connect the local project to the existing shared GitHub repository;
* fetch remote changes;
* inspect branches;
* pull changes using rebase;
* handle non-fast-forward push errors; and
* push local commits to the shared repository.

**How the output was verified:**
Commands were run individually in the VS Code terminal.

The repository state was checked using commands including:

```bash
git status
git log --oneline
git branch -a
git remote -v
```

The GitHub repository was also checked to confirm that commits were successfully uploaded.

---

## AI Use 4 — Dataset Loading

**AI tool:** ChatGPT

**Purpose:**
Requested assistance writing Python code to load the project's CSV dataset.

**AI assistance:**
ChatGPT suggested creating a `load_data()` function in `src/data_loader.py`.

The suggested implementation used:

* Pandas to read the CSV file;
* `pathlib.Path` to construct the dataset path; and
* file-existence checking to provide an appropriate error if the dataset could not be located.

**How the output was used:**
The function was added to the project and kept separate from the Streamlit interface so that data loading can be reused by different parts of the application.

**How the output was tested:**
A manual development script named `check_data.py` was created and run.

The initial test confirmed:

* **275 records** were loaded;
* the expected columns were present:

  * `noongar`
  * `english`
  * `source_url`

The first records were printed to confirm that the CSV was being interpreted correctly.

---

## AI Use 5 — Dataset Validation and Cleaning

**AI tool:** ChatGPT

**Purpose:**
Requested assistance checking whether the dataset met the project requirements and whether there were data-quality issues that could affect the application.

**AI assistance:**
ChatGPT suggested validating:

* whether the dataset file exists;
* whether required columns are present;
* whether the dataset contains at least 200 records;
* whether completely empty rows exist;
* whether text contains unnecessary surrounding whitespace;
* whether missing values exist;
* whether completely duplicated rows exist; and
* whether repeated Noongar entries exist.

**How the output was tested:**
The validation was checked using `check_data.py`.

The results were:

* **275 records**
* **0 missing values**
* **0 completely duplicated rows**
* **1 repeated Noongar entry**

**Decision made:**
The repeated Noongar entry was not automatically removed. A repeated entry may have different English descriptions, so removing it based only on the Noongar field could remove valid source data.

The application therefore preserves the published records rather than assuming repeated Noongar entries are errors.

---

## AI Use 6 — Initial Search Algorithm

**AI tool:** ChatGPT

**Purpose:**
Requested assistance designing meaningful search functionality rather than relying only on a simple DataFrame lookup.

**AI assistance:**
ChatGPT suggested implementing a custom search algorithm that:

1. normalises user input;
2. removes surrounding whitespace;
3. converts text to lowercase;
4. loops through dataset records;
5. identifies exact matches;
6. identifies entries beginning with the query;
7. identifies entries containing the query; and
8. combines the different match types in priority order.

A separate `normalise_text()` function was suggested so the text-cleaning behaviour could be reused.

**How the output was used:**
The algorithm was implemented in `src/search.py` rather than directly inside the Streamlit interface.

Comments were added to the code to explain the purpose of important operations and make the algorithm easier for the development team to understand.

---

## AI Use 7 — Manual Search Testing and Debugging

**AI tool:** ChatGPT

**Purpose:**
Requested assistance testing the search algorithm before integrating it into Streamlit.

**AI assistance:**
ChatGPT suggested creating `check_search.py`, which loads the dataset, accepts a terminal search query, calls the search function, and prints matching records.

During testing, the following Python error occurred:

```text
ModuleNotFoundError: No module named 'src.search'
```

ChatGPT helped identify that the search algorithm needed to be stored in:

```text
src/search.py
```

while:

```text
check_search.py
```

should remain a separate development/testing script.

**How the problem was resolved:**
`src/search.py` was created in the correct location and `check_search.py` imported the search function from that module.

Manual tests were then performed using exact matches, uppercase input, surrounding whitespace, partial searches, and unknown input.

---

## AI Use 8 — Streamlit Interface Development

**AI tool:** ChatGPT

**Purpose:**
Requested assistance connecting the Python functionality to an interactive web interface.

**AI assistance:**
ChatGPT suggested using Streamlit and provided guidance for:

* page configuration;
* page headings;
* text input;
* search buttons;
* displaying search results;
* warnings for blank input;
* messages when no results are found; and
* handling dataset loading errors.

**Problem encountered:**
The `streamlit` command was initially not recognised by PowerShell.

**AI assistance with debugging:**
ChatGPT explained how to check whether Streamlit was installed and suggested running Streamlit through the active Python interpreter using:

```bash
python -m streamlit run app.py
```

The development environment was configured successfully and the application was then run locally in a web browser.

---

## AI Use 9 — Multi-Page Streamlit Structure

**AI tool:** ChatGPT

**Purpose:**
Requested assistance creating multiple application views to support the project's user-interface requirements.

**AI assistance:**
ChatGPT suggested using Streamlit's `pages/` structure with:

* Home
* Dictionary
* Data Explorer
* Quiz
* About

Placeholder pages were initially created so the navigation and application architecture could be established before every feature was completed.

**How the output was modified:**
The original `app.py` entry point was renamed to `Home.py` so the main Streamlit navigation displays **Home** rather than **app**.

The application is now run using:

```bash
python -m streamlit run Home.py
```

---

## AI Use 10 — English-to-Noongar Dictionary Redesign

**AI tool:** ChatGPT

**Purpose:**
The original search direction allowed a Noongar word to be entered to find its English meaning. The project design was changed so users instead enter an English word or meaning and discover corresponding published Noongar entries.

ChatGPT was asked for assistance implementing this change.

**AI assistance:**
ChatGPT suggested changing the search algorithm from searching the `noongar` column to searching the `english` column.

The revised algorithm:

1. receives an English search query;
2. normalises the input;
3. removes surrounding whitespace;
4. converts the query to lowercase;
5. loops through the published English meanings;
6. identifies exact matches;
7. identifies meanings beginning with the query;
8. identifies meanings containing the query; and
9. combines results in ranked order.

The function was changed from `search_noongar()` to `search_english()`.

**How the output was used:**
The search algorithm remained in `src/search.py`.

`check_search.py` was modified to accept English input, and the Streamlit Dictionary page was modified to display the corresponding published Noongar entries.

**How the output was tested:**
Manual searches included:

* `water`
* `WATER`
* input containing surrounding whitespace
* `kangaroo`
* partial search queries
* unknown input such as `xyzabc`
* blank input

The testing confirmed that the search was case-insensitive, handled surrounding whitespace, returned matching records, and safely handled searches with no results.

**Important limitation:**
The application is not using AI to translate English into Noongar.

It searches English descriptions already present in the published dataset and returns the Noongar entries associated with those descriptions.

---

## AI Use 11 — Data Explorer Planning

**AI tool:** ChatGPT

**Purpose:**
Requested assistance planning meaningful analysis and visualisation for the Data Explorer.

**Initial suggestion:**
ChatGPT initially suggested analysing Noongar entry lengths and displaying a frequency distribution.

**Decision/rejection:**
After reviewing the idea, the development direction was changed because character length was considered less relevant to the purpose of a language exploration application.

The team instead decided that the Data Explorer should focus on the **meaning and relationships between entries**.

**Revised AI assistance:**
ChatGPT suggested investigating transparent groupings based on keywords in the published English descriptions, potentially allowing users to explore related records such as animals, plants/food, family/people, actions, and environmental terms.

**Current status:**
This functionality has not yet been implemented.

Any grouping system will need to be clearly described as an **application-defined analysis of the published English descriptions**, rather than representing official Noongar linguistic or cultural categories.

No AI-generated Noongar language information will be added to the dataset.

---

# Verification of AI-Generated Work

AI suggestions are treated as development assistance rather than automatically accepted solutions.

For AI-assisted programming work, the development process includes:

1. reading the suggested code;
2. understanding the purpose of the functions and important statements;
3. adding or modifying code where appropriate;
4. running the code locally;
5. manually testing expected behaviour;
6. testing invalid and edge-case input;
7. investigating errors;
8. checking that the implementation matches the project requirements; and
9. committing working development milestones to GitHub.

Automated testing using `pytest` will also be added as the application develops.

---

# Cultural and Language Content

Generative AI is **not used as a source of Noongar language, cultural, or historical information** for this project.

The application's Noongar entries and English descriptions are obtained from the project's published dataset.

The current dataset identifies its source as:

**Wirlomin Noongar Language and Stories — Language List**

https://www.wirlomin.com.au/language-list/

The project's final documentation will identify the data source and relevant usage conditions.

Any computational categories or analyses created by the application will be clearly distinguished from categories or interpretations supplied by the original language source.

## AI Use 12 — Related-Word Grouping Algorithm Development and Refinement

**AI tool:** ChatGPT

**Purpose:**
Requested assistance developing the related-word grouping system for the Data Explorer. The goal was to analyse the published English meanings in the dataset and allow users to explore entries with related meanings.

**Initial AI assistance:**
ChatGPT suggested creating a separate `src/analysis.py` module containing application-defined categories and associated English keywords.

The initial categories were:

* Animals
* Plants and Food
* People and Family
* Body
* Actions
* Nature and Environment

The initial algorithm looped through each dataset record, examined its published English meaning, and checked whether category keywords appeared within the meaning. Records could belong to more than one category.

A `count_groups()` function was also created to count the number of records assigned to each group for later use in data visualisation.

**Initial testing:**
A separate `check_analysis.py` development script was created to test the grouping algorithm.

The first group counts were:

* Animals: 8
* Plants and Food: 17
* People and Family: 13
* Body: 20
* Actions: 15
* Nature and Environment: 21

The grouped entries were then manually inspected rather than assuming that the AI-suggested algorithm was correct.

**Problems identified during manual review:**
Manual inspection revealed several incorrect classifications.

Examples included:

* `sweat` being classified as Plants and Food because it contains the letters `eat`;
* `many (emphatically)` being classified as People and Family because `many` contains `man`;
* `earth, sand, country` being classified as Body because `earth` contains `ear`;
* `Frenchman's Peak` being classified as People and Family because `Frenchman's` contains `man`;
* `hear, understand` being classified as Body because `hear` contains `ear`.

Other records contained multiple words that could cause ambiguous classification. For example, `seal (lit. 'dog his head')` contained both an animal keyword and a body keyword.

**Changes made after reviewing the AI output:**
The original substring-matching approach was rejected because it produced false-positive classifications.

The algorithm was changed to use regular-expression word boundaries so keywords are matched as complete words or phrases rather than arbitrary sequences of letters.

For example:

* `eat` can match `eat` but not `sweat`;
* `man` can match `man` but not `many`;
* `ear` can match `ear` but not `earth`.

Explicit category overrides were also introduced for known ambiguous English descriptions where ordinary keyword matching did not represent the intended grouping in the application.

Examples tested included:

* `kangaroo berries` → Plants and Food
* `sweat` → Other
* `feathers` → Animals
* `spirit creature/little man` → Other
* `beneath` → Other
* `many (emphatically)` → Other
* `Frenchman's Peak` → Nature and Environment
* `earth, sand, country` → Nature and Environment
* `hear, understand` → Actions
* `seal (lit. 'dog his head')` → Animals
* `firestick (lit. fire-leg)` → Other
* `very sweet to ear when ripe, grows on the ground of prickly bushes` → Plants and Food
* `hunt, search, track` → Actions
* `searching` → Actions

An `Other` category was also added so that records are not forced into an unsuitable category when no appropriate keyword is found.

**Revised testing:**
After the algorithm was changed, the manually identified problem cases were tested again using `check_analysis.py`.

The final refined group counts were:

- Animals: 14
- Plants and Food: 29
- People and Family: 16
- Body: 18
- Actions: 64
- Nature and Environment: 21
- Places and Position: 25
- Time: 7
- Objects and Shelter: 7
- Descriptions and States: 31
- Other: 57

After inspecting the 197 entries initially classified as Other, the keyword lists were expanded using recurring English descriptions that were actually present in the dataset. Additional application-defined categories were introduced for Places and Position, Time, Objects and Shelter, and Descriptions and States.

The Other category was deliberately retained for entries that did not meaningfully fit the defined groups. The goal was not to force every dataset record into a category, but to provide transparent and useful exploratory groupings.

All of the specifically tested misclassified and ambiguous examples produced the intended application-defined group after the changes.

**Evaluation of the results:**
The revised algorithm reduced false-positive matches, but the testing also showed that 197 of the 275 dataset records currently fall into the `Other` category.

This indicates that the existing keyword lists are too limited to provide useful coverage of the complete dataset. The next development step will therefore be to inspect the published English meanings currently classified as `Other` and refine the grouping system based on patterns that actually occur in the dataset rather than inventing additional keywords without evidence.

**Important limitation:**
These categories are created by the application for data exploration. They are **not official Noongar linguistic or cultural categories**.

AI is not being used to generate Noongar words, meanings, or cultural information. The algorithm only analyses the published English descriptions already contained in the project dataset.

**How AI output was handled:**
The initial AI-generated approach was not accepted without testing. Manual inspection identified weaknesses in the suggested substring-matching algorithm, and the implementation was modified to address those problems. This process demonstrated the need to test and critically evaluate AI-generated code before including it in the project.

### Final refinement and interface implementation

After the initial refinement, the remaining entries classified as Other were manually inspected again. Several clear cases were identified from their published English meanings, including "kiss", "small sweet pigface", "blue mallee, grows pink flowers", "cooking, fixing", "back (anatomical)", "screaming", and "all talking together".

The keyword rules and explicit overrides were refined to classify these entries without introducing overly broad substring matching. For example, "back (anatomical)" was handled specifically rather than treating every occurrence of "back" as a Body entry, because other meanings use the word "back" in different contexts.

The final group counts were:

- Animals: 14
- Plants and Food: 31
- People and Family: 16
- Body: 18
- Actions: 68
- Nature and Environment: 21
- Places and Position: 25
- Time: 7
- Objects and Shelter: 7
- Descriptions and States: 31
- Other: 51

The Other category was deliberately retained because some published English meanings do not meaningfully fit the application's defined groups. The goal was not to force every record into a category.

The grouping algorithm was then integrated into the Streamlit Data Explorer. The interface displays dataset summary statistics, a bar chart comparing group counts, identifies the largest defined group, and allows users to select a category and inspect its matching entries.

All classifications are based on the English meanings already present in the published dataset. AI was not used to generate, translate, or interpret Noongar language content. The categories are application-defined exploratory groups and are not presented as official Noongar linguistic or cultural categories.


---

# Ongoing AI Use

This log will continue to be updated when AI is used significantly during later development stages, including:

* related-word analysis;
* data visualisation;
* quiz algorithm development;
* automated testing;
* debugging;
* application architecture;
* deployment; and
* final documentation.

The development team remains responsible for understanding, verifying, testing, and explaining all submitted work.