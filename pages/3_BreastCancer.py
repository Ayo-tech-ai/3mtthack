import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="🎀",
    layout="centered"
)

st.title("🎀 Breast Cancer Prediction")
st.write("Enter patient metrics to predict whether the tumor is Malignant or Benign.")

# -------------------------------
# Load model and scaler
# -------------------------------
@st.cache_resource
def load_model_scaler():
    # Model/scaler in ../models relative to this app.py
    model_path = os.path.join(os.path.dirname(__file__), "../models/rf_breast_top10.joblib")
    scaler_path = os.path.join(os.path.dirname(__file__), "../models/scaler_top10.joblib")
    
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        st.error(f"Model or scaler files not found!\nExpected:\n{model_path}\n{scaler_path}")
        return None, None

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    return model, scaler

model, scaler = load_model_scaler()
if model is None:
    st.stop()

# -------------------------------
# Sidebar: User input for 10 features
# -------------------------------
st.sidebar.header("Patient Metrics Input")
feature_names = [
    'radius_mean', 'perimeter_mean', 'area_mean',
    'concavity_mean', 'concave points_mean',
    'radius_worst', 'perimeter_worst', 'area_worst',
    'concavity_worst', 'concave points_worst'
]

input_data = {}
for feature in feature_names:
    input_data[feature] = st.sidebar.number_input(
        feature, min_value=0.0, max_value=1000.0, step=0.01
    )

# Convert to DataFrame and scale
input_df = pd.DataFrame([input_data])
input_scaled = scaler.transform(input_df)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict"):
    pred = model.predict(input_scaled)[0]
    pred_proba = model.predict_proba(input_scaled)[0][pred]

    label = "Malignant" if pred == 1 else "Benign"
    st.markdown(f"### Prediction: **{label}**")
    st.markdown(f"Confidence: **{pred_proba*100:.2f}%**")
