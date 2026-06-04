import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/startup_data.csv")

st.title("📈 Profitability Insights")

profit = df.groupby('Industry')['Profitable'].mean()*100

fig = px.bar(
    profit.reset_index(),
    x='Industry',
    y='Profitable'
)

st.plotly_chart(fig)

heat = df.corr(numeric_only=True)

st.dataframe(heat)
