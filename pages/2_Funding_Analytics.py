import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/startup_data.csv")

st.title("💰 Funding Analysis")

fig = px.histogram(
    df,
    x='Funding Amount (M USD)',
    nbins=30
)

st.plotly_chart(fig)

fig2 = px.box(
    df,
    x='Industry',
    y='Funding Amount (M USD)',
    color='Industry'
)

st.plotly_chart(fig2)
