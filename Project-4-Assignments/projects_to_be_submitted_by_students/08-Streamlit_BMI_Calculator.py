import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("⚖️ BMI Calculator")

st.markdown("---")

height = st.slider("📏 Enter your height (in cm)", 100, 250, 175)
weight = st.slider("🏋️ Enter your weight (in kg)", 40, 200, 70)

bmi: float = weight / ((height / 100) ** 2)

st.markdown(f"## 💡 Your BMI is: `{bmi:.2f}`")

if bmi < 18.5:
    category: str = "🔹 Underweight"
elif 18.5 <= bmi < 25:
    category: str = "✅ Normal weight"
elif 25 <= bmi < 30:
    category: str = "⚠️ Overweight"
else:
    category: str = "🔴 Obesity"

st.markdown(f"### 🧬 Category: {category}")

st.markdown("---")

st.markdown("#### 📊 BMI Categories")
st.markdown("""
- 🔹 **Underweight**: BMI less than 18.5  
- ✅ **Normal weight**: BMI between 18.5 and 24.9  
- ⚠️ **Overweight**: BMI between 25 and 29.9  
- 🔴 **Obesity**: BMI 30 or greater  
""")
