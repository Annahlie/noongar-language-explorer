import streamlit as st

from src.data_loader import load_data
from src.quiz import generate_question


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Quiz | Noongar Language Explorer",
    page_icon="🧠",
    layout="wide"
)


# ==================================================
# CUSTOM STYLING
# ==================================================

st.markdown(
    """
    <style>

    /* Page background */
    .stApp {
        background:
            radial-gradient(
                circle at 92% 8%,
                #FFE29A 0%,
                #FFE29A 9%,
                transparent 9.2%
            ),
            radial-gradient(
                circle at 84% 35%,
                #FFF0C7 0%,
                #FFF0C7 12%,
                transparent 12.2%
            ),
            radial-gradient(
                circle at 12% 10%,
                #C8EEE8 0%,
                #C8EEE8 8%,
                transparent 8.2%
            ),
            linear-gradient(
                135deg,
                #FFFDF8 0%,
                #FFF9E8 55%,
                #F1FBF9 100%
            );
    }

    /* Keep content compact enough for one screen */
    .block-container {
        max-width: 900px;
        padding-top: 1.5rem;
        padding-bottom: 1rem;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #DDF5F2 0%,
                #EFFAF8 100%
            );

        border-right: 1px solid #CAE5E1;
    }

    /* Headings */
    h1 {
        color: #092F63 !important;
        font-weight: 850 !important;
        letter-spacing: -1.5px;
    }

    h2 {
        color: #092F63 !important;
        font-weight: 800 !important;
    }

    h3 {
        color: #08747D !important;
        font-weight: 750 !important;
    }

    p {
        line-height: 1.5;
    }

    /* Containers */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 22px !important;
        background: rgba(255, 255, 255, 0.92);
        border: 1px solid #E8DFC4 !important;
        box-shadow: 0 8px 25px rgba(70, 65, 35, 0.07);
    }

    /* Metrics */
    [data-testid="stMetric"] {
        background:
            linear-gradient(
                135deg,
                #FFFFFF,
                #FFF6D9
            );

        border: 1px solid #F0DFAB;
        border-radius: 18px;
        padding: 1rem;
    }

    [data-testid="stMetricValue"] {
        color: #087F8C;
        font-weight: 800;
    }

    /* Radio answers */
    [data-testid="stRadio"] label {
        border-radius: 12px;
        padding: 0.25rem 0.4rem;
        transition: background 0.2s ease;
    }

    [data-testid="stRadio"] label:hover {
        background: #F4FAF8;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        background:
            linear-gradient(
                90deg,
                #087F8C,
                #08A095
            );

        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.65rem 1.2rem;
        font-weight: 750;
    }

    .stButton > button:hover {
        color: white;
        transform: translateY(-1px);
        box-shadow: 0 6px 15px rgba(8, 127, 140, 0.20);
    }

    .stButton > button:disabled {
        opacity: 0.55;
    }

    /* Progress bar */
    [data-testid="stProgressBar"] > div > div {
        background-color: #0A9990;
    }

    [data-testid="stCaptionContainer"] {
        color: #60777C;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# LOAD DATASET
# ==================================================

try:
    data = load_data()

except FileNotFoundError:
    st.error("The dataset could not be found.")
    st.stop()

except ValueError as error:
    st.error(f"Dataset error: {error}")
    st.stop()


# ==================================================
# QUIZ SETTINGS
# ==================================================

TOTAL_QUESTIONS = 10


# ==================================================
# SESSION STATE
# ==================================================

if "quiz_question" not in st.session_state:
    st.session_state.quiz_question = generate_question(data)

if "quiz_answered" not in st.session_state:
    st.session_state.quiz_answered = False

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "quiz_total" not in st.session_state:
    st.session_state.quiz_total = 0

if "quiz_selected_answer" not in st.session_state:
    st.session_state.quiz_selected_answer = None

if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False


# ==================================================
# RESTART FUNCTION
# ==================================================

def restart_quiz():

    st.session_state.quiz_question = generate_question(data)
    st.session_state.quiz_answered = False
    st.session_state.quiz_score = 0
    st.session_state.quiz_total = 0
    st.session_state.quiz_selected_answer = None
    st.session_state.quiz_finished = False


# ==================================================
# FINISHED SCREEN
# ==================================================

if st.session_state.quiz_finished:

    st.caption("QUIZ COMPLETE")

    st.title("🏆 Quiz Complete!")

    st.write(
        "You have completed all 10 questions."
    )

    st.progress(1.0)

    score = st.session_state.quiz_score

    percentage = round(
        (score / TOTAL_QUESTIONS) * 100
    )

    with st.container(border=True):

        st.subheader("Your final result")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Correct",
                f"{score}/{TOTAL_QUESTIONS}"
            )

        with col2:
            st.metric(
                "Score",
                f"{percentage}%"
            )

        with col3:
            st.metric(
                "Questions",
                TOTAL_QUESTIONS
            )

        st.write("")

        if st.button(
            "↻ Try Again",
            use_container_width=True
        ):
            restart_quiz()
            st.rerun()

    st.stop()


# ==================================================
# ACTIVE QUIZ HEADER
# ==================================================

question = st.session_state.quiz_question

current_question = st.session_state.quiz_total + 1

# If the current question has already been answered,
# it is still the same question number.
if st.session_state.quiz_answered:
    current_question = st.session_state.quiz_total


st.caption("INTERACTIVE QUIZ")

st.title("🧠 Test Your Knowledge")

header_col1, header_col2 = st.columns([3, 1])

with header_col1:

    st.write(
        "Choose the Noongar entry that matches "
        "the English meaning."
    )

with header_col2:

    st.markdown(
        f"### Question {current_question}/{TOTAL_QUESTIONS}"
    )


# ==================================================
# PROGRESS
# ==================================================

st.progress(
    st.session_state.quiz_total / TOTAL_QUESTIONS
)


# ==================================================
# QUESTION CARD
# ==================================================

with st.container(border=True):

    st.subheader(
        "Which Noongar entry matches this English meaning?"
    )

    st.markdown(
        f"### 💬 {question['english']}"
    )

    selected_answer = st.radio(
        "Choose an answer:",
        question["options"],
        index=None,
        disabled=st.session_state.quiz_answered,
        key=f"answer_{current_question}"
    )

    if not st.session_state.quiz_answered:

        if st.button(
            "✓ Check Answer",
            use_container_width=True
        ):

            if selected_answer is None:

                st.warning(
                    "Please choose an answer before checking."
                )

            else:

                st.session_state.quiz_selected_answer = (
                    selected_answer
                )

                st.session_state.quiz_answered = True
                st.session_state.quiz_total += 1

                if (
                    selected_answer
                    == question["correct_answer"]
                ):
                    st.session_state.quiz_score += 1

                st.rerun()


# ==================================================
# FEEDBACK
# ==================================================

if st.session_state.quiz_answered:

    saved_answer = (
        st.session_state.quiz_selected_answer
    )

    if (
        saved_answer
        == question["correct_answer"]
    ):

        st.success(
            "🎉 Correct!"
        )

    else:

        st.error(
            "Not quite!"
        )

        st.info(
            f"The correct answer is "
            f"**{question['correct_answer']}**."
        )


    # ==================================================
    # QUESTION 10
    # ==================================================

    if st.session_state.quiz_total >= TOTAL_QUESTIONS:

        if st.button(
            "See Final Score →",
            use_container_width=True
        ):

            st.session_state.quiz_finished = True
            st.rerun()


    # ==================================================
    # QUESTIONS 1–9
    # ==================================================

    else:

        if st.button(
            "Next Question →",
            use_container_width=True
        ):

            st.session_state.quiz_question = (
                generate_question(data)
            )

            st.session_state.quiz_answered = False
            st.session_state.quiz_selected_answer = None

            st.rerun()