# AI Use Log

## Project

**Noongar Language Explorer**

**CITS1501 Introduction to Programming with Python**

## Purpose of This Log

This document records significant uses of generative AI during the development of the Noongar Language Explorer.

ChatGPT has been used as a development assistance tool for project planning, programming explanations, debugging, algorithm design, Streamlit development, Git/GitHub assistance, testing guidance, and documentation.

AI-generated suggestions are not automatically accepted into the project. The development team is responsible for reading, understanding, testing, modifying, and verifying suggested code before including it in the application.

AI is **not used to generate Noongar language, cultural, or historical content**. Noongar entries and English meanings displayed by the application come from the published dataset used by the project.

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

The suggestions were reviewed and used to develop the initial application plan. Features have been implemented progressively rather than copying a complete generated application.

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

The current application separates data loading, search, analysis, and quiz logic from the Streamlit user interface.

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

ChatGPT explained how to check whether Streamlit was installed and suggested running Streamlit through the active Python interpreter.

The application is now run using:

```bash
python -m streamlit run Home.py
```

The development environment was configured successfully and the application was run locally in a web browser.

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

**Status at this stage of development:**

This functionality had not yet been implemented at this stage. It was subsequently developed, tested, refined, and integrated into the application as documented in AI Use 12.

Any grouping system needed to be clearly described as an **application-defined analysis of the published English descriptions**, rather than representing official Noongar linguistic or cultural categories.

No AI-generated Noongar language information was added to the dataset.

---

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

### Initial Testing

A separate `check_analysis.py` development script was created to test the grouping algorithm.

The first group counts were:

* Animals: 8
* Plants and Food: 17
* People and Family: 13
* Body: 20
* Actions: 15
* Nature and Environment: 21

The grouped entries were then manually inspected rather than assuming that the AI-suggested algorithm was correct.

### Problems Identified During Manual Review

Manual inspection revealed several incorrect classifications.

Examples included:

* `sweat` being classified as Plants and Food because it contains the letters `eat`;
* `many (emphatically)` being classified as People and Family because `many` contains `man`;
* `earth, sand, country` being classified as Body because `earth` contains `ear`;
* `Frenchman's Peak` being classified as People and Family because `Frenchman's` contains `man`;
* `hear, understand` being classified as Body because `hear` contains `ear`.

Other records contained multiple words that could cause ambiguous classification. For example, `seal (lit. 'dog his head')` contained both an animal keyword and a body keyword.

### Changes Made After Reviewing the AI Output

The original substring-matching approach was rejected because it produced false-positive classifications.

The algorithm was changed to use regular-expression word boundaries so keywords are matched as complete words or phrases rather than arbitrary sequences of letters.

For example:

* `eat` can match `eat` but not `sweat`;
* `man` can match `man` but not `many`;
* `ear` can match `ear` but not `earth`.

Explicit category overrides were also introduced for known ambiguous English descriptions where ordinary keyword matching did not represent the intended grouping in the application.

Examples tested during the refinement process included:

* `kangaroo berries` → Plants and Food
* `sweat` → Other
* `feathers` → Animals
* `spirit creature/little man` → Other
* `beneath` → Other at an intermediate stage
* `many (emphatically)` → Other
* `Frenchman's Peak` → Nature and Environment
* `earth, sand, country` → Nature and Environment
* `hear, understand` → Actions
* `seal (lit. 'dog his head')` → Animals
* `firestick (lit. fire-leg)` → Other at an intermediate stage
* `very sweet to ear when ripe, grows on the ground of prickly bushes` → Plants and Food
* `hunt, search, track` → Actions
* `searching` → Actions

These classifications represented an intermediate stage of development. Further manual inspection later changed some classifications, including `beneath` to Places and Position and `firestick (lit. fire-leg)` to Objects and Shelter.

An `Other` category was added so that records are not forced into an unsuitable category when no appropriate keyword is found.

### Revised Testing

After the algorithm was changed, manually identified problem cases were tested again using `check_analysis.py`.

At one stage of refinement, the group counts were:

* Animals: 14
* Plants and Food: 29
* People and Family: 16
* Body: 18
* Actions: 64
* Nature and Environment: 21
* Places and Position: 25
* Time: 7
* Objects and Shelter: 7
* Descriptions and States: 31
* Other: 57

Additional application-defined categories had been introduced for:

* Places and Position
* Time
* Objects and Shelter
* Descriptions and States

The `Other` category was deliberately retained for entries that did not meaningfully fit the defined groups.

### Evaluation of the Results

Earlier testing showed that 197 of the 275 dataset records initially fell into the `Other` category. This demonstrated that the first keyword lists were too limited to provide useful coverage of the complete dataset.

