import streamlit as st
import pandas as pd

st.title("📄 Report Center")

df = pd.read_csv("data/startup_data.csv")

csv = df.to_csv(index=False)

st.download_button(
    "Download Dataset",
    csv,
    "startup_report.csv",
    "text/csv"
)

st.dataframe(df.head(50))
