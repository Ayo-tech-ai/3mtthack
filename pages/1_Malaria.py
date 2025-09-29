import streamlit as st
import joblib
from fpdf import FPDF
import base64
import os

# ✅ Load your saved model from the models/ folder
model_path = os.path.join("models", "Malpred.joblib")
model = joblib.load(model_path)

# Label mapping
label_mapping = {1: "High Possibility of Malaria", 0: "Low Possibility of Malaria"}

# Define the prediction function
def predict_malaria(input_data):
    prediction = model.predict([input_data])[0]  # Predict the class (0 or 1)
    return label_mapping[prediction]

# Function to generate and save the PDF
def generate_pdf(result, symptoms, bp, temperature):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Medical Report", ln=True, align='C')
    pdf.ln(10)
    
    # Add prediction result
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, txt="Prediction Result:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Likelihood of Illness: {result}", ln=True)
    pdf.ln(10)
    
    # Add symptoms section
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, txt="Symptoms:", ln=True)
    pdf.set_font("Arial", size=12)
    for symptom_name, presence in symptoms.items():
        pdf.cell(200, 10, txt=f"{symptom_name}: {presence}", ln=True)
    pdf.ln(10)
    
    # Add additional medical information
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, txt="Additional Medical Information:", ln=True)
    pdf.set_font("Arial", size=12)
    if bp:
        pdf.cell(200, 10, txt=f"Blood Pressure: {bp}", ln=True)
    else:
        pdf.cell(200, 10, txt="Blood Pressure: Invalid or not provided.", ln=True)
    pdf.cell(200, 10, txt=f"Temperature: {temperature:.1f}°C", ln=True)
    
    # Save PDF to a file
    pdf_file = "medical_report.pdf"
    pdf.output(pdf_file)
    return pdf_file

# Streamlit App
st.title("🦟 Malaria Prediction")
st.write("This AI-powered tool predicts the likelihood of a Patient having malaria based on symptoms.")

# Dropdowns for symptoms
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

# Map "Yes" and "No" to 1 and 0 for model input
input_data = [1 if value == "Yes" else 0 for value in symptoms.values()]

# Section for additional inputs
st.subheader("Additional Medical Inputs")
bp = st.text_input("Blood Pressure (e.g., 120/80)")
temperature = st.number_input("Temperature (in °C)", min_value=30.0, max_value=45.0, step=0.1)

# Prediction button
if st.button("Predict"):
    # Validate BP input
    try:
        systolic, diastolic = map(int, bp.split("/"))
        bp_valid = f"{systolic}/{diastolic} mmHg"
    except ValueError:
        bp_valid = None  # Set None if BP is invalid

    # Model prediction
    result = predict_malaria(input_data)

    # Display prediction
    st.markdown(f"### 🧾 Prediction Result: **{result}**")

    # Display additional medical information
    st.subheader("Additional Information:")
    if bp_valid:
        st.write(f"Blood Pressure: {bp_valid}")
    else:
        st.write("Blood Pressure: Invalid or not provided.")
    st.write(f"Temperature: {temperature:.1f}°C")

    # Generate PDF
    pdf_file = generate_pdf(result, symptoms, bp_valid, temperature)

    # Provide Download Option
    with open(pdf_file, "rb") as pdf:
        b64_pdf = base64.b64encode(pdf.read()).decode('utf-8')
        href = f'<a href="data:application/octet-stream;base64,{b64_pdf}" download="{pdf_file}">📥 Download Medical Report (PDF)</a>'
        st.markdown(href, unsafe_allow_html=True)
