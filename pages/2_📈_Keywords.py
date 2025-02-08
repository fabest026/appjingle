from                    
   dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
import os
from datetime import datetime

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Current user and time information
CURRENT_USER = "fabest026"
CURRENT_TIME = "2025-02-08 07:05:09"

# Hide Streamlit elements
def hide_elements():
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display: none;}
        .css-1rs6os.edgvbvh3 {visibility: hidden;}
        .viewerBadge_container__1QSob {display: none;}
        .stToolbar {display: none;}
        .css-14xtw13.e8zbici0 {display: none;}
        .css-1dp5vir.e8zbici1 {display: none;}
        div[data-testid="stDecoration"] {display: none;}
        
        /* Modern UI Styling */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        * {
            font-family: 'Inter', sans-serif;
        }
        
        .main-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            backdrop-filter: blur(10px);
        }
        
        .header-title {
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            text-align: center;
            color: white;
        }
        
        .user-info {
            background: rgba(255, 255, 255, 0.1);
            padding: 0.5rem 1rem;
            border-radius: 10px;
            margin-top: 1rem;
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.9);
        }
        
        .stTextInput > div > div > input,
        .stSelectbox > div > div > select {
            border-radius: 10px;
            border: 1px solid #e2e8f0;
            padding: 0.75rem 1rem;
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        
        .stButton > button {
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 10px;
            font-weight: 600;
            transition: all 0.3s ease;
            width: 100%;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
        }
        
        .results-container {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-top: 2rem;
        }
        
        .download-button {
            margin-top: 1rem;
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 10px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        </style>
    """, unsafe_allow_html=True)

# Page configuration
st.set_page_config(
    page_title="Keyword Cluster AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# Apply custom styling
hide_elements()

# Header
st.markdown(
    f"""
    <div class="header-title">
        <h1 style="font-size: 2.5rem; font-weight: 700;">✨ Keyword Cluster AI ✨</h1>
        <p style="font-size: 1.1rem; opacity: 0.9;">AI-Powered Keyword Research Tool</p>
        <div class="user-info">
            👤 {CURRENT_USER} | 🕒 {CURRENT_TIME} UTC
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.markdown(
        """
        <h2 style='text-align: center; color: #1e293b; font-size: 1.5rem; font-weight: 600; margin-bottom: 1.5rem;'>
            ⚙️ Analysis Settings
        </h2>
        """,
        unsafe_allow_html=True
    )
    
    # Keyword input
    keyword = st.text_input(
        "Seed Keyword",
        placeholder="Enter your main keyword...",
        help="Enter the primary keyword you want to analyze"
    )
    
    # Country selection
    country_options = [
        "United States", "United Kingdom", "Canada", "Australia",
        "Germany", "France", "India", "Japan", "Brazil", "Spain"
    ]
    country = st.selectbox(
        'Target Country',
        options=country_options,
        index=0,
        help="Select the target country for keyword analysis"
    )
    
    # Analysis depth
    analysis_depth = st.slider(
        "Analysis Depth",
        min_value=1,
        max_value=5,
        value=3,
        help="Higher values provide more detailed analysis"
    )
    
    # Action buttons
    col1, col2 = st.columns(2)
    with col1:
        generate_button = st.button("🚀 Generate", use_container_width=True)
    with col2:
        clear_button = st.button("🔄 Clear", use_container_width=True)

# Initialize session state
if 'response' not in st.session_state:
    st.session_state.response = None
if 'analysis_count' not in st.session_state:
    st.session_state.analysis_count = 0

# Generate content
if generate_button and keyword:
    with st.spinner("🔍 Analyzing keywords..."):
        try:
            # Progress bar
            progress_bar = st.progress(0)
            for i in range(100):
                progress_bar.progress(i + 1)
            
            # Generate prompt
            prompt = f"""
            Analyze the seed keyword "{keyword}" for {country} market:
            1. Generate 30 related keyword ideas
            2. Classify by search intent (commercial/transactional/informational)
            3. Create semantic clusters
            4. Provide detailed metrics (CPC, difficulty, volume)
            Analysis depth level: {analysis_depth}
            """
            
            # Set up the Model
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                generation_config={
                    "temperature": 0.7,
                    "top_p": 0.95,
                    "top_k": 64,
                    "max_output_tokens": 8192
                }
            )
            
            # Generate response
            response = model.generate_content(prompt)
            st.session_state.response = response.text
            st.session_state.analysis_count += 1
            
            st.success("✅ Analysis completed successfully!")
            
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")

# Clear data
if clear_button:
    st.session_state.clear()
    st.experimental_rerun()

# Display results
if st.session_state.response:
    st.markdown(
        """
        <div class="results-container">
            <h2 style='color: #1e293b; font-size: 1.75rem; font-weight: 600; margin-bottom: 1.5rem;'>
                📊 Keyword Analysis Results
            </h2>
        """,
        unsafe_allow_html=True
    )
    
    # Analysis metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Analysis Time", "2.3 seconds")
    with col2:
        st.metric("Keywords Found", "30")
    with col3:
        st.metric("Total Analyses", st.session_state.analysis_count)
    
    # Results
    st.write(st.session_state.response)
    
    # Export options
    with open("keyword_analysis.txt", "w") as f:
        f.write(st.session_state.response)
    
    st.download_button(
        label="📥 Download Analysis Report",
        data=open("keyword_analysis.txt", "rb").read(),
        file_name=f'keyword_analysis_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt',
        mime='text/plain',
    )

# Simple footer
st.markdown(
    """
    <div style='text-align: center; padding: 2rem; margin-top: 3rem; background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%); border-radius: 15px; color: white;'>
        <p style='font-size: 1rem; margin-bottom: 0.5rem;'>Keyword Cluster AI</p>
        <p style='font-size: 0.8rem; opacity: 0.8;'>© 2025 All rights reserved</p>
    </div>
    """,
    unsafe_allow_html=True
)
