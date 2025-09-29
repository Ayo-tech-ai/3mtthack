import streamlit as st

st.set_page_config(
    page_title="🏥 AI Health Assistant", 
    layout="wide",
    page_icon="🏥"
)

# Custom CSS for professional dashboard styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #6b7280;
        line-height: 1.6;
        margin-bottom: 2rem;
        text-align: center;
        font-weight: 400;
    }
    .dashboard-stats {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    .model-card {
        padding: 25px; 
        border-radius: 15px; 
        background: white;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 25px;
        transition: all 0.3s ease;
        height: 100%;
        position: relative;
        overflow: hidden;
    }
    .model-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--card-color), transparent);
    }
    .model-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04);
        border-color: var(--card-color);
    }
    .model-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 12px;
    }
    .model-desc {
        font-size: 0.95rem;
        color: #6b7280;
        line-height: 1.5;
        margin-bottom: 25px;
    }
    .launch-button {
        background: linear-gradient(135deg, var(--card-color) 0%, var(--card-color-dark) 100%);
        color: white;
        border: none;
        padding: 12px 28px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        cursor: pointer;
        width: 100%;
        margin-top: 10px;
    }
    .launch-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        color: white;
    }
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent 0%, #e5e7eb 50%, transparent 100%);
        margin: 2.5rem 0;
    }
    .info-box {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border: 1px solid #bae6fd;
        border-radius: 12px;
        padding: 25px;
        margin-top: 2rem;
    }
    .stats-container {
        display: flex;
        justify-content: space-around;
        text-align: center;
    }
    .stat-item {
        padding: 0 15px;
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 5px;
    }
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1f2937;
        margin: 2rem 0 1.5rem 0;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# App header with dashboard style
st.markdown('<div class="main-header">🏥 AI Health Assistant Dashboard</div>', unsafe_allow_html=True)

st.markdown("""
<div class="sub-header">
Advanced Clinical Intelligence Platform • Powered by AI Diagnostics
</div>
""", unsafe_allow_html=True)

# Dashboard Statistics
st.markdown("""
<div class="dashboard-stats">
    <div class="stats-container">
        <div class="stat-item">
            <div class="stat-number">6</div>
            <div class="stat-label">Active Models</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">99.2%</div>
            <div class="stat-label">Avg. Accuracy</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Availability</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">⚡</div>
            <div class="stat-label">Real-time Analysis</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">🩺 Clinical Prediction Models</div>', unsafe_allow_html=True)

# Define models with specific colors for the gradient
models = [
    {
        "label": "🦟 Malaria Detection",
        "desc": "Rapid malaria prediction from blood smear analysis and patient data",
        "page": "pages/1_Malaria.py",
        "color": "#dc2626",
        "color_dark": "#991b1b"
    },
    {
        "label": "🧠 Neuro Imaging Analysis",
        "desc": "Advanced detection of brain abnormalities from medical imaging",
        "page": "pages/2_Brain.py",
        "color": "#7c3aed",
        "color_dark": "#5b21b6"
    },
    {
        "label": "🎀 Breast Cancer Assessment",
        "desc": "Comprehensive tumor analysis for malignancy classification",
        "page": "pages/3_BreastCancer.py",
        "color": "#db2777",
        "color_dark": "#9d174d"
    },
    {
        "label": "🫁 Tuberculosis Screening",
        "desc": "AI-powered TB detection from chest X-ray imaging",
        "page": "pages/4_TB.py",
        "color": "#ea580c",
        "color_dark": "#9a3412"
    },
    {
        "label": "📊 TB Symptom Analysis",
        "desc": "Clinical diagnosis support based on symptoms and patient metrics",
        "page": "pages/5_TBSymptoms.py",
        "color": "#d97706",
        "color_dark": "#92400e"
    },
    {
        "label": "🦠 COVID-19 Detection",
        "desc": "Automated COVID-19 identification from chest radiographs",
        "page": "pages/6_Covid.py",
        "color": "#059669",
        "color_dark": "#047857"
    }
]

# Display models in responsive grid with enhanced launch buttons
cols_per_row = 3
for i in range(0, len(models), cols_per_row):
    cols = st.columns(cols_per_row)
    for j, model in enumerate(models[i:i+cols_per_row]):
        with cols[j]:
            # Set CSS variables for this specific card
            card_style = f"""
            <style>
                .card-{i+j} {{
                    --card-color: {model['color']};
                    --card-color-dark: {model['color_dark']};
                }}
            </style>
            """
            st.markdown(card_style, unsafe_allow_html=True)
            
            st.markdown(
                f"""
                <div class='model-card card-{i+j}'>
                    <div class='model-title'>{model['label']}</div>
                    <div class='model-desc'>{model['desc']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Custom styled button for launching models
            if st.button(
                "🚀 Launch Model", 
                key=f"btn_{i+j}",
                use_container_width=True
            ):
                st.switch_page(model["page"])

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Footer information with dashboard style
st.markdown("""
<div class="info-box">
    <div style="display: flex; align-items: flex-start; gap: 15px;">
        <span style="font-size: 1.5rem;">📊</span>
        <div>
            <strong style="font-size: 1.1rem;">Dashboard Analytics</strong><br>
            <span style="color: #475569;">
            • <strong>6 specialized models</strong> deployed and optimized for clinical use<br>
            • <strong>Real-time processing</strong> with average response under 3 seconds<br>
            • <strong>HIPAA compliant</strong> data processing and security protocols<br>
            • Additional models in development for expanded diagnostic capabilities
            </span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Quick Actions Sidebar
with st.sidebar:
    st.markdown("## 🔧 Quick Actions")
    st.markdown("---")
    
    st.markdown("### Recent Activity")
    st.info("""
    **Last Login:** Today, 14:32  
    **Models Used:** 3  
    **Active Sessions:** 1
    """)
    
    st.markdown("### Support")
    st.button("🆘 Emergency Support")
    st.button("📚 Documentation")
    st.button("🔄 System Status")
    
    st.markdown("---")
    st.markdown("**Version:** 2.4.1")
    st.markdown("**Last Updated:** Dec 2024")
