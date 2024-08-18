## loading all the environment variables
from dotenv import load_dotenv
load_dotenv() 

# Import Important libraries
import streamlit as st

import torch
from diffusers import FluxPipeline

pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-schnell", torch_dtype=torch.bfloat16)
pipe.enable_model_cpu_offload() #save some VRAM by offloading the model to CPU. Remove this if you have enough GPU power


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
    st.markdown("<h4>Enter Details for the Rephrasing: </h4>", unsafe_allow_html=True)

    # Blog Title
    text = st.text_area("Text/Paragraph") 

    # Primary Keyword
    #keyword = st.text_input("Keyword")
    
    # Add the Voice Tones
    voice_tones = st.sidebar.selectbox("Choose Voice Tones:", ["Formal", "Informal", "Friendly", "Bold", "Adventurous", "Witty", "Professional", "Casual", "Informative", "Creative", "Trendy", "Caring", "Cheerful", "Excited", "Funny", "Sad", "Serious", "Tense", "Vulnerable", "Angry", "Surprised", "Worried", "Assertive", "Confident", "Cooperative", "Encouraging" ])
    
    # Add the Writing Styles
    writing_styles = st.sidebar.selectbox("Choose Writing Styles:", ["Academic", "Conversational", "Creative", "Critical", "Descriptive", "Instructive", "Technical", "Analytical","Business", "Causal", "Emotional", "Expository", "Formal", "Informal", "Legal", "Medical", "Poetic", "Persuasive"])
    
    # Audience
    audience = st.selectbox("Audience: Who is the target audience?", ["Teenager", "Adult", "20-years-old", "30-years-old",  "40-years-old", "50-years-old", "Senior", "Everyone", "Uninformed Audience", "Neutral Audience", "Business Audience", "Researcher", "Expert Audience", "My Boss", "My Student", "My Teacher", "My Family", "My Friends", "My Colleagues"] )
    
    # Word Counter
    word_count = st.number_input("Word Count", min_value=50, max_value=3000, step=10)

prompt = "A cat holding a sign that says hello world"
image = pipe(
    prompt,
    guidance_scale=0.0,
    num_inference_steps=4,
    max_sequence_length=256,
    generator=torch.Generator("cpu").manual_seed(0)
).images[0]
image.save("flux-schnell.png")
