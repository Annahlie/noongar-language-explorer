import streamlit as st

from src.data_loader import load_data
from src.quiz import generate_question


st.title("🧠 Quiz")

st.write(
    "Test your recognition of Noongar entries using meanings "
    "from the published wordlist."
)

st.caption(
    "All quiz questions and answers are taken directly from "
    "the published dataset."
)


# -----------------------------
# Load dataset
# -----------------------------
try:
    data = load_data()

except FileNotFoundError:
    st.error("The dataset could not be found.")
    st.stop()

except ValueError as error:
    st.error(f"Dataset error: {error}")
    st.stop()


# -----------------------------
# Session state setup
# -----------------------------
if "quiz_question" not in st.session_state:
    st.session_state.quiz_question = generate_question(data)

if "quiz_answered" not in st.session_state:
    st.session_state.quiz_answered = False

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "quiz_total" not in st.session_state:
    st.session_state.quiz_total = 0


question = st.session_state.quiz_question


# -----------------------------
# Score display
# -----------------------------
st.subheader("Score")

st.write(
    f"{st.session_state.quiz_score} correct "
    f"out of {st.session_state.quiz_total} answered"
)


# -----------------------------
# Question
# -----------------------------
st.subheader("Question")

st.write(
    f"Which Noongar entry matches the English meaning "
    f"**'{question['english']}'**?"
)


selected_answer = st.radio(
    "Choose an answer:",
    question["options"],
    index=None
)


# -----------------------------
# Check answer
# -----------------------------
if st.button(
    "Check Answer",
    disabled=st.session_state.quiz_answered
):

    if selected_answer is None:
        st.warning(
            "Please choose an answer before checking."
        )

    else:
        st.session_state.quiz_answered = True
        st.session_state.quiz_total += 1

        if selected_answer == question["correct_answer"]:
            st.session_state.quiz_score += 1

# -----------------------------
# Keep feedback visible
# -----------------------------
if st.session_state.quiz_answered:

    if selected_answer == question["correct_answer"]:
        st.success("Correct!")

    else:
        st.error("Not quite.")

        st.info(
            f"The correct answer is "
            f"**{question['correct_answer']}**."
        )

# -----------------------------
# Next question
# -----------------------------
if st.session_state.quiz_answered:

    if st.button("Next Question"):

        st.session_state.quiz_question = generate_question(data)
        st.session_state.quiz_answered = False

        st.rerun()

# -----------------------------
# Restart quiz
# -----------------------------
st.divider()

if st.button("Restart Quiz"):

    st.session_state.quiz_question = generate_question(data)
    st.session_state.quiz_answered = False
    st.session_state.quiz_score = 0
    st.session_state.quiz_total = 0

    st.rerun()