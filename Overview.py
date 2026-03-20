import streamlit as st
import pandas as pd
from ui_components import set_page_style, kpi_card, navigation_bar

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Overview | Bank Customer Churn Prediction",
    layout="wide"
)

# Apply premium dark styling
set_page_style()

# ------------------ NAVIGATION (Top Tab Navigation) ------------------
navigation_bar()

# ------------------ LOAD RAW DATA ------------------
@st.cache_data
def load_data():
    return pd.read_csv("indian_bank_customer_churn.csv")

df = load_data()

# ------------------ KPI CALCULATIONS ------------------
total_customers = df.shape[0]
churned_customers = df[df["Churn"] == 1].shape[0]
retained_customers = df[df["Churn"] == 0].shape[0]
active_customers = df[df["Is_Active_Member"] == 1].shape[0]
inactive_customers = df[df["Is_Active_Member"] == 0].shape[0]
churn_rate = round((churned_customers / total_customers) * 100, 2)

# ------------------ HEADER ------------------
st.header("🏢 Overview & Key Metrics")
st.markdown(
    """
    <div class="premium-card">
    This application predicts whether a bank customer is likely to <b>churn (leave the bank)</b> 
    based on their demographic, financial, and behavioral information.
    </div>
    """, unsafe_allow_html=True
)

# ------------------ PROBLEM STATEMENT ------------------
st.header("📌 Problem Statement")

st.markdown(
    """
    <div class="premium-card">
    Customer churn is a major challenge for banks, as acquiring new customers is significantly 
    more expensive than retaining existing ones.
    
    <b>Objectives:</b>
    <ul>
        <li>Identify customers who are at high risk of churn</li>
        <li>Enable proactive customer retention strategies</li>
        <li>Improve customer lifetime value using data-driven insights</li>
    </ul>
    </div>
    """, unsafe_allow_html=True
)

# ------------------ DATASET KPIs ------------------
st.header("📊 Dataset KPIs (Raw Data)")

k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    kpi_card("Total Customers", f"{total_customers:,}", icon="👥")

with k2:
    kpi_card("Churned", f"{churned_customers:,}", icon="❌")

with k3:
    kpi_card("Retained", f"{retained_customers:,}", icon="✅")

with k4:
    kpi_card("Active Members", f"{active_customers:,}", icon="🟢")

with k5:
    kpi_card("Churn Rate", f"{churn_rate}%", icon="📉")

# ------------------ ML PIPELINE ------------------
st.header("⚙️ Machine Learning Pipeline")

st.markdown(
    """
    <div class="premium-card" style="text-align: center; font-weight: 600; font-family: 'Inter', sans-serif;">
    Data Cleaning → Feature Engineering → Model Training → Model Evaluation → Deployment
    </div>
    """, unsafe_allow_html=True
)

# ------------------ MODELS USED ------------------
st.header("🤖 Models Used")

m1, m2 = st.columns(2)

with m1:
    st.markdown(
        """
        <div class="premium-card">
        <h3 style="color: #FBBF24; margin-top:0;">🌲 Random Forest</h3>
        <p>Used as an initial benchmark to establish baseline performance metrics.</p>
        </div>
        """, unsafe_allow_html=True
    )

with m2:
    st.markdown(
        """
        <div class="premium-card">
        <h3 style="color: #FBBF24; margin-top:0;">⚡ XGBoost</h3>
        <p>Optimized for high recall to ensure maximum detection of potential churners.</p>
        </div>
        """, unsafe_allow_html=True
    )

# No bottom navigation needed


