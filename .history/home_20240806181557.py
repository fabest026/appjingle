import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="AppJingle Solutions",
                   page_icon=":software:",
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
    title = "<h1> <div style='text-align: center;'><font color='#ec1c25'>Net</font><font color='#019649'>Phenix</font> IT Solutions</div></h1>"
    st.markdown(title, unsafe_allow_html=True)

    tag_line = "<div style='text-align: center;'>Simple solutions for complex problems</div>"
    st.markdown(tag_line, unsafe_allow_html=True)

    moto = "<h2> <div style='text-align: center;'>OUR CLIENTS ARE OUR FIRST PRIORITY</div></h2>"
    st.markdown(moto, unsafe_allow_html=True)

    moto_line = "<div style='text-align: center;'>NetPhenix is a company that provides value to clients by combining our experience with our commitment to deliver quality service to our customers.</div>"
    st.markdown(moto_line, unsafe_allow_html=True)
    st.write("---")

with st.container():
    title = "<h2> <div style='text-align: center;'>What We Do</div></h2>"
    st.markdown(title, unsafe_allow_html=True)

    dev_title = "<div style='text-align: center;'>We specialize in crafting revenue-generating applications leveraging state-of-the-art web and mobile technologies. Our distinctive approach sets us apart, as we meticulously immerse ourselves in understanding the intricacies of your business before making informed and strategic technology choices.</div>"
    st.markdown(dev_title, unsafe_allow_html=True)
    st.write('')

with st.container():
    left_column, center_column, right_column = st.columns(3)

    with left_column:
        st.header('Web Development', divider='rainbow')
        st.write("Elevate your online presence with NetPhenix's expert web application development services. From intuitive user interfaces to robust backend systems, we bring your vision to life, creating seamless and engaging web experiences.")

    with center_column:
        st.header('Mobile Development', divider='rainbow')
        st.write("Harness the power of mobile technology with NetPhenix's innovative mobile development solutions. Whether it's iOS or Android, we design and develop cutting-edge mobile applications that resonate with your audience, delivering a user-centric experience on every device.")

    with right_column:
        st.header('IOT Development', divider='rainbow')
        st.write("Embrace the future of connectivity with NetPhenix's IoT development expertise. Our team is skilled in designing and implementing smart solutions that seamlessly integrate devices, providing you with actionable insights and enhancing efficiency across your connected ecosystem.")