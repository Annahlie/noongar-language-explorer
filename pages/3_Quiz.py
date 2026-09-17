import streamlit as st

from src.data_loader import load_data
from src.quiz import generate_question


# ---------------------------------------------------------
# Page heading
# ---------------------------------------------------------

st.title("🧠 Noongar Language Quiz")

st.write(
    "Choose the Noongar entry that matches the English meaning."
)


# ---------------------------------------------------------
# Load dataset
# ---------------------------------------------------------

try:
    data = load_data()

except FileNotFoundError:
    st.error("The dataset could not be found.")
    st.stop()

except ValueError as error:
    st.error(f"Dataset error: {error}")
    st.stop()


# ---------------------------------------------------------
# Session state setup
# ---------------------------------------------------------

if "quiz_question" not in st.session_state:
    st.session_state.quiz_question = generate_question(data)

if "quiz_answered" not in st.session_state:
    st.session_state.quiz_answered = False

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "quiz_total" not in st.session_state:
    st.session_state.quiz_total = 0

if "quiz_submitted_answer" not in st.session_state:
    st.session_state.quiz_submitted_answer = None

question = st.session_state.quiz_question


# ---------------------------------------------------------
# Score
# ---------------------------------------------------------

st.markdown(
    f"**Score:** {st.session_state.quiz_score} correct "
    f"out of {st.session_state.quiz_total} answered"
)


# ---------------------------------------------------------
# Question
# ---------------------------------------------------------

st.markdown(
    f"#### Which Noongar entry matches "
    f"**'{question['english']}'**?"
)

selected_answer = st.radio(
    "Choose an answer",
    question["options"],
    index=None,
    disabled=st.session_state.quiz_answered,
    label_visibility="collapsed"
)


# ---------------------------------------------------------
# Quiz controls
# ---------------------------------------------------------

st.write("")

left_col, right_col = st.columns(2)

with left_col:
    if not st.session_state.quiz_answered:
        check_answer = st.button(
            "Check Answer",
            type="primary",
            use_container_width=True
        )

    else:
        check_answer = False

        if st.button(
            "Next Question",
            icon="➡️",
            use_container_width=True
        ):
            st.session_state.quiz_question = generate_question(data)
            st.session_state.quiz_answered = False
            st.session_state.quiz_submitted_answer = None
            st.rerun()

with right_col:
    if st.button(
        "Restart Quiz",
        icon="🔄",
        use_container_width=True
    ):
        st.session_state.quiz_question = generate_question(data)
        st.session_state.quiz_answered = False
        st.session_state.quiz_submitted_answer = None
        st.session_state.quiz_score = 0
        st.session_state.quiz_total = 0
        st.rerun()


# ---------------------------------------------------------
# Check answer
# ---------------------------------------------------------

if check_answer:
    if selected_answer is None:
        st.warning("Please choose an answer before checking.")

    else:
        st.session_state.quiz_submitted_answer = selected_answer
        st.session_state.quiz_answered = True
        st.session_state.quiz_total += 1

        if selected_answer == question["correct_answer"]:
            st.session_state.quiz_score += 1

        st.rerun()


# ---------------------------------------------------------
# Feedback
# ---------------------------------------------------------

if st.session_state.quiz_answered:
    st.write("")

    submitted_answer = st.session_state.quiz_submitted_answer

    if submitted_answer == question["correct_answer"]:
        st.success("Correct!")

    else:
        st.error(
            f"Not quite. The correct answer is "
            f"**{question['correct_answer']}**."
        )