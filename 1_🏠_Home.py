# (Previous imports and page configuration remain the same)

st.markdown("""
    <style>
        /* Previous styles remain the same until service card styles */
        
        .service-card {
            background: #e4dbe6;  /* Updated background color */
            padding: 2.5rem;
            border-radius: 24px;
            transition: all 0.4s ease;
            height: 100%;
            border: 1px solid rgba(0,0,0,0.1);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }
        
        .service-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            border-color: #FF1493;
        }
        
        .service-title {
            color: #333333;  /* Darker text for better contrast on new background */
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
        
        /* Developer name styling */
        .developer-name {
            color: #e4dbe6;  /* Updated color */
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            text-align: center;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
            background: #333333;
            padding: 0.5rem 2rem;
            border-radius: 12px;
            display: inline-block;
        }
        
        /* Service text styling */
        .service-text {
            color: #333333;  /* Darker text for better contrast */
            font-size: 1.1rem;
            line-height: 1.6;
            text-align: center;
            font-weight: 500;
        }
        
        /* Modern footer with updated color */
        .modern-footer {
            background: #333333;  /* Dark background for contrast */
            padding: 3rem;
            border-radius: 24px;
            margin-top: 5rem;
            border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.05);
        }
        
        .footer-text {
            color: #e4dbe6;  /* Updated color */
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 0.5rem;
            text-align: center;
        }
        
        /* Date-Time Display */
        .datetime-display {
            background: #333333;
            color: #e4dbe6;
            padding: 0.8rem 1.5rem;
            border-radius: 12px;
            font-size: 0.9rem;
            margin-bottom: 2rem;
            text-align: right;
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-weight: 500;
            letter-spacing: 0.5px;
        }
    </style>
""", unsafe_allow_html=True)

# DateTime Display
st.markdown("""
    <div class="datetime-display">
        🕒 2025-02-08 06:24:28 UTC | 👤 fabest026
    </div>
""", unsafe_allow_html=True)

# (Rest of the header section remains the same)

# Services Section with updated colors
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

# Footer with updated colors
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
