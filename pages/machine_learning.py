import streamlit as st
import pandas as pd

from src.ml.model_trainer import ModelTrainer

st.title("Machine Learning Dashboard")

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.write(df.head())

    target = st.selectbox(
        "Select Target Column",
        df.columns
    )

    if st.button("Train Models"):

        trainer = ModelTrainer(
            df,
            target
        )

        results = trainer.train_models()

        st.subheader("Model Comparison")

        st.dataframe(results)

        st.bar_chart(
            results.set_index("Model")
        )
