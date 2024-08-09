import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="AppJingle Solutions",
                   page_icon="💻",
                   layout="wide",
                   initial_sidebar_state="auto",
                   menu_items=None)

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
            
        <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)


# with st.sidebar:
#     selected = option_menu(
#         menu_title="Main Menu",
#         options=["Home", "About", "Services", "Contact"],
#         icons=["house", "info-circle", "list", "envelope"],
#         menu_icon="cast",
#         default_index=0,
#         orientation="horizontal",
#     )

# if selected == "Home":
#     pass


with st.container():
    title = "<h1> <div style='text-align: center;'><font color='#e01c80'>App</font><font color='#e01c80'>Jingle</font> Solutions</div></h1>"
    st.markdown(title, unsafe_allow_html=True)
  
    tag_line = "<div style='text-align: center;'>Boost your business with our IT solutions</div>"
    st.markdown(tag_line, unsafe_allow_html=True)
    
    moto = "<h3> <div style='text-align: center;'>YOUR SUCCESS IS OUR TOP CONCERN</div></h3>"
    st.markdown(moto, unsafe_allow_html=True)

    moto_line = "<div style='text-align: center;'>At AppJingle, we use our experience and commitment to provide great service and real value to our clients.</div>"
    st.markdown(moto_line, unsafe_allow_html=True)
    st.write("---")

with st.container():
    title = "<h2> <div style='text-align: center;'>What We Do</div></h2>"
    st.markdown(title, unsafe_allow_html=True)

    dev_title = "<div style='text-align: center;'>We build AI-powered apps for your website and phone that help you make more money. We understand your business and choose the best technology to help you grow. Let's work together to make your business even better!</div>"
    st.markdown(dev_title, unsafe_allow_html=True)
    st.write('')

with st.container():
    left_column, center_column, right_column = st.columns(3)

    with left_column:
        st.header('Web Development', divider='rainbow')
        st.write("We help you build a stunning and functional website that perfectly aligns with your business goals. With our expertise, we create intuitive interfaces and robust backend systems, ensuring a seamless user experience that enriches your online presence and drives conversions.")
    with center_column:
        st.header('Mobile Development', divider='rainbow')
        st.write("We assist you in creating mobile applications that are simple to use and offer a smooth user experience. Whether you're looking to develop an app for Android or iOS, our team of skilled developers will work closely with you to understand your needs and deliver a product that fits your demands.")

    with right_column:
        st.header('AI Development', divider='rainbow')
        st.write("Tap into the power of artificial intelligence with AppJingle's AI app development services. Our team of experts is dedicated to creating innovative applications that leverage machine learning and deep learning algorithms to automate processes, enhance decision-making, and unlock new possibilities for your business.")

# Adding the HTML footer
# Profile footer HTML for sidebar


# Render profile footer in sidebar at the "bottom"
# Set a background image
def set_background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.pexels.com/photos/4097159/pexels-photo-4097159.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1);
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_image()

# Set a background image for the sidebar
sidebar_background_image = '''
<style>
[data-testid="stSidebar"] {
    background-image: url("https://www.pexels.com/photo/abstract-background-with-green-smear-of-paint-6423446/");
    background-size: cover;
}
</style>
'''

st.sidebar.markdown(sidebar_background_image, unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Custom CSS to inject into the Streamlit app
footer_css = """
<style>
.footer {
    position: fixed;
    right: 0;
    bottom: 0;
    width: auto;
    background-color: transparent;
    color: black;
    text-align: right;
    padding-right: 10px;
}
</style>
"""


# HTML for the footer - replace your credit information here
footer_html = f"""
<div class="footer">
    <p style="font-size: 12px; font-style: italic; color: gray; margin-bottom: 0px; opacity: 0.7; line-height: 1.2; text-align: center;">
        <span style="display: block; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 8px; font-family: 'Open Sans', sans-serif;">Developed by::</span>
        <span style="font-size: 20px; font-weight: 800; text-transform: uppercase; font-family: 'Open Sans', sans-serif;">Farhan Akbar</span>
    </p>
    <a href="https://www.linkedin.com/in/farhan-akbar-ai/"><img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"/></a>
    <a href="https://api.whatsapp.com/send?phone=923034532403"><img src="https://img.shields.io/badge/WhatsApp-Chat%20Me-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/></a>
    <a href="https://www.facebook.com/appjingle"><img src="https://img.shields.io/badge/Facebook-Connect-1877F2?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook"/></a>
    <a href="mailto:rasolehri@gmail.com"><img src="https://img.shields.io/badge/Email-Contact%20Me-red?style=for-the-badge&logo=email" alt="Email"/></a>
</div>
"""

# Combine CSS and HTML for the footer
st.markdown(footer_css, unsafe_allow_html=True)
st.markdown(footer_html, unsafe_allow_html=True) 
