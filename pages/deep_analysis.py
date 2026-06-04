import streamlit as st
import pandas as pd

from src.analytics.deep_analysis import (
    dataset_summary,
    correlation_analysis
)

st.title("Deep Analytics")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Summary")

    st.json(
        dataset_summary(df)
    )

    st.subheader("Correlation Matrix")

    st.dataframe(
        correlation_analysis(df)
    )
