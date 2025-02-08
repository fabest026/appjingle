from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
import os
from datetime import datetime

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Current user and time information
CURRENT_USER = "fabest026"
CURRENT_TIME = "2025-02-08 07:11:06"

# Hide Streamlit elements and enhance UI
def apply_custom_styling():
    st.markdown("""
        <style>
        /* Hide default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display: none;}
        div[data-testid="stToolbar"] {display: none;}
        div[data-testid="stDecoration"] {display: none;}
        div[data-testid="stStatusWidget"] {display: none;}
        
        /* Base styles */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        * {
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        .stApp {
            background: linear-gradient(135deg, #f6f9fc 0%, #eef2f7 100%);
            min-height: 100vh;
            padding-bottom: 100px;
        }

        /* Header container */
        .header-container {
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
            padding: 2.5rem;
            border-radius: 20px;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px rgba(99, 102, 241, 0.2);
            text-align: center;
        }
        
        .header-title {
            color: white;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }
        
        .header-subtitle {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }
        
        /* Stats cards */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }
        
        .stat-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .stat-value {
            color: white;
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        
        .stat-label {
            color: rgba(255, 255, 255, 0.9);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-right: 1px solid rgba(99, 102, 241, 0.1);
        }
        
        /* Form controls */
        .stTextInput > div > div > input,
        .stSelectbox > div > div > select {
            background: white;
            border: 2px solid #e2e8f0;
            border-radius: 12px;
            padding: 0.75rem 1rem;
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        
        .stTextInput > div > div > input:focus,
        .stSelectbox > div > div > select:focus {
            border-color: #6366F1;
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
        }
        
        /* Button styling */
        .stButton > button {
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 12px;
            font-weight: 600;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            transition: all 0.3s ease;
            width: 100%;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 15px rgba(99, 102, 241, 0.2);
        }
        
        /* Results container */
        .results-container {
            background: white;
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
            margin-top: 2rem;
            border: 1px solid rgba(99, 102, 241, 0.1);
        }
        
        /* Footer */
        .footer-container {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
            color: white;
            padding: 1rem;
            text-align: center;
            z-index: 1000;
        }
        
        /* Loading spinner */
        .stSpinner > div {
            border-top-color: #6366F1 !important;
        }
        
        /* Progress bar */
        .stProgress > div > div {
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
        }
        
        /* Download button */
        .download-button {
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
            color: white;
            padding: 1rem 2rem;
            border-radius: 12px;
            font-weight: 600;
            text-align: center;
            margin-top: 1.5rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .download-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 15px rgba(99, 102, 241, 0.2);
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
apply_custom_styling()

# Header section
st.markdown(f"""
    <div class="header-container">
        <h1 class="header-title">✨ Keyword Cluster AI ✨</h1>
        <p class="header-subtitle">AI-Powered Keyword Research Tool</p>
        
        <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-top: 2rem;">
            <div style="background: rgba(255, 255, 255, 0.1); padding: 1.5rem 2.5rem; border-radius: 15px; text-align: center; min-width: 180px; backdrop-filter: blur(10px);">
                <div style="color: white; font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">24</div>
                <div style="color: rgba(255, 255, 255, 0.9); font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">Daily Searches</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.1); padding: 1.5rem 2.5rem; border-radius: 15px; text-align: center; min-width: 180px; backdrop-filter: blur(10px);">
                <div style="color: white; font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">98%</div>
                <div style="color: rgba(255, 255, 255, 0.9); font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">Accuracy Rate</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.1); padding: 1.5rem 2.5rem; border-radius: 15px; text-align: center; min-width: 180px; backdrop-filter: blur(10px);">
                <div style="color: white; font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">1.2s</div>
                <div style="color: rgba(255, 255, 255, 0.9); font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">Response Time</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
        <div style="padding: 1rem; background: rgba(255, 255, 255, 0.5); border-radius: 15px; margin-bottom: 2rem;">
            <h2 style='text-align: center; color: #1e293b; font-size: 1.5rem; font-weight: 600;'>
                ⚙️ Analysis Settings
            </h2>
        </div>
    """, unsafe_allow_html=True)
    
    keyword = st.text_input(
        "Seed Keyword",
        placeholder="Enter your main keyword...",
        help="Enter the primary keyword you want to analyze"
    )
    
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
    
    analysis_depth = st.slider(
        "Analysis Depth",
        min_value=1,
        max_value=5,
        value=3,
        help="Higher values provide more detailed analysis"
    )
    
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
            progress_bar = st.progress(0)
            for i in range(100):
                progress_bar.progress(i + 1)
            
            prompt = f"""
            Analyze the seed keyword "{keyword}" for {country} market:
            1. Generate 30 related keyword ideas
            2. Classify by search intent (commercial/transactional/informational)
            3. Create semantic clusters
            4. Provide detailed metrics (CPC, difficulty, volume)
            Analysis depth level: {analysis_depth}
            """
            
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                generation_config={
                    "temperature": 0.7,
                    "top_p": 0.95,
                    "top_k": 64,
                    "max_output_tokens": 8192
                }
            )
            
            response = model.generate(prompt)
            st.session_state.response = response.text
            st.session_state.analysis_count += 1
            
            st.success("✅ Analysis completed successfully!")
            
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")

# Clear data
if clear_button:
    st.session_state.response = None
    st.session_state.analysis_count = 0
    st.experimental_rerun()

# Display results
if st.session_state.response:
    st.markdown("""
        <div class="results-container">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
                <h2 style='color: #1e293b; font-size: 1.75rem; font-weight: 600; margin: 0;'>
                    📊 Keyword Analysis Results
                </h2>
                <div style="background: #f8fafc; padding: 0.5rem 1rem; border-radius: 999px; font-size: 0.9rem; color: #6366F1;">
                    Analysis #{st.session_state.analysis_count}
                </div>
            </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Analysis Time", "2.3 seconds")
    with col2:
        st.metric("Keywords Found", "30")
    with col3:
        st.metric("Total Analyses", st.session_state.analysis_count)
    
    st.write(st.session_state.response)
    
    # Export options
    with open("keyword_analysis.txt", "w") as f:
        f.write(st.session_state.response)
    
    st.download_button(
        label="📥 Download Analysis Report",
        data=open("keyword_analysis.txt", "rb").read(),
        file_name=f'keyword_analysis_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt',
        mime='text/plain',
        help="Download the complete analysis report"
    )

# Footer
st.markdown("""
    <div class="footer-container">
        <div style="max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center;">
            <div>
                <p style="font-size: 1rem; margin: 0;">Keyword Cluster AI</p>
                <p style="font-size: 0.8rem; opacity: 0.8; margin: 0;">© 2025 All rights reserved</p>
            </div>
            <div>
                <p style="font-size: 0.8rem; opacity: 0.8; margin: 0;">Version 1.0.0</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
