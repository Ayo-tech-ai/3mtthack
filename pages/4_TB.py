import streamlit as st
import tensorflow as tf
from tensorflow.keras import layers
from PIL import Image
import numpy as np
import os

# -------------------------------
# Page title
# -------------------------------
st.title("🫁 Lung X-ray Disease Classifier")
st.write("Upload a chest X-ray image, and the model will predict whether it is NORMAL, PNEUMONIA, or TUBERCULOSIS.")

# -------------------------------
# Load the trained model
# -------------------------------
@st.cache_resource
def load_model():
    # Path relative to this file
    MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/NPT lungs_model.keras")
    
    if not os.path.exists(MODEL_PATH):
        st.error(f"Model file not found at {MODEL_PATH}")
        return None

    model = tf.keras.models.load_model(MODEL_PATH)
    return model

model = load_model()
if model is None:
    st.stop()

# -------------------------------
# Class names
# -------------------------------
class_names = ['NORMAL', 'PNEUMONIA', 'TUBERCULOSIS']

# -------------------------------
# Image upload
# -------------------------------
uploaded_file = st.file_uploader("Choose a chest X-ray image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load and display the image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded X-ray", use_column_width=True)

    # Preprocess image
    IMG_SIZE = (224, 224)
    img = image.resize(IMG_SIZE)
    img_array = np.array(img) / 255.0        # normalize to [0,1]
    img_array = np.expand_dims(img_array, axis=0)  # add batch dimension

    # Make prediction
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_index]
    confidence = predictions[0][predicted_index]

    # Display results
    st.markdown(f"### Prediction: **{predicted_class}**")
    st.markdown(f"Confidence: **{confidence*100:.2f}%**")

    # Optional: show all class probabilities as a bar chart
    st.bar_chart({class_names[i]: float(predictions[0][i]) for i in range(len(class_names))})
