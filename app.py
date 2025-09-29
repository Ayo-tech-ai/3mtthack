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

# Define models: label, description, page path, color
models = [
    {"label": "🦟 Malaria Prediction", "desc": "Quickly predict Malaria from patient data.", "page": "pages/1_Malaria.py", "color": "#FFCDD2"},
    {"label": "🧠 Brain Abnormalities Detection", "desc": "Detect brain abnormalities from medical images.", "page": "pages/2_Brain.py", "color": "#C5CAE9"},
    {"label": "🎀 Breast Cancer Prediction", "desc": "Predict if a tumor is Malignant or Benign.", "page": "pages/3_BreastCancer.py", "color": "#F8BBD0"},
    {"label": "🫁 Tuberculosis Prediction", "desc": "Predict TB presence from patient X-ray and symptoms.", "page": "pages/4_TB.py", "color": "#B2EBF2"},
    {"label": "🫁 TB Diagnosis", "desc": "Assist diagnosis based on symptoms and patient metrics.", "page": "pages/5_TBSymptoms.py", "color": "#DCEDC8"},
    {"label": "🫁 Covid Image Detection", "desc": "Detect Covid from chest X-ray images.", "page": "pages/6_Covid.py", "color": "#FFE0B2"}
]

cols_per_row = 3
for i in range(0, len(models), cols_per_row):
    cols = st.columns(cols_per_row, gap="medium")
    for j, model in enumerate(models[i:i+cols_per_row]):
        with cols[j]:
            st.markdown(
                f"""
                <div style='
                    height: 220px;
                    padding: 20px; 
                    border-radius: 15px; 
                    background-color: {model['color']}; 
                    box-shadow: 3px 3px 15px rgba(0,0,0,0.15);
                    text-align: center;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;
                '>
                    <div>
                        <h3>{model['label']}</h3>
                        <p style='font-size:14px; color:#333;'>{model['desc']}</p>
                    </div>
                    <div>
                        <a href='{model["page"]}' style='
                            display:inline-block;
                            padding:8px 15px;
                            background-color:#1976D2;
                            color:white;
                            border-radius:8px;
                            text-decoration:none;
                            font-weight:bold;
                        '>➡️ Go to Model</a>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown("---")
st.info("ℹ️ More models will be added soon. Stay tuned!")
