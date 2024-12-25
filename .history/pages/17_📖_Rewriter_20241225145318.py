## loading all the environment variables
from dotenv import load_dotenv
load_dotenv() 

# Import Important libraries
import streamlit as st
import google.generativeai as genai
import os

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)


# Navbar
st.set_page_config(
    page_title="Rewriter",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Add the Title
st.markdown(
    "<h1 style='text-align: center; color: black;'>"
    "✨ Rewriter ✨"
    "</h1>",
    unsafe_allow_html=True
)

#st.title('✨ AI Blog Section Generator')

# create a subheader
st.markdown('''
<style>
h3 {
    font-family: 'Open Sans', sans-serif;
    font-size: 18px;
    line-height: 0px;
    margin-top: 0;
    margin-bottom: 24px;
    text-align: center;
    display: flex;
    justify-content: center;
}
</style>
<h3 style="text-align: center; color: black; font-weight: 300; font-style: italic;">💥&nbsp;&nbsp;Powered by: AppJingle Solutions&nbsp;&nbsp;💥</h3>
''', unsafe_allow_html=True)

# sidebar for the user input

with st.sidebar:
    st.markdown(
        "<style>h1 {text-align: center;}</style>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<style>h1 {text-align: center; color: black;}</style>",
        unsafe_allow_html=True
    )
    st.title("Input Settings")

    st.markdown(
        "<style>"
        "h4 {text-align: left; color: black; margin-top: 4px;}"
        "p {text-align: left; color: black;}"
        "</style>",
        unsafe_allow_html=True
    )
    st.markdown("<h4>Enter Details for the Article: </h4>", unsafe_allow_html=True)
    
    
    # Section Heading
    # focus_keyword = st.text_input("Focus Keyword (required)", placeholder="enter focus keyword")
    
    # Primary Keyword
    primary_keyword = st.text_input("Primary Keyword (required)", placeholder="enter primary keyword")
    
    # Secondary Keywords
    secondary_keywords = st.text_input("Secondary Keyword", placeholder="enter secondary keyword")
    
    # Input Section
    input_section = st.text_area("Input Section", height=300)
    
    # Language
    language = st.selectbox("Language", ["English", "French", "Spanish", "German", "Italian", "Portuguese", "Dutch", "Russian", "Chinese (Simplified)", "Japanese", "Korean"])
    
    # Add the Voice Tones
    # voice_tones = st.sidebar.selectbox("Choose Voice Tones:", ["Formal", "Informal", "Friendly", "Bold", "Adventurous", "Witty", "Personalized", "Professional", "Casual", "Informative", "Creative", "Trendy", "Caring", "Cheerful", "Excited", "Funny", "Sad", "Serious", "Tense", "Vulnerable", "Angry", "Surprised", "Worried", "Assertive", "Confident", "Cooperative", "Encouraging" ])
    
    # Add the Writing Styles
    # writing_styles = st.sidebar.selectbox("Choose Writing Styles:", ["Academic", "Conversational", "Creative", "Critical", "Descriptive", "Instructive", "Technical", "Analytical","Business", "Causal", "Emotional", "Expository", "Formal", "Informal", "Legal", "Medical", "Poetic", "Persuasive"])
    
    # Audience
    # audience = st.selectbox("Audience: Who is the target audience?", ["Digital Marketers", "General Audience", "Everyone", "Uninformed Audience", "Industry Experts", "Neutral Audience", "Business Owners and Entrepreneurs", "Researcher", "Expert Audience", "Potential Clients", "Tech", "Academic", "Teenager", "Adult", "20-years-old", "30-years-old",  "40-years-old", "50-years-old"] )
    
    # Word Counter
    # num_words = st.number_input("Number of words", min_value=800, max_value=3000, step=250)
    
    #Heading Counter
    # num_headings = st.number_input("Number of Headings", min_value=8, max_value=20, step=1)
    
    # Secondary Keyword
    #secondary_keyword = st.text_input("Secondary Keyword")
    
    # Reference Article Link
    # reference_article_link = st.text_input("Reference Article Link")

    # Prompt
    prompt_parts = [
            f"""
                 Please ignore all previous instructions. {input_section} make a new unique copy You are an AI assistant writing in {language}. You are a professional SEO and high-end copywriter who speaks and writes {language} fluently. It would be best to pretend that you could write unique, onpage SEO optimized content for the topic: {primary_keyword}. The article should contain rich, comprehensive, and very detailed paragraphs with lots of details. Let the report be an extended form of a minimum of more than 1500 words. Write proper subheadings with related and LSI keywords of the topic. The article must be written in an active voice (in a way that sounds like an actual human), using simple {language}, contractions, idioms, transitional phrases, interjections, dangling modifiers, and colloquialisms. You should also avoid using the exact words repeatedly and putting sentences together in a way that doesn't sound natural. Write an SEO-friendly introduction and write more than 10 headings like  H2, H3, and H4. Count the given topic as the main keyword, my topic is: {primary_keyword}. write a 1200 words plus,  100% unique, free from any plagiarism, AI detection-free detailed article including more than 10 times  of the keywords. Choose the keyword from: "{primary_keyword}", using related and human search intention. You must write more than two external and internal links for additional resources in the body of the article as references. At the end of the article, write a conclusion also. Don't copy from others;  It would be best to do deep research about: {primary_keyword}. Use a formal tone and improve highest readability scores.  also incorporated these keywords: {primary_keyword}, {secondary_keywords} according to SEO rules naturally. but our focus keyword is {primary_keyword} also focus that headings and content must be unique and also the format of content must be unique new copy also change the headings structure also make the h1,h2,h3. Please make the content 100% unique, free from plagiarism, and less detectable by AI, You will rephrase the content while retaining its meaning and flow.  
            """
            ]

import streamlit as st
import io

# Initialize session state variables if they do not exist
if 'response' not in st.session_state:
    st.session_state.response = None

# Add the Clear all button
clear_button = st.sidebar.button("Clear All")
if clear_button:
    st.session_state.clear()
    st.experimental_rerun()  # This ensures the page is rerun to reflect the cleared state

# Sidebar Submit Button
submit_button = st.sidebar.button("Generate")

if submit_button and 'response' in st.session_state and not clear_button:
    # Display the spinner
    with st.spinner("Generating...."):
        # Generate the response
        response = model.generate_content(prompt_parts)
        # Store the response in session state
        st.session_state.response = response.text

# Write results if response is available
if st.session_state.response:
    st.write(st.session_state.response)

    # Download file option
    with open("keyword_analysis.txt", "w", encoding="utf-8") as f:
        f.write(st.session_state.response)
    st.download_button(
        label="Download File",
        data=io.BytesIO(st.session_state.response.encode("utf-8")).getvalue(),
        file_name='keyword_analysis.txt',
        mime='text/plain',
    )

    # Add styling to the generated text
    st.markdown('''
        <style>
            p {
                font-family: 'Open Sans', sans-serif;
                font-size: 16px;
                line-height: 24px;
                margin-top: 0;
                margin-bottom: 24px;
            }
            strong {
                font-weight: 600;
            }
            em {
                font-style: italic;
            }
            code {
                background-color: #f5f5f5;
                border-radius: 3px;
                display: inline-block;
                font-family: 'Menlo', monospace;
                font-size: 14px;
                margin: 0 1px;
                padding: 2px 4px;
            }
        </style>
    ''', unsafe_allow_html=True)
    
    
    
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
