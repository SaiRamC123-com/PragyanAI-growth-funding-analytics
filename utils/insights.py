def generate_business_insights(df):

    insights = []

    insights.append(
        f"Dataset contains {df.shape[0]} records."
    )

    insights.append(
        f"Dataset contains {df.shape[1]} columns."
    )

    missing = df.isnull().sum().sum()

    insights.append(
        f"Missing Values Found: {missing}"
    )

    return insights
