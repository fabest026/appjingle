import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(
    page_title="AppJingle Solutions 2025",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="auto",
)

# Custom CSS with modern 2025 design trends
st.markdown("""
    <style>
        /* Modern CSS Reset and Imports */
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
        
        * {
            font-family: 'Space Grotesk', sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        /* Main Container */
        .block-container {
            padding: 0;
            max-width: 100%;
        }
        
        /* Glass Morphism Effects */
        .glass-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 32px;
        }
        
        /* Header Styles */
        .hero-section {
            background: linear-gradient(135deg, #FF1493, #7928CA);
            min-height: 100vh;
            padding: 4rem 2rem;
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        }
        
        .hero-content {
            position: relative;
            z-index: 2;
            text-align: center;
        }
        
        .company-name {
            font-size: 8rem;
            font-weight: 800;
            background: linear-gradient(to right, #FFFFFF, #E0E0E0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 2rem;
            animation: glow 2s ease-in-out infinite alternate;
        }
        
        @keyframes glow {
            from {
                text-shadow: 0 0 20px #FF1493;
            }
            to {
                text-shadow: 0 0 30px #7928CA;
            }
        }
        
        .tag-line {
            font-size: 2rem;
            color: rgba(255, 255, 255, 0.9);
            margin-bottom: 3rem;
            font-weight: 500;
        }
        
        /* Service Cards */
        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            padding: 4rem 2rem;
        }
        
        .service-card {
            background: rgba(255, 255, 255, 0.05);
            padding: 3rem;
            border-radius: 32px;
            transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            position: relative;
            overflow: hidden;
        }
        
        .service-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(255, 20, 147, 0.1), rgba(121, 40, 202, 0.1));
            z-index: -1;
            transition: opacity 0.5s ease;
            opacity: 0;
        }
        
        .service-card:hover {
            transform: translateY(-10px) scale(1.02);
        }
        
        .service-card:hover::before {
            opacity: 1;
        }
        
        .service-icon {
            font-size: 4rem;
            margin-bottom: 2rem;
            display: block;
            text-align: center;
            filter: drop-shadow(0 0 10px rgba(255, 20, 147, 0.5));
        }
        
        .service-title {
            color: #FFFFFF;
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            text-align: center;
        }
        
        .service-text {
            color: rgba(255, 255, 255, 0.8);
            font-size: 1.1rem;
            line-height: 1.8;
            text-align: center;
        }
        
        /* Footer */
        .modern-footer {
            background: rgba(0, 0, 0, 0.3);
            padding: 4rem 2rem;
            backdrop-filter: blur(10px);
            margin-top: 5rem;
        }
        
        .social-links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 3rem;
        }
        
        .social-links a {
            transition: all 0.3s ease;
            opacity: 0.8;
        }
        
        .social-links a:hover {
            transform: translateY(-5px) scale(1.1);
            opacity: 1;
        }
        
        /* Floating Elements */
        .floating-element {
            position: absolute;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            pointer-events: none;
            animation: float 20s infinite linear;
        }
        
        @keyframes float {
            0% { transform: translate(0, 0) rotate(0deg); }
            100% { transform: translate(400px, -400px) rotate(360deg); }
        }
        
        /* Hide Streamlit Elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .company-name {
                font-size: 4rem;
            }
            
            .tag-line {
                font-size: 1.5rem;
            }
            
            .services-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Dynamic Background Elements
st.markdown("""
    <div style='position: fixed; top: 0; left: 0; right: 0; bottom: 0; z-index: -1;
         background: linear-gradient(135deg, #000000, #1A1A1A);'></div>
    <div class='floating-element' style='width: 300px; height: 300px; top: 10%; left: 10%;'></div>
    <div class='floating-element' style='width: 200px; height: 200px; top: 50%; right: 10%;'></div>
    <div class='floating-element' style='width: 150px; height: 150px; bottom: 20%; left: 30%;'></div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <h1 class="company-name">AppJingle Solutions</h1>
            <p class="tag-line">Shaping Tomorrow's Digital Landscape</p>
            <div style="margin-top: 2rem;">
                <a href="#services" style="
                    background: linear-gradient(135deg, #FF1493, #7928CA);
                    color: white;
                    padding: 1rem 2rem;
                    border-radius: 50px;
                    text-decoration: none;
                    font-weight: 600;
                    font-size: 1.2rem;
                    transition: all 0.3s ease;
                    display: inline-block;
                    box-shadow: 0 10px 20px rgba(255, 20, 147, 0.3);">
                    Explore Our Services
                </a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Services Section
st.markdown('<div id="services"></div>', unsafe_allow_html=True)
services = [
    {
        "icon": "🌟",
        "title": "AI-Powered Solutions",
        "description": "Harness the power of advanced artificial intelligence and machine learning to transform your business operations and drive innovation."
    },
    {
        "icon": "🚀",
        "title": "Web3 Development",
        "description": "Build decentralized applications and smart contracts using cutting-edge blockchain technology and web3 infrastructure."
    },
    {
        "icon": "🎯",
        "title": "XR Experiences",
        "description": "Create immersive augmented and virtual reality experiences that revolutionize how users interact with your brand."
    }
]

st.markdown('<div class="services-grid">', unsafe_allow_html=True)
for service in services:
    st.markdown(f"""
        <div class="service-card">
            <span class="service-icon">{service['icon']}</span>
            <h3 class="service-title">{service['title']}</h3>
            <p class="service-text">{service['description']}</p>
        </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="modern-footer">
        <div style="text-align: center;">
            <h3 style="color: white; font-size: 2rem; font-weight: 700; margin-bottom: 1rem;">Farhan Akbar</h3>
            <p style="color: rgba(255, 255, 255, 0.8); font-size: 1.2rem; margin-bottom: 2rem;">
                Innovation Architect & Digital Strategist
            </p>
            <div class="social-links">
                <a href="https://www.linkedin.com/in/farhan-akbar-ai/" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&style=flat-square" alt="LinkedIn"/>
                </a>
                <a href="https://api.whatsapp.com/send?phone=923034532403" target="_blank">
                    <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white&style=flat-square" alt="WhatsApp"/>
                </a>
                <a href="https://www.facebook.com/appjingle" target="_blank">
                    <img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white&style=flat-square" alt="Facebook"/>
                </a>
                <a href="mailto:rasolehri@gmail.com">
                    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white&style=flat-square" alt="Email"/>
                </a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
