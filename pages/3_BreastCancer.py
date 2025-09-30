import streamlit as st
import joblib
import pandas as pd
import os

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="🎀 Breast Cancer Predictor",
    layout="wide",
    page_icon="🩺"
)

# ----------------------------
# Custom CSS for UI/UX
# ----------------------------
st.markdown("""
    <style>
    /* General page styling */
    .stApp {
        background-color: #f5f8fa;
        font-family: 'Arial', sans-serif;
    }

    /* Main title */
    .main-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #0a3d62;
        text-align: center;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .sub-title {
        font-size: 1.1rem;
        color: #3c6382;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Card styling */
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }

    /* Input with icon styling */
    .input-icon {
        display: flex;
        align-items: center;
        margin-bottom: 12px;
    }

    .input-icon span {
        margin-right: 8px;
        font-size: 1.2rem;
    }

    /* Prediction result box */
    .result-box {
        padding: 15px;
        border-radius: 12px;
        font-size: 1.2rem;
        font-weight: bold;
        text-align: center;
        color: white;
    }

    .malignant {
        background-color: #eb2f06;
    }

    .benign {
        background-color: #079992;
    }

    /* Button styling */
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
st.markdown('<div class="main-title">🎀 Breast Cancer Prediction Tool</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Enter patient metrics to predict whether the tumor is Malignant or Benign.</div>', unsafe_allow_html=True)

# ----------------------------
# Load Model and Scaler
# ----------------------------
model_path = os.path.join("models", "rf_breast_top10 (1).joblib")
scaler_path = os.path.join("models", "scaler_top10.joblib")

if not os.path.exists(model_path) or not os.path.exists(scaler_path):
    st.error("Model or scaler files not found in the models folder!")
    st.stop()

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# ----------------------------
# Patient Metrics Input (Main Page)
# ----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Patient Metrics Input")

feature_names = [
    'radius_mean', 'perimeter_mean', 'area_mean',
    'concavity_mean', 'concave points_mean',
    'radius_worst', 'perimeter_worst', 'area_worst',
    'concavity_worst', 'concave points_worst'
]

# Optional: simple icons for features (you can replace with emojis or font-awesome)
feature_icons = ['📏', '📐', '📊', '🔺', '⚫', '📏', '📐', '📊', '🔺', '⚫']

col1, col2 = st.columns(2)
input_data = {}

for i, feature in enumerate(feature_names):
    target_col = col1 if i % 2 == 0 else col2
    with target_col:
        st.markdown(f'<div class="input-icon"><span>{feature_icons[i]}</span> {feature}</div>', unsafe_allow_html=True)
        input_data[feature] = st.number_input(feature, min_value=0.0, max_value=1000.0, step=0.01, key=feature)

st.markdown('</div>', unsafe_allow_html=True)

# Convert to DataFrame and scale
input_df = pd.DataFrame([input_data])
input_scaled = scaler.transform(input_df)

# ----------------------------
# Prediction Button
# ----------------------------
if st.button("Predict"):
    pred = model.predict(input_scaled)[0]
    pred_proba = model.predict_proba(input_scaled)[0][pred]
    label = "Malignant" if pred == 1 else "Benign"

    # Display result with color box
    risk_class = "malignant" if label == "Malignant" else "benign"
    st.markdown(f'<div class="result-box {risk_class}">🧾 Prediction: {label}</div>', unsafe_allow_html=True)
    st.markdown(f"Confidence: **{pred_proba*100:.2f}%**")
