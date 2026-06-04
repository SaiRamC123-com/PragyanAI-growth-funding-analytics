import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Regional Analysis")

df = pd.read_csv("data/startup_data.csv")

region_count = df["Region"].value_counts().reset_index()

fig = px.pie(
    region_count,
    names="Region",
    values="count"
)

st.plotly_chart(fig,use_container_width=True)

fig2 = px.bar(
    df.groupby("Region")[
        "Revenue (M USD)"
    ].sum().reset_index(),
    x="Region",
    y="Revenue (M USD)"
)

st.plotly_chart(fig2,use_container_width=True)
