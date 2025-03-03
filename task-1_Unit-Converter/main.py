import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()

# Configure Gemini AI API
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)


# Use a valid Gemini model
model = genai.GenerativeModel("gemini-1.5-pro")

def get_conversion_result(query):
    try:
        response = model.generate_content(query)
        return response.text if response else "No response received."
    except Exception as e:
        return f"Error: {str(e)}"

# Set Page Config
st.set_page_config(page_title="🔁 Unit Converter App", page_icon="🔁", layout="wide")
st.title("🔁 Unit Converter App")

st.markdown("""
    <style>
    /* Global styles */
    body {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #1e3c72, #2a5298) !important;
        color: #ffffff !important;
    }

    /* Override default Streamlit background */
    .stApp {
        background: linear-gradient(135deg, #1e3c72, #2a5298) !important;
        padding: 20px;
    }

    /* Sidebar styling */
    .stSidebar {
        background: linear-gradient(135deg, #2a5298, #1e3c72) !important;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    /* Title styling */
    .stTitle {
        color: #ffffff !important;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Input fields styling */
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>select {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 8px;
        padding: 10px;
        font-size: 1rem;
    }

    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #00c6ff, #0072ff) !important;
        color: #ffffff !important;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #0072ff, #00c6ff) !important;
        transform: scale(1.05);
    }

    /* Success message styling */
    .stSuccess {
        background-color: rgba(0, 255, 0, 0.1) !important;
        color: #00ff00 !important;
        border: 1px solid #00ff00;
        border-radius: 8px;
        padding: 10px;
        margin: 10px 0;
    }

    /* Warning message styling */
    .stWarning {
        background-color: rgba(255, 255, 0, 0.1) !important;
        color: #ffff00 !important;
        border: 1px solid #ffff00;
        border-radius: 8px;
        padding: 10px;
        margin: 10px 0;
    }

    /* History section styling */
    .stSubheader {
        color: #ffffff !important;
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 20px;
    }

    .stWrite {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: #ffffff !important;
        border-radius: 8px;
        padding: 10px;
        margin: 10px 0;
    }

    /* Tabs styling */
    .stTabs>div>button {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: #ffffff !important;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 1rem;
        font-weight: bold;
        font-color: #e1e815 !important;
        transition: all 0.3s ease;
    }
    
    .stTabs {
        color: #e1e815 !important;
    }
    
    .stTabs>div>button:focus {
        background-color: rgba(255, 255, 255, 0.2) !important;
        color: #00c6ff !important;
    }
    .stTabs>div>button:hover {
        background-color: rgba(255, 255, 255, 0.2) !important;
        color: #00c6ff !important;
    }

    .stTabs .stMarkdown {
        background: linear-gradient(135deg, #154ae8, #0f72ff) !important;
        color: #ffffff !important;
    }
    
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        color: #ffffff;
        underline: none;
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] [data-testid="stMarkdownContainer"] p {
        color: #0cedd6;
        underline: solid #ffffff;
    }

    /* Gradient background for the main content */
    .stMarkdown:not(:has(style)):not(:has(css)) {
        background: linear-gradient(135deg, rgba(30, 60, 114, 0.8), rgba(42, 82, 152, 0.8)) !important;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
</style>
""", unsafe_allow_html=True)


with st.sidebar:
    tab1, tab2 = st.tabs(["Gemini AI Conversion", "Settings"])
    with tab1:
        st.title("Gemini AI Conversion 🤖")
        query = st.text_input("💬 Enter your conversion query (e.g, 'Convert 5 miles to kilometers'):")
        if st.button("Ask Gemini AI 🚀"):
            if query:
                result = get_conversion_result(query)
                if any(unit in query.lower() for unit in ["km", "miles", "kg", "grams", "celsius", "fahrenheit", "inches", "cm", "meters", "feet", "pounds", "kilograms" , "liters", "gallons", "ounces", "milliliters"]):
                    st.success(f"✅ Result: \n {result}")
                else:
                    st.warning("⚠️ Please ask only about unit conversions.")
            else:
                st.warning("⚠️ Please enter a conversion query.")
    with tab2:
        st.title("Unit Converter Information ℹ️")
        st.markdown("""
        - **Length Converter:** Convert Kilometers to Miles, Miles to Kilometers, Meters to Feet, Feet to Meters.
        - **Weight Converter:** Convert Kilograms to Pounds, Pounds to Kilograms, Grams to Ounces, Ounces to Grams.
        - **Temperature Converter:** Convert Celsius to Fahrenheit, Fahrenheit to Celsius.
        - **Time Converter:** Convert Hours to Minutes, Minutes to Seconds, Seconds to Milliseconds, Milliseconds to Seconds.
        - **Speed Converter:** Convert Kilometers per Hour to Miles per Hour, Miles per Hour to Kilometers per Hour.
        - **Data Converter:** Convert Megabytes to Gigabytes, Gigabytes to Megabytes, Gigabytes to Terabytes, Terabytes to Gigabytes, Kilobytes to Megabytes, Megabytes to Kilobytes, Bytes to Kilobytes, Kilobytes to Bytes
        """)
        reset_button = st.button("🔄 Reset All")
        if reset_button:
            st.session_state.clear()
        

