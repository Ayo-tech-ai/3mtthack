import streamlit as st
import joblib
import pandas as pd
import os

st.title("🫁 Tuberculosis Prediction")
st.write("Enter patient details to predict whether they have TB or are Normal.")

# -------------------------------
# Load model and scaler
# -------------------------------
@st.cache_resource
def load_model_scaler():
    model_path = os.path.join("models", "rf_tb_top.joblib")
    scaler_path = os.path.join("models", "scaler_tb_top (1).joblib")
    
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
# Feature inputs
# -------------------------------
st.sidebar.header("Patient Details Input")
feature_names = [
    "Age", "Gender", "Chest_Pain", "Cough_Severity", "Breathlessness",
    "Fatigue", "Weight_Loss", "Fever", "Night_Sweats", "Sputum_Production",
    "Blood_in_Sputum", "Smoking_History", "Previous_TB_History"
]

categorical_features = [
    "Gender", "Chest_Pain", "Fever", "Night_Sweats",
    "Sputum_Production", "Blood_in_Sputum", "Smoking_History",
    "Previous_TB_History"
]

input_data = {}
for feature in feature_names:
    if feature in categorical_features:
        input_data[feature] = st.sidebar.number_input(f"{feature} (encoded)", min_value=0, step=1)
    else:
        input_data[feature] = st.sidebar.number_input(f"{feature}", min_value=0.0, step=0.01)

# -------------------------------
# Prepare input DataFrame
# -------------------------------
input_df = pd.DataFrame([input_data])[feature_names]

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
