import streamlit as st
import joblib
from fpdf import FPDF
import base64
import os

# ----------------------------
# Load your model
# ----------------------------
model_path = os.path.join("models", "Malpred.joblib")
model = joblib.load(model_path)

# Label mapping
label_mapping = {1: "High Possibility of Malaria", 0: "Low Possibility of Malaria"}

# Prediction function
def predict_malaria(input_data):
    prediction = model.predict([input_data])[0]  # Predict the class (0 or 1)
    return label_mapping[prediction]

# PDF generation function
def generate_pdf(result, symptoms, bp, temperature):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Medical Report", ln=True, align='C')
    pdf.ln(10)
    
    # Prediction result
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, txt="Prediction Result:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Likelihood of Illness: {result}", ln=True)
    pdf.ln(10)
    
    # Symptoms
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, txt="Symptoms:", ln=True)
    pdf.set_font("Arial", size=12)
    for symptom_name, presence in symptoms.items():
        pdf.cell(200, 10, txt=f"{symptom_name}: {presence}", ln=True)
    pdf.ln(10)
    
    # Additional info
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, txt="Additional Medical Information:", ln=True)
    pdf.set_font("Arial", size=12)
    if bp:
        pdf.cell(200, 10, txt=f"Blood Pressure: {bp}", ln=True)
    else:
        pdf.cell(200, 10, txt="Blood Pressure: Invalid or not provided.", ln=True)
    pdf.cell(200, 10, txt=f"Temperature: {temperature:.1f}°C", ln=True)
    
    pdf_file = "medical_report.pdf"
    pdf.output(pdf_file)
    return pdf_file

# ----------------------------
# Streamlit App UI/UX Styling
# ----------------------------
st.set_page_config(
    page_title="🦟 Malaria Detector",
    layout="wide",
    page_icon="🩺"
)

# Custom CSS
st.markdown("""
    <style>
    /* General background and font */
    .stApp {
        background-color: #f5f8fa;
        font-family: 'Arial', sans-serif;
    }

    /* Title styling */
    .main-title {
        font-size: 2.8rem;
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

    /* Card-like sections */
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        margin-bottom: 25px;
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

    .high-risk {
        background-color: #eb2f06;
    }

    .low-risk {
        background-color: #079992;
    }

    /* Buttons styling */
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
st.markdown('<div class="main-title">🦟 Malaria Detection Tool</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Predict the likelihood of malaria based on patient symptoms.</div>', unsafe_allow_html=True)

# ----------------------------
# Symptoms Input Section
# ----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Patient Symptoms")

col1, col2 = st.columns(2)

with col1:
    symptoms = {
        "Fever": st.selectbox("Fever", options=["Yes", "No"]),
        "Cold": st.selectbox("Cold", options=["Yes", "No"]),
        "Rigor": st.selectbox("Rigor", options=["Yes", "No"]),
        "Fatigue": st.selectbox("Fatigue", options=["Yes", "No"]),
    }

with col2:
    symptoms.update({
        "Headache": st.selectbox("Headache", options=["Yes", "No"]),
        "Bitter Tongue": st.selectbox("Bitter Tongue", options=["Yes", "No"]),
        "Vomiting": st.selectbox("Vomiting", options=["Yes", "No"]),
        "Diarrhea": st.selectbox("Diarrhea", options=["Yes", "No"]),
    })

st.markdown('</div>', unsafe_allow_html=True)

# Map "Yes"/"No" to 1/0
input_data = [1 if value == "Yes" else 0 for value in symptoms.values()]

# ----------------------------
# Additional Medical Inputs
# ----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Additional Medical Inputs")
bp = st.text_input("Blood Pressure (e.g., 120/80)")
temperature = st.number_input("Temperature (°C)", min_value=30.0, max_value=45.0, step=0.1)
st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# Prediction Button
# ----------------------------
if st.button("Predict"):
    try:
        systolic, diastolic = map(int, bp.split("/"))
        bp_valid = f"{systolic}/{diastolic} mmHg"
    except ValueError:
        bp_valid = None

    result = predict_malaria(input_data)

    # ----------------------------
    # Display Prediction
    # ----------------------------
    if result == "High Possibility of Malaria":
        risk_class = "high-risk"
    else:
        risk_class = "low-risk"

    st.markdown(f'<div class="result-box {risk_class}">🧾 Prediction Result: {result}</div>', unsafe_allow_html=True)

    # ----------------------------
    # Additional Info
    # ----------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Additional Information:")
    if bp_valid:
        st.write(f"Blood Pressure: {bp_valid}")
    else:
        st.write("Blood Pressure: Invalid or not provided.")
    st.write(f"Temperature: {temperature:.1f}°C")
    st.markdown('</div>', unsafe_allow_html=True)

    # ----------------------------
    # Generate PDF
    # ----------------------------
    pdf_file = generate_pdf(result, symptoms, bp_valid, temperature)
    with open(pdf_file, "rb") as pdf:
        b64_pdf = base64.b64encode(pdf.read()).decode('utf-8')
        href = f'<a href="data:application/octet-stream;base64,{b64_pdf}" download="{pdf_file}">📥 Download Medical Report (PDF)</a>'
        st.markdown(href, unsafe_allow_html=True)
