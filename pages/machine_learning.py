import streamlit as st
import pandas as pd

from utils.ml_models import train_all_models

st.title("Machine Learning Studio")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.dataframe(df.head())

    target = st.selectbox(
        "Target Column",
        df.columns
    )

    if st.button("Train Models"):

        results = train_all_models(
            df,
            target
        )

        st.subheader("Model Leaderboard")

        st.dataframe(results)

        st.bar_chart(
            results.set_index("Model")
        )

        best_model = results.sort_values(
            "Accuracy",
            ascending=False
        ).iloc[0]

        st.success(
            f"Best Model: {best_model['Model']} "
            f"({best_model['Accuracy']}%)"
        )