The published English meanings classified as `Other` were therefore manually inspected and the grouping system was progressively refined using patterns that actually occurred in the dataset rather than inventing additional keywords without evidence.

The final refinement reduced the `Other` group to 51 matched records while deliberately retaining the category for entries that did not meaningfully fit the application's defined groups.

### Final Refinement and Interface Implementation

After the initial refinement, the remaining entries classified as `Other` were manually inspected again.

Several clear cases were identified from their published English meanings, including:

* `kiss`
* `small sweet pigface`
* `blue mallee, grows pink flowers`
* `cooking, fixing`
* `back (anatomical)`
* `screaming`
* `all talking together`

The keyword rules and explicit overrides were refined to classify these entries without introducing overly broad substring matching.

For example, `back (anatomical)` was handled specifically rather than treating every occurrence of `back` as a Body entry, because other meanings use the word `back` in different contexts.

The final group counts were:

* Animals: 14
* Plants and Food: 31
* People and Family: 16
* Body: 18
* Actions: 68
* Nature and Environment: 21
* Places and Position: 25
* Time: 7
* Objects and Shelter: 7
* Descriptions and States: 31
* Other: 51

The `Other` category was deliberately retained because some published English meanings do not meaningfully fit the application's defined groups. The goal was not to force every record into a category.

The grouping algorithm was then integrated into the Streamlit Data Explorer.

The interface:

* displays dataset summary statistics;
* displays a bar chart comparing group counts;
* identifies the largest defined group; and
* allows users to select a category and inspect its matching entries.

### Important Limitation

These categories are created by the application for data exploration. They are **not official Noongar linguistic or cultural categories**.

All classifications are based on the English meanings already present in the published dataset.

AI was not used to generate, translate, or interpret Noongar language content.

### How AI Output Was Handled

The initial AI-generated approach was not accepted without testing.

Manual inspection identified weaknesses in the suggested substring-matching algorithm, and the implementation was modified to address those problems.

The grouping system was then repeatedly tested and refined using published English descriptions actually contained in the dataset.

This process demonstrated the need to test and critically evaluate AI-generated code before including it in the project.

---

## AI Use 13 — Quiz Algorithm and Interactive Quiz Development

**AI tool:** ChatGPT

**Purpose:**

AI was used to assist with designing and implementing the interactive quiz feature for the Noongar Language Explorer.

The goal was to create a multiple-choice quiz using only information already contained in the published dataset.

### Initial AI Suggestion

AI suggested creating a separate `src/quiz.py` module containing a `generate_question()` function.

The proposed algorithm:

1. randomly selects a dataset record;
2. uses the published English meaning as the question;
3. uses the corresponding published Noongar entry as the correct answer;
4. searches the dataset for possible incorrect Noongar entries;
5. excludes the correct answer from the distractor list;
6. removes duplicate distractor options;
7. randomly selects three distractors;
8. combines the correct answer with the distractors; and
9. shuffles the four options.

The function also checks that the dataset contains enough records and unique Noongar entries to construct a valid multiple-choice question.

### Testing the Question Generator

A separate `check_quiz.py` development script was created to inspect generated questions and verify several conditions.

The checks included:

* exactly four answer options are produced;
* the correct answer is included;
* all displayed options are unique.

Multiple randomly generated questions were manually tested.

Examples of English meanings encountered during testing included:

* `to kill`
* `understanding`
* `hunt, search, track`

The generated questions passed the checks for four options, inclusion of the correct answer, and uniqueness of options.

### Refining Suitable Quiz Questions

During testing, the randomly selected English meaning `many (emphatically)` appeared as a quiz question.

Although this content exists in the published dataset, it was judged to be a less suitable prompt for the intended quiz experience.

AI suggested introducing an `is_suitable_quiz_meaning()` function.

The function filters obvious unsuitable quiz prompts containing:

* `(emphasis)`
* `(emphatically)`
* question marks

This filtering changes only which published records are selected as quiz questions. It does not modify, translate, or generate Noongar language content.

The revised generator was manually run several times to verify that suitable questions continued to generate correctly.

### Streamlit Quiz Interface

AI then assisted with integrating the quiz algorithm into `pages/3_Quiz.py`.

Streamlit session state was used to store:

* the current quiz question;
* whether the current question has been answered;
* the user's score;
* the total number of questions answered.

The interface allows the user to select one of four answers, check the answer, receive feedback, view their current score, and move to another randomly generated question.

### Feedback Duplication Bug

During manual testing, a UI bug was identified.

When a correct answer was selected, the success message appeared twice. When an incorrect answer was selected, the message displaying the correct answer also appeared twice.

