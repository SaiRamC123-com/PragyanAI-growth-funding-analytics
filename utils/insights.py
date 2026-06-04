import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI Insights",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Powered Startup Insights")

df = pd.read_csv("data/startup_data.csv")

# ==================================
# KEY INSIGHTS
# ==================================

st.subheader("📌 Executive Insights")

top_industry = (
    df.groupby("Industry")
    ["Revenue (M USD)"]
    .mean()
    .idxmax()
)

top_region = (
    df.groupby("Region")
    ["Valuation (M USD)"]
    .mean()
    .idxmax()
)

highest_funding_industry = (
    df.groupby("Industry")
    ["Funding Amount (M USD)"]
    .sum()
    .idxmax()
)

highest_market_share = (
    df.groupby("Industry")
    ["Market Share (%)"]
    .mean()
    .idxmax()
)

most_profitable = (
    df.groupby("Industry")
    ["Profitable"]
    .mean()
    .idxmax()
)

col1,col2,col3 = st.columns(3)

with col1:
    st.success(
        f"🏆 Top Revenue Industry: {top_industry}"
    )

with col2:
    st.info(
        f"🌍 Top Valuation Region: {top_region}"
    )

with col3:
    st.warning(
        f"💰 Highest Funded Industry: {highest_funding_industry}"
    )

st.divider()

# ==================================
# INDUSTRY SCORECARD
# ==================================

st.subheader("🏭 Industry Scorecard")

industry_stats = df.groupby("Industry").agg({

    "Funding Amount (M USD)" : "sum",
    "Revenue (M USD)" : "sum",
    "Valuation (M USD)" : "mean",
    "Market Share (%)" : "mean"

}).reset_index()

st.dataframe(
    industry_stats,
    use_container_width=True
)

# ==================================
# BEST STARTUPS
# ==================================

st.subheader("🚀 Top 10 Valued Startups")

top10 = df.nlargest(
    10,
    "Valuation (M USD)"
)

st.dataframe(
    top10[
        [
            "Startup Name",
            "Industry",
            "Valuation (M USD)",
            "Revenue (M USD)"
        ]
    ],
    use_container_width=True
)

# ==================================
# FUNDING VS VALUATION
# ==================================

st.subheader("📈 Funding vs Valuation")

fig = px.scatter(
    df,
    x="Funding Amount (M USD)",
    y="Valuation (M USD)",
    size="Revenue (M USD)",
    color="Industry",
    hover_name="Startup Name"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==================================
# PROFITABILITY ANALYSIS
# ==================================

st.subheader("💹 Profitability Analysis")

profit_df = (
    df.groupby("Industry")
    ["Profitable"]
    .mean()
    .reset_index()
)

profit_df["Profitable"] = (
    profit_df["Profitable"] * 100
)

fig2 = px.bar(
    profit_df,
    x="Industry",
    y="Profitable",
    color="Industry",
    title="Profitability % by Industry"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==================================
# MARKET SHARE ANALYSIS
# ==================================

st.subheader("🎯 Market Share Leaders")

market_df = (
    df.groupby("Industry")
    ["Market Share (%)"]
    .mean()
    .reset_index()
)

fig3 = px.pie(
    market_df,
    names="Industry",
    values="Market Share (%)"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ==================================
# AI GENERATED RECOMMENDATIONS
# ==================================

st.subheader("🤖 AI Recommendations")

recommendations = []

recommendations.append(
    f"Investors should focus on {top_industry} because it generates the highest average revenue."
)

recommendations.append(
    f"{top_region} shows the highest average valuation and has strong startup potential."
)

recommendations.append(
    f"{highest_funding_industry} attracts the largest amount of funding."
)

recommendations.append(
    f"{highest_market_share} dominates market share and can provide sustainable growth."
)

recommendations.append(
    f"{most_profitable} has the highest profitability ratio among industries."
)

for rec in recommendations:
    st.success(rec)

# ==================================
# STARTUP HEALTH SCORE
# ==================================

st.subheader("❤️ Startup Health Score")

df["Health Score"] = (

    df["Revenue (M USD)"] * 0.4 +

    df["Valuation (M USD)"] * 0.3 +

    df["Market Share (%)"] * 0.2 +

    df["Funding Amount (M USD)"] * 0.1

)

health = df.nlargest(
    10,
    "Health Score"
)

fig4 = px.bar(
    health,
    x="Startup Name",
    y="Health Score",
    color="Industry",
    title="Top Startup Health Scores"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# ==================================
# EXIT STATUS ANALYSIS
# ==================================

if "Exit Status" in df.columns:

    st.subheader("🏁 Exit Status Analysis")

    fig5 = px.pie(
        df,
        names="Exit Status"
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

# ==================================
# FINAL AI SUMMARY
# ==================================

st.subheader("📋 Final AI Summary")

st.markdown(f"""
### Business Summary

- Top Revenue Industry : **{top_industry}**
- Top Valuation Region : **{top_region}**
- Highest Funding Industry : **{highest_funding_industry}**
- Largest Market Share Industry : **{highest_market_share}**
- Most Profitable Industry : **{most_profitable}**

### Suggested Investment Focus

Focus on startups operating in **{top_industry}** and regions like **{top_region}**.
These segments show stronger funding activity, higher valuation trends, and better profitability metrics.
""")
