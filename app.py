import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit page configuration
st.set_page_config(page_title="Data Visualizer", layout="wide")

st.title("📊 Visualizations")

# Upload your CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the dataset
    df = pd.read_csv(uploaded_file)

    # Show data preview
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # Dropdown to select visualization
    chart_type = st.selectbox("Choose Visualization", [
        "Correlation Heatmap",
        "Missing Values Heatmap",
        "Basic Statistics"
    ])

    if chart_type == "Correlation Heatmap":
        st.subheader("Correlation Heatmap")

        # Select numeric columns only
        numeric_df = df.select_dtypes(include=[np.number])

        if numeric_df.empty:
            st.error("No numeric columns found in the dataset.")
        else:
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.heatmap(
                numeric_df.corr(),
                annot=True,
                fmt=".2f",
                cmap="coolwarm",
                ax=ax
            )
            st.pyplot(fig)

    elif chart_type == "Missing Values Heatmap":
        st.subheader("Missing Values Heatmap")
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(df.isnull(), cbar=False, cmap="viridis", ax=ax)
        st.pyplot(fig)

    elif chart_type == "Basic Statistics":
        st.subheader("Descriptive Statistics")
        st.write(df.describe())

else:
    st.info("📁 Please upload a CSV file to begin.")
