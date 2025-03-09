import streamlit as st

st.set_page_config(page_title="Text Analyzer", page_icon="📝", layout="wide")

# Custom CSS for enhanced UI styling
st.markdown("""
<style>
    <style>
    /* Background gradient for the entire app */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }

    .stHeading {
        text-align: center;
        background: linear-gradient(135deg, #ff6b6b 0%, #ffd93d 100%);   
        border-radius: 20px;
        margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(0, 206, 201, 0.5);
        text-shadow: 0 0 15px #000000;
        }
    
    /* Styling for input fields */
    .stTextInput>label, .stTextArea>label {
        font-weight: bold;
        font-size: 16px;
        color: #ffffff;
    }

    .stTextInput>div>input, .stTextArea>div>textarea {
        background: #ff6b6b;
        color: #ffffff;
        border: 2px solid #ff6b6b;
        border-radius: 12px;
        padding: 12px;
        transition: all 0.3s ease-in-out;
    }

    .stTextInput>div>input:focus, .stTextArea>div>textarea:focus {
        border: 2px solid #00cec9;
        box-shadow: 0 0 15px rgba(0, 206, 201, 0.5);
    }

    /* Styling for metric cards */
    .metric-card {
        background: linear-gradient(135deg, #ff6b6b 0%, #ffd93d 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(255, 107, 107, 0.3);
        text-align: center;
        font-size: 21px;
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
    }

    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 15px rgba(255, 107, 107, 0.5);
    }

    /* Styling for modified text box */
    .stCode {
        background: rgba(0, 0, 0, 0.2);
        border: 2px solid #00cec9;
        border-radius: 12px;
        font-family: 'Courier New', monospace;
        color: #ffffff;
        font-size: 14px;
        box-shadow: 0 4px 10px rgba(0, 206, 201, 0.3);
    }

    /* Custom button styling */
    .stFormSubmitButton>button {
        background: linear-gradient(45deg, #ff6b6b, #ffd93d);
        color: #ffffff;
        text-shadow: 0 0 5px #000000;
        border: none;
        padding: 12px 24px;
        border-radius: 25px;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.3s ease-in-out;
    }

    .stFormSubmitButton>button:hover {
        background: linear-gradient(45deg, #ffd93d, #ff6b6b);
        color: #ffffff;
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(255, 107, 107, 0.5);
    }
    
    .stFormSubmitButton>button:focus {
        background: linear-gradient(45deg, #ffd93d, #ff6b6b);
        color: #ffffff;
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(255, 107, 107, 0.5);
    }

    .st-emotion-cache-b0y9n5:focus:not(:active) {
        color: #ffffff;
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
        transition: all 0.5s ease !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(45deg, #ff6b6b, #ffd93d) !important;
        padding: 8px 16px !important;
        color: white !important;
        transform: scale(1.05);
    }
  

    /* Styling for alert messages */
    .stAlert {
        border: 2px solid #698f91;
        border-radius: 12px;
        color: #ff0000;
        font-weight: bold;
    }


</style>
""", unsafe_allow_html=True)

st.title("📝 Text Analyzer Tool")

# Using a form to group inputs together
with st.form(key="text_analyzer_form"):
    st.markdown("### ✍️ Input Section")
    text_input = st.text_area("**Enter your text here:**", height=200, 
                              placeholder="Paste or type your text here...")

    col1, col2 = st.columns(2)
    with col1:
        key_word = st.text_input("**Keyword to find:**", 
                                 placeholder="Enter keyword to search...")
    with col2:
        st.markdown("### 🔄 Find & Replace")
        search_word = st.text_input("**Find word:**", 
                                    placeholder="Word to search...")
        replace_word = st.text_input("**Replace with:**", 
                                     placeholder="Replacement word...")

    submit_button = st.form_submit_button("🚀 Analyze Text")

# Process input when the form is submitted
if submit_button:
    if not text_input.strip():
        st.error("❌ No text found! Please enter some text to analyze.")
    else:
        # Metrics calculation
        word_count = len(text_input.split())
        char_count = len(text_input)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = sum(1 for c in text_input.lower() if c in vowels)
        avg_word_length = char_count / word_count if word_count > 0 else 0

        # Display metrics in columns
        st.markdown("### 📊 Analysis Results")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f'<div class="metric-card">📝 <b>Words</b><br><h2>{word_count}</h2></div>', 
                        unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="metric-card">🔤 <b>Characters</b><br><h2>{char_count}</h2></div>', 
                        unsafe_allow_html=True)
        with col3:
            st.markdown(f'<div class="metric-card">🎵 <b>Vowels</b><br><h2>{vowel_count}</h2></div>', 
                        unsafe_allow_html=True)
        with col4:
            st.markdown(f'<div class="metric-card">📏 <b>Avg Word Length</b><br><h2>{avg_word_length:.2f}</h2></div>', 
                        unsafe_allow_html=True)

        # Keyword check
        if key_word:
            st.markdown("### 🔍 Keyword Search")
            if key_word in text_input:
                st.success(f"✅ **'{key_word}' Found** in the text")
            else:
                st.error(f"❌ **'{key_word}' Not Found** in the text")

        # Case conversion section
        st.markdown("### 🔠 Case Conversion")
        tab1, tab2 = st.tabs(["UPPERCASE", "lowercase"])
        
        with tab1:
            st.code(text_input.upper(), language="text")
        
        with tab2:
            st.code(text_input.lower(), language="text")

        # Search and replace functionality
        if search_word:
            modified_text = text_input.replace(search_word, replace_word)
            st.markdown("### ✨ Modified Text")
            st.code(modified_text, language="text")
