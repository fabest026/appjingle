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

# Enhanced Custom CSS with Modern Design Principles
st.markdown("""
    <style>
        /* Import multiple modern fonts for better typography */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Manrope:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');
        
        /* CSS Variables for consistent theming */
        :root {
            --primary-color: #6366F1;
            --secondary-color: #4F46E5;
            --accent-color: #EC4899;
            --background-color: #F8FAFC;
            --card-background: #FFFFFF;
            --text-primary: #1E293B;
            --text-secondary: #475569;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.12);
            --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1);
            --shadow-lg: 0 20px 25px -5px rgba(0,0,0,0.1);
            --gradient-primary: linear-gradient(135deg, #6366F1, #4F46E5);
            --gradient-accent: linear-gradient(135deg, #EC4899, #D946EF);
        }

        /* Base styles */
        * {
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        .stApp {
            background: var(--background-color);
        }

        /* Enhanced container styling */
        .block-container {
            padding: 2rem 4rem;
            max-width: 1600px;
        }

        /* Modern header with glass morphism effect */
        .company-header {
            background: var(--gradient-primary);
            backdrop-filter: blur(10px);
            padding: 5rem 2rem;
            border-radius: 32px;
            margin-bottom: 4rem;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: var(--shadow-lg);
        }

        /* Enhanced typography */
        .company-name {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 6rem;
            font-weight: 800;
            background: var(--gradient-accent);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 2rem;
            letter-spacing: -2px;
            line-height: 1;
        }

        .tag-line {
            font-family: 'Manrope', sans-serif;
            color: #FFFFFF;
            font-size: 1.8rem;
            font-weight: 500;
            margin-bottom: 2.5rem;
            text-align: center;
            opacity: 0.9;
        }

        /* Modern card design with hover effects */
        .service-card {
            background: var(--card-background);
            padding: 3rem;
            border-radius: 24px;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            height: 100%;
            border: 1px solid rgba(99, 102, 241, 0.1);
            box-shadow: var(--shadow-sm);
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
            background: var(--gradient-primary);
            transform: scaleX(0);
            transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .service-card:hover {
            transform: translateY(-8px);
            box-shadow: var(--shadow-lg);
        }

        .service-card:hover::before {
            transform: scaleX(1);
        }

        /* Enhanced service components */
        .service-icon {
            font-size: 4rem;
            margin-bottom: 2rem;
            display: block;
            text-align: center;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .service-title {
            font-family: 'Space Grotesk', sans-serif;
            color: var(--primary-color);
            font-weight: 700;
            margin-bottom: 1.5rem;
            font-size: 2rem;
            text-align: center;
        }

        .service-text {
            color: var(--text-secondary);
            font-size: 1.1rem;
            line-height: 1.8;
            text-align: center;
        }

        /* Modern section styling */
        .section-title {
            font-family: 'Space Grotesk', sans-serif;
            color: var(--primary-color);
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 2.5rem;
            text-align: center;
            letter-spacing: -1px;
        }

        .section-description {
            color: var(--text-secondary);
            font-size: 1.4rem;
            max-width: 1000px;
            margin: 0 auto 5rem auto;
            text-align: center;
            line-height: 1.8;
            font-family: 'Manrope', sans-serif;
        }

        /* Enhanced footer design */
        .modern-footer {
            background: var(--card-background);
            padding: 4rem;
            border-radius: 32px;
            margin-top: 6rem;
            border: 1px solid rgba(99, 102, 241, 0.1);
            box-shadow: var(--shadow-lg);
        }

        .footer-text {
            color: var(--primary-color);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 3px;
            margin-bottom: 1rem;
            text-align: center;
            font-size: 0.9rem;
        }

        .developer-name {
            font-family: 'Space Grotesk', sans-serif;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 2rem;
            text-align: center;
        }

        /* Enhanced social links */
        .social-links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 3rem;
        }

        .social-links a {
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            opacity: 0.9;
        }

        .social-links a:hover {
            transform: translateY(-6px) scale(1.05);
            opacity: 1;
        }

        /* Hide Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Responsive Design */
        @media (max-width: 768px) {
            .block-container {
                padding: 1rem;
            }
            
            .company-name {
                font-size: 4rem;
            }
            
            .tag-line {
                font-size: 1.4rem;
            }
            
            .service-card {
                padding: 2rem;
            }
            
            .section-title {
                font-size: 2.5rem;
            }
            
            .section-description {
                font-size: 1.2rem;
            }
        }

        /* Animation Classes */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .animate-fade-in {
            animation: fadeIn 0.6s ease-out forwards;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section with enhanced animation
with st.container():
    st.markdown("""
        <div class="company-header animate-fade-in">
            <h1 class="company-name">AppJingle Solutions</h1>
            <p class="tag-line">Elevate Your Business with Innovative IT Solutions</p>
            <h2 style="color: white; font-size: 2.2rem; font-weight: 600; margin-top: 2.5rem; text-align: center; opacity: 0.9;">
                TRANSFORMING IDEAS INTO DIGITAL REALITY
            </h2>
            <p style="color: white; font-size: 1.3rem; font-weight: 400; margin-top: 1.5rem; text-align: center; opacity: 0.8;">
                We combine creativity, technology, and strategy to deliver exceptional digital solutions 
                that drive your business forward.
            </p>
        </div>
    """, unsafe_allow_html=True)

# What We Do Section
st.markdown("""
    <div style='margin: 6rem 0;' class="animate-fade-in">
        <h2 class="section-title">What We Do</h2>
        <p class="section-description">
            We specialize in creating intelligent, AI-powered applications that transform your digital presence. 
            Our solutions are tailored to your unique business needs, combining cutting-edge technology 
            with user-centric design to deliver exceptional results.
        </p>
    </div>
""", unsafe_allow_html=True)

# Enhanced Services Section
col1, col2, col3 = st.columns(3)

services = [
    {
        "icon": "💻",
        "title": "Web Development",
        "description": "Create stunning, responsive websites that captivate your audience. Our expert team delivers seamless user experiences with cutting-edge technologies and robust backend systems."
    },
    {
        "icon": "📱",
        "title": "Mobile Development",
        "description": "Build powerful mobile applications that engage users and drive results. We specialize in creating intuitive, feature-rich apps for both iOS and Android platforms."
    },
    {
        "icon": "🤖",
        "title": "AI Development",
        "description": "Harness the power of artificial intelligence to automate processes and gain valuable insights. We develop smart solutions that help your business stay ahead of the competition."
    }
]

for col, service in zip([col1, col2, col3], services):
    with col:
        st.markdown(f"""
            <div class="service-card animate-fade-in">
                <div class="service-icon">{service['icon']}</div>
                <h3 class="service-title">{service['title']}</h3>
                <p class="service-text">
                    {service['description']}
                </p>
            </div>
        """, unsafe_allow_html=True)

# Enhanced Footer
st.markdown("""
    <div class="modern-footer animate-fade-in">
        <div style="text-align: center;">
            <p class="footer-text">
                Crafted with ❤️ by
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
