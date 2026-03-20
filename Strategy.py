import streamlit as st
from ui_components import set_page_style, navigation_bar

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Strategy | Bank Customer Churn Prediction",
    layout="wide"
)

# Apply premium dark styling
set_page_style()

# ------------------ NAVIGATION (Top Tab Navigation) ------------------
navigation_bar()

st.header("📌 Retention Strategy Dashboard")

st.markdown("""
<div class="premium-card">
    This page translates <b>churn predictions</b> into <b>business retention actions</b>. 
    The objective is to reduce customer churn by applying data-driven strategies based on predicted risk levels.
</div>
""", unsafe_allow_html=True)

# ---------------- RISK SEGMENT INPUT ----------------
st.header("🔍 Analyze Customer Risk Level")
st.markdown("Adjust the slider to see strategies for different churn probability levels.")

churn_prob = st.slider(
    "Select Customer Churn Probability (%)",
    min_value=0,
    max_value=100,
    value=45,
    key="churn_slider"
) / 100

# ---------------- STRATEGY OUTPUT ----------------
st.divider()

if churn_prob < 0.30:
    st.markdown("""
    <div style="background: rgba(16, 185, 129, 0.1); padding: 25px; border-radius: 16px; border: 1px solid #10B981; margin-bottom: 20px;">
        <h3 style="color: #10B981; margin-top: 0;">🟢 Low Churn Risk Customer</h3>
        <p><b>Recommended Actions:</b></p>
        <ul style="color: #F8FAFC;">
            <li>Cross-sell premium banking products (High-yield savings, Investment plans)</li>
            <li>Offer loyalty reward points and exclusive benefits</li>
            <li>Promote long-term relationship programs</li>
            <li>Encourage digital banking and auto-pay features</li>
        </ul>
        <p style="color: #10B981;"><b>Business Goal:</b> Increase customer lifetime value (CLV)</p>
    </div>
    """, unsafe_allow_html=True)

elif churn_prob < 0.60:
    st.markdown("""
    <div style="background: rgba(251, 191, 36, 0.1); padding: 25px; border-radius: 16px; border: 1px solid #FBBF24; margin-bottom: 20px;">
        <h3 style="color: #FBBF24; margin-top: 0;">🟡 Medium Churn Risk Customer</h3>
        <p><b>Recommended Actions:</b></p>
        <ul style="color: #F8FAFC;">
            <li>Personalized offers (lower fees, cashback on utility bills)</li>
            <li>Proactive customer support "check-in" calls</li>
            <li>Targeted product nudges based on usage history</li>
            <li>Short-term retention incentives</li>
        </ul>
        <p style="color: #FBBF24;"><b>Business Goal:</b> Improve engagement and prevent risk escalation</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div style="background: rgba(239, 68, 68, 0.1); padding: 25px; border-radius: 16px; border: 1px solid #EF4444; margin-bottom: 20px;">
        <h3 style="color: #EF4444; margin-top: 0;">🔴 High Churn Risk Customer</h3>
        <p><b>Recommended Actions:</b></p>
        <ul style="color: #F8FAFC;">
            <li><b>Immediate relationship manager intervention</b></li>
            <li>Offer exclusive fee waivers or interest rate benefits</li>
            <li>Customized "Win-back" retention plans</li>
            <li>Priority grievance resolution and account audit</li>
        </ul>
        <p style="color: #EF4444;"><b>Business Goal:</b> Prevent customer exit at all costs</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- BUSINESS INSIGHTS ----------------
st.header("📈 Key Business Insights")

st.markdown("""
<div class="premium-card">
    <ul style="margin-bottom:0;">
        <li><b>Dormancy Risk:</b> Customers with low activity and high balance are prime churn candidates.</li>
        <li><b>Complexity Risk:</b> Low credit score combined with 3+ products suggests account overload.</li>
        <li><b>Retention Shield:</b> Active members are 4x more likely to stay than inactive ones.</li>
    </ul>
    <p style="margin-top:10px; font-weight:600; color: #FBBF24;">Conclusion: Retention strategies should be risk-based, personalized, and timely.</p>
</div>
""", unsafe_allow_html=True)

# No bottom navigation needed

