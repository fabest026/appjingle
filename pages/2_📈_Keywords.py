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
  model_name="gemini-2.5-flash-lite", # Updated model name here
  generation_config=generation_config,
)

# Navbar
st.set_page_config(
    page_title="Keyword Cluster AI",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Add the Title
st.markdown(
    "<h1 style='text-align: center; color: black;'>"
    "✨ Keyword Cluster AI ✨"
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
<h3 style="text-align: center; color: black; font-weight: 300; font-style: italic;">💥&nbsp;&nbsp;Powered By: AppJingle Solutions&nbsp;&nbsp;💥</h3>
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
    st.markdown("<h4>Enter Details </h4>", unsafe_allow_html=True)
    
    # Section Heading
    keyword = st.text_input("Seed Keyword")
    
    # Subpoints
    
    country_options = ["United States", "Canada", "United Kingdom", "Australia", "Germany", "France", "India", "Pakistan", "Nigeria", "Brazil", "Russia", "China", "Japan", "South Korea", "South Africa", "Spain", "Italy", "Turkey", "Netherlands", "Belgium", "Sweden", "Switzerland", "New Zealand", "Singapore", "Malaysia"]
    country = st.selectbox('Country', country_options)
    
    # Add the Voice Tones
    #voice_tones = st.sidebar.selectbox("Choose Voice Tones:", ["Formal", "Informal", "Friendly", "Bold", "Adventurous", "Witty", "Professional", "Casual", "Informative", "Creative", "Trendy", "Caring", "Cheerful", "Excited", "Funny", "Sad", "Serious", "Tense", "Vulnerable", "Angry", "Surprised", "Worried", "Assertive", "Confident", "Cooperative", "Encouraging" ])
    
    # Add the Writing Styles
    #writing_styles = st.sidebar.selectbox("Choose Writing Styles:", ["Academic", "Conversational", "Creative", "Critical", "Descriptive", "Instructive", "Technical", "Analytical","Business", "Causal", "Emotional", "Expository", "Formal", "Informal", "Legal", "Medical", "Poetic", "Persuasive"])
    
    # Audience
    #audience = st.selectbox("Audience: Who is the target audience?", ["Teenager", "Adult", "20-years-old", "30-years-old",  "40-years-old", "50-years-old", "Senior", "Everyone", "Uninformed Audience", "Neutral Audience", "Business Audience", "Researcher", "Expert Audience", "My Boss", "My Student", "My Teacher", "My Family", "My Friends", "My Colleagues"] )
    
    #num_words = st.number_input("Number of words", min_value=250, max_value=3000, step=50)

    # Primary Keyword
    #primary_keyword = st.text_input("Primary Keyword ")
    
    # Secondary Keyword
    #secondary_keyword = st.text_input("Secondary Keyword")
    
    # Reference Article Link
    # reference_article_link = st.text_input("Reference Article Link")
    
    

    # Prompt
    prompt_parts = [
            f"""
            Please ignore all previous instructions. I want you to respond only in English language. I want you to act as a keyword research expert that speaks and writes fluent English. I want you to do keyword research for this seed keyword {keyword} and then i want you to create a table of low competition easy to rank for keywords related to the keyword. On the chart include the search term, search volume, difficulty to rank, CPC.
            Follow this instructions below:
            1. First find the 30 keyword ideas that are related to {keyword}. 
            3. Then Use the Seed Keyword Alternate Or Synonym of keyword usually used in the specified {country}.
            2. Classify them by the search intent, whether commercial, transactional or informational.
            3. Then cluster them into groups based on their semantic relevance. First I want you to give me back a short over list of cluster topics found. 
            4. Then I want a list in table, with the following columns:  
            5. cluster, keyword, search intent, keywords 2-5 words with cpc , difficulty, volume on the basis of user search intent by {country} and country. 
            6. Please merge cells by clusters of the first column in one cell.
            """
            ]


import streamlit as st

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
    with open("keyword_analysis.txt", "w") as f:
        f.write(st.session_state.response)
    st.download_button(
        label="Download File",
        data=open("keyword_analysis.txt", "rb").read(),
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
        
        
        


