# 5_TBSymptoms.py
import streamlit as st
import joblib
import pandas as pd
import os

st.title("🫁 Tuberculosis Prediction")
st.write("Enter patient details to predict whether they have TB or are Normal.")

# -------------------------------
# Load model, scaler, and label encoders
# -------------------------------
model_path = os.path.join("models", "rf_tb_top.joblib")
scaler_path = os.path.join("models", "scaler_tb_top.joblib")
encoders_path = os.path.join("models", "tb_label_encoders.joblib")

if not all(os.path.exists(p) for p in [model_path, scaler_path, encoders_path]):
    st.error("One or more required files (model, scaler, encoders) are missing in the models folder!")
    st.stop()

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)
label_encoders = joblib.load(encoders_path)

# -------------------------------
# Sidebar: User input
# -------------------------------
st.sidebar.header("Patient Details Input")
features = [
    "Age", "Gender", "Chest_Pain", "Cough_Severity", "Breathlessness",
    "Fatigue", "Weight_Loss", "Fever", "Night_Sweats", "Sputum_Production",
    "Blood_in_Sputum", "Smoking_History", "Previous_TB_History"
]

categorical_features = [
    "Gender", "Chest_Pain", "Fever", "Night_Sweats", 
    "Sputum_Production", "Blood_in_Sputum", 
    "Smoking_History", "Previous_TB_History"
]

input_data = {}

for feature in features:
    if feature in categorical_features:
        # Dropdown with human-readable labels
        input_data[feature] = st.sidebar.selectbox(
            f"{feature}", options=list(label_encoders[feature].classes_)
        )
    else:
        input_data[feature] = st.sidebar.number_input(feature, min_value=0.0, step=0.01)

# Convert input to DataFrame
input_df = pd.DataFrame([input_data])

# Encode categorical features dynamically
for feature in categorical_features:
    le = label_encoders[feature]
    input_df[feature] = le.transform(input_df[feature])

# Apply scaler only to numeric columns (as in notebook)
numeric_cols = ["Age", "Cough_Severity", "Breathlessness", "Fatigue", "Weight_Loss"]
input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict"):
    pred = model.predict(input_df)[0]
    pred_proba = model.predict_proba(input_df)[0][pred]
    
    # Decode target label
    class_le = label_encoders["Class"]
    label = class_le.inverse_transform([pred])[0]
    
    st.markdown(f"### Prediction: **{label}**")
    st.markdown(f"Confidence: **{pred_proba*100:.2f}%**")
