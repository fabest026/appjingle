import                    
   streamlit as st
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

# Custom CSS with improved visibility
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
            background: linear-gradient(135deg, #2D3436, #000000);
            padding: 4rem 2rem;
            border-radius: 24px;
            margin-bottom: 3rem;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
        }
        
        .company-name {
            font-size: 5rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            letter-spacing: -1px;
            line-height: 1.1;
            color: #FF1493;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        
        .tag-line {
            color: #FFFFFF;
            font-size: 1.5rem;
            font-weight: 500;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        /* Service card styles */
        .service-card {
            background: #FFFFFF;
            padding: 2.5rem;
            border-radius: 24px;
            transition: all 0.4s ease;
            height: 100%;
            border: 1px solid #E2E8F0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }
        
        .service-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            border-color: #FF1493;
        }
        
        .service-title {
            color: #FF1493;
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
            color: #FF1493;
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
            background: #FFFFFF;
            padding: 3rem;
            border-radius: 24px;
            margin-top: 5rem;
            border: 1px solid #E2E8F0;
            box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.05);
        }
        
        .footer-text {
            color: #FF1493;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 0.5rem;
            text-align: center;
        }
        
        .developer-name {
            color: #FF1493;
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
            background: linear-gradient(to bottom right, #F7FAFC, #EDF2F7);
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
    </style>
""", unsafe_allow_html=True)

# Header Section
with st.container():
    st.markdown("""
        <div class="company-header">
            <h1 class="company-name">AppJingle Solutions</h1>
            <p class="tag-line">Boost your business with our IT solutions</p>
            <h2 style="color: white; font-size: 2rem; font-weight: 600; margin-top: 2rem; text-align: center;">
                YOUR SUCCESS IS OUR TOP CONCERN
            </h2>
            <p style="color: white; font-size: 1.2rem; font-weight: 400; margin-top: 1rem; text-align: center;">
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
        "icon": "💻",
        "title": "Web Development",
        "description": "We help you build stunning and functional websites that perfectly align with your business goals. With our expertise, we create intuitive interfaces and robust backend systems."
    },
    {
        "icon": "📱",
        "title": "Mobile Development",
        "description": "We assist you in creating mobile applications that are simple to use and offer a smooth user experience. Our team of skilled developers will work closely with you."
    },
    {
        "icon": "🤖",
        "title": "AI Development",
        "description": "Tap into the power of artificial intelligence with our AI app development services. We create innovative applications that leverage machine learning to automate processes."
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
                Developed by
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
