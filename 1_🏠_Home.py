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

# Get current UTC time
current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

# Custom CSS with 2025 design trends
st.markdown("""
    <style>
        /* Modern Container Styling */
        .block-container {
            padding: 1rem 3rem;
            max-width: 1400px;
        }
        
        /* Typography */
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
        
        * {
            font-family: 'Space Grotesk', sans-serif;
        }
        
        /* User Info Bar */
        .user-info-bar {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 12px;
            padding: 0.8rem 1.5rem;
            margin-bottom: 2rem;
            display: flex;
            justify-content: flex-end;
            align-items: center;
            font-size: 0.9rem;
            color: #94A3B8;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        
        /* Header styles */
        .company-header {
            background: linear-gradient(135deg, #7928CA, #FF0080);
            padding: 4rem 2rem;
            border-radius: 24px;
            margin-bottom: 3rem;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 20px 40px rgba(121, 40, 202, 0.2);
        }
        
        .company-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at top right, rgba(255, 255, 255, 0.2), transparent);
            pointer-events: none;
        }
        
        .company-name {
            color: white;
            font-size: 5rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            letter-spacing: -1px;
            line-height: 1.1;
            background: linear-gradient(to right, #fff, #E2E8F0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .tag-line {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.5rem;
            font-weight: 400;
            margin-bottom: 2rem;
        }
        
        /* Service card styles */
        .service-card {
            background: rgba(255, 255, 255, 0.95);
            padding: 2.5rem;
            border-radius: 24px;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            height: 100%;
            border: 1px solid rgba(255, 255, 255, 0.2);
            position: relative;
            overflow: hidden;
        }
        
        .service-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #7928CA, #FF0080);
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .service-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        }
        
        .service-card:hover::before {
            opacity: 1;
        }
        
        .service-title {
            color: #1E293B;
            font-weight: 600;
            margin-bottom: 1.5rem;
            font-size: 1.8rem;
        }
        
        /* Section styling */
        .section-title {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 2rem;
            text-align: center;
            background: linear-gradient(135deg, #7928CA, #FF0080);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -1px;
        }
        
        .section-description {
            color: #64748B;
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
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.05);
        }
        
        .social-links {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-top: 2rem;
        }
        
        .social-links a {
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .social-links a:hover {
            transform: translateY(-4px) scale(1.05);
        }
        
        /* Background styling */
        .stApp {
            background: linear-gradient(to bottom, #F8FAFC, #EFF6FF);
        }
        
        /* Hide Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Service icon styling */
        .service-icon {
            font-size: 3rem;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, #7928CA, #FF0080);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    </style>
""", unsafe_allow_html=True)

# User Info Bar
st.markdown(f"""
    <div class="user-info-bar">
        🕒 {current_time} UTC &nbsp;&nbsp;|&nbsp;&nbsp; 👤 {st.session_state.get('user', 'fabest026')}
    </div>
""", unsafe_allow_html=True)

# Header Section
with st.container():
    st.markdown("""
        <div class="company-header">
            <h1 class="company-name">AppJingle Solutions</h1>
            <p class="tag-line">Boost your business with our IT solutions</p>
            <h2 style="color: white; font-size: 2rem; font-weight: 600; margin-top: 2rem;">
                YOUR SUCCESS IS OUR TOP CONCERN
            </h2>
            <p style="color: rgba(255, 255, 255, 0.9); font-size: 1.2rem; font-weight: 300; margin-top: 1rem;">
                At AppJingle, we use our experience and commitment to provide great service 
                and real value to our clients.
            </p>
        </div>
    """, unsafe_allow_html=True)

# What We Do Section
st.markdown("""
    <div style='margin: 5rem 0;'>
        <h2 class="section-title">What We Do</h2>
        <p class="section-description">
            We build AI-powered apps for your website and phone that help you make more money. 
            We understand your business and choose the best technology to help you grow. 
            Let's work together to make your business even better!
        </p>
    </div>
""", unsafe_allow_html=True)

# Services Section
col1, col2, col3 = st.columns(3)

services = [
    {
        "icon": "🌐",
        "title": "Web Development",
        "description": "We help you build stunning and functional websites that perfectly align with your business goals. With our expertise, we create intuitive interfaces and robust backend systems, ensuring a seamless user experience."
    },
    {
        "icon": "📱",
        "title": "Mobile Development",
        "description": "We assist you in creating mobile applications that are simple to use and offer a smooth user experience. Our team of skilled developers will work closely with you to understand your needs and deliver exceptional results."
    },
    {
        "icon": "🤖",
        "title": "AI Development",
        "description": "Tap into the power of artificial intelligence with our AI app development services. We create innovative applications that leverage machine learning to automate processes and enhance decision-making."
    }
]

for col, service in zip([col1, col2, col3], services):
    with col:
        st.markdown(f"""
            <div class="service-card">
                <div class="service-icon">{service['icon']}</div>
                <h3 class="service-title">{service['title']}</h3>
                <p style="font-size: 1.1rem; line-height: 1.6; color: #64748B;">
                    {service['description']}
                </p>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="modern-footer">
        <div style="text-align: center;">
            <p style="font-weight: 600; text-transform: uppercase; letter-spacing: 2px; color: #7928CA; margin-bottom: 0.5rem;">
                Developed by
            </p>
            <h3 style="background: linear-gradient(135deg, #7928CA, #FF0080); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2rem; margin-bottom: 1.5rem;">
                Farhan Akbar
            </h3>
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
