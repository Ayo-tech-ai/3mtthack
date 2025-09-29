import streamlit as st
import joblib
import pandas as pd
import os

st.title("🫁 Tuberculosis Prediction")
st.write("Enter patient details to predict whether they have TB or are Normal.")

# -------------------------------
# Load model, scaler, and encoders
# -------------------------------
@st.cache_resource
def load_model_resources():
    model_path = os.path.join("models", "rf_tb_top.joblib")
    scaler_path = os.path.join("models", "scaler_tb_top.joblib")
    encoder_path = os.path.join("models", "tb_label_encoders.joblib")  # saved dict of LabelEncoders

    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        st.error("Model or scaler files not found in the models folder!")
        return None, None, None

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    
    # Optional: load encoders if you saved them during training
    encoders = {}
    if os.path.exists(encoder_path):
        encoders = joblib.load(encoder_path)

    return model, scaler, encoders

model, scaler, encoders = load_model_resources()
if model is None:
    st.stop()

# -------------------------------
# Feature inputs
# -------------------------------
st.sidebar.header("Patient Details Input")
feature_names = [
    "Age", "Gender", "Chest_Pain", "Cough_Severity", "Breathlessness",
    "Fatigue", "Weight_Loss", "Fever", "Night_Sweats", "Sputum_Production",
    "Blood_in_Sputum", "Smoking_History", "Previous_TB_History"
]

# Define which features are categorical
categorical_features = [
    "Gender", "Chest_Pain", "Fever", "Night_Sweats",
    "Sputum_Production", "Blood_in_Sputum", "Smoking_History",
    "Previous_TB_History"
]

input_data = {}
for feature in feature_names:
    if feature in categorical_features:
        # Use integer input for encoded categories
        input_data[feature] = st.sidebar.number_input(f"{feature} (encoded)", min_value=0, step=1)
    else:
        input_data[feature] = st.sidebar.number_input(f"{feature}", min_value=0.0, step=0.01)

# -------------------------------
# Prepare input DataFrame
# -------------------------------
# Ensure correct order matching scaler training
scaler_features = feature_names
input_df = pd.DataFrame([input_data])[scaler_features]

# -------------------------------
# Scale input
# -------------------------------
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
