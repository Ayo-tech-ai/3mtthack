import streamlit as st

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="🏥 AI Health Assistant",
    layout="wide"
)

# -------------------------------
# App title and introduction
# -------------------------------
st.title("🏥 AI Health Assistant")
st.markdown("""
Welcome to the **AI Health Assistant**!  
This app assists healthcare professionals—doctors, nurses, and caregivers—in making faster, more accurate diagnoses using AI-powered models.
""")
st.markdown("---")

# -------------------------------
# Models info: page, label, icon, description
# -------------------------------
models = [
    {
        "page": "pages/1_Malaria.py",
        "label": "🦟 Malaria Prediction",
        "desc": "Predict malaria risk based on patient symptoms and clinical data."
    },
    {
        "page": "pages/2_Brain.py",
        "label": "🧠 Brain Abnormalities Detection",
        "desc": "Detect possible brain abnormalities from MRI or CT scans quickly."
    },
    {
        "page": "pages/3_BreastCancer.py",
        "label": "🎀 Breast Cancer Prediction",
        "desc": "Predict tumor malignancy based on patient metrics with high accuracy."
    },
    {
        "page": "pages/4_TB.py",
        "label": "🫁 Tuberculosis Prediction",
        "desc": "Screen for TB using patient clinical details and AI-assisted diagnosis."
    },
    {
        "page": "pages/5_TBSymptoms.py",
        "label": "🫁 TB Diagnosis",
        "desc": "Detailed TB symptom analysis to support quick clinical decisions."
    },
    {
        "page": "pages/6_Covid.py",
        "label": "🫁 Covid Image Detection",
        "desc": "Detect COVID-19 infections from X-ray or CT images efficiently."
    },
]

# -------------------------------
# Display models in "cards"
# -------------------------------
cols_per_row = 3
for i in range(0, len(models), cols_per_row):
    cols = st.columns(cols_per_row)
    for j, model in enumerate(models[i:i+cols_per_row]):
        with cols[j]:
            st.markdown(
                f"""
                <div style='
                    padding: 15px; 
                    border-radius: 10px; 
                    background-color: #f0f2f6; 
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                    text-align: center;
                    margin-bottom: 15px;
                '>
                    <h3>{model['label']}</h3>
                    <p style='font-size:14px; color:#333;'>{model['desc']}</p>
                    <a href="{model['page']}" style='
                        text-decoration:none; 
                        color:white; 
                        background-color:#4B7BEC; 
                        padding:8px 15px; 
                        border-radius:5px;
                        display:inline-block;
                        margin-top:10px;
                    '>➡️ Go to Model</a>
                </div>
                """, unsafe_allow_html=True
            )

# -------------------------------
# Footer info
# -------------------------------
st.markdown("---")
st.info("ℹ️ More models will be added soon. This app is continuously updated to assist caregivers and healthcare professionals.")
