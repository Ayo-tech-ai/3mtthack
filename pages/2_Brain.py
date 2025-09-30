import streamlit as st
import tensorflow as tf
from tensorflow.keras import layers
from PIL import Image
import numpy as np
import os
import time
import random

# -------------------------------
# Page title
# -------------------------------
st.set_page_config(
    page_title="🧠 Brain Tumor MRI Classifier",
    layout="wide",
    page_icon="🩺"
)

# -------------------------------
# Custom CSS for UI/UX
# -------------------------------
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

    .result-box {
        padding: 15px;
        border-radius: 12px;
        font-size: 1.2rem;
        font-weight: bold;
        text-align: center;
        color: white;
        margin-bottom: 10px;
    }

    .glioma {
        background-color: #eb2f06;
    }

    .meningioma {
        background-color: #ff7f50;
    }

    .pituitary {
        background-color: #f7b731;
    }

    .notumor {
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

# -------------------------------
# Header
# -------------------------------
st.markdown('<div class="main-title">🧠 Brain Tumor MRI Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Upload an MRI brain scan image, and analyze it to predict the tumor type or if it is normal.</div>', unsafe_allow_html=True)

# -------------------------------
# Load the trained model
# -------------------------------
@st.cache_resource
def load_model():
    MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/Brain_model.keras")
    
    if not os.path.exists(MODEL_PATH):
        st.error(f"Model file not found at {MODEL_PATH}")
        return None

    model = tf.keras.models.load_model(MODEL_PATH)
    return model

model = load_model()
if model is None:
    st.stop()

# -------------------------------
# Class names and clinical tooltips
# -------------------------------
class_names = ['glioma', 'meningioma', 'notumor', 'pituitary']
class_tooltips = {
    'glioma': "Malignant tumor originating from glial cells in the brain.",
    'meningioma': "Usually benign tumor arising from the meninges, the brain's protective membranes.",
    'pituitary': "Tumor located in the pituitary gland affecting hormonal function.",
    'notumor': "No tumor detected; MRI appears normal."
}

# -------------------------------
# Image upload
# -------------------------------
uploaded_file = st.file_uploader("Choose a brain MRI image...", type=["jpg", "jpeg", "png"])

# Analyze button: disabled if no image
analyze_disabled = uploaded_file is None
col1, col2 = st.columns([2,1])

with col1:
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded MRI", use_container_width=True)

# -------------------------------
# Analyze Image Button
# -------------------------------
with col2:
    if st.button("🩺 Analyze Image", disabled=analyze_disabled):
        # -------------------------------
        # Spinner / analyzing
        # -------------------------------
        analyze_time = random.randint(7, 12)
        with st.spinner(f"Analyzing MRI scan... (approximately {analyze_time} seconds)"):
            time.sleep(analyze_time)

        # -------------------------------
        # Preprocess image
        # -------------------------------
        IMG_SIZE = (224, 224)
        img = image.resize(IMG_SIZE)
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Make prediction
        predictions = model.predict(img_array)
        predicted_index = np.argmax(predictions[0])
        predicted_class = class_names[predicted_index]
        confidence = predictions[0][predicted_index]

        # -------------------------------
        # Display results
        # -------------------------------
        st.markdown(f'<div class="result-box {predicted_class}">Prediction: {predicted_class}</div>', unsafe_allow_html=True)
        st.markdown(f"Confidence: **{confidence*100:.2f}%**")

        # Clinical explanation / tooltip
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Clinical Interpretation")
        st.write(f"{class_tooltips[predicted_class]}")
        st.markdown('</div>', unsafe_allow_html=True)