The cause was that feedback was being displayed both inside the `Check Answer` button logic and again in a separate section intended to keep feedback visible after Streamlit reruns.

AI suggested separating state updates from feedback display.

The `Check Answer` logic was changed so that it updates quiz state and score without displaying duplicate feedback. A separate feedback section is now responsible for displaying the result.

The application was manually retested and the duplicate feedback problem was confirmed to be resolved.

### Restart Quiz Functionality

AI suggested adding a Restart Quiz function to provide users with a way to begin a new quiz session without reloading the application.

The Restart Quiz button resets the relevant Streamlit session-state values. It:

* generates a new quiz question;
* sets the answered state back to false;
* resets the correct-answer score to zero;
* resets the number of answered questions to zero;
* reruns the Streamlit page so that the reset state is immediately displayed.

The feature was manually tested after implementation to confirm that the score returns to `0 correct out of 0 answered` and that a new question is displayed.

### Verification and Decisions

AI-generated code was not accepted without testing.

The quiz generator was tested repeatedly using `check_quiz.py`, and the Streamlit interface was manually tested for:

* correct answers;
* incorrect answers;
* score updates;
* moving to the next question;
* checking without selecting an answer;
* duplicate feedback;
* restarting the quiz.

The duplicated-feedback problem was identified during manual testing rather than accepting the initial AI-generated interface as correct. The suggested fix was applied and manually verified.

The final quiz design continues to use the project's published CSV dataset as the source of both English meanings and Noongar entries.

### Cultural and Language-Content Considerations

AI was used to assist with programming logic and interface design only.

AI was not used to:

* generate Noongar words;
* translate English into Noongar;
* correct or reinterpret Noongar entries;
* create cultural knowledge;
* create historical information.

All language content displayed in the quiz is retrieved from the published project dataset.

---

## AI Use 14 — About Page Development

**AI tool:** ChatGPT

**Purpose:**

AI was used to assist with planning and implementing the About page for the application.

The purpose of the page was to provide users with clear information about the application, its language-data source, cultural considerations, application-defined analysis, and educational purpose.

**AI assistance:**

ChatGPT suggested structuring the About page into sections covering:

- the purpose of the application;
- the published language-data source;
- information about Wirlomin Noongar Language and Stories Inc.;
- cultural and language-content considerations;
- the role of AI in the project;
- the application-defined nature of the Data Explorer categories;
- the educational purpose and limitations of the application.

A link to the original Wirlomin Word List was also added.

A Streamlit warning box was used to emphasise that the related-word groups displayed in the Data Explorer are application-defined exploratory categories and are not official Noongar linguistic or cultural categories.

**Cultural and language-content considerations:**

The About page states that Noongar entries and English meanings come from the published wordlist rather than being generated by AI.

The page also explains that AI has been used for programming, debugging, testing, and application development, but not to generate Noongar words, translations, cultural information, or historical information.

The application is described as a dataset exploration tool rather than an AI translation service.

No claim is made that the source material is copyright-free, openly licensed, or used with permission.

**Testing:**

The About page was manually tested in Streamlit.

Testing confirmed that:

- the page loads without errors;
- the headings display correctly;
- the link to the Wirlomin Word List works;
- the application-defined category warning is displayed correctly; and
- the page content displays correctly within the Streamlit interface.

**How AI output was handled:**

The suggested content was reviewed before being added to the application. Care was taken not to use AI as a source of Noongar language or cultural knowledge and not to make unsupported claims about permissions or licensing.

---

## AI Use 15 — Automated Testing with pytest

**AI tool:** ChatGPT

**Purpose:**

AI was used to assist with developing an automated test suite using `pytest` for the application's core Python functionality.

**AI assistance:**

ChatGPT suggested tests for:

* text normalisation and dictionary searching;
* exact, case-insensitive, and blank dictionary queries;
* application-defined related-word classification;
* protection against accidental substring matches;
* explicit category overrides;
* grouping dataset records into categories;
* quiz meaning validation;
* quiz option generation;
* correct-answer inclusion;
* quiz boundary conditions; and
* dataset loading and validation.

Placeholder values such as `test_entry_1` were used when testing algorithms rather than generating Noongar language content.

The automated test suite contains 18 tests across:

* `test_search.py`;
* `test_analysis.py`;
* `test_quiz.py`; and
* `test_data_loader.py`.

**Testing and debugging:**

The initial search tests passed successfully.

During testing of the Data Explorer algorithm, an automated test for the English meaning `back (anatomical)` failed. The expected category was `Body`, but the algorithm returned `Other`.

