import streamlit as st
import pandas as pd
import numpy as np
import pickle
from ui_components import set_page_style, navigation_bar

# ---------------- LOAD ARTIFACTS ----------------
@st.cache_resource
def load_artifacts():
    with open("xgb_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    with open("encoder.pkl", "rb") as f:
        encoder = pickle.load(f)
    with open("model_features.pkl", "rb") as f:
        final_feature_names = pickle.load(f)
    return model, scaler, encoder, final_feature_names

model, scaler, encoder, final_feature_names = load_artifacts()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Prediction | Bank Customer Churn Prediction",
    layout="wide"
)

# Apply premium dark styling
set_page_style()

# ------------------ NAVIGATION (Top Tab Navigation) ------------------
navigation_bar()

st.header("🔮 Live Churn Prediction")
st.markdown(
    """
    <div class="premium-card">
    Enter customer details below to <b>predict churn risk in real time</b>. Our XGBoost model analyzes 
    demographic and behavioral data to provide localized risk assessments.
    </div>
    """, unsafe_allow_html=True
)

# ---------------- USER INPUT ----------------
with st.container():
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.subheader("📋 Customer Profile")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("🎂 Age", 18, 100, 35)
        tenure = st.number_input("📆 Tenure (Years)", 0, 20, 5)
        credit_score = st.number_input("💳 Credit Score", 300, 900, 650)
    
    with col2:
        balance = st.number_input("💰 Account Balance (INR)", 0.0, 10_000_000.0, 50000.0)
        salary = st.number_input("💼 Estimated Salary (INR)", 0.0, 10_000_000.0, 600000.0)
        num_products = st.selectbox("📦 Number of Products", [1, 2, 3, 4])
    
    with col3:
        has_cc = st.selectbox("💳 Has Credit Card?", ["Yes", "No"])
        active = st.selectbox("⚡ Is Active Member?", ["Yes", "No"])
        gender = st.selectbox("🧑 Gender", ["Male", "Female"])
    
    c1, c2 = st.columns(2)
    with c1:
        state = st.selectbox(
            "📍 State",
            ["Gujarat", "Karnataka", "Maharashtra", "Tamil Nadu",
             "Telangana", "Uttar Pradesh", "West Bengal"]
        )
    with c2:
        account_type = st.selectbox("🏦 Account Type", ["Savings", "Salary"])
        
    st.markdown("<br>", unsafe_allow_html=True)
    predict_btn = st.button("🔍 Predict Churn Risk", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PREDICTION LOGIC ----------------
if predict_btn:
    # Feature Engineering
    has_cc_val = 1 if has_cc == "Yes" else 0
    active_val = 1 if active == "Yes" else 0
    balance_to_salary = balance / salary if salary > 0 else 0
    tenure_numproducts = tenure * num_products
    low_credit_score = 1 if credit_score < 600 else 0
    highbalance_lowactivity = 1 if (balance > 100000 and active_val == 0) else 0

    input_df = pd.DataFrame({
        "Age": [age],
        "Tenure_Years": [tenure],
        "Balance_INR": [balance],
        "Num_Products": [num_products],
        "Has_Credit_Card": [has_cc_val],
        "Is_Active_Member": [active_val],
        "Estimated_Salary_INR": [salary],
        "Credit_Score": [credit_score],
        "Balance_to_Salary": [balance_to_salary],
        "Tenure_NumProducts": [tenure_numproducts],
        "Low_Credit_Score": [low_credit_score],
        "HighBalance_LowActivity": [highbalance_lowactivity],
        "Gender": [gender],
        "State": [state],
        "Account_Type": [account_type]
    })

    # Preprocess
    num_cols = ["Age", "Tenure_Years", "Balance_INR", "Num_Products", "Has_Credit_Card", "Is_Active_Member", "Estimated_Salary_INR", "Credit_Score", "Balance_to_Salary", "Tenure_NumProducts", "Low_Credit_Score", "HighBalance_LowActivity"]
    cat_cols = ["Gender", "State", "Account_Type"]
    
    X_num = scaler.transform(input_df[num_cols])
    X_cat = encoder.transform(input_df[cat_cols])
    X_final = np.concatenate([X_num, X_cat], axis=1)
    X_final = pd.DataFrame(X_final, columns=final_feature_names)

    with st.spinner("Analyzing data patterns..."):
        prob = model.predict_proba(X_final)[0][1]
        prediction = model.predict(X_final)[0]

    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.subheader("📊 Prediction Result")
    
    res_col1, res_col2 = st.columns([1, 2])
    
    with res_col1:
        if prediction == 1:
            st.error("⚠️ **High Churn Risk**")
        else:
            st.success("✅ **Low Churn Risk**")
        st.metric("Churn Probability", f"{prob:.1%}")
    
    with res_col2:
        st.progress(int(prob * 100))
        if prob > 0.7:
            st.warning("📢 **Immediate Action Required:** Customer shows strong exit intent indicators.")
        elif prob > 0.4:
            st.info("📌 **Observation Needed:** Customer engagement is declining.")
        else:
            st.success("🎉 **Stable Customer:** High likelihood of retention.")
            
    st.markdown('</div>', unsafe_allow_html=True)

# No bottom navigation needed

