import streamlit as st
import pandas as pd

st.title("🧠 AI Insights")

df = pd.read_csv("data/startup_data.csv")

best_industry = df.groupby(
    "Industry"
)["Revenue (M USD)"].mean().idxmax()

st.success(
    f"Highest Revenue Industry: {best_industry}"
)

best_region = df.groupby(
    "Region"
)["Valuation (M USD)"].mean().idxmax()

st.info(
    f"Highest Valuation Region: {best_region}"
)

st.write("""
### Recommendations

• Invest in high valuation industries

• Focus on profitable startups

• Target regions with high revenue growth

• Scale employee productivity
""")
