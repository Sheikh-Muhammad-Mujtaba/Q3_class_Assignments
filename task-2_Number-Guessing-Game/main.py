import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Number Guessing Game", page_icon="🎲", layout="wide")

# Custom CSS for gaming theme
st.markdown("""
<style>
/* General app background and text color */
.stApp {
    background: linear-gradient(135deg, #1a1a2e, #16213e); /* Dark blue gradient */
    color: #ffffff;
    font-family: 'Arial', sans-serif;
}

/* Title styling */
h1 {
    color: #ff6f61; /* Coral color for the title */
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

/* Instructions text styling */
p {
    color: #a8dadc; /* Light cyan for instructions */
    font-size: 1.2rem;
    text-align: center;
}

/* Button styling */
.stButton>button {
    background-color: #ff6f61; /* Coral color */
    color: #ffffff;
    border-radius: 12px;
    border: none;
    padding: 12px 28px;
    font-size: 1.1rem;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

.stButton>button:hover {
    background-color: #ff4a4a; /* Brighter coral on hover */
    transform: translateY(-2px);
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.3);
}

/* Number input field styling */
.stNumberInput>div>div>input {
    background-color: #1e1e2e; /* Darker blue */
    color: #ffffff;
    border-radius: 12px;
    border: 2px solid #ff6f61; /* Coral border */
    padding: 10px;
    font-size: 1.1rem;
    transition: all 0.3s ease;
}

.stNumberInput>div>div>input:focus {
    border-color: #ff4a4a; /* Brighter coral on focus */
    box-shadow: 0 0 8px rgba(255, 111, 97, 0.5);
}

/* Success message styling */
.stSuccess {
    color: #4caf50; /* Green for success */
    font-size: 1.2rem;
    font-weight: bold;
    text-align: center;
    background-color: rgba(76, 175, 80, 0.1); /* Light green background */
    padding: 10px;
    border-radius: 8px;
    border: 1px solid #4caf50;
}

/* Warning message styling */
.stWarning {
    color: #ffa500; /* Orange for warnings */
    font-size: 1.2rem;
    font-weight: bold;
    text-align: center;
    background-color: rgba(255, 165, 0, 0.1); /* Light orange background */
    padding: 10px;
    border-radius: 8px;
    border: 1px solid #ffa500;
}

/* Error message styling */
.stError {
    color: #ff4444; /* Red for errors */
    font-size: 1.2rem;
    font-weight: bold;
    text-align: center;
    background-color: rgba(255, 68, 68, 0.1); /* Light red background */
    padding: 10px;
    border-radius: 8px;
    border: 1px solid #ff4444;
}

/* Remaining chances text styling */
.remaining-chances {
    color: #a8dadc; /* Light cyan */
    font-size: 1.2rem;
    font-weight: bold;
    text-align: center;
    margin-top: 20px;
}

/* Play Again button styling */
.st-key-play_again>div>button {
    background-color: #00bcd4; /* Cyan for Play Again button */
    color: #ffffff;
    border-radius: 12px;
    border: none;
    padding: 12px 28px;
    font-size: 1.1rem;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

.st-key-play_again>div>button:hover {
    background-color: #00acc1; /* Darker cyan on hover */
    transform: translateY(-2px);
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.3);
}
</style>
    """, unsafe_allow_html=True)

# Title and instructions
st.title("Welcome to Number Guessing Game 🎮")
st.write("I'm thinking of a number between **50 and 100** 🤔")
st.write("You have **5 chances** to guess the number. Good Luck! 🍀")

# Function to initialize/reset the game
def initialize_game():
    """
    Initialize or reset the game state
    """
    st.session_state.number_to_guess = random.randrange(50, 100)
    st.session_state.guess_count = 0
    st.session_state.game_over = False
    st.session_state.message = ""
    st.session_state.won = False


if 'number_to_guess' not in st.session_state:
    initialize_game()
        
# Function to play sound effects
def play_sound(sound_file):
    st.markdown(f"""
        <audio autoplay>
            <source src="{sound_file}" type="audio/mp3">
        </audio>
        """, unsafe_allow_html=True)

# Number input field for user to enter their guess
guess = st.number_input(
        "Enter your guess (50-100):",
        min_value=50,
        max_value=100,
        key="guess_input"
    )

if st.button("Check", disabled=st.session_state.game_over):
    st.session_state.guess_count += 1
    remaining_chances = 5 - st.session_state.guess_count        
    if guess < st.session_state.number_to_guess:
        st.session_state.message = "Your guess is too low, Try again 😕"
    elif guess > st.session_state.number_to_guess:
        st.session_state.message = "Your guess is too high, Try again 😕"
    else:
        st.session_state.game_over = True
        st.session_state.won = True
        st.session_state.message = (f"Congratulations! You guessed the number {st.session_state.number_to_guess} in 5 tries. 🎉")
        st.balloons()
        play_sound("https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3")  # Win sound      
        
          
    if remaining_chances == 0 and not st.session_state.won:
        st.session_state.game_over = True
        st.markdown(f"<div class='stError'>Sorry! You didn't guess the number {st.session_state.number_to_guess} in 5 tries. 😔</div>", unsafe_allow_html=True)
        play_sound("https://www.soundjay.com/misc/sounds/fail-buzzer-01.mp3")  # Game over sound

if st.session_state.message:
    if st.session_state.won:
        st.markdown(f'<div class="stSuccess">{st.session_state.message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="stWarning">{st.session_state.message}</div>', unsafe_allow_html=True)

# Display remaining chances
st.markdown(f'<div class="remaining-chances">Remaining Chances: {5 - st.session_state.guess_count}</div>', unsafe_allow_html=True)


# Play Again button
if st.session_state.game_over and st.button("Play Again"):
    initialize_game()
    st.rerun()
