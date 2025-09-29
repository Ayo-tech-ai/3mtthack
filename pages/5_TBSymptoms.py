import streamlit as st
import joblib
import pandas as pd
import os

st.title("🫁 Tuberculosis Prediction")
st.write("Enter patient details to predict whether they have TB or are Normal.")

# -------------------------------
# ✅ Load your saved model and scaler from the models/ folder
# -------------------------------
model_path = os.path.join("models", "rf_tb_top.joblib")
scaler_path = os.path.join("models", "scaler_tb_top (1).joblib")

if not os.path.exists(model_path) or not os.path.exists(scaler_path):
    st.error("Model or scaler files not found in the models folder!")
    st.stop()

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# -------------------------------
# Sidebar: User input
# -------------------------------
st.sidebar.header("Patient Details Input")
features = [
    "Age", "Gender", "Chest_Pain", "Cough_Severity", "Breathlessness",
    "Fatigue", "Weight_Loss", "Fever", "Night_Sweats", "Sputum_Production",
    "Blood_in_Sputum", "Smoking_History", "Previous_TB_History"
]

input_data = {}
for feature in features:
    # For categorical features, use number inputs for encoded values
    if feature in ["Gender", "Chest_Pain", "Fever", "Night_Sweats",
                   "Sputum_Production", "Blood_in_Sputum", "Smoking_History",
                   "Previous_TB_History"]:
        input_data[feature] = st.sidebar.number_input(f"{feature} (encoded)", min_value=0, step=1)
    else:
        input_data[feature] = st.sidebar.number_input(f"{feature}", min_value=0.0, step=0.01)

# Convert to DataFrame and scale
input_df = pd.DataFrame([input_data])
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
