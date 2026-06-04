import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Startup Analytics Dashboard",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Startup Analytics Dashboard")

df = pd.read_csv("data/startup_data.csv")

# --------------------------
# KPIs
# --------------------------

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "Total Startups",
        len(df)
    )

with col2:
    st.metric(
        "Total Funding",
        f"${df['Funding Amount (M USD)'].sum():,.0f}M"
    )

with col3:
    st.metric(
        "Avg Valuation",
        f"${df['Valuation (M USD)'].mean():,.0f}M"
    )

with col4:
    st.metric(
        "Profitability %",
        f"{df['Profitable'].mean()*100:.1f}%"
    )

st.divider()

# Sidebar Filters

st.sidebar.header("Filters")

industry = st.sidebar.multiselect(
    "Industry",
    df['Industry'].unique(),
    default=df['Industry'].unique()
)

region = st.sidebar.multiselect(
    "Region",
    df['Region'].unique(),
    default=df['Region'].unique()
)

filtered = df[
    (df['Industry'].isin(industry)) &
    (df['Region'].isin(region))
]

# Funding by Industry

fig = px.bar(
    filtered.groupby('Industry')['Funding Amount (M USD)']
    .sum()
    .reset_index(),
    x='Industry',
    y='Funding Amount (M USD)',
    title='Funding by Industry'
)

st.plotly_chart(fig, use_container_width=True)

# Revenue by Industry

fig2 = px.pie(
    filtered,
    names='Industry',
    values='Revenue (M USD)',
    title='Revenue Share'
)

st.plotly_chart(fig2, use_container_width=True)

# Correlation

fig3 = px.scatter(
    filtered,
    x='Funding Amount (M USD)',
    y='Valuation (M USD)',
    color='Industry',
    size='Revenue (M USD)',
    hover_name='Startup Name',
    title='Funding vs Valuation'
)

st.plotly_chart(fig3, use_container_width=True)
