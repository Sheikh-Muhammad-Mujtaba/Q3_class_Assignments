import streamlit as st
import string
import random


def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))


def password_strength_meter(password):
    strength = "Baba Eww 😂"
    score = 0

    if len(password) < 8:
        return 0, strength
    elif len(password) < 12:
        score += 1
    else:
        score += 2

    if any(char.isdigit() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1
    if score < 2:
        strength = "Baba Eww 😂"
    elif score < 3:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    elif score == 5:
        strength = "Very Strong"

    return score, strength


st.set_page_config(page_title="Password Strength Meter", page_icon="🔒",
                   layout="centered", initial_sidebar_state="expanded")
st.markdown("""
    <style>
    /* Main app container styling */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        min-height: 100vh;
        font-family: 'Segoe UI', sans-serif;
        color: #ffffff;
    }

    .stAppHeader {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        color: white;
    }
    
    /* Header styling with 3D effect */
    .stHeading {
    text-align: center;
    padding: 1rem 2rem;
    color: linear-gradient(45deg, #ff6b6b 20%, #ffd93d 70%, #ff6b6b 100%);
    border-radius: 15px;
    text-shadow: 
        2px 2px 4px rgba(0, 0, 0, 0.3),
        4px 4px 8px rgba(255, 107, 107, 0.4);
    padding-bottom: 0.2em;
    display: inline-block;
    margin-bottom: 1rem;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease-in-out;
}

/* Success message styling */
    .stAlert {
        border: 1px solid #ffffff;
        border-radius: 8px;
        margin: 10px 0;
    }

    /* Markdown text styling */
    .stMarkdown {
        color: #ffffffdd;
        font-size: 1.1rem;
        line-height: 1.6;
    }

    /* Custom button styling */
    .stButton>button {
        background: linear-gradient(45deg, #ff6b6b, #ffd93d);
        color: white;
        border: none;
        padding: 12px 20px;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 12px;
        transition: all 0.3s ease-in-out;
        cursor: pointer;
        text-transform: uppercase;
        box-shadow: 0px 4px 10px rgba(255, 107, 107, 0.3);
    }

    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 6px 15px rgba(255, 217, 61, 0.4);
    }

    .stButton>button:active {
        transform: scale(0.98);
        box-shadow: 0px 2px 8px rgba(255, 217, 61, 0.3);
    }

    /* Enhanced sidebar styling */
    .st-emotion-cache-6qob1r {
        background: linear-gradient(45deg, #1a1a2e, #16213e) !important;
        box-shadow: 5px 0 15px rgba(0, 0, 0, 0.2);
    }

    /* Tab styling */
    .stTabs [role="tablist"] {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px;
        padding: 8px;
    }

    .stTabs [role="tab"] {
        color: #ffffffaa !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(45deg, #ff6b6b, #ffd93d) !important;
        padding: 8px 16px !important;
        color: white !important;
        transform: scale(1.05);
    }

    /* Help item cards */
    .help-item {
        background: linear-gradient(145deg, rgba(255,107,107,0.1), rgba(255,217,61,0.1));
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        border: 1px solid #ff6b6b33;
        backdrop-filter: blur(10px);
    }

    /* Tip box animations */
    .tip-box {
        background: linear-gradient(145deg, rgba(255,107,107,0.15), rgba(255,217,61,0.15));
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        transform-style: preserve-3d;
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .tip-box:hover {
        transform: perspective(1000px) rotateX(5deg) rotateY(5deg);
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
    }

    /* Floating animation for generated password (preserved) */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    .stCode {
        animation: float 3s ease-in-out infinite;
        background: rgba(0, 0, 0, 0.3) !important;
        border: 2px solid #ff6b6b !important;
        border-radius: 15px;
        padding: 1rem !important;
        font-size: 1.4rem;
        letter-spacing: 2px;
    }

    /* Footer styling */
    .footer {
        position: relative;
        margin-top: 3rem;
        padding: 2rem;
        bottom: -20vh;
        border-top: 1px solid #ff6b6b33;
        text-align: center;
        text-shadow: 0 -5px 15px rgba(0, 0, 0, 0.2);
    }

    /* Checkbox styling */
    .stCheckbox [role="checkbox"] {
        border: 2px solid #ff6b6b !important;
        background: rgba(255, 107, 107, 0.1) !important;
    }

    .stCheckbox [role="checkbox"]:checked {
        background: #ff6b6b !important;
    }

    /* Slider thumb styling */
    .stSlider .st-az {
        background: #ff6b6b !important;
        border: 2px solid white !important;
        box-shadow: 0 0 10px rgba(255, 107, 107, 0.5);
    }
</style>
""", unsafe_allow_html=True)


with st.sidebar:
    tab1, tab2, tab3 = st.tabs(["Generate Password", "Help", "Security Tips"])
    with tab1:
        st.title("🔐 Password Generator")
        length = st.slider("📏 Length of password",
                           min_value=8, max_value=30, value=16)
        use_digits = st.checkbox("🔢 Use digits")
        use_special = st.checkbox("✨ Use special characters")

        if st.button("Generate Password 🚀"):
            password = generate_password(length, use_digits, use_special)
            st.write(f"**🔒 Generated Password:**")
            st.code(password, language="text")

    with tab2:
        st.markdown("""
        <div class="help-item">
            <h3>📌 How to Use</h3>
            <ol>
                <li>Go to the 'Generate Password' tab</li>
                <li>Select password length (8-30 characters)</li>
                <li>Choose character types (digits/special characters)</li>
                <li>Click 'Generate Password'</li>
            </ol>
        </div>

        <div class="help-item">
            <h3>🔑 Strength Criteria</h3>
            <div class="strength-criteria">
                <p>✔️ Length (8+ characters)</p>
                <p>✔️ Uppercase & lowercase letters</p>
                <p>✔️ Numbers (0-9)</p>
                <p>✔️ Special characters (!@#$%^&*)</p>
            </div>
        </div>

        <div class="help-item">
            <h3>📊 Strength Ratings</h3>
            <p>💪 <strong>Very Strong (5 points):</strong> 12+ chars with all character types</p>
            <p>🛡️ <strong>Strong (4 points):</strong> 10+ chars with 3 character types</p>
            <p>⚠️ <strong>Moderate (3 points):</strong> 8+ chars with 2 character types</p>
            <p>🚨 <strong>Weak (0-2 points):</strong> Below minimum requirements</p>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
        <div class="tip-box">
            <h3>🔐 Password Best Practices</h3>
            <p>➊ Use 12+ characters with mixed character types</p>
            <p>➋ Avoid personal information & common phrases</p>
            <p>➌ Change passwords every 3-6 months</p>
        </div>

        <div class="tip-box">
            <h3>🛡️ Account Protection</h3>
            <p>➍ Enable 2-factor authentication (2FA)</p>
            <p>➎ Use unique passwords for each account</p>
            <p>➏ Monitor for suspicious activity</p>
        </div>

        <div class="tip-box">
            <h3>📱 Device Security</h3>
            <p>➐ Keep software updated</p>
            <p>➑ Use antivirus software</p>
            <p>➒ Avoid public Wi-Fi for sensitive tasks</p>
        </div>

        <div class="tip-box">
            <h3>🧠 Security Mindset</h3>
            <p>➓ Be cautious of phishing attempts</p>
            <p>⓫ Verify website security (HTTPS)</p>
            <p>⓬ Use password managers</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('<div class="footer">Stay safe and secure online!</div>',
                unsafe_allow_html=True)


st.title("Password Strength Meter")
st.markdown("💡 *'A strong password is the first step to digital security.'*")
st.write("Enter your password to check its strength")
user_input = st.text_input("Enter your password", type="password")
if user_input:
    score, strength = password_strength_meter(user_input)
    st.write(f"Password Strength: {strength}")
    st.progress(score / 5)

    if strength == "Baba Eww 😂":
        st.error("🤣 'Baba Eww! Your password is so weak, it’s practically begging to be cracked. Time to level up!'")
    elif strength == "Weak":
        st.info("🔴 'A weak password is like a paper shield—it won’t protect you when it matters most. Time to level up!'")
    elif strength == "Moderate":
        st.info(
            "🟡 'Your password is like a sturdy lock—but it could use a few more bolts to be truly secure!'")
    elif strength == "Strong":
        st.info(
            "🟢 'A strong password is like a fortress wall—hard to crack and built to last. Great job!'")
    else:
        st.info("💪 'A very strong password is like an impenetrable vault—your data is safe and sound. You’re unstoppable!'")

    if strength == "Baba Eww 😂":
        st.error("🤣 **Baba Eww Password Alert!** Your password is too weak. Time to level up and make it strong.")
    elif strength == "Weak":
        st.error("🚨 **Weak Password Alert!** Your password is too easy to crack. Add uppercase, lowercase, numbers, and special characters to fortify it!")
    elif strength == "Moderate":
        st.warning("⚠️ **Moderate Password Warning!** Your password is decent, but it’s not bulletproof. Add more complexity to make it stronger!")
    elif strength == "Strong":
        st.success(
            "✅ **Strong Password!** Your password is solid and secure. Keep up the good work!")
    else:
        st.success(
            "🌟 **Very Strong Password!** Your password is a fortress! You’ve mastered the art of password security!")


st.markdown('<div class="footer">Made with ❤️ by Mujtaba | 🌟 Enjoy your secure passwords!</div>',
            unsafe_allow_html=True)
