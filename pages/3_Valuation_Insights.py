import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Valuation Insights")

df = pd.read_csv("data/startup_data.csv")

top10 = df.nlargest(
    10,
    "Valuation (M USD)"
)

fig = px.bar(
    top10,
    x="Startup Name",
    y="Valuation (M USD)",
    color="Industry"
)

st.plotly_chart(fig,use_container_width=True)

fig2 = px.scatter(
    df,
    x="Revenue (M USD)",
    y="Valuation (M USD)",
    color="Industry"
)

st.plotly_chart(fig2,use_container_width=True)
