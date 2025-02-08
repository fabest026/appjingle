import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="AppJingle Solutions",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None
)

# Custom CSS with user-friendly colors
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
            background: linear-gradient(135deg, #2C3E50, #3498DB);
            padding: 4rem 2rem;
            border-radius: 16px;
            margin-bottom: 3rem;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        
        .company-name {
            font-size: 4.5rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            letter-spacing: -1px;
            line-height: 1.1;
            color: #FFFFFF;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        
        .tag-line {
            color: #ECF0F1;
            font-size: 1.5rem;
            font-weight: 500;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        /* Service card styles */
        .service-card {
            background: #FFFFFF;
            padding: 2.5rem;
            border-radius: 16px;
            transition: all 0.3s ease;
            height: 100%;
            border: 1px solid #E0E0E0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }
        
        .service-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            border-color: #3498DB;
        }
        
        .service-title {
            color: #2C3E50;
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
            color: #2C3E50;
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        .section-description {
            color: #34495E;
            font-size: 1.3rem;
            max-width: 900px;
            margin: 0 auto 4rem auto;
            text-align: center;
            line-height: 1.8;
        }
        
        /* Footer styles */
        .modern-footer {
            background: #FFFFFF;
            padding: 3rem;
            border-radius: 16px;
            margin-top: 5rem;
            border: 1px solid #E0E0E0;
            box-shadow: 0 -5px 15px rgba(0, 0, 0, 0.05);
        }
        
        .footer-text {
            color: #2C3E50;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 0.5rem;
            text-align: center;
        }
        
        .developer-name {
            color: #3498DB;
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
            transform: translateY(-3px);
        }
        
        /* Background styling */
        .stApp {
            background: #F8F9FA;
        }
        
        /* Hide Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Service text styling */
        .service-text {
            color: #34495E;
            font-size: 1.1rem;
            line-height: 1.6;
            text-align: left;
        }
        
        /* Current time display */
        .time-display {
            background: #FFFFFF;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            color: #2C3E50;
            font-size: 0.9rem;
            margin-bottom: 1rem;
            display: inline-block;
            border: 1px solid #E0E0E0;
        }
        
        /* User info display */
        .user-info {
            color: #2C3E50;
            font-size: 0.9rem;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Display current time and user info
st.markdown(f"""
    <div style="text-align: right;">
        <div class="time-display">
            UTC: 2025-02-08 06:36:30
        </div>
        <div class="user-info">
            Welcome, fabest026
        </div>
    </div>
""", unsafe_allow_html=True)

# Header Section
with st.container():
    st.markdown("""
        <div class="company-header">
            <h1 class="company-name">AppJingle Solutions</h1>
            <p class="tag-line">Smart Solutions for Your Digital Success</p>
            <h2 style="color: #ECF0F1; font-size: 2rem; font-weight: 600; margin-top: 2rem; text-align: center;">
                YOUR TRUSTED TECHNOLOGY PARTNER
            </h2>
            <p style="color: #ECF0F1; font-size: 1.2rem; font-weight: 400; margin-top: 1rem; text-align: center;">
                We deliver innovative solutions that help your business grow and succeed in the digital world.
            </p>
        </div>
    """, unsafe_allow_html=True)

# What We Do Section
st.markdown("""
    <div style='margin: 5rem 0;'>
        <h2 class="section-title">Our Services</h2>
        <p class="section-description">
            We specialize in creating powerful digital solutions that help businesses thrive. 
            Our expert team combines technical expertise with creative innovation to deliver 
            outstanding results for our clients.
        </p>
    </div>
""", unsafe_allow_html=True)

# Services Section
col1, col2, col3 = st.columns(3)

services = [
    {
        "icon": "💻",
        "title": "Web Development",
        "description": "Professional websites built with modern technologies. We focus on creating responsive, fast-loading sites that provide excellent user experience and drive conversions."
    },
    {
        "icon": "📱",
        "title": "Mobile Development",
        "description": "Custom mobile applications for iOS and Android. We create user-friendly apps that engage your audience and help achieve your business objectives."
    },
    {
        "icon": "🤖",
        "title": "AI Solutions",
        "description": "Smart AI-powered applications that streamline your business processes. We implement practical AI solutions that deliver real value to your organization."
    }
]

for col, service in zip([col1, col2, col3], services):
    with col:
        st.markdown(f"""
            <div class="service-card">
                <div class="service-icon">{service['icon']}</div>
                <h3 class="service-title">{service['title']}</h3>
                <p class="service-text">
                    {service['description']}
                </p>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="modern-footer">
        <div style="text-align: center;">
            <p class="footer-text">
                Created by
            </p>
            <h3 class="developer-name">Farhan Akbar</h3>
            <div class="social-links">
                <a href="https://www.linkedin.com/in/farhan-akbar-ai/" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
                </a>
                <a href="https://api.whatsapp.com/send?phone=923034532403" target="_blank">
                    <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/>
                </a>
                <a href="https://www.facebook.com/appjingle" target="_blank">
                    <img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook"/>
                </a>
                <a href="mailto:rasolehri@gmail.com">
                    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
                </a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
