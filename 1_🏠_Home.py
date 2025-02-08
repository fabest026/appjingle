import streamlit as st
from streamlit_option_menu import option_menu

# Page Configuration
st.set_page_config(
    page_title="AppJingle Solutions",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None
)

# Custom CSS
st.markdown("""
    <style>
        /* Main container padding */
        .block-container {
            padding: 2rem 5rem;
        }
        
        /* Typography */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        
        h1, h2, h3, h4, h5, h6, p {
            font-family: 'Poppins', sans-serif;
        }
        
        /* Header styles */
        .company-header {
            background: linear-gradient(120deg, #FF6B6B, #e01c80);
            padding: 3rem 2rem;
            border-radius: 20px;
            margin-bottom: 2rem;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
        
        .company-title {
            font-size: 3.5rem;
            font-weight: 700;
            background: linear-gradient(120deg, #ffffff, #f0f0f0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }
        
        .tag-line {
            color: white;
            font-size: 1.2rem;
            font-weight: 300;
            margin-bottom: 0.5rem;
        }
        
        /* Service card styles */
        .service-card {
            background: rgba(255, 255, 255, 0.95);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            transition: transform 0.3s ease;
            height: 100%;
        }
        
        .service-card:hover {
            transform: translateY(-5px);
        }
        
        .service-title {
            color: #e01c80;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        
        /* Footer styles */
        .modern-footer {
            background: rgba(255, 255, 255, 0.95);
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 -5px 15px rgba(0,0,0,0.05);
            margin-top: 3rem;
        }
        
        .social-links {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-top: 1rem;
        }
        
        .social-links a {
            transition: transform 0.3s ease;
        }
        
        .social-links a:hover {
            transform: translateY(-3px);
        }
        
        /* Hide Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Background overlay */
        .stApp {
            background: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)),
                        url("https://images.pexels.com/photos/4097159/pexels-photo-4097159.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
            background-size: cover;
            background-attachment: fixed;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
with st.container():
    st.markdown("""
        <div class="company-header">
            <h1 class="company-title">AppJingle Solutions</h1>
            <p class="tag-line">Boost your business with our IT solutions</p>
            <h2 style="color: white; font-size: 1.8rem; font-weight: 600; margin-top: 1.5rem;">
                YOUR SUCCESS IS OUR TOP CONCERN
            </h2>
            <p style="color: white; font-size: 1.1rem; font-weight: 300;">
                At AppJingle, we use our experience and commitment to provide great service 
                and real value to our clients.
            </p>
        </div>
    """, unsafe_allow_html=True)

# What We Do Section
st.markdown("""
    <div style='text-align: center; margin: 3rem 0;'>
        <h2 style='color: #e01c80; font-size: 2.5rem; font-weight: 600; margin-bottom: 1.5rem;'>
            What We Do
        </h2>
        <p style='font-size: 1.2rem; color: #333; max-width: 800px; margin: 0 auto;'>
            We build AI-powered apps for your website and phone that help you make more money. 
            We understand your business and choose the best technology to help you grow. 
            Let's work together to make your business even better!
        </p>
    </div>
""", unsafe_allow_html=True)

# Services Section
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="service-card">
            <h3 class="service-title">🌐 Web Development</h3>
            <p>We help you build stunning and functional websites that perfectly align with your 
            business goals. With our expertise, we create intuitive interfaces and robust backend 
            systems, ensuring a seamless user experience that enriches your online presence and 
            drives conversions.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="service-card">
            <h3 class="service-title">📱 Mobile Development</h3>
            <p>We assist you in creating mobile applications that are simple to use and offer 
            a smooth user experience. Whether you're looking to develop an app for Android or iOS, 
            our team of skilled developers will work closely with you to understand your needs and 
            deliver a product that fits your demands.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="service-card">
            <h3 class="service-title">🤖 AI Development</h3>
            <p>Tap into the power of artificial intelligence with AppJingle's AI app development 
            services. Our team of experts is dedicated to creating innovative applications that 
            leverage machine learning and deep learning algorithms to automate processes, enhance 
            decision-making, and unlock new possibilities for your business.</p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="modern-footer">
        <div style="text-align: center;">
            <p style="font-weight: 600; text-transform: uppercase; letter-spacing: 1.5px; color: #666;">
                Developed by
            </p>
            <h3 style="color: #e01c80; font-size: 1.5rem; margin: 0.5rem 0;">Farhan Akbar</h3>
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
