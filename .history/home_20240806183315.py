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

    tag_line = "<div style='text-align: center;'>Simple solutions for complex problems</div>"
    st.markdown(tag_line, unsafe_allow_html=True)

    moto = "<h2> <div style='text-align: center;'>OUR CLIENTS ARE OUR FIRST PRIORITY</div></h2>"
    st.markdown(moto, unsafe_allow_html=True)

    moto_line = "<div style='text-align: center;'>AppJingle is a agency that provides value to clients by combining our experience with our commitment to deliver quality service to our customers.</div>"
    st.markdown(moto_line, unsafe_allow_html=True)
    st.write("---")

with st.container():
    title = "<h2> <div style='text-align: center;'>What We Do</div></h2>"
    st.markdown(title, unsafe_allow_html=True)

    dev_title = "<div style='text-align: center;'>We specialize in development revenue-generating applications leveraging state-of-the-art web and mobile technologies. Our distinctive approach sets us apart, as we meticulously immerse ourselves in understanding the intricacies of your business before making informed and strategic technology choices.</div>"
    st.markdown(dev_title, unsafe_allow_html=True)
    st.write('')

with st.container():
    left_column, center_column, right_column = st.columns(3)

    with left_column:
        st.header('Web Development', divider='rainbow')
<<<<<<<<<<<<<<  ✨ Codeium Command 🌟 >>>>>>>>>>>>>>>>
        st.write("We help you build a stunning and functional website that perfectly aligns with your business goals. With our expertise, we create intuitive interfaces and robust backend systems, ensuring a seamless user experience that enriches your online presence and drives conversions.")
        st.write("We assist you in creating functional and visually appealing websites that suit your business requirements. We design user-friendly interfaces and develop robust backend systems to create a smooth and engaging online presence for your brand.")
<<<<<<<  118916fb-1e53-4dc3-a2ba-0635e6b9a657  >>>>>>>
    with center_column:
        st.header('Mobile Development', divider='rainbow')
        st.write("We assist you in creating mobile applications that are simple to use and offer a smooth user experience. Whether you're looking to develop an app for Android or iOS, our team of skilled developers will work closely with you to understand your needs and deliver a product that fits your demands.")

    with right_column:
        st.header('AI Development', divider='rainbow')
        st.write("Tap into the power of artificial intelligence with AppJingle's AI app development services. Our team of experts is dedicated to creating innovative applications that leverage machine learning and deep learning algorithms to automate processes, enhance decision-making, and unlock new possibilities for your business.")
