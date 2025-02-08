import streamlit as st
from streamlit_option_menu import option_menu

# Page Configuration
st.set_page_config(
    page_title="AppJingle Solutions",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None
)

# Custom CSS with advanced UI elements
st.markdown("""
    <style>
        /* Main container styling */
        .block-container {
            padding: 0;
            max-width: 100%;
        }
        
        /* Typography */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        
        * {
            font-family: 'Plus Jakarta Sans', sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        /* Header styles */
        .company-header {
            background: linear-gradient(135deg, #1a1c23 0%, #242938 100%);
            padding: 8rem 2rem;
            position: relative;
            overflow: hidden;
            margin-bottom: 4rem;
        }
        
        .company-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQ0MCIgaGVpZ2h0PSI1MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGRlZnM+PGxpbmVhckdyYWRpZW50IHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiIGlkPSJhIj48c3RvcCBzdG9wLWNvbG9yPSIjMkM1MzY0IiBvZmZzZXQ9IjAlIi8+PHN0b3Agc3RvcC1jb2xvcj0iIzIwMjgzRCIgb2Zmc2V0PSIxMDAlIi8+PC9saW5lYXJHcmFkaWVudD48L2RlZnM+PHBhdGggZD0iTTAgMGgxNDQwdjUwMEgweiIgZmlsbD0idXJsKCNhKSIgZmlsbC1ydWxlPSJldmVub2RkIi8+PC9zdmc+');
            opacity: 0.1;
            z-index: 0;
        }
        
        .header-content {
            position: relative;
            z-index: 1;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .company-name {
            font-size: 5.5rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, #00FF87 0%, #60EFFF 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            line-height: 1.1;
            letter-spacing: -2px;
        }
        
        .tag-line {
            color: #FFFFFF;
            font-size: 1.8rem;
            font-weight: 500;
            margin-bottom: 2rem;
            text-align: center;
            opacity: 0.9;
        }
        
        /* Service card styles */
        .services-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            padding: 0 4rem;
            margin-bottom: 4rem;
        }
        
        .service-card {
            background: rgba(255, 255, 255, 0.98);
            padding: 3rem;
            border-radius: 20px;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            border: 1px solid rgba(0, 0, 0, 0.08);
        }
        
        .service-card::before {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: 20px;
            padding: 2px;
            background: linear-gradient(135deg, #00FF87 0%, #60EFFF 100%);
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            opacity: 0;
            transition: all 0.4s ease;
        }
        
        .service-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
        }
        
        .service-card:hover::before {
            opacity: 1;
        }
        
        .service-icon {
            font-size: 4rem;
            margin-bottom: 2rem;
            display: block;
            text-align: center;
            position: relative;
        }
        
        .service-icon::after {
            content: '';
            position: absolute;
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #00FF87 0%, #60EFFF 100%);
            border-radius: 50%;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            opacity: 0.1;
            z-index: -1;
        }
        
        .service-title {
            color: #1a1c23;
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            text-align: center;
        }
        
        .service-text {
            color: #4a5568;
            font-size: 1.1rem;
            line-height: 1.7;
            text-align: center;
        }
        
        /* Section styling */
        .section-title {
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, #1a1c23 0%, #242938 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            letter-spacing: -1px;
        }
        
        .section-description {
            color: #4a5568;
            font-size: 1.4rem;
            max-width: 800px;
            margin: 0 auto 5rem auto;
            text-align: center;
            line-height: 1.8;
        }
        
        /* Footer styles */
        .modern-footer {
            background: #1a1c23;
            padding: 5rem 2rem;
            margin-top: 8rem;
            position: relative;
            overflow: hidden;
        }
        
        .footer-content {
            position: relative;
            z-index: 1;
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
        }
        
        .footer-text {
            color: rgba(255, 255, 255, 0.7);
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 1rem;
        }
        
        .developer-name {
            background: linear-gradient(135deg, #00FF87 0%, #60EFFF 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 2rem;
        }
        
        .social-links {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-top: 3rem;
        }
        
        .social-links a {
            transition: all 0.3s ease;
            opacity: 0.8;
        }
        
        .social-links a:hover {
            transform: translateY(-5px);
            opacity: 1;
        }
        
        /* Background styling */
        .stApp {
            background: #f8fafc;
        }
        
        /* Hide Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .services-grid {
                grid-template-columns: 1fr;
                padding: 0 2rem;
            }
            
            .company-name {
                font-size: 3.5rem;
            }
            
            .tag-line {
                font-size: 1.4rem;
            }
            
            .section-title {
                font-size: 2.5rem;
            }
            
            .section-description {
                font-size: 1.2rem;
                padding: 0 2rem;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
with st.container():
    st.markdown("""
        <div class="company-header">
            <div class="header-content">
                <h1 class="company-name">AppJingle Solutions</h1>
                <p class="tag-line">Transforming Ideas into Digital Excellence</p>
                <h2 style="color: rgba(255,255,255,0.9); font-size: 2.2rem; font-weight: 600; margin-top: 2rem; text-align: center;">
                    INNOVATIVE • RELIABLE • CUTTING-EDGE
                </h2>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Services Section
st.markdown("""
    <div style='padding: 0 2rem;'>
        <h2 class="section-title">Our Expertise</h2>
        <p class="section-description">
            We deliver cutting-edge solutions that help businesses thrive in the digital age. 
            Our team combines technical excellence with creative innovation to create 
            exceptional digital experiences.
        </p>
    </div>
""", unsafe_allow_html=True)

# Services Grid
services = [
    {
        "icon": "💻",
        "title": "Web Development",
        "description": "Creating powerful, responsive web applications using cutting-edge technologies. We focus on performance, security, and exceptional user experience."
    },
    {
        "icon": "📱",
        "title": "Mobile Development",
        "description": "Building native and cross-platform mobile applications that engage users and drive business growth. Expert solutions for iOS and Android."
    },
    {
        "icon": "🤖",
        "title": "AI Solutions",
        "description": "Implementing intelligent AI systems that automate processes and provide valuable insights. Custom AI solutions tailored to your business needs."
    }
]

st.markdown('<div class="services-grid">', unsafe_allow_html=True)
for service in services:
    st.markdown(f"""
        <div class="service-card">
            <div class="service-icon">{service['icon']}</div>
            <h3 class="service-title">{service['title']}</h3>
            <p class="service-text">
                {service['description']}
            </p>
        </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="modern-footer">
        <div class="footer-content">
            <p class="footer-text">
                Crafted with Precision
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
