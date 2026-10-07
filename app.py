import streamlit as st
import random
import time

st.set_page_config(
    page_title="Shivani's Rock Paper Scissors",
    page_icon="🍋",
    layout="centered"
)

# =========================
# ANIMATED STYLE
# =========================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #F9FFB5 0%,
        #EFFF8A 35%,
        #FFFFFF 70%,
        #F5FF9A 100%
    );
    overflow-x: hidden;
}

/* Remove dark colors */
html, body, [class*="css"] {
    color: #6A8500;
}

/* Floating background emojis */

.floating {
    position: fixed;
    z-index: 0;
    opacity: 0.18;
    pointer-events: none;
    animation: floatAround 10s infinite ease-in-out;
}

.f1 {
    top: 12%;
    left: 5%;
    font-size: 55px;
    animation-delay: 0s;
}

.f2 {
    top: 25%;
    right: 5%;
    font-size: 65px;
    animation-delay: 2s;
}

.f3 {
    bottom: 15%;
    left: 8%;
    font-size: 60px;
    animation-delay: 4s;
}

.f4 {
    bottom: 25%;
    right: 8%;
    font-size: 50px;
    animation-delay: 6s;
}

.f5 {
    top: 55%;
    left: 45%;
    font-size: 45px;
    animation-delay: 1s;
}

@keyframes floatAround {

    0% {
        transform: translateY(0px) rotate(0deg);
    }

    25% {
        transform: translateY(-25px) rotate(15deg);
    }

    50% {
        transform: translateY(15px) rotate(-15deg);
    }

    75% {
        transform: translateY(-20px) rotate(10deg);
    }

    100% {
        transform: translateY(0px) rotate(0deg);
    }
}


/* Main title */

.main-title {
    text-align: center;
    font-size: 46px;
    font-weight: 900;
    color: #7A9700;
    animation: titleGlow 2.5s infinite alternate;
    margin-top: 10px;
}

@keyframes titleGlow {
    from {
        transform: scale(1);
        text-shadow: 0 0 5px #E7F85A;
    }

    to {
        transform: scale(1.03);
        text-shadow: 0 0 22px #D7EC45;
    }
}

.subtitle {
    text-align: center;
    color: #9AAE22;
    font-size: 19px;
    font-weight: 600;
}


/* Game container */

.game-card {
    background: rgba(255,255,255,0.88);
    border-radius: 30px;
    padding: 25px;
    border: 3px solid #E5F36A;
    box-shadow:
        0 10px 35px rgba(190,210,40,0.25);
}


/* Score cards */

.score-card {
    background: linear-gradient(
        145deg,
        #FFFFFF,
        #F8FFB9
    );

    border-radius: 22px;
    padding: 16px;
    text-align: center;

    border: 2px solid #E4F15B;

    box-shadow:
        0 7px 18px rgba(190,210,40,0.18);

    transition: 0.3s;
}

.score-card:hover {
    transform: translateY(-7px) scale(1.03);
}


/* Choice buttons */

div.stButton > button {

    background: linear-gradient(
        135deg,
        #F4FF64,
        #DDF45A
    );

    color: #6F8500;

    border: 3px solid #D4E943;

    border-radius: 22px;

    min-height: 65px;

    font-size: 19px;
    font-weight: 900;

    box-shadow:
        0 7px 15px rgba(190,210,40,0.25);

    transition: all 0.25s ease;
}

div.stButton > button:hover {

    background: linear-gradient(
        135deg,
        #E8FA3E,
        #F8FF75
    );

    transform: translateY(-6px) scale(1.04);

    box-shadow:
        0 12px 25px rgba(190,210,40,0.35);
}

div.stButton > button:active {
    transform: scale(0.96);
}


/* Result */

.result-box {

    background: linear-gradient(
        135deg,
        #FFFFFF,
        #F8FFB8
    );

    border: 3px solid #DCEB48;

    border-radius: 28px;

    padding: 25px;

    text-align: center;

    animation: resultPop 0.6s ease;

    box-shadow:
        0 10px 30px rgba(190,210,40,0.25);
}

@keyframes resultPop {

    0% {
        opacity: 0;
        transform: scale(0.7);
    }

    70% {
        transform: scale(1.08);
    }

    100% {
        opacity: 1;
        transform: scale(1);
    }
}


/* Section headings */

h1, h2, h3 {

    color: #819900 !important;
}


/* Info box */