st.write("Convert Length, Weight, Temperature, Time, Speed, Data Units and etc. with Ease! 📏⚖️🌡️⏰🚗💾")

conversion_type = st.selectbox("📌 Choose Conversion Type", [
        "Length Converter", "Weight Converter", "Temperature Converter", 
        "Time Converter", "Speed Converter", "Data Converter"
    ])
    
options = {
        "Length Converter": ["Kilometers to Miles", "Miles to Kilometers", "Meters to Feet", "Feet to Meters"],
        "Weight Converter": ["Kilograms to Pounds", "Pounds to Kilograms", "Grams to Ounces", "Ounces to Grams"],
        "Temperature Converter": ["Celsius to Fahrenheit", "Fahrenheit to Celsius"],
        "Time Converter": ["Hours to Minutes", "Minutes to Seconds", "Seconds to Milliseconds", "Milliseconds to Seconds"],
        "Speed Converter": ["Kilometers per Hour to Miles per Hour", "Miles per Hour to Kilometers per Hour"],
        "Data Converter": ["Megabytes to Gigabytes", "Gigabytes to Megabytes" , "Gigabytes to Terabytes", "Terabytes to Gigabytes", "Kilobytes to Megabytes", "Megabytes to Kilobytes", "Bytes to Kilobytes", "Kilobytes to Bytes"]
    }

result = ""  # Default value to prevent errors
    
choice = st.selectbox("🔽 Select Conversion", options[conversion_type])
value = st.number_input("✏️ Enter Value", min_value=0.0, format="%.4f")


conversions = {
        "Kilometers to Miles": value * 0.621371,
        "Miles to Kilometers": value * 1.60934, #1
        "Meters to Feet": value * 3.28084,
        "Feet to Meters": value * 0.3048, #2
        "Kilograms to Pounds": value * 2.20462,
        "Pounds to Kilograms": value * 0.453592,#3
        "Grams to Ounces": value * 0.035274,
        "Ounces to Grams": value * 28.3495,#4
        "Celsius to Fahrenheit": (value * 9/5) + 32,
        "Fahrenheit to Celsius": (value - 32) * 5/9,#5
        "Hours to Minutes": value * 60,
        "Minutes to Seconds": value * 60,
        "Seconds to Milliseconds": value * 1000,
        "Milliseconds to Seconds": value / 1000,#6
        "Kilometers per Hour to Miles per Hour": value * 0.621371,
        "Miles per Hour to Kilometers per Hour": value * 1.60934,#7
        "Megabytes to Gigabytes": value / 1024,
        "Gigabytes to Megabytes": value * 1024,#8
        "Gigabytes to Terabytes": value / 1024,
        "Terabytes to Gigabytes": value * 1024,#9
        "Kilobytes to Megabytes": value / 1024,
        "Megabytes to Kilobytes": value * 1024,#10
        "Bytes to Kilobytes": value / 1024,
        "Kilobytes to Bytes": value * 1024,#11
    }
    
if choice in conversions:
    result = f"📌 {value} {choice.split()[0]} = {conversions[choice]:.4f} {choice.split()[-1]}"
    st.success(result)    
if 'history' not in st.session_state:
    st.session_state['history'] = []    
if st.button("💾 Add to History") and result:
    st.session_state['history'].append(result)    
if st.session_state['history']:
    st.subheader("📜 Conversion History")
    for i, entry in enumerate(st.session_state['history'], 1):
        st.write(f"{i}. {entry}")    
if st.button("🗑️ Clear History"):
    st.session_state['history'] = []
    st.success("🧹 History cleared!")    
