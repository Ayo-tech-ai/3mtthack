import streamlit as st
import tensorflow as tf
from tensorflow.keras import layers
from PIL import Image
import numpy as np

# -------------------------------
# App title
# -------------------------------
st.set_page_config(page_title="Lung Disease Classifier", page_icon="🫁")
st.title("🫁 Lung X-ray Disease Classifier")
st.write("Upload a chest X-ray image, and the model will predict whether it is NORMAL, PNEUMONIA, or TUBERCULOSIS.")

# -------------------------------
# Load the trained model from Models folder
# -------------------------------
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("Models/NPT lungs_model.keras")
    return model

model = load_model()

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

    # Preprocess the image
    IMG_SIZE = (224, 224)
    img = image.resize(IMG_SIZE)
    img_array = np.array(img) / 255.0           # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Make prediction
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_index]
    confidence = predictions[0][predicted_index]

    # Display results
    st.markdown(f"### Prediction: **{predicted_class}**")
    st.markdown(f"Confidence: **{confidence*100:.2f}%**")
