import streamlit as st

# App title
st.title("🏥 AI Health Assistant")
st.write("""
Welcome to the AI Health Assistant!  
This app allows you to check different diseases using AI-powered models.  
Select a condition below to start your prediction.
""")

# Buttons to navigate to each page
st.subheader("Available Models")

st.page_link("pages/1_Malaria.py", label="🦟 Malaria Prediction")
st.page_link("pages/2_Brain.py", label="🧠 Brain Abnormalities Detection")
st.page_link("pages/3_BreastCancer.py", label="🎀 Breast Cancer Prediction")
st.page_link("pages/4_TB.py", label="🫁 Tuberculosis Prediction")
st.page_link("pages/5_TBSymptoms.py", label ="TB Diagnosis")

st.markdown("---")
st.info("ℹ️ More models will be added soon. Stay tuned!")
