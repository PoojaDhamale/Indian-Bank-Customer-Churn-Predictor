import streamlit as st
import pandas as pd
from ui_components import set_page_style, navigation_bar

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Engineering | Bank Customer Churn Prediction",
    layout="wide"
)

# Apply premium dark styling
set_page_style()

# ------------------ NAVIGATION (Top Tab Navigation) ------------------
navigation_bar()

# ------------------ LOAD FEATURED DATA ------------------
@st.cache_data
def load_data():
    return pd.read_csv("indian_bank_customer_churn_featured.csv")

df = load_data()

# ------------------ HEADER ------------------
st.header("🧠 Feature Engineering & Preprocessing")
st.markdown(
    """
    <div class="premium-card">
    This section explains the <b>feature engineering techniques</b> applied to the raw dataset 
    to improve model performance and capture hidden customer behavior patterns.
    </div>
    """, unsafe_allow_html=True
)

# ================== WHY FEATURE ENGINEERING ==================
st.header("📌 Why Feature Engineering?")

st.markdown(
    """
    <div class="premium-card">
    Raw customer attributes often fail to fully represent <b>customer risk and behavior</b>. 
    Feature engineering helps:
    <ul>
        <li>Capture financial stress indicators</li>
        <li>Represent customer engagement strength</li>
        <li>Flag specific high-risk churn patterns</li>
        <li>Improve model learning capabilities</li>
    </ul>
    </div>
    """, unsafe_allow_html=True
)

# ================== ENGINEERED FEATURES ==================
st.header("⚙️ Engineered Features")

st.markdown(
    """
    <div class="premium-card">
    <b>1️⃣ Balance_to_Salary:</b> Ratio of account balance to estimated salary. Indicates financial pressure and dependency on the bank.<br><br>
    <b>2️⃣ Tenure_NumProducts:</b> Interaction term between tenure and number of products. Represents depth of customer relationship.<br><br>
    <b>3️⃣ Low_Credit_Score:</b> Binary flag for Credit Score < 600. Highlights potential financial instability.<br><br>
    <b>4️⃣ HighBalance_LowActivity:</b> Flags customers with substantial balance but minimal interactions. High exit intent indicator.
    </div>
    """, unsafe_allow_html=True
)

# ================== SAMPLE DATA ==================
st.header("🔍 Engineered Dataset Preview")
st.dataframe(df.head(10), use_container_width=True)

# No bottom navigation needed


