import streamlit as st

def set_page_style():
    """Sets a premium dark/black theme for the application."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Outfit:wght@400;600;700&display=swap');

        :root {
            --primary: #FBBF24; /* Gold */
            --bg-dark: #000000;
            --card-dark: #111111;
            --text-light: #F8FAFC;
            --glass: rgba(255, 255, 255, 0.05);
            --glass-border: rgba(255, 255, 255, 0.1);
        }

        /* Global Font & Background */
        html, body, [class*="st-"] {
            font-family: 'Outfit', sans-serif;
            color: var(--text-light) !important;
        }

        .stApp {
            background-color: var(--bg-dark);
        }

        /* Hide Sidebar */
        [data-testid="stSidebar"] {
            display: none;
        }
        
        [data-testid="stSidebarNav"] {
            display: none;
        }

        /* Adjust Main Content width when sidebar is hidden */
        .main .block-container {
            padding-top: 2rem;
            max-width: 1000px;
        }

        /* Cards & Containers */
        .premium-card {
            background: var(--card-dark);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 20px;
        }

        /* Metrics Styling */
        [data-testid="stMetric"] {
            background: var(--card-dark);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            padding: 15px !important;
        }
        
        [data-testid="stMetricValue"] {
            color: var(--primary) !important;
            font-size: 1.8rem !important;
            font-weight: 700 !important;
        }
        
        [data-testid="stMetricLabel"] {
            color: #94A3B8 !important;
        }

        /* Buttons */
        .stButton>button {
            background-color: transparent;
            color: var(--primary);
            border: 1px solid var(--primary);
            border-radius: 8px;
            padding: 8px 16px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--primary);
            color: black;
            box-shadow: 0 0 15px rgba(251, 191, 36, 0.4);
        }

        /* Headers */
        h1, h2, h3 {
            color: var(--text-light) !important;
            font-weight: 700 !important;
        }
        
        /* Links in markdown */
        a {
            color: var(--primary) !important;
        }
        /* Inputs (Text, Number, Selectbox) */
        div[data-baseweb="input"], div[data-baseweb="select"], .stSelectbox > div {
            background-color: #1A1A1A !important;
            border: 1px solid var(--glass-border) !important;
            border-radius: 8px !important;
        }
        
        input, select, textarea, div[data-baseweb="select"] span {
            color: var(--text-light) !important;
            background-color: transparent !important;
        }

        /* Specific fix for selectbox text */
        .stSelectbox div[data-baseweb="select"] > div {
            color: var(--text-light) !important;
        }

        div[role="listbox"] {
            background-color: #1A1A1A !important;
            color: var(--text-light) !important;
        }
        
        div[role="option"] {
            background-color: #1A1A1A !important;
            color: var(--text-light) !important;
        }
        
        div[role="option"]:hover {
            background-color: var(--primary) !important;
            color: black !important;
        }

        /* Labels for inputs */
        .st-at, .st-ae, .st-af, .st-ag, label {
            color: #94A3B8 !important;
            font-weight: 500 !important;
        }

        </style>
    """, unsafe_allow_html=True)

def navigation_bar():
    """Renders a navigation bar at the top or bottom of the page."""
    
    pages = {
        "Home": "app.py",
        "Overview": "pages/Overview.py",
        "Analysis": "pages/Analysis.py",
        "Engineering": "pages/Engineering.py",
        "Evaluation": "pages/Evaluation.py",
        "Prediction": "pages/Prediction.py",
        "Strategy": "pages/Strategy.py"
    }
    
def navigation_bar():
    """Renders a premium centered navigation bar with the project title at the top."""
    
    # Global Project Title
    st.markdown("""
        <div style="text-align: center; margin-bottom: 1.5rem;">
            <h1 style="color: #FBBF24; font-size: 2.5rem; margin-bottom: 0.2rem;">🛡️ Indian Bank Customer Churn Predictor</h1>
            <p style="color: #64748B; font-size: 1rem; font-weight: 500;">End-to-End Machine Learning Retention System</p>
        </div>
    """, unsafe_allow_html=True)
    
    pages = {
        "Home": "app.py",
        "Overview": "pages/Overview.py",
        "Analysis": "pages/Analysis.py",
        "Engineering": "pages/Engineering.py",
        "Evaluation": "pages/Evaluation.py",
        "Prediction": "pages/Prediction.py",
        "Strategy": "pages/Strategy.py"
    }
    
    # Custom CSS for the top navigation buttons
    st.markdown("""
        <style>
        .stButton>button[key^="nav_"] {
            font-size: 0.85rem !important;
            padding: 2px 8px !important;
            border-radius: 20px !important;
            height: auto !important;
            min-height: 0 !important;
            border: 1px solid rgba(251, 191, 36, 0.2) !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    cols = st.columns([1] + [1.8]*len(pages) + [1])
    for i, (name, path) in enumerate(pages.items()):
        with cols[i+1]:
            if st.button(name, key=f"nav_{name}", use_container_width=True):
                st.switch_page(path)
    
    st.markdown("<hr style='margin: 0.5rem 0 2rem 0; opacity: 0.1;'>", unsafe_allow_html=True)

def kpi_card(title, value, delta=None, icon="📊"):
    """Displays a custom KPI card (Dark mode)."""
    st.markdown(f"""
        <div class="premium-card">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                <span style="font-size: 1.5rem;">{icon}</span>
                <span style="font-size: 1rem; font-weight: 600; color: #94A3B8;">{title}</span>
            </div>
            <div style="font-size: 2rem; font-weight: 700; color: #FBBF24;">{value}</div>
            {f'<div style="font-size: 0.9rem; color: #10B981; margin-top: 5px;">{delta}</div>' if delta else ''}
        </div>
    """, unsafe_allow_html=True)

