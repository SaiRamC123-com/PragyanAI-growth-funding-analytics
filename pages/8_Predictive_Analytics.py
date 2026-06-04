import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("data/startup_data.csv")

X = df[
[
'Funding Amount (M USD)',
'Revenue (M USD)',
'Employees',
'Market Share (%)'
]
]

y = df['Valuation (M USD)']

model = RandomForestRegressor()
model.fit(X,y)

st.title("🤖 Valuation Predictor")

funding = st.number_input("Funding")
revenue = st.number_input("Revenue")
employees = st.number_input("Employees")
market = st.number_input("Market Share")

if st.button("Predict"):
    pred = model.predict(
        [[funding,revenue,employees,market]]
    )[0]

    st.success(
        f"Estimated Valuation: ${pred:,.2f}M"
    )
