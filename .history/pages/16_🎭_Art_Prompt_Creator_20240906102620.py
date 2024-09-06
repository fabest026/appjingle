from dotenv import load_dotenv
load_dotenv()  ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import random

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini Pro model and get reponses
model=genai.GenerativeModel("gemini-1.5-pro-latest")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

# Navbar
st.set_page_config(
    page_title="ArtPormpter",
    page_icon="🎭",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Add the Title
st.markdown(
    "<h1 style='text-align: center; color: black;'>"
    "ArtPormpter 🎨🎭"
    "</h1>",
    unsafe_allow_html=True
)

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
<style>
    h3 {
        text-align: center;
        color: black;
        margin-top: 0;
        margin-bottom: 24px;
    }
</style>
<h3>
    🖌️ AI-powered Image-to-Text Generator 📝<br />
    <span style="font-weight: 300; font-style: italic;">Generate creative and inspiring prompts based on any image!</span>
</h3>
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
 
with st.sidebar:
    
    description_keywords_placeholder = "Keyword: How would you like to describe the image (optional)"
    description_keywords = st.text_input(description_keywords_placeholder)
    
    # Add the photographic style
    
    photographic_style_placeholder = "Photographic Styles: Describe the style of the image Eg: portrait, landscape etc.(optional)"
    photographic_style = st.multiselect(photographic_style_placeholder, ["photo","illustration" , "3d render", "topography", "cinematic", "poster", "painting" , "fashion", "product", "anime", "architecture", "dark fantasy", "vibrant", "graffiti", "portrait phtography", "wildlife photography", "conceptual art", "ukiyo" ])

    
    # Add the ratio
    
    ratio_placeholder = "Ratio: ratio of the image"
    ratio = st.selectbox(ratio_placeholder, ["16:9", "4:3", "1:1", "3:4", "9:16", "1:2", "2:1"])
    
    # Add the object Placeholder
    
    object_placeholder = "Object: identify the main object in the image Eg: person, dog, cat, etc."
    object = st.text_input(object_placeholder)
    
    # Add the Action Placeholder
    
    action_placeholder = "Action: Describe what the object is doing, or what you want it to do? Eg: drawing, painting, writing, etc. (optional)"
    action = st.text_input(action_placeholder)
    input_prompt = st.text_input("Input Prompt:", value="", key="input")

    image_placeholder = "Upload an image" 
    uploaded_file = st.file_uploader(image_placeholder, type=["jpg", "jpeg", "png"])
    image_name = "Uploaded Image"
    if uploaded_file is not None:
        uploaded_image = Image.open(uploaded_file)
        image = uploaded_image
        uploaded_image = st.image(uploaded_image, caption=image_name, use_column_width=True)

prompt_parts = [
            f"""
            Please ignore the pervious response. Act as a Prompt Engineer, To create an AI prompt, start by defining your goal and gathering data. Next, write a clear, concise prompt that will guide the AI you're using to generate the output you desire. Generate an effective AI prompt is a critical to obtaining the expected results out of language models like Midjourney, Dalle-3, Stable Diffusion etc.  Finally, test and iterate on your prompt until you achieve the desired results. With a little bit of southern patience and some New Yorker creativity, you'll have an amazing AI prompt that can help you automate tasks and enhance your workflows!
            Follow these guidelines:

            1. Clarity: Ensure that the prompt is clear, concise, and direct. This increases the likelihood that the AI will understand what you are asking and generate an appropriate response.
            2. Context: The more specific and contextual your prompt, the better the large language model can generate relevant responses. If you're looking for a specific type of response, include that information in your prompt.
            3. Completeness: Provide as much relevant information as possible to help guide the AI. If there are crucial details about the scenario or question that the AI wouldn't know, make sure to include them.
            4. Instruction: If you want a particular style or format for the response, specify this in the prompt. For instance, if you want a response in the form of a poem, bullet points, or formal language, indicate this.
            5. Open-ended vs. Closed-ended: If you're looking for creative or expansive responses, use open-ended questions. For more specific, concise answers, use closed-ended questions.
            6. Grammar and Spelling: Check your prompt for grammar and spelling mistakes. 
            
            Goal: {image_name if image_name else '(no uploaded file)'}
            Topic: {description_keywords}
            Photographic Styles: {', '.join(photographic_style)}
            
            """
         
      ]  

with st.sidebar:
    submit=st.button("Tell me about the image")


# if submit is clicked
if submit:
    with st.spinner("Converting desired input to prompt..."):
        st.markdown('''
            <style>
                .element-container .element-spinner .spinner {
                    color: #3498db;
                }
            </style>
        ''', unsafe_allow_html=True)

        example_prompt = (
            "Write a detailed, creative, and imaginative description of the image based on the information provided in the prompt"
        )
        magic_prompt = (
            example_prompt + 
            " with unique photographic style {}".format(random.choice(photographic_style)) +
            " with unique keywords {}".format(" ".join(set(description_keywords))) +
            " with unique Action {}".format(random.choice(action)) +
            " with unique Object {}".format(random.choice(object))
        )

        lines = magic_prompt.splitlines()
        magic_prompt = "\n".join(lines[:3])

        full_prompt = "\n".join(prompt_parts)
        example_response = "<br/>".join(["<p>{}</p>".format(p) for p in get_gemini_response(example_prompt, image).splitlines()])
        magic_response = "<br/>".join(["<p>{}</p>".format(p) for p in get_gemini_response(magic_prompt, image).splitlines()])
        
        st.write(
            "<span style='font-weight:bold'>Image dimensions:</span> {}x{}<br/>".format(image.width, image.height),
            "<span style='font-weight:bold'>Aspect Ratio:</span> {}<br/>".format(image.width / image.height),
            "<span style='font-weight:bold'>Photographic Style:</span> ", ", ".join(photographic_style), "<br/>",
            "<span style='font-weight:bold'>Description Keywords:</span> " + " ".join(set(description_keywords)) + "<br/>",
            "<span style='font-weight:bold'>Action:</span> ", action, "<br/>",
            "<span style='font-weight:bold'>Object:</span> ", object, "<br/>",
            "<span style='font-weight:bold'>Image Description:</span><br/>",
            "<div class='st-magic-response'>{}</div>".format(example_response),
            "<span style='font-weight:bold'>Magic Prompt:</span><br/>",
            "<div class='st-magic-response'>{}</div>".format(magic_response),
            unsafe_allow_html=True, 
        )
        
        
        
 # Add the code of streamlit running icons and deploy is not working
      
# Streamlit Running Icons

st.markdown(
    """
    <style>
    .stLoadingIndicator {
        background-image: url('https://raw.githubusercontent.com/streamlit/branding/master/st_logo_loading/st_logo_loading_spinning.svg');
        background-repeat: no-repeat;
        background-size: 30px;
    }
    .stLoadingIndicator.on-hover {
        background-image: url('https://raw.githubusercontent.com/streamlit/branding/master/st_logo_loading/st_logo_loading_hover.svg');
    }
    .stLoadingIndicator.on-click {
        background-image: url('https://raw.githubusercontent.com/streamlit/branding/master/st_logo_loading/st_logo_loading_click.svg');
    }
    </style>
    """,
    unsafe_allow_html=True
)


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
    <a href="https://api.whatsapp.com/send?phone=923114202358"><img src="https://img.shields.io/badge/WhatsApp-Chat%20Me-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/></a>
    <a href="mailto:rasolehri@gmail.com"><img src="https://img.shields.io/badge/Email-Contact%20Me-red?style=for-the-badge&logo=email" alt="Email"/></a>
</div>
"""

# Combine CSS and HTML for the footer
st.markdown(footer_css, unsafe_allow_html=True)
st.markdown(footer_html, unsafe_allow_html=True)



    
    
    
