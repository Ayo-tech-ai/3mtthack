import streamlit as st
import joblib
import pandas as pd
import os

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="🫁 Tuberculosis Predictor",
    layout="wide",
    page_icon="🩺"
)

# ----------------------------
# Custom CSS for UI/UX
# ----------------------------
st.markdown("""
    <style>
    .stApp {
        background-color: #f5f8fa;
        font-family: 'Arial', sans-serif;
    }

    .main-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #0a3d62;
        text-align: center;
        margin-bottom: 5px;
    }

    .sub-title {
        font-size: 1.1rem;
        color: #3c6382;
        text-align: center;
        margin-bottom: 30px;
    }

    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }

    .input-icon {
        display: flex;
        align-items: center;
        margin-bottom: 12px;
    }

    .input-icon span {
        margin-right: 8px;
        font-size: 1.2rem;
    }

    .result-box {
        padding: 15px;
        border-radius: 12px;
        font-size: 1.2rem;
        font-weight: bold;
        text-align: center;
        color: white;
    }

    .tb-positive {
        background-color: #eb2f06;
    }

    .tb-negative {
        background-color: #079992;
    }

    .stButton button {
        background-color: #0a3d62;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }

    .stButton button:hover {
        background-color: #3c6382;
        color: white;
    }

    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Header
# ----------------------------
st.markdown('<div class="main-title">🫁 Tuberculosis Prediction Tool</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Enter patient details to predict whether they have TB or are Normal.</div>', unsafe_allow_html=True)

# ----------------------------
# Load model, scaler, encoders
# ----------------------------
model_path = os.path.join("models", "rf_tb_top.joblib")
scaler_path = os.path.join("models", "scaler_tb_top.joblib")
encoders_path = os.path.join("models", "tb_label_encoders.joblib")

if not all(os.path.exists(p) for p in [model_path, scaler_path, encoders_path]):
    st.error("One or more required files (model, scaler, encoders) are missing in the models folder!")
    st.stop()

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)
label_encoders = joblib.load(encoders_path)

# ----------------------------
# Patient Details Input (Main Page)
# ----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Patient Details Input")

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

# Optional icons for features
feature_icons = {
    "Age":"🎂", "Gender":"🚻", "Chest_Pain":"❤️", "Cough_Severity":"🤧", 
    "Breathlessness":"😮‍💨", "Fatigue":"😴", "Weight_Loss":"⚖️", "Fever":"🌡️",
    "Night_Sweats":"💦", "Sputum_Production":"🩸", "Blood_in_Sputum":"🩸",
    "Smoking_History":"🚬", "Previous_TB_History":"🏥"
}

# Organize inputs in two columns
col1, col2 = st.columns(2)
input_data = {}

for i, feature in enumerate(features):
    target_col = col1 if i % 2 == 0 else col2
    with target_col:
        icon = feature_icons.get(feature, "🩺")
        st.markdown(f'<div class="input-icon"><span>{icon}</span> {feature}</div>', unsafe_allow_html=True)
        if feature in categorical_features:
            input_data[feature] = st.selectbox(
                feature, options=list(label_encoders[feature].classes_), key=feature
            )
        else:
            input_data[feature] = st.number_input(feature, min_value=0.0, step=0.01, key=feature)

st.markdown('</div>', unsafe_allow_html=True)

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Encode categorical features
for feature in categorical_features:
    le = label_encoders[feature]
    input_df[feature] = le.transform(input_df[feature])

# Scale numeric features
numeric_cols = ["Age", "Cough_Severity", "Breathlessness", "Fatigue", "Weight_Loss"]
input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict"):
    pred = model.predict(input_df)[0]
    pred_proba = model.predict_proba(input_df)[0][pred]
    
    # Decode target label
    class_le = label_encoders["Class"]
    label = class_le.inverse_transform([pred])[0]

    # Display result with color box
    risk_class = "tb-positive" if label.lower() == "tb" else "tb-negative"
    st.markdown(f'<div class="result-box {risk_class}">🧾 Prediction: {label}</div>', unsafe_allow_html=True)
    st.markdown(f"Confidence: **{pred_proba*100:.2f}%**")
