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
  "top_k": 40,
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
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)


# Navbar
st.set_page_config(
    page_title="Prompt Generator",
    page_icon="👨‍🎓",
    layout="centered",
    initial_sidebar_state="collapsed",
)



# title of our app
#st.title('✍️ AI Prompt Generator')

# Add the Title
st.markdown(
    "<h1 style='text-align: center; color: black;'>"
    "✨ AI Prompt Generator"
    "</h1>",
    unsafe_allow_html=True
)


# create a subheader
#st.subheader("You can generate any type of Prompt for your blog or any other purpose. 🤖")

# create a subheader
st.markdown('''
<style>
h3 {
    font-family: 'Open Sans', sans-serif;
    font-size: 16px;
    line-height: 24px;
    margin-top: 0;
    margin-bottom: 24px;
}
</style>
<h3 style="text-align: center; color: black;">🔥 Enhance Your Creativity with AI Prompt Engineer! 🔥<br />Generate prompts for blogs, social media, content marketing, and more!</h3>
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
    st.markdown("<h4>Enter Details for the Prompt: </h4>", unsafe_allow_html=True)
    
    # Topic
    topic = st.text_input("Topic: What is the topic of the prompt? Eg: python, machine learning,..")
    
    # Goal
    task = st.text_input(" Task: What do you want to achieve with the prompt? Eg: writing a blog, analyzing a text,..")
    
    # Add the Voice Tones
    voice_tones = st.sidebar.selectbox("Choose Voice Tones:", ["Formal","Friendly", "Bold", "Adventurous", "Witty", "Professional", "Casual", "Informative", "Creative", "Trendy", "Caring", "Cheerful", "Excited", "Funny", "Sad", "Serious", "Tense", "Vulnerable", "Angry", "Surprised", "Worried", "Assertive", "Confident", "Cooperative", "Encouraging" ])
    
    # Add the Writing Styles
    writing_styles = st.sidebar.selectbox("Choose Writing Styles:", ["Academic", "Conversational", "Creative", "Critical", "Descriptive", "Instructive", "Technical", "Analytical","Business", "Causal", "Emotional", "Expository", "Formal", "Informal", "Legal", "Medical", "Poetic", "Persuasive"])
    
    # Audience
    audience = st.selectbox("Audience: Who is the target audience?", ["Teenager", "Adult", "20-years-old", "30-years-old",  "40-years-old", "50-years-old", "Senior", "Everyone", "Uninformed Audience", "Neutral Audience", "Business Audience", "Researcher", "Expert Audience", "My Boss", "My Student", "My Teacher", "My Family", "My Friends", "My Colleagues"] )
    
    # Word Counter
    word_count = st.number_input("Word Count", min_value=10, max_value=3000, step=100)
    
    # Character Counter
    character_count = st.number_input("Character Count", min_value=10, max_value=3000, step=100)
    
    # Prompt Context
    prompt_context = st.text_area("Prompt Context: Provide a brief context or situation where the prompt will be used (optional)")
    
    # Example prompt
    example_prompt = st.text_area("Example prompt: Provide an example of a prompt that you would like your generated prompts to be similar to (optional)")
    
    

    # Prompt
    prompt_parts = [
            f"""
            Please ignore all previous instructions. Act as a Prompt Engineer, To create an AI prompt, start by defining your goal and gathering data. Next, write a clear, concise prompt that will guide the AI you' re using to generate the output you desire. Generate an effective AI prompt is a critical to obtaining the expected results out of language models like ChatGPT, GPT-3, Gemini etc.  Finally, test and iterate on your prompt until you achieve the desired results. With a little bit of southern patience and some New Yorker creativity, you'll have an amazing AI prompt that can help you automate tasks and enhance your workflows!
            Follow these guidelines:

            Clarity: Ensure that the prompt is clear, concise, and direct. This increases the likelihood that the AI will understand what you are asking and generate an appropriate response.
            Context: The more specific and contextual your prompt, the better the large language model can generate relevant responses. If you're looking for a specific type of response, include that information in your prompt.
            Completeness: Provide as much relevant information as possible to help guide the AI. If there are crucial details about the scenario or question that the AI wouldn't know, make sure to include them.
            Instruction: If you want a particular style or format for the response, specify this in the prompt. For instance, if you want a response in the form of a poem, bullet points, or formal language, indicate this.
            Open-ended vs. Closed-ended: If you're looking for creative or expansive responses, use open-ended questions. For more specific, concise answers, use closed-ended questions.
            Grammar and Spelling: Check your prompt for grammar and spelling mistakes. 
            
            Goal: {task} {topic} {voice_tones} {audience} {writing_styles} of {word_count} words and {character_count} characters optional.
            Prompt Context: Provide a brief context or situation where the prompt will be used {prompt_context}  
            Example prompt: Provide an example of a prompt that you would like your generated prompts to be similar to {example_prompt}
            
            Based on the context and example prompt, write an effective AI prompt that will guide the AI you're using to generate the output you desire.
            
            
            """
            ]
    # Submit Button
    submit_button = st.button("Generate")

if submit_button:
    # Display the spinner
    with st.spinner("Converting desired input to prompt..."):
        # Generate the response
        response = model.generate_content(prompt_parts)
        # Write results
        st.write(response.text)

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

clear_button = st.sidebar.button("Clear All")
with st.sidebar:
    st.markdown('''
        <style>
            .element-container .stButton.stBtn {
                background-color: #ffc107 !important;
                border-color: #ffc107 !important;
            }
        </style>
    ''', unsafe_allow_html=True)

    if clear_button:
        for key in st.session_state:
            if isinstance(st.session_state[key], str) and st.session_state[key] != "":
                st.session_state[key] = ""
            elif isinstance(st.session_state[key], list) and st.session_state[key] != []:
                st.session_state[key] = []
            elif isinstance(st.session_state[key], dict) and st.session_state[key] != {}:
                st.session_state[key] = {}
        
        
        
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
