import pandas as pd

from sklearn.ensemble import (
    RandomForestRegressor,
    RandomForestClassifier
)

from sklearn.model_selection import (
    train_test_split
)

from sklearn.metrics import (
    mean_absolute_error,
    accuracy_score
)


# =====================================
# VALUATION PREDICTION MODEL
# =====================================

def train_valuation_model(df):

    features = [
        "Funding Amount (M USD)",
        "Revenue (M USD)",
        "Employees",
        "Market Share (%)"
    ]

    X = df[features]

    y = df["Valuation (M USD)"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    return model, mae


# =====================================
# VALUATION PREDICTION
# =====================================

def predict_valuation(
    model,
    funding,
    revenue,
    employees,
    market_share
):

    result = model.predict(
        [[
            funding,
            revenue,
            employees,
            market_share
        ]]
    )

    return round(result[0], 2)


# =====================================
# PROFITABILITY MODEL
# =====================================

def train_profitability_model(df):

    features = [
        "Funding Amount (M USD)",
        "Revenue (M USD)",
        "Employees",
        "Market Share (%)"
    ]

    X = df[features]

    y = df["Profitable"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=150,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    return model, accuracy


# =====================================
# PROFITABILITY PREDICTION
# =====================================

def predict_profitability(
    model,
    funding,
    revenue,
    employees,
    market_share
):

    result = model.predict(
        [[
            funding,
            revenue,
            employees,
            market_share
        ]]
    )

    probability = model.predict_proba(
        [[
            funding,
            revenue,
            employees,
            market_share
        ]]
    )

    return result[0], probability.max()


# =====================================
# STARTUP HEALTH SCORE
# =====================================

def calculate_health_score(df):

    df["Health Score"] = (

        df["Revenue (M USD)"] * 0.40 +

        df["Valuation (M USD)"] * 0.30 +

        df["Market Share (%)"] * 0.20 +

        df["Funding Amount (M USD)"] * 0.10

    )

    return df


# =====================================
# TOP HEALTHY STARTUPS
# =====================================

def top_healthy_startups(df):

    df = calculate_health_score(df)

    return df.nlargest(
        10,
        "Health Score"
    )


# =====================================
# FEATURE IMPORTANCE
# =====================================

def feature_importance(model, columns):

    importance_df = pd.DataFrame({

        "Feature": columns,

        "Importance":
        model.feature_importances_

    })

    importance_df = importance_df.sort_values(
        "Importance",
        ascending=False
    )

    return importance_df
