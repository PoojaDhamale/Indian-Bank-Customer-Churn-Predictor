import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ui_components import set_page_style, kpi_card, navigation_bar

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Evaluation | Bank Customer Churn Prediction",
    layout="wide"
)

# Apply premium dark styling
set_page_style()

# ------------------ NAVIGATION (Top Tab Navigation) ------------------
navigation_bar()

# ------------------ HEADER ------------------
st.header("🤖 Model Training & Evaluation")
st.markdown(
    """
    <div class="premium-card">
    This section explains the <b>modeling strategy</b>, <b>class imbalance considerations</b>, 
    and <b>hyperparameter tuning</b> that led to the final model selection.
    </div>
    """, unsafe_allow_html=True
)


# ================== CLASS IMBALANCE ==================
st.header("⚠️ Class Imbalance Problem")

st.markdown(
    """
    <div class="premium-card">
    The dataset shows a strong <b>class imbalance</b>, where churned customers are
    significantly fewer than retained customers.
    <ul>
        <li>Training directly on imbalanced data biases models toward predicting non-churn</li>
        <li>Accuracy alone becomes misleading</li>
        <li><b>Recall</b> for churn customers becomes the key business metric</li>
    </ul>
    </div>
    """, unsafe_allow_html=True
)


# ================== FINAL MODEL ==================
st.header("🚀 Final Model: XGBoost")

st.markdown(
    """
    <div class="premium-card">
    <b>Why XGBoost?</b>
    <ul>
        <li>Performs exceptionally well on structured tabular data</li>
        <li>Handles class imbalance effectively via specialized parameters</li>
        <li>Selected for final deployment due to superior recall</li>
    </ul>
    </div>
    """, unsafe_allow_html=True
)


# ================== MODEL PERFORMANCE ==================
st.header("📊 Model Performance Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    kpi_card("Final Model", "XGBoost", icon="🚀")

with col2:
    kpi_card("Accuracy", "49.5%", icon="✅")

with col3:
    kpi_card("Recall (Churn)", "90.0%", icon="🎯")

with col4:
    kpi_card("Precision (Churn)", "42.0%", icon="🔍")

# ================== CONFUSION MATRIX ==================
st.header("🧮 Confusion Matrix (XGBoost)")

st.markdown(
    """
    <div class="premium-card">
    The confusion matrix highlights the model’s ability to correctly identify churned customers (Recall).
    </div>
    """, unsafe_allow_html=True
)

# Confusion Matrix Data
cm = [[3049, 9373], [733, 6845]]

plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(6, 4))
sns.heatmap(
    cm, 
    annot=True, 
    fmt="d", 
    cmap="YlOrBr", 
    cbar=False, 
    annot_kws={"size": 14, "weight": "bold"},
    ax=ax
)
ax.set_xlabel("Predicted Label", color="white")
ax.set_ylabel("True Label", color="white")
ax.set_title("Confusion Matrix", color="#FBBF24", pad=20)
fig.patch.set_facecolor('#111111')
ax.set_facecolor('#111111')

st.pyplot(fig)

# No bottom navigation needed
