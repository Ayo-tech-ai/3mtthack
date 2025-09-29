import streamlit as st

# Page configuration
st.set_page_config(
    page_title="🏥 AI Health Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    * { font-family: 'Inter', sans-serif; }
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 0 0 20px 20px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    
    .feature-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        height: 240px;
        border: 1px solid #e0e0e0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        margin-bottom: 2.5rem;  /* Increased spacing between rows */
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        border-color: #1976D2;
    }
    
    .card-title { font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a1a1a; }
    .card-desc { font-size: 0.9rem; color: #666; line-height: 1.4; }
    
    .cta-button {
        background: linear-gradient(135deg, #1976D2 0%, #1565C0 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        text-decoration: none;
        font-weight: 500;
        display: inline-block;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        text-align: center;
        width: 100%;
    }
    
    .cta-button:hover {
        background: linear-gradient(135deg, #1565C0 0%, #0D47A1 100%);
        transform: scale(1.02);
        color: white;
        text-decoration: none;
    }
    
    .welcome-text { font-size: 1.1rem; line-height: 1.6; color: #444; text-align: center; max-width: 800px; margin: 0 auto 2rem auto; }
    .section-title { font-size: 1.5rem; font-weight: 600; color: #333; margin-bottom: 1.5rem; text-align: center; }
    .coming-soon { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 12px; padding: 1.5rem; text-align: center; margin-top: 2rem; }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="main-header">
    <h1 style="margin:0; font-size:2.5rem; font-weight:700;">🏥 AI Health Assistant</h1>
    <p style="margin:0.5rem 0 0 0; font-size:1.2rem; opacity:0.9;">
        Intelligent Diagnostics for Healthcare Professionals
    </p>
</div>
""", unsafe_allow_html=True)

# Welcome Section
st.markdown("""
<div class="welcome-text">
    Welcome to the next generation of medical diagnostics. Our AI-powered platform assists 
    <strong>doctors, nurses, and healthcare professionals</strong> with accurate, rapid predictions 
    to enhance diagnostic speed and precision. Select a specialized model below to begin.
</div>
""", unsafe_allow_html=True)

# Models Grid Section
st.markdown('<div class="section-title">🔬 Available Diagnostic Models</div>', unsafe_allow_html=True)

# Define models
models = [
    {"label": "🦟 Malaria Prediction", "desc": "Quickly predict Malaria from patient data.", "page": "pages/1_Malaria.py", "color": "#FFEBEE", "icon": "🦟"},
    {"label": "🧠 Brain Abnormalities Detection", "desc": "Detect brain abnormalities from medical images.", "page": "pages/2_Brain.py", "color": "#F3E5F5", "icon": "🧠"},
    {"label": "🎀 Breast Cancer Prediction", "desc": "Predict if a tumor is Malignant or Benign.", "page": "pages/3_BreastCancer.py", "color": "#FCE4EC", "icon": "🎀"},
    {"label": "🫁 Tuberculosis Prediction", "desc": "Predict TB presence from patient X-ray and symptoms.", "page": "pages/4_TB.py", "color": "#E1F5FE", "icon": "🫁"},
    {"label": "🫁 TB Diagnosis", "desc": "Assist diagnosis based on symptoms and patient metrics.", "page": "pages/5_TBSymptoms.py", "color": "#E8F5E8", "icon": "📊"},
    {"label": "🫁 Covid Image Detection", "desc": "Detect Covid from chest X-ray images.", "page": "pages/6_Covid.py", "color": "#FFF3E0", "icon": "🦠"}
]

# Create grid layout
cols_per_row = 3
for i in range(0, len(models), cols_per_row):
    cols = st.columns(cols_per_row, gap="large")
    for j, model in enumerate(models[i:i+cols_per_row]):
        with cols[j]:
            st.markdown(
                f"""
                <div class="feature-card" style="border-left: 4px solid {model['color'].replace('#', '#80')}">
                    <div>
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">{model['icon']}</div>
                        <div class="card-title">{model['label']}</div>
                        <div class="card-desc">{model['desc']}</div>
                    </div>
                    <div style="margin-top: 1rem;">
                        <a href='{model["page"]}' class="cta-button">
                            ➡️ Go to Model
                        </a>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

# Footer Section
st.markdown("---")
st.markdown("""
<div class="coming-soon">
    <h4 style="margin:0 0 0.5rem 0; color:#333;">ℹ️ More Models Coming Soon</h4>
    <p style="margin:0; color:#666;">More models will be added soon. Stay tuned for updates!</p>
</div>
""", unsafe_allow_html=True)

# Security Notice
st.markdown("""
<div style="text-align: center; margin-top: 2rem; padding: 1rem; background: #f8f9fa; border-radius: 10px;">
    <small style="color: #666;">
        🔒 <strong>Secure & Confidential</strong> • All data is processed with privacy in mind
    </small>
</div>
""", unsafe_allow_html=True)
