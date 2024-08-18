import streamlit as st
import torch 
from diffusers import FluxPipeline
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the pipeline
pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-schnell", torch_dtype=torch.bfloat16)

# Enable model CPU offload to save GPU memory
pipe.enable_model_cpu_offload()

# Sidebar for user input
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

    # Text/Paragraph Input
    input_text = st.text_input("Text/Paragraph")

# If user has input text, generate image
if input_text:
    prompt = f"{input_text}"
    image = pipe(
        prompt,
        guidance_scale=0.0,
        num_inference_steps=4,
        max_sequence_length=256,
        generator=torch.Generator("cpu").manual_seed(0)
    ).images[0]
    
    # Save and display the image
    image.save("flux-schnell.png")
    st.image("flux-schnell.png", caption="Generated Image")

# Error handling
try:
    # Generate and display the image
    image = pipe(
        prompt,
        guidance_scale=0.0,
        num_inference_steps=4,
        max_sequence_length=256,
        generator=torch.Generator("cpu").manual_seed(0)
    ).images[0]
    
    # Save and display the image
    image.save("flux-schnell.png")
    st.image("flux-schnell.png", caption="Generated Image")
    
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
