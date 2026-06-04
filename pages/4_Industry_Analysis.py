import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏭 Industry Analysis")

df = pd.read_csv("data/startup_data.csv")

fig = px.treemap(
    df,
    path=["Industry"],
    values="Revenue (M USD)"
)

st.plotly_chart(fig,use_container_width=True)

industry = df.groupby("Industry").agg({
    "Funding Amount (M USD)":"sum",
    "Revenue (M USD)":"sum"
})

st.dataframe(industry)
