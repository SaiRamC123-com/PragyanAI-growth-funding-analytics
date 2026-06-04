import streamlit as st
import pandas as pd

from utils.insights import generate_business_insights

st.title("AI Insights")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    insights = generate_business_insights(df)

    for insight in insights:

        st.info(insight)
