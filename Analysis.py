import streamlit as st
import pandas as pd
import plotly.express as px
from ui_components import set_page_style, navigation_bar

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Analysis | Bank Customer Churn Prediction",
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

# Map churn labels for readability
df["Churn_Label"] = df["Churn"].map({0: "Retained", 1: "Churned"})

# Custom Colors for Dark Mode
churn_colors = {"Retained": "#64748B", "Churned": "#FBBF24"}

# ------------------ HEADER ------------------
st.header("📊 Churn Analysis & Visual Insights")
st.markdown(
    """
    <div class="premium-card">
    This section explores <b>customer churn patterns</b> using the <b>raw dataset only</b>. 
    The objective is to understand customer behavior <i>before</i> applying feature engineering 
    or machine learning models.
    </div>
    """, unsafe_allow_html=True
)

# ================== 1️⃣ OVERALL CHURN DISTRIBUTION ==================
st.header("1️⃣ Overall Churn Distribution")

churn_counts = df["Churn_Label"].value_counts().reset_index()
churn_counts.columns = ["Churn Status", "Customer Count"]

fig_churn = px.pie(
    churn_counts,
    names="Churn Status",
    values="Customer Count",
    hole=0.5,
    title="Churn vs Retained Customers",
    color="Churn Status",
    color_discrete_map=churn_colors
)

fig_churn.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=2)))
fig_churn.update_layout(
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color="white")
)

st.plotly_chart(fig_churn, use_container_width=True)

st.markdown(
    """
    <div style="background: rgba(251, 191, 36, 0.1); padding: 15px; border-radius: 10px; border-left: 5px solid #FBBF24; margin-bottom: 20px;">
    🔍 <b>Insight:</b> The dataset is imbalanced, with churned customers forming a smaller proportion of the total population.
    </div>
    """, unsafe_allow_html=True
)

# ================== 2️⃣ CHURN BY GENDER ==================
st.header("2️⃣ Churn by Gender")

fig_gender = px.histogram(
    df,
    x="Gender",
    color="Churn_Label",
    barmode="group",
    title="Churn Distribution by Gender",
    labels={"Churn_Label": "Customer Status"},
    color_discrete_map=churn_colors
)

fig_gender.update_layout(
    xaxis_title="Gender",
    yaxis_title="Customer Count",
    legend_title_text="Status",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color="white")
)

st.plotly_chart(fig_gender, use_container_width=True)

# ================== 3️⃣ CHURN BY GEOGRAPHY ==================
st.header("3️⃣ Churn by Geography")

fig_geo = px.histogram(
    df,
    x="State",
    color="Churn_Label",
    barmode="group",
    title="Churn Distribution by Geography",
    labels={"Churn_Label": "Customer Status"},
    color_discrete_map=churn_colors
)

fig_geo.update_layout(
    xaxis_title="State",
    yaxis_title="Customer Count",
    legend_title_text="Status",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color="white")
)

st.plotly_chart(fig_geo, use_container_width=True)

# ================== 4️⃣ CHURN VS ACTIVE MEMBER ==================
st.header("4️⃣ Churn vs Active Membership")

fig_active = px.histogram(
    df,
    x="Is_Active_Member",
    color="Churn_Label",
    barmode="group",
    title="Churn vs Active Membership",
    text_auto=True,
    labels={"Churn_Label": "Customer Status"},
    color_discrete_map=churn_colors
)

fig_active.update_layout(
    xaxis_title="Active Member (0 = No, 1 = Yes)",
    yaxis_title="Customer Count",
    legend_title_text="Status",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color="white")
)

st.plotly_chart(fig_active, use_container_width=True)

# ================== 5️⃣ CREDIT SCORE VS CHURN ==================
st.header("5️⃣ Credit Score vs Churn")

fig_credit = px.box(
    df,
    x="Churn_Label",
    y="Credit_Score",
    title="Credit Score Distribution by Churn Status",
    labels={"Churn_Label": "Customer Status"},
    color="Churn_Label",
    color_discrete_map=churn_colors
)

fig_credit.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color="white")
)

st.plotly_chart(fig_credit, use_container_width=True)

# No bottom navigation needed


