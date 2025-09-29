import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder

st.title("🫁 Tuberculosis Prediction")
st.write("Enter patient details to predict whether they have TB or are Normal.")

# -------------------------------
# Load model and scaler
# -------------------------------
@st.cache_resource
def load_model_scaler():
    model_path = os.path.join("models", "rf_tb_top.joblib")
    scaler_path = os.path.join("models", "scaler_tb_top.joblib")
    
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        st.error("Model or scaler files not found in the models folder!")
        return None, None

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    return model, scaler

model, scaler = load_model_scaler()
if model is None:
    st.stop()

# -------------------------------
# Define categorical features and known classes
# -------------------------------
categorical_features = {
    "Gender": ["Male", "Female"],
    "Chest_Pain": ["No", "Yes"],
    "Fever": ["Mild", "Moderate", "High"],
    "Night_Sweats": ["No", "Yes"],
    "Sputum_Production": ["Low", "Medium", "High"],
    "Blood_in_Sputum": ["No", "Yes"],
    "Smoking_History": ["Never", "Former", "Current"],
    "Previous_TB_History": ["No", "Yes"]
}

# Initialize label encoders dynamically
label_encoders = {}
for feature, classes in categorical_features.items():
    le = LabelEncoder()
    le.fit(classes)
    label_encoders[feature] = le

# -------------------------------
# User input
# -------------------------------
st.sidebar.header("Patient Details Input")
input_data = {}

# Numerical features
numerical_features = ["Age", "Cough_Severity", "Breathlessness", "Fatigue", "Weight_Loss"]
for feature in numerical_features:
    input_data[feature] = st.sidebar.number_input(f"{feature}", min_value=0.0, step=0.01)

# Categorical features
for feature, classes in categorical_features.items():
    input_data[feature] = st.sidebar.selectbox(f"{feature}", classes)

# -------------------------------
# Encode categorical features dynamically
# -------------------------------
for feature in categorical_features.keys():
    input_data[feature] = label_encoders[feature].transform([input_data[feature]])[0]

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Scale input
input_scaled = scaler.transform(input_df)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict"):
    pred = model.predict(input_scaled)[0]
    pred_proba = model.predict_proba(input_scaled)[0][pred]
    
    label = "Tuberculosis" if pred == 1 else "Normal"
    st.markdown(f"### Prediction: **{label}**")
    st.markdown(f"Confidence: **{pred_proba*100:.2f}%**")
