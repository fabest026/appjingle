## loading all the environment variables
from dotenv import load_dotenv
load_dotenv() 

# Import Important libraries
import streamlit as st
import google.generativeai as genai
import os

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the Model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

# Load Gemini Pro model
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

# Navbar
st.set_page_config(
    page_title="SEO Content Creator",
    page_icon="👷🏻‍♂️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Add the Title
st.markdown(
    "<h1 style='text-align: center; color: black;'>"
    "✨ SEO Content Creator ✨"
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
    focus_keyword = st.text_input("Focus Keyword (required)", placeholder="enter focus keyword")
    
    # Primary Keyword
    primary_keyword = st.text_input("Primary Keyword (required)", placeholder="enter primary keyword")
    
    # Secondary Keywords
    secondary_keywords = st.text_input("Secondary Keyword", placeholder="enter secondary keyword")
   
    
    # Add the Voice Tones
    voice_tones = st.sidebar.selectbox("Choose Voice Tones:", ["Formal", "Informal", "Friendly", "Bold", "Adventurous", "Witty", "Professional", "Casual", "Informative", "Creative", "Trendy", "Caring", "Cheerful", "Excited", "Funny", "Sad", "Serious", "Tense", "Vulnerable", "Angry", "Surprised", "Worried", "Assertive", "Confident", "Cooperative", "Encouraging" ])
    
    # Add the Writing Styles
    writing_styles = st.sidebar.selectbox("Choose Writing Styles:", ["Academic", "Conversational", "Creative", "Critical", "Descriptive", "Instructive", "Technical", "Analytical","Business", "Causal", "Emotional", "Expository", "Formal", "Informal", "Legal", "Medical", "Poetic", "Persuasive"])
    
    # Audience
    audience = st.selectbox("Audience: Who is the target audience?", ["Digital Marketers", "General Audience", "Everyone", "Uninformed Audience", "Industry Experts", "Neutral Audience", "Business Owners and Entrepreneurs", "Researcher", "Expert Audience", "Potential Clients", "Tech", "Academic", "Teenager", "Adult", "20-years-old", "30-years-old",  "40-years-old", "50-years-old"] )
    
    # Word Counter
    num_words = st.number_input("Number of words", min_value=800, max_value=3000, step=250)
    
    #Heading Counter
    num_headings = st.number_input("Number of Headings", min_value=8, max_value=20, step=1)
    
    # Secondary Keyword
    #secondary_keyword = st.text_input("Secondary Keyword")
    
    # Reference Article Link
    # reference_article_link = st.text_input("Reference Article Link")

    # Prompt
    prompt_parts = [
            f"""
                Forget all previous instructions.
                    Assume the role of a proficient article writer fluent in English. Your task is to compose a {num_words}-word article on focus keyword "{focus_keyword}" that effectively capture the attention of the {audience} audience. Also SEO Optimize this article for Primary keyword {primary_keyword} and Secondary Keywords  {secondary_keywords}.
                    Here are the instructions to follow:

                    1. Use a {voice_tones} tone using {writing_styles} writing style.
                    2. Content must be {num_words} words. 
		            2. Write in human don't use complex terms like showcase, leverage, delve, craft, dig, dive, tailored etc. write uniquely.
                    3. The content should be original to avoid plagiarism. Also, ensure it doesn't appear AI-generated.
                    4. Apply Markdown language and Heading tags (H1 for the main title, H2 for headings, and Strong or bold tags for subheadings) to enhance readability and SEO.  
		            5. Inject Focus Keyword in the main title (H1)
                    6. Inject Focus Keyword at the beginning of the main title (H1).
                    6. Inject Primary Keyword at the beginning of the H2.
                    7. H2 must be separted to H1. 
                    7. Inject the Secondary keyword in H3.
		            7. Inject the Focus keyword in first 100 words of introduction.
                    8. Focus Keyword density must be less than 0.2%.
                    9. Primary keyword density must be less than 0.1%.
                    10. Secondary keyword density must be less than 0.1%.  
                    11. Inject naturally Focus Keyword atleast 3 times precisely in content body.
                    9. Inject naturally Primary Keyword atleast 3 times precisely in content body.
                    10. Inject naturally the Secondary keyword atleast 2 times precisely in content body.
                    11. Must be add Link out to external resources.
                    12. Must Add DoFollow links pointing to external resources.
                    13. Add external links in content body.
                    Generate an eye-catchy meta title and meta description related to content body with the Focus keyword "{focus_keyword}"

                    1. Ensure the meta title must be less than 60 characters length limit.
                    2. Focus Keyword must be Fully injected in naturally in the meta title in every variation.
                    3. Ensure the meta description must be less than 160 characters length limit.
                    4. Focus Keyword must be Fully injected in naturally in the meta description in every variation.
                    3. Use a conversational tone using simple language, avoiding jargon and complex terms.
                    4. Please be natural, write like a human.
                    7. Headlines that are about 55 characters long will display fully in search results and tend to get more clicks.
                    7. Headlines are more likely to be clicked on in search results if they have about 6 words.
                    8. Positive headlines tend to get better engagement than neutral or negative ones.
                    9. Headlines that are lists and how-to get more engagement on average than other types of headlines.
                    8. Headlines that are lists and how-to get more engagement on average than other types of headlines.
                    9. Headline will be more compelling and attract more clicks if you add more emotional and power words.
                    1. Beginning and Ending Words must be in the meta title and meta description. Most readers only look at the first and last 3 words of a headline before deciding whether to click.
                    
                    Following the introduction, include a Table of Contents (TOC) in a table format with two columns: 1. Sr# 2. Headings. Write must be {num_headings} headings, relevant subheadings and explain them in detail. Develop {writing_styles}, detailed paragraphs using these headings and subheadings. The introduction and conclusion paragraph should not be more than 10% of text.
                    Conclude the article and follow up with five pertinent FAQs (with answers) relevant to the topic. Ensure each question ends with a question mark (?). Write in Markdown Form Pattern of content is like this. 1. Meta title and Meta description 2. H1 3. H2  4. Table of Contents 5. detailed paragraphs using these headings and subheadings 6. Conclusion. 7. FAQs.
                    The goal is to produce valuable content that engages readers and satisfies SEO needs. Bold the headings, subheadings and keypoints.
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
