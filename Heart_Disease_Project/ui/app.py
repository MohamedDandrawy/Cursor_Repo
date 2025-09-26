import sys
from pathlib import Path

import streamlit as st
import pandas as pd
from joblib import load


PROJECT_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_DIR / "models" / "final_model.pkl"


@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        st.warning("Model not found. Please run supervised learning notebook to create models/final_model.pkl")
        return None
    return load(MODEL_PATH)


st.title("Heart Disease Risk Prediction")
st.write("Input patient data to predict heart disease risk.")

model = load_model()

default_vals = {
    "age": 57,
    "sex": 1,
    "cp": 2,
    "trestbps": 130,
    "chol": 250,
    "fbs": 0,
    "restecg": 1,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 1.0,
    "slope": 2,
    "ca": 0,
    "thal": 2,
}

with st.form("input_form"):
    cols = st.columns(2)
    inputs = {}
    keys = list(default_vals.keys())
    for i, k in enumerate(keys):
        with cols[i % 2]:
            if k in {"oldpeak"}:
                inputs[k] = st.number_input(k, value=float(default_vals[k]))
            else:
                inputs[k] = st.number_input(k, value=int(default_vals[k]))
    submitted = st.form_submit_button("Predict")

if submitted:
    df = pd.DataFrame([inputs])
    if model is None:
        st.stop()
    proba = None
    if hasattr(model, "predict_proba"):
        proba = float(model.predict_proba(df)[:, 1][0])
    pred = int(model.predict(df)[0])
    st.subheader("Prediction")
    st.write(f"Predicted class: {pred}")
    if proba is not None:
        st.write(f"Risk probability: {proba:.3f}")