[data-testid="stAlert"] {

    background: #FFFFE7 !important;

    border: 2px solid #E3F05A !important;

    border-radius: 20px !important;

}


/* Footer */

.footer {

    text-align: center;

    color: #A0B52A;

    font-size: 15px;

    margin-top: 30px;

    animation: fadeIn 2s ease;
}

@keyframes fadeIn {

    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}


/* Lemon decoration */

.lemon-decoration {

    text-align: center;

    font-size: 30px;

    letter-spacing: 12px;

    animation: lemonBounce 3s infinite ease-in-out;
}

@keyframes lemonBounce {

    0%, 100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-8px);
    }
}

</style>


<div class="floating f1">✂️</div>
<div class="floating f2">🪨</div>
<div class="floating f3">📄</div>
<div class="floating f4">✂️</div>
<div class="floating f5">🍋</div>

""", unsafe_allow_html=True)


# =========================
# TITLE
# =========================

st.markdown(
    '<div class="main-title">🍋 Shivani\'s Rock Paper Scissors 🎮</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Choose your move • Beat the computer • Have fun!</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="lemon-decoration">🍋 ✨ 🍋 ✨ 🍋</div>',
    unsafe_allow_html=True
)


# =========================
# SCORE
# =========================

if "player_score" not in st.session_state:
    st.session_state.player_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "draw_score" not in st.session_state:
    st.session_state.draw_score = 0


st.markdown("### 🏆 Your Scoreboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="score-card">
        👩<br>
        <b>You</b>
        <h2>{st.session_state.player_score}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="score-card">
        🤝<br>
        <b>Draw</b>
        <h2>{st.session_state.draw_score}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="score-card">
        🤖<br>
        <b>Computer</b>
        <h2>{st.session_state.computer_score}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")


# =========================
# GAME LOGIC
# =========================

def play_game(player):

    computer = random.choice(
        ["Rock", "Paper", "Scissors"]
    )

    if player == computer:
        result = "draw"

    elif (
        (player == "Rock" and computer == "Scissors")
        or
        (player == "Paper" and computer == "Rock")
        or
        (player == "Scissors" and computer == "Paper")
    ):
        result = "win"

    else:
        result = "lose"

    return computer, result


# =========================
# CHOICES
# =========================

st.markdown("### 🎯 Make Your Move")

col1, col2, col3 = st.columns(3)

with col1:
    rock = st.button(
        "🪨 ROCK",
        use_container_width=True
    )

with col2:
    paper = st.button(
        "📄 PAPER",
        use_container_width=True
    )

with col3:
    scissors = st.button(
        "✂️ SCISSORS",
        use_container_width=True
    )


player_choice = None

if rock:
    player_choice = "Rock"

elif paper:
    player_choice = "Paper"

elif scissors:
    player_choice = "Scissors"


# =========================
# RESULT
# =========================

if player_choice:

    computer_choice, result = play_game(player_choice)

    if result == "win":

        st.session_state.player_score += 1

        st.balloons()

        message = "🎉 YOU WON! 🎉"

        st.success(
            "Amazing! You defeated the computer! 🍋💚"
        )

    elif result == "lose":

        st.session_state.computer_score += 1

        message = "🤖 COMPUTER WON!"

        st.info(
            "Good try! Next round is yours! 🍋✨"
        )

    else:

        st.session_state.draw_score += 1

        message = "🤝 IT'S A DRAW!"

        st.info(
            "Great minds think alike! 😄🍋"
        )


    st.markdown(
        f"""
        <div class="result-box">

        <h2>{message}</h2>

        <p>👩 Your Choice</p>
        <h3>{player_choice}</h3>

        <p>🤖 Computer Choice</p>
        <h3>{computer_choice}</h3>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================
# NEW GAME
# =========================

st.write("")

if st.button(
    "🍋 NEW GAME",
    use_container_width=True
):

    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.draw_score = 0

    st.rerun()


# =========================
# RULES
# =========================

st.write("")

st.markdown("### 🍋 How To Play")

st.info(
    "🪨 Rock beats ✂️ Scissors\n\n"
    "📄 Paper beats 🪨 Rock\n\n"
    "✂️ Scissors beats 📄 Paper"
)


# =========================
# FOOTER
# =========================

st.markdown(
    """
    <div class="footer">
    🍋 Made with 💛 by Shivani • Play • Win • Repeat! 🌿
    </div>
    """,
    unsafe_allow_html=True
)