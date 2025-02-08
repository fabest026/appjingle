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

# Custom CSS with pink color scheme
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
            background: linear-gradient(135deg, #FF69B4 0%, #FF1493 100%);
            padding: 4rem 2rem;
            border-radius: 20px;
            margin-bottom: 3rem;
            box-shadow: 0 10px 30px rgba(255, 20, 147, 0.2);
            border: 1px solid rgba(255, 182, 193, 0.3);
            text-align: center;
        }
        
        .company-name {
            color: white;
            font-size: 4.2rem;
            font-weight: 700;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
            letter-spacing: 2px;
            line-height: 1.2;
        }
        
        .tag-line {
            color: white;
            font-size: 1.5rem;
            font-weight: 400;
            margin-bottom: 1.5rem;
            letter-spacing: 0.5px;
        }
        
        /* Service card styles */
        .service-card {
            background: rgba(255, 255, 255, 0.97);
            padding: 2.5rem;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(255, 20, 147, 0.1);
            transition: all 0.3s ease;
            height: 100%;
            border: 1px solid rgba(255, 182, 193, 0.3);
            color: #333;
        }
        
        .service-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(255, 20, 147, 0.2);
            border-color: #FF1493;
        }
        
        .service-title {
            color: #FF1493;
            font-weight: 600;
            margin-bottom: 1.5rem;
            font-size: 1.8rem;
        }
        
        /* Footer styles */
        .modern-footer {
            background: rgba(255, 255, 255, 0.97);
            padding: 2.5rem;
            border-radius: 15px;
            box-shadow: 0 -5px 15px rgba(255, 20, 147, 0.1);
            margin-top: 4rem;
            border: 1px solid rgba(255, 182, 193, 0.3);
        }
        
        .social-links {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-top: 1.5rem;
        }
        
        .social-links a {
            transition: all 0.3s ease;
        }
        
        .social-links a:hover {
            transform: translateY(-3px);
            filter: brightness(1.2);
        }
        
        /* Background styling */
        .stApp {
            background: linear-gradient(rgba(255, 240, 245, 0.97), rgba(255, 240, 245, 0.97)),
                        url("https://images.pexels.com/photos/4097159/pexels-photo-4097159.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
            background-size: cover;
            background-attachment: fixed;
        }
        
        /* Section styling */
        .section-title {
            color: #FF1493;
            font-size: 3rem;
            font-weight: 600;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        .section-description {
            color: #333;
            font-size: 1.3rem;
            max-width: 900px;
            margin: 0 auto 3rem auto;
            text-align: center;
            line-height: 1.8;
        }
        
        /* Service icon styling */
        .service-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #FF1493;
        }
        
        /* Hide Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
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
            <p style="color: white; font-size: 1.2rem; font-weight: 300; margin-top: 1rem;">
                At AppJingle, we use our experience and commitment to provide great service 
                and real value to our clients.
            </p>
        </div>
    """, unsafe_allow_html=True)

# What We Do Section
st.markdown("""
    <div style='margin: 4rem 0;'>
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

with col1:
    st.markdown("""
        <div class="service-card">
            <div class="service-icon">🌐</div>
            <h3 class="service-title">Web Development</h3>
            <p style="font-size: 1.1rem; line-height: 1.6;">
            We help you build stunning and functional websites that perfectly align with your 
            business goals. With our expertise, we create intuitive interfaces and robust backend 
            systems, ensuring a seamless user experience that enriches your online presence and 
            drives conversions.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="service-card">
            <div class="service-icon">📱</div>
            <h3 class="service-title">Mobile Development</h3>
            <p style="font-size: 1.1rem; line-height: 1.6;">
            We assist you in creating mobile applications that are simple to use and offer 
            a smooth user experience. Whether you're looking to develop an app for Android or iOS, 
            our team of skilled developers will work closely with you to understand your needs and 
            deliver a product that fits your demands.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="service-card">
            <div class="service-icon">🤖</div>
            <h3 class="service-title">AI Development</h3>
            <p style="font-size: 1.1rem; line-height: 1.6;">
            Tap into the power of artificial intelligence with AppJingle's AI app development 
            services. Our team of experts is dedicated to creating innovative applications that 
            leverage machine learning and deep learning algorithms to automate processes, enhance 
            decision-making, and unlock new possibilities for your business.</p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="modern-footer">
        <div style="text-align: center;">
            <p style="font-weight: 600; text-transform: uppercase; letter-spacing: 2px; color: #FF1493; margin-bottom: 0.5rem;">
                Developed by
            </p>
            <h3 style="color: #FF1493; font-size: 1.8rem; margin-bottom: 1.5rem;">Farhan Akbar</h3>
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
