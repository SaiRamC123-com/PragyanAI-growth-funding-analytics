import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎯 Startup Segmentation")

df = pd.read_csv("data/startup_data.csv")

fig = px.scatter(
    df,
    x="Employees",
    y="Revenue (M USD)",
    color="Industry",
    size="Valuation (M USD)"
)

st.plotly_chart(fig,use_container_width=True)
