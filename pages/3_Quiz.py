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


    /* Main content */
    .block-container {
        max-width: 950px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
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
        line-height: 1.65;
    }


    /* ==================================================
       CONTAINERS
       ================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 24px !important;

        background:
            rgba(255, 255, 255, 0.92);

        border:
            1px solid #E8DFC4 !important;

        box-shadow:
            0 10px 30px
            rgba(70, 65, 35, 0.07);
    }


    /* ==================================================
       METRICS
       ================================================== */

    [data-testid="stMetric"] {
        background:
            linear-gradient(
                135deg,
                #FFFFFF,
                #FFF6D9
            );

        border:
            1px solid #F0DFAB;

        border-radius:
            18px;

        padding:
            1.2rem;

        box-shadow:
            0 7px 20px
            rgba(80, 70, 30, 0.07);
    }


    [data-testid="stMetricValue"] {
        color:
            #087F8C;

        font-weight:
            800;
    }


    /* ==================================================
       RADIO ANSWERS
       ================================================== */

    [data-testid="stRadio"] label {
        border-radius:
            14px;

        padding:
            0.4rem 0.5rem;

        transition:
            background 0.2s ease;
    }


    [data-testid="stRadio"] label:hover {
        background:
            #F4FAF8;
    }


    /* ==================================================
       BUTTONS
       ================================================== */

    .stButton > button {
        width: 100%;

        background:
            linear-gradient(
                90deg,
                #087F8C,
                #08A095
            );

        color:
            white;

        border:
            none;

        border-radius:
            50px;

        padding:
            0.7rem 1.3rem;

        font-weight:
            750;

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }


    .stButton > button:hover {
        color:
            white;

        transform:
            translateY(-2px);

        box-shadow:
            0 8px 18px
            rgba(8, 127, 140, 0.23);
    }


    .stButton > button:disabled {
        opacity:
            0.55;
    }


    /* ==================================================
       PROGRESS BAR
       ================================================== */

    [data-testid="stProgressBar"] > div > div {
        background-color:
            #0A9990;
    }


    /* ==================================================
       DIVIDERS
       ================================================== */

    hr {
        border:
            none !important;

        height:
            2px !important;

        background:
            linear-gradient(
                90deg,
                #FFC83D,
                #52BEB3,
                transparent
            ) !important;
    }


    /* Caption */
    [data-testid="stCaptionContainer"] {
        color:
            #60777C;
    }


    /* Mobile */
    @media (max-width: 800px) {

        h1 {
            font-size:
                2.8rem !important;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# PAGE HEADER
# ==================================================

with st.container(border=True):

    st.caption("INTERACTIVE QUIZ")

    st.title("🧠 Test Your Knowledge")

    st.write(
        "Test your recognition of Noongar entries using "
        "English meanings from the published wordlist."
    )

    st.info(
        "All quiz questions and answers are taken directly "
        "from the published dataset."
    )


# ==================================================
# LOAD DATASET
# ==================================================

try:
    data = load_data()

except FileNotFoundError:

    st.error(
        "The dataset could not be found."
    )

    st.stop()

except ValueError as error:

    st.error(
        f"Dataset error: {error}"
    )

    st.stop()


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


question = st.session_state.quiz_question


# ==================================================
# SCORE AREA
# ==================================================

st.write("")
st.divider()

st.header("🏆 Your score")


score_col, answered_col, accuracy_col = st.columns(
    3,
    gap="medium"
)


with score_col:

    st.metric(
        label="Correct",
        value=st.session_state.quiz_score
    )


with answered_col:

    st.metric(
        label="Answered",
        value=st.session_state.quiz_total
    )


with accuracy_col:

    if st.session_state.quiz_total == 0:

        accuracy = 0

    else:

        accuracy = round(
            (
                st.session_state.quiz_score
                / st.session_state.quiz_total
            )
            * 100
        )

    st.metric(
        label="Accuracy",
        value=f"{accuracy}%"
    )


# ==================================================
# PROGRESS
# ==================================================

if st.session_state.quiz_total > 0:

    st.progress(
        st.session_state.quiz_score
        / st.session_state.quiz_total
    )


# ==================================================
# QUESTION
# ==================================================

st.write("")
st.divider()

st.header("Question")


with st.container(border=True):

    st.subheader(
        "Which Noongar entry matches this English meaning?"
    )

    st.write("")

    st.markdown(
        f"### 💬 {question['english']}"
    )

    st.write("")

    selected_answer = st.radio(
        "Choose an answer:",
        question["options"],
        index=None,
        disabled=st.session_state.quiz_answered
    )

    st.write("")

    check_answer = st.button(
        "✓ Check Answer",
        disabled=st.session_state.quiz_answered
    )


# ==================================================
# CHECK ANSWER
# ==================================================

if check_answer:

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


        # Rerun so all interface elements immediately
        # reflect the updated session state.
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
            "🎉 Correct! Great job."
        )


    else:

        st.error(
            "Not quite — try the next one!"
        )

        st.info(
            f"The correct answer is "
            f"**{question['correct_answer']}**."
        )


# ==================================================
# NEXT QUESTION
# ==================================================

if st.session_state.quiz_answered:

    st.write("")

    if st.button(
        "Next Question  →"
    ):

        st.session_state.quiz_question = (
            generate_question(data)
        )

        st.session_state.quiz_answered = False

        st.session_state.quiz_selected_answer = None

        st.rerun()


# ==================================================
# RESTART QUIZ
# ==================================================

st.write("")
st.divider()

st.subheader("Start again")

st.write(
    "Restarting will reset your score and generate "
    "a new question."
)


if st.button(
    "↻ Restart Quiz"
):

    st.session_state.quiz_question = (
        generate_question(data)
    )

    st.session_state.quiz_answered = False

    st.session_state.quiz_score = 0

    st.session_state.quiz_total = 0

    st.session_state.quiz_selected_answer = None

    st.rerun()


# ==================================================
# FOOTER
# ==================================================

st.write("")

st.caption(
    "Noongar Language Explorer • Quiz"
)