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

# Custom CSS with purple color scheme
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
            background: linear-gradient(135deg, #2D1B69, #6B46C1);
            padding: 4rem 2rem;
            border-radius: 24px;
            margin-bottom: 3rem;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 20px 40px rgba(107, 70, 193, 0.2);
        }
        
        .company-name {
            font-size: 5rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            letter-spacing: -1px;
            line-height: 1.1;
            background: linear-gradient(45deg, #FF1493, #9F7AEA);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        .tag-line {
            color: #E9D8FD;
            font-size: 1.5rem;
            font-weight: 500;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        /* Service card styles */
        .service-card {
            background: rgba(255, 255, 255, 0.95);
            padding: 2.5rem;
            border-radius: 24px;
            transition: all 0.4s ease;
            height: 100%;
            border: 1px solid #E9D8FD;
            box-shadow: 0 4px 6px rgba(107, 70, 193, 0.1);
            backdrop-filter: blur(10px);
        }
        
        .service-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(107, 70, 193, 0.2);
            border-color: #9F7AEA;
            background: linear-gradient(135deg, #ffffff, #F7FAFC);
        }
        
        .service-title {
            background: linear-gradient(45deg, #6B46C1, #9F7AEA);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
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
            filter: drop-shadow(0 4px 6px rgba(107, 70, 193, 0.2));
        }
        
        /* Section styling */
        .section-title {
            background: linear-gradient(45deg, #6B46C1, #9F7AEA);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 2rem;
            text-align: center;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
        }
        
        .section-description {
            color: #4A5568;
            font-size: 1.3rem;
            max-width: 900px;
            margin: 0 auto 4rem auto;
            text-align: center;
            line-height: 1.8;
        }
        
        /* Footer styles */
        .modern-footer {
            background: rgba(255, 255, 255, 0.95);
            padding: 3rem;
            border-radius: 24px;
            margin-top: 5rem;
            border: 1px solid #E9D8FD;
            box-shadow: 0 -10px 40px rgba(107, 70, 193, 0.1);
            backdrop-filter: blur(10px);
        }
        
        .footer-text {
            background: linear-gradient(45deg, #6B46C1, #9F7AEA);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 0.5rem;
            text-align: center;
        }
        
        .developer-name {
            background: linear-gradient(45deg, #6B46C1, #9F7AEA);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
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
            background: linear-gradient(135deg, #F7FAFC, #E9D8FD);
        }
        
        /* Hide Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Service text styling */
        .service-text {
            color: #4A5568;
            font-size: 1.1rem;
            line-height: 1.6;
            text-align: center;
        }
        
        /* Animation for cards */
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }
        
        .service-card {
            animation: float 6s ease-in-out infinite;
        }
        
        /* Gradient border effect */
        .service-card::before {
            content: '';
            position: absolute;
            top: -1px;
            left: -1px;
            right: -1px;
            bottom: -1px;
            border-radius: 24px;
            background: linear-gradient(45deg, #6B46C1, #9F7AEA);
            z-index: -1;
            opacity: 0;
            transition: opacity 0.4s ease;
        }
        
        .service-card:hover::before {
            opacity: 1;
        }
        
        /* Glowing effect for icons */
        .service-icon {
            position: relative;
        }
        
        .service-icon::after {
            content: '';
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            background: radial-gradient(circle, rgba(107, 70, 193, 0.2) 0%, transparent 70%);
            filter: blur(10px);
            z-index: -1;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
with st.container():
    st.markdown("""
        <div class="company-header">
            <h1 class="company-name">AppJingle Solutions</h1>
            <p class="tag-line">Elevate Your Business with Our IT Solutions</p>
            <h2 style="color: #E9D8FD; font-size: 2rem; font-weight: 600; margin-top: 2rem; text-align: center;">
                TRANSFORMING IDEAS INTO DIGITAL REALITY
            </h2>
            <p style="color: #E9D8FD; font-size: 1.2rem; font-weight: 400; margin-top: 1rem; text-align: center;">
                At AppJingle, we combine innovation with expertise to deliver exceptional digital solutions 
                that drive your business forward.
            </p>
        </div>
    """, unsafe_allow_html=True)

# What We Do Section
st.markdown("""
    <div style='margin: 5rem 0;'>
        <h2 class="section-title">What We Do</h2>
        <p class="section-description">
            We create cutting-edge AI-powered applications that revolutionize your digital presence. 
            Our team of experts crafts tailored solutions using state-of-the-art technology to help your business thrive 
            in the digital age. Let's collaborate to transform your vision into reality!
        </p>
    </div>
""", unsafe_allow_html=True)

# Services Section
col1, col2, col3 = st.columns(3)

services = [
    {
        "icon": "💻",
        "title": "Web Development",
        "description": "Create stunning, responsive websites with modern frameworks and cutting-edge technologies. We deliver seamless user experiences that convert visitors into customers."
    },
    {
        "icon": "📱",
        "title": "Mobile Development",
        "description": "Build powerful mobile applications that engage users and drive business growth. Our expert team develops native and cross-platform solutions tailored to your needs."
    },
    {
        "icon": "🤖",
        "title": "AI Solutions",
        "description": "Harness the power of artificial intelligence to automate processes and gain valuable insights. We develop smart applications that learn and adapt to your business needs."
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
                Crafted with ❤️ by
            </p>
            <h3 class="developer-name">Farhan Akbar</h3>
            <div class="social-links">
                <a href="https://www.linkedin.com/in/farhan-akbar-ai/" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-6B46C1?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
                </a>
                <a href="https://api.whatsapp.com/send?phone=923034532403" target="_blank">
                    <img src="https://img.shields.io/badge/WhatsApp-9F7AEA?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/>
                </a>
                <a href="https://www.facebook.com/appjingle" target="_blank">
                    <img src="https://img.shields.io/badge/Facebook-6B46C1?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook"/>
                </a>
                <a href="mailto:rasolehri@gmail.com">
                    <img src="https://img.shields.io/badge/Email-9F7AEA?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
                </a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