Reviewing the code showed that `back (anatomical)` was present in the Body keyword list but was not present in the explicit override dictionary. Because the keyword contains punctuation and the matching algorithm uses regular-expression word boundaries, the expected keyword match did not occur.

The existing override mechanism was used to classify this specific published English meaning as `Body`.

After this correction, all Data Explorer tests passed.

Additional automated tests were then added for the quiz algorithm and data loader.

At the completion of this testing stage:

```text
18 tests passed
```

**Environment setup:**

While setting up automated testing, `pytest` was initially unavailable because the project did not yet have an active virtual environment containing the required dependency.

A `.venv` virtual environment was created, `requirements.txt` was updated to include `streamlit`, `pandas`, and `pytest`, and the dependencies were installed.

Tests are run from the project root using:

```text
python -m pytest
```

Running pytest from inside the `tests` directory caused Python to be unable to locate the `src` package. Returning to the project root resolved the import error.

**How AI output was handled:**

The suggested tests were added incrementally and executed after each stage rather than being accepted without verification.

Test failures were investigated before changes were made to the application code. The automated tests use controlled placeholder data where appropriate so that AI-generated Noongar language content is not introduced.

The final test suite was run successfully with all 18 tests passing.

---

## AI Use 16 — System Architecture and Data-Flow Planning

**AI tool:** ChatGPT

**Purpose:**

AI was used to assist with planning how the existing Noongar Language Explorer application could be represented in a system architecture and data-flow diagram.

**AI assistance:**

ChatGPT helped identify the main components of the existing application and explain how they are connected.

The discussion identified the following main layers:

- the user;
- the Streamlit user interface;
- application logic;
- data loading and validation; and
- the CSV dataset.

The application components discussed included:

- the Dictionary page and `search.py`;
- the Data Explorer page and `analysis.py`;
- the Quiz page and `quiz.py`;
- `data_loader.py`; and
- `data/noongar_words.csv`.

The Home and About pages were identified primarily as informational and navigation pages.

ChatGPT also explained examples of data flow through the application, including:

- an English search query being processed by the dictionary search logic and matching entries being returned;
- dataset records being processed by the analysis logic to produce groups and statistics;
- dataset records being used by the quiz logic to generate questions and answer options; and
- application components accessing the CSV dataset through the data-loading component.

**Final diagram:**

The final system architecture and data-flow diagram will be designed and drawn manually by the student.

AI-generated artwork or diagrams are not being used as the final architecture diagram.

The AI discussion is being used only as a planning aid to help understand the relationships between components already implemented in the project.

**How AI output was handled:**

The suggested architecture was compared with the application's existing files and functionality.

The final diagram will be independently created by the student based on their understanding of the application.

The architecture description was also documented in `README.md`.

No Noongar language or cultural content was generated as part of this assistance.

---

## AI Use 17 – User Interface Refinement

**Purpose:**  
AI was used to assist with reviewing and refining the Streamlit user interface across the Home, Dictionary, Data Explorer, Quiz, and About pages.

**AI assistance:**  
AI suggested changes to improve page layout, navigation, readability, and spacing while reducing unnecessary vertical scrolling. Suggestions included reorganising page navigation, using Streamlit forms and columns, adjusting quiz controls, and using tabs to organise the About page.

**Review and modification:**  
AI suggestions were not accepted automatically. Different layouts were tested in the running Streamlit application and adjusted based on their appearance and usability.

Some suggested layouts were rejected because they made the interface feel too cramped. For example, a more compressed Home layout and a side-by-side Data Explorer layout were tested but not retained. The final layouts were modified to provide more spacing while still keeping the interface compact.

The Dictionary search was placed inside a Streamlit form so that users can submit a search using either the Search button or the Enter key.

The Quiz interface was refined so that Check Answer and Restart Quiz appear next to each other. After an answer is submitted, Next Question replaces Check Answer while Restart Quiz remains available. Session state is used to preserve the submitted answer, score, and current quiz state.

The About page was reorganised into tabs so that source information, cultural and AI considerations, and project information can be accessed without displaying all of the text vertically at once.

**Verification:**  
The updated pages were manually checked in the running Streamlit application. After the interface changes were completed, the full automated test suite was run using:

`python -m pytest`

All **18 automated tests passed**.

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

Any computational categories or analyses created by the application are clearly distinguished from categories or interpretations supplied by the original language source.

# Ongoing AI Use

This log will continue to be updated when AI is used significantly during later development stages, including:

* automated testing;
* debugging and UI refinement;
* application architecture;
* security and privacy review;
* deployment;
* report preparation; and
* final documentation.

The development team remains responsible for understanding, verifying, testing, and explaining all submitted work.