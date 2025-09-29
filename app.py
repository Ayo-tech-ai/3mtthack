import streamlit as st

st.set_page_config(
    page_title="🏥 AI Health Assistant", 
    layout="wide",
    page_icon="🏥"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4b5563;
        line-height: 1.6;
        margin-bottom: 2rem;
    }
    .model-card {
        padding: 25px; 
        border-radius: 12px; 
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
        text-align: center;
        margin-bottom: 25px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        height: 100%;
    }
    .model-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05);
    }
    .model-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 12px;
    }
    .model-desc {
        font-size: 0.95rem;
        color: #64748b;
        line-height: 1.5;
        margin-bottom: 20px;
    }
    .stButton button {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent 0%, #e2e8f0 50%, transparent 100%);
        margin: 2rem 0;
    }
    .info-box {
        background: #f0f9ff;
        border: 1px solid #bae6fd;
        border-radius: 10px;
        padding: 20px;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# App header
st.markdown('<div class="main-header">🏥 AI Health Assistant</div>', unsafe_allow_html=True)

st.markdown("""
<div class="sub-header">
Welcome to the AI Health Assistant—your intelligent partner in healthcare diagnostics.  
This platform empowers medical professionals with AI-driven insights to enhance diagnostic accuracy, 
accelerate decision-making, and improve patient outcomes. Select a specialized model below to begin.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Section header
st.subheader("🩺 Clinical Prediction Models")

# Define models
models = [
    {
        "label": "🦟 Malaria Detection",
        "desc": "Rapid malaria prediction from blood smear analysis and patient data",
        "page": "pages/1_Malaria.py",
        "color": "#dc2626"
    },
    {
        "label": "🧠 Neuro Imaging Analysis",
        "desc": "Advanced detection of brain abnormalities from medical imaging",
        "page": "pages/2_Brain.py",
        "color": "#7c3aed"
    },
    {
        "label": "🎀 Breast Cancer Assessment",
        "desc": "Comprehensive tumor analysis for malignancy classification",
        "page": "pages/3_BreastCancer.py",
        "color": "#db2777"
    },
    {
        "label": "🫁 Tuberculosis Screening",
        "desc": "AI-powered TB detection from chest X-ray imaging",
        "page": "pages/4_TB.py",
        "color": "#ea580c"
    },
    {
        "label": "📊 TB Symptom Analysis",
        "desc": "Clinical diagnosis support based on symptoms and patient metrics",
        "page": "pages/5_TBSymptoms.py",
        "color": "#d97706"
    },
    {
        "label": "🦠 COVID-19 Detection",
        "desc": "Automated COVID-19 identification from chest radiographs",
        "page": "pages/6_Covid.py",
        "color": "#059669"
    }
]

# Display models in responsive grid
cols_per_row = 3
for i in range(0, len(models), cols_per_row):
    cols = st.columns(cols_per_row)
    for j, model in enumerate(models[i:i+cols_per_row]):
        with cols[j]:
            st.markdown(
                f"""
                <div class='model-card'>
                    <div class='model-title' style='color: {model["color"]};'>{model['label']}</div>
                    <div class='model-desc'>{model['desc']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.page_link(model["page"], label="Access Model", use_container_width=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Footer information
st.markdown("""
<div class="info-box">
    <div style="display: flex; align-items: center; gap: 10px;">
        <span style="font-size: 1.2rem;">ℹ️</span>
        <div>
            <strong>Platform Information</strong><br>
            Additional specialized models are currently in development and will be deployed shortly. 
            For technical support or to request new features, please contact our clinical support team.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
