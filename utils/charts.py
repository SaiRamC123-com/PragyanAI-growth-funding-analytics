import plotly.express as px

def funding_by_industry(df):

    chart = px.bar(
        df.groupby("Industry")
        ["Funding Amount (M USD)"]
        .sum()
        .reset_index(),
        x="Industry",
        y="Funding Amount (M USD)",
        color="Industry"
    )

    return chart


def valuation_vs_funding(df):

    chart = px.scatter(
        df,
        x="Funding Amount (M USD)",
        y="Valuation (M USD)",
        color="Industry",
        size="Revenue (M USD)"
    )

    return chart


def revenue_share(df):

    chart = px.pie(
        df,
        names="Industry",
        values="Revenue (M USD)"
    )

    return chart


def regional_chart(df):

    chart = px.bar(
        df.groupby("Region")
        ["Revenue (M USD)"]
        .sum()
        .reset_index(),
        x="Region",
        y="Revenue (M USD)"
    )

    return chart


def employee_vs_revenue(df):

    chart = px.scatter(
        df,
        x="Employees",
        y="Revenue (M USD)",
        color="Industry"
    )

    return chart
