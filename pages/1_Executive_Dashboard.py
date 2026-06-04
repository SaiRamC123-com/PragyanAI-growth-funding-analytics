import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/startup_data.csv")

st.title("🏭 Industry Analysis")

industry_stats = df.groupby('Industry').agg({
    'Funding Amount (M USD)':'sum',
    'Revenue (M USD)':'sum',
    'Valuation (M USD)':'mean'
}).reset_index()

fig = px.bar(
    industry_stats,
    x='Industry',
    y='Funding Amount (M USD)',
    color='Industry'
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.treemap(
    industry_stats,
    path=['Industry'],
    values='Revenue (M USD)'
)

st.plotly_chart(fig2, use_container_width=True)
