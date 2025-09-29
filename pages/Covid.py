import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import tensorflow as tf
import os
import gdown  # Used to download from Google Drive

# Google Drive file ID for the .h5 model
FILE_ID = "1eLk7CUpfx5ZnTcoiV6w-ecuI4JfzKXIS"
MODEL_PATH = "my1_cnn_lung_model.h5"

# Download the model if it doesn't exist
if not os.path.exists(MODEL_PATH):
    gdown.download(f"https://drive.google.com/uc?id={FILE_ID}", MODEL_PATH, quiet=False)

# Load the model
model = load_model(MODEL_PATH)

# Define class names
class_names = ['COVID', 'NORMAL']

# App title
st.title("AI COVID Lung Detection System")

# Upload image
uploaded_file = st.file_uploader("Upload a chest X-ray image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess image
    image = image.resize((180, 180))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

    # Predict
    prediction = model.predict(image_array)[0]
    confidence = float(np.max(prediction)) * 100
    predicted_class = class_names[np.argmax(prediction)]

    # Display result
    st.markdown(f"### Prediction: **{predicted_class}**")
    st.markdown(f"**Confidence:** {confidence:.2f}%")

    if st.button("Like"):
        st.success("Thanks for your support!")

# Footer
st.markdown("---")
st.markdown("This tool is for educational purposes only and not a substitute for professional medical advice.")
  
