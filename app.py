import streamlit as st
from ui_components import set_page_style, navigation_bar

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="India Bank Churn Prediction",
    page_icon="🏦",
    layout="wide"
)

# Apply premium dark styling
set_page_style()

# ------------------ NAVIGATION (Top Tab Navigation) ------------------
navigation_bar()

# Global title is in the navigation bar

st.markdown("""
<div class="premium-card">
    <h2 style="margin-top:0;">Welcome to the Churn Prediction System</h2>
    <p>This application leverages advanced <b>Machine Learning</b> to predict customer churn in the Indian banking sector. 
    By analyzing demographic and behavioral patterns, we provide <b>actionable retention strategies</b> to help banks minimize 
    customer attrition and improve long-term value.</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# PROJECT HIGHLIGHTS
# --------------------------------------------------
st.markdown("""
<div class="premium-card">
    <h3 style="margin-top:0;">✅ Project Highlights</h3>
    <ul style="margin-bottom:0;">
        <li><b>Realistic Dataset:</b> Derived from Indian banking scenarios.</li>
        <li><b>Feature Engineering:</b> Domain-driven behavioral features.</li>
        <li><b>XGBoost Model:</b> Optimized for high recall to catch potential churners.</li>
        <li><b>Business Logic:</b> Strategies tailored to risk levels.</li>
    </ul>
    <p style="margin-top:10px; font-size:0.9rem; color:#64748B;">This project demonstrates end-to-end ML engineering and data-driven decision-making.</p>
</div>
""", unsafe_allow_html=True)

# No bottom navigation needed

