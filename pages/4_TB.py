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
    page_title="🫁 Lung X-ray Disease Classifier",
    layout="wide",
    page_icon="🩺"
)

# -------------------------------
# Custom CSS for UI/UX
# -------------------------------
st.markdown("""
<style>
.stApp { background-color: #f5f8fa; font-family: 'Arial', sans-serif; }
.main-title { font-size: 2.5rem; font-weight: bold; color: #0a3d62; text-align: center; margin-bottom: 5px; }
.sub-title { font-size: 1.1rem; color: #3c6382; text-align: center; margin-bottom: 30px; }
.card { background-color: #ffffff; padding: 20px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.08); margin-bottom: 25px; }
.result-box { padding: 15px; border-radius: 12px; font-size: 1.2rem; font-weight: bold; text-align: center; color: white; margin-bottom: 10px; }
.NORMAL { background-color: #079992; }
.PNEUMONIA { background-color: #f7b731; }
.TUBERCULOSIS { background-color: #eb2f06; }
.stButton button { background-color: #0a3d62; color: white; font-weight: bold; border-radius: 8px; padding: 10px 20px; border: none; }
.stButton button:hover { background-color: #3c6382; color: white; }
.progress-bar { height: 25px; border-radius: 8px; text-align: center; color: white; font-weight: bold; line-height: 25px; }
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Header
# -------------------------------
st.markdown('<div class="main-title">🫁 Lung X-ray Disease Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Upload a chest X-ray image to analyze and predict the lung condition.</div>', unsafe_allow_html=True)

# -------------------------------
# Load model
# -------------------------------
@st.cache_resource
def load_model():
    MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/NPT lungs_model.keras")
    if not os.path.exists(MODEL_PATH):
        st.error(f"Model file not found at {MODEL_PATH}")
        return None
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()
if model is None:
    st.stop()

# -------------------------------
# Classes and descriptions
# -------------------------------
class_names = ['NORMAL', 'PNEUMONIA', 'TUBERCULOSIS']
class_descriptions = {
    "NORMAL": "No apparent lung disease detected; X-ray appears within normal limits.",
    "PNEUMONIA": "Lung infection causing inflammation; characterized by opacities on X-ray.",
    "TUBERCULOSIS": "Chronic bacterial infection affecting lungs; X-ray shows lesions or cavities."
}
class_colors = {
    "NORMAL": "#079992",
    "PNEUMONIA": "#f7b731",
    "TUBERCULOSIS": "#eb2f06"
}

# -------------------------------
# Image upload
# -------------------------------
uploaded_file = st.file_uploader("Choose a chest X-ray image...", type=["jpg", "jpeg", "png"])
analyze_disabled = uploaded_file is None
col1, col2 = st.columns([2,1])

with col1:
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded X-ray", use_container_width=True)

# -------------------------------
# Analyze button
# -------------------------------
with col2:
    if st.button("🩺 Analyze Image", disabled=analyze_disabled):
        # Spinner with random delay
        analyze_time = random.randint(7, 12)
        with st.spinner(f"Analyzing X-ray image... (approx {analyze_time} seconds)"):
            time.sleep(analyze_time)

        # Preprocess
        IMG_SIZE = (224, 224)
        img = image.resize(IMG_SIZE)
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        predictions = model.predict(img_array)
        predicted_index = np.argmax(predictions[0])
        predicted_class = class_names[predicted_index]
        confidence = predictions[0][predicted_index]

        # Display predicted class with tooltip
        st.markdown(
            f'<div class="result-box {predicted_class}" title="{class_descriptions[predicted_class]}">'
            f'Prediction: {predicted_class}</div>', unsafe_allow_html=True)

        # Confidence progress bar
        st.markdown(
            f'<div class="progress-bar" style="width:{confidence*100}%; background-color:{class_colors[predicted_class]}">'
            f'{confidence*100:.2f}%</div>', unsafe_allow_html=True)

        # Clinical card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Clinical Interpretation")
        st.write(class_descriptions[predicted_class])
        st.markdown('</div>', unsafe_allow_html=True)
