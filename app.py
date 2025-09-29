import streamlit as st

st.set_page_config(page_title="🏥 AI Health Assistant", layout="wide")

# App title and intro
st.title("🏥 AI Health Assistant")
st.write("""
Welcome to the AI Health Assistant!  
This app is designed to assist healthcare professionals—doctors, nurses, caregivers—with AI-powered predictions to speed up diagnosis and improve accuracy.  
Select a condition below to start your prediction.
""")

st.markdown("---")
st.subheader("Available Models")

# Define models: label, description, page path
models = [
    {
        "label": "🦟 Malaria Prediction",
        "desc": "Quickly predict Malaria from patient data.",
        "page": "pages/1_Malaria.py"
    },
    {
        "label": "🧠 Brain Abnormalities Detection",
        "desc": "Detect brain abnormalities from medical images.",
        "page": "pages/2_Brain.py"
    },
    {
        "label": "🎀 Breast Cancer Prediction",
        "desc": "Predict if a tumor is Malignant or Benign.",
        "page": "pages/3_BreastCancer.py"
    },
    {
        "label": "🫁 Tuberculosis Prediction",
        "desc": "Predict TB presence from patient X-ray and symptoms.",
        "page": "pages/4_TB.py"
    },
    {
        "label": "🫁 TB Diagnosis",
        "desc": "Assist diagnosis based on symptoms and patient metrics.",
        "page": "pages/5_TBSymptoms.py"
    },
    {
        "label": "🫁 Covid Image Detection",
        "desc": "Detect Covid from chest X-ray images.",
        "page": "pages/6_Covid.py"
    }
]

# Display in two rows of three columns
cols_per_row = 3
for i in range(0, len(models), cols_per_row):
    cols = st.columns(cols_per_row)
    for j, model in enumerate(models[i:i+cols_per_row]):
        with cols[j]:
            st.markdown(
                f"""
                <div style='
                    padding: 20px; 
                    border-radius: 15px; 
                    background-color: #f5f5f5; 
                    box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
                    text-align: center;
                    margin-bottom: 20px;
                '>
                    <h3>{model['label']}</h3>
                    <p style='font-size:14px; color:#333;'>{model['desc']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            # Proper multi-page navigation
            st.page_link(model["page"], label="➡️ Go to Model")

st.markdown("---")
st.info("ℹ️ More models will be added soon. Stay tuned!")
