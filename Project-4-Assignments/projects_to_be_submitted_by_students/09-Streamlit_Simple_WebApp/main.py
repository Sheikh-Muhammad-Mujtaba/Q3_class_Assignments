import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="📊 Simple Data Dashboard",
    layout="wide",
    page_icon="📈"
)

st.title("📊 Simple Data Dashboard")
st.markdown("Upload a CSV file to explore, filter, and visualize your data.")

uploaded_file = st.file_uploader("📁 Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("✅ File successfully uploaded!")

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head(), use_container_width=True)

    st.subheader("📋 Data Summary")
    st.dataframe(df.describe(), use_container_width=True)

    st.subheader("🔎 Filter Data")
    with st.expander("Apply Filter"):
        columns = df.columns.tolist()
        selected_column = st.selectbox("Select column to filter by", columns)
        unique_values = df[selected_column].dropna().unique()
        selected_value = st.selectbox("Select value", sorted(unique_values))

        filtered_df = df[df[selected_column] == selected_value]
        st.markdown(f"Showing rows where **{selected_column} = {selected_value}**")
        st.dataframe(filtered_df, use_container_width=True)

    st.subheader("📈 Plot Data")

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    if numeric_columns:
        x_column = st.selectbox("Select X-axis (Index)", df.columns)
        y_column = st.selectbox("Select Y-axis (Numeric)", numeric_columns)

        if st.button("Generate Line Chart"):
            try:
                st.line_chart(filtered_df.set_index(x_column)[y_column])
            except Exception as e:
                st.error(f"🚫 Error while plotting: {e}")
    else:
        st.warning("⚠️ No numeric columns available for plotting.")
else:
    st.info("⬆️ Please upload a CSV file to get started.")
