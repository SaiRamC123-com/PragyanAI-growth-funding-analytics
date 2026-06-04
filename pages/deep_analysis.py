import streamlit as st
import pandas as pd

st.title("Deep Analytics")

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Shape")

    st.write(df.shape)

    st.subheader("Missing Values")

    st.write(df.isnull().sum())

    st.subheader("Duplicate Rows")

    st.write(df.duplicated().sum())

    st.subheader("Statistical Summary")

    st.dataframe(
        df.describe()
    )

    st.subheader("Correlation Matrix")

    numeric_df = df.select_dtypes(
        include="number"
    )

    st.dataframe(
        numeric_df.corr()
    )
