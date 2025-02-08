
import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="AppJingle Solutions",
    page_icon="💫",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None
)
                                        

# Updated CSS with purple color scheme
st.markdown("""
    <style>
        /* Main container styling */
        .block-container {
            padding: 1rem 3rem;
            max-width: 1400px;
        }
        
        /* Typography */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        
        * {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        
        /* Header styles */
        .company-header {
            background: linear-gradient(135deg, #4B0082, #663399);  /* Indigo to Rebecca Purple */
            padding: 4rem 2rem;
            border-radius: 24px;
            margin-bottom: 3rem;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 20px 40px rgba(75, 0, 130, 0.3);
        }
        
        .company-name {
            font-size: 5rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            letter-spacing: -1px;
            line-height: 1.1;
            color: #E6E6FA;  /* Lavender */
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        
        .tag-line {
            color: #E6E6FA;
            font-size: 1.5rem;
            font-weight: 500;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        /* Service card styles */
        .service-card {
            background: #F8F7FF;  /* Light purple tint */
            padding: 2.5rem;
            border-radius: 24px;
            transition: all 0.4s ease;
            height: 100%;
            border: 1px solid #E6E6FA;
            box-shadow: 0 4px 6px rgba(75, 0, 130, 0.1);
        }
        
        .service-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(75, 0, 130, 0.2);
            border-color: #9370DB;  /* Medium Purple */
        }
        
        .service-title {
            color: #4B0082;  /* Indigo */
            font-weight: 700;
            margin-bottom: 1.5rem;
            font-size: 1.8rem;
        }
        
        /* Service icon styles */
        .service-icon {
            font-size: 3.5rem;
            margin-bottom: 1.5rem;
            display: block;
            text-align: center;
        }
        
        /* Section styling */
        .section-title {
            color: #4B0082;  /* Indigo */
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 2rem;
            text-align: center;
            text-shadow: 1px 1px 2px rgba(75, 0, 130, 0.1);
        }
        
        .section-description {
            color: #483D8B;  /* Dark Slate Blue */
            font-size: 1.3rem;
            max-width: 900px;
            margin: 0 auto 4rem auto;
            text-align: center;
            line-height: 1.8;
        }
        
        /* Footer styles */
        .modern-footer {
            background: #F8F7FF;
            padding: 3rem;
            border-radius: 24px;
            margin-top: 5rem;
            border: 1px solid #E6E6FA;
            box-shadow: 0 -10px 40px rgba(75, 0, 130, 0.05);
        }
        
        .footer-text {
            color: #4B0082;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 0.5rem;
            text-align: center;
        }
        
        .developer-name {
            color: #663399;  /* Rebecca Purple */
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            text-align: center;
        }
        
        .social-links {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-top: 2rem;
        }
        
        .social-links a {
            transition: transform 0.3s ease;
        }
        
        .social-links a:hover {
            transform: translateY(-4px);
        }
        
        /* Background styling */
        .stApp {
            background: linear-gradient(to bottom right, #F8F7FF, #E6E6FA);
        }
        
        /* Service text styling */
        .service-text {
            color: #483D8B;  /* Dark Slate Blue */
            font-size: 1.1rem;
            line-height: 1.6;
            text-align: center;
        }
        
        /* User info bar */
        .user-info-bar {
            background: rgba(75, 0, 130, 0.1);
            padding: 0.8rem 1.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            color: #4B0082;
            font-size: 0.9rem;
            text-align: right;
            backdrop-filter: blur(10px);
        }
    </style>
""", unsafe_allow_html=True)

# Add User Info Bar
st.markdown("""
    <div class="user-info-bar">
        🕒 2025-02-08 06:28:17 UTC | 👤 fabest026
    </div>
""", unsafe_allow_html=True)

# (Rest of the code remains the same, the styling changes will be applied automatically)
