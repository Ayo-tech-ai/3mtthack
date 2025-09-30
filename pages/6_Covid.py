import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import tensorflow as tf
import os
import gdown
import time
import random

# -------------------------------
# Download and load model
# -------------------------------
FILE_ID = "1eLk7CUpfx5ZnTcoiV6w-ecuI4JfzKXIS"
MODEL_PATH = "my1_cnn_lung_model.h5"

if not os.path.exists(MODEL_PATH):
    gdown.download(f"https://drive.google.com/uc?id={FILE_ID}", MODEL_PATH, quiet=False)

model = load_model(MODEL_PATH)

# -------------------------------
# Classes and clinical info
# -------------------------------
class_names = ['COVID', 'NORMAL']
class_descriptions = {
    'COVID': "Chest X-ray shows signs consistent with COVID-19 infection, including lung opacities and inflammation.",
    'NORMAL': "No signs of infection detected; lungs appear healthy and normal on X-ray."
}
class_colors = {
    'COVID': '#eb2f06',
    'NORMAL': '#079992'
}

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>
.stApp { background-color: #f5f8fa; font-family: 'Arial', sans-serif; }
.main-title { font-size: 2.5rem; font-weight: bold; color: #0a3d62; text-align: center; margin-bottom: 5px; }
.sub-title { font-size: 1.1rem; color: #3c6382; text-align: center; margin-bottom: 30px; }
.card { background-color: #ffffff; padding: 20px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.08); margin-bottom: 25px; }
.result-box { padding: 15px; border-radius: 12px; font-size: 1.2rem; font-weight: bold; text-align: center; color: white; margin-bottom: 10px; }
.COVID { background-color: #eb2f06; }
.NORMAL { background-color: #079992; }
.stButton button { background-color: #0a3d62; color: white; font-weight: bold; border-radius: 8px; padding: 10px 20px; border: none; }
.stButton button:hover { background-color: #3c6382; color: white; }
.progress-bar { height: 25px; border-radius: 8px; text-align: center; color: white; font-weight: bold; line-height: 25px; }
</style>
""", unsafe_allow_html=True)

# -------------------------------
# App header
# -------------------------------
st.markdown('<div class="main-title">AI COVID Lung Detection System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Upload a chest X-ray to analyze for COVID-19 infection.</div>', unsafe_allow_html=True)

# -------------------------------
# Image upload
# -------------------------------
uploaded_file = st.file_uploader("Upload a chest X-ray image", type=["jpg", "jpeg", "png"])
analyze_disabled = uploaded_file is None
col1, col2 = st.columns([2,1])

with col1:
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)

# -------------------------------
# Analyze Image button
# -------------------------------
with col2:
    if st.button("🩺 Analyze Image", disabled=analyze_disabled):
        # Spinner with random delay
        analyze_time = random.randint(7, 12)
        with st.spinner(f"Analyzing X-ray image... (approx {analyze_time} seconds)"):
            time.sleep(analyze_time)

        # Preprocess
        image_resized = image.resize((180, 180))
        image_array = np.array(image_resized) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        # Predict
        prediction = model.predict(image_array)[0]
        predicted_class = class_names[np.argmax(prediction)]
        confidence = float(np.max(prediction))

        # Result box with tooltip
        st.markdown(
            f'<div class="result-box {predicted_class}" title="{class_descriptions[predicted_class]}">'
            f'Prediction: {predicted_class}</div>', unsafe_allow_html=True)

        # Confidence progress bar
        st.markdown(
            f'<div class="progress-bar" style="width:{confidence*100}%; background-color:{class_colors[predicted_class]}">'
            f'{confidence*100:.2f}%</div>', unsafe_allow_html=True)

        # Clinical explanation card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Clinical Interpretation")
        st.write(class_descriptions[predicted_class])
        st.markdown('</div>', unsafe_allow_html=True)
