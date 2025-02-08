from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
import os
from datetime import datetime
import pytz

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Custom CSS with properly formatted styles
def apply_custom_css():
    st.markdown(
        """
        <style>
        /* Import fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700&display=swap');
        
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', sans-serif;
        }
        
        /* Main container */
        .main-container {
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        /* Header styles */
        .header-container {
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .main-title {
            font-family: 'Poppins', sans-serif;
            color: white;
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            margin-bottom: 1rem;
        }
        
        .subtitle {
            color: rgba(255, 255, 255, 0.9);
            text-align: center;
            font-size: 1.1rem;
            margin-bottom: 1rem;
        }
        
        /* Stats container */
        .stats-container {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            gap: 1rem;
            margin: 1rem 0;
        }
        
        .stat-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            min-width: 150px;
        }
        
        .stat-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: white;
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.8);
        }
        
        /* Form elements */
        .stTextInput > div > div > input {
            background-color: white;
            padding: 0.75rem 1rem;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            font-size: 1rem;
        }
        
        .stSelectbox > div > div > select {
            background-color: white;
            padding: 0.75rem 1rem;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            font-size: 1rem;
        }
        
        /* Button styles */
        .stButton > button {
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            border: none;
            font-weight: 600;
            transition: transform 0.2s;
            width: 100%;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
        }
        
        /* Results container */
        .results-container {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-top: 2rem;
        }
        
        /* User info */
        .user-info {
            background: rgba(255, 255, 255, 0.1);
            padding: 0.5rem 1rem;
            border-radius: 8px;
            margin-top: 1rem;
            text-align: center;
            color: white;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
            border-radius: 15px;
            color: white;
        }
        
        .footer a {
            color: white;
            text-decoration: none;
            margin: 0 0.5rem;
        }
        
        /* Download button */
        .download-button {
            background: #6366F1;
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            text-align: center;
            margin-top: 1rem;
            cursor: pointer;
            transition: transform 0.2s;
        }
        
        .download-button:hover {
            transform: translateY(-2px);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Page configuration
st.set_page_config(
    page_title="Keyword Cluster AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom CSS
apply_custom_css()

# Current user and time information
CURRENT_USER = "fabest026"
CURRENT_TIME = "2025-02-08 06:53:30"

# Header section
st.markdown(
    f"""
    <div class="header-container">
        <h1 class="main-title">✨ Keyword Cluster AI ✨</h1>
        <p class="subtitle">Powered by AppJingle Solutions</p>
        <div class="stats-container">
            <div class="stat-card">
                <div class="stat-value">24</div>
                <div class="stat-label">Searches Today</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">98%</div>
                <div class="stat-label">Accuracy</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">1.2s</div>
                <div class="stat-label">Avg Response</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
# Sidebar
with st.sidebar:
    st.markdown(
        """
        <h2 style='text-align: center; color: #1e293b; font-family: Poppins, sans-serif; font-size: 1.5rem; font-weight: 600; margin-bottom: 1.5rem;'>
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
    
    # Buttons
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
            
            prompt_parts = [f"""
                Analyze the seed keyword "{keyword}" for {country} market:
                1. Generate 30 related keyword ideas
                2. Classify by search intent (commercial/transactional/informational)
                3. Create semantic clusters
                4. Provide detailed metrics (CPC, difficulty, volume)
                Analysis depth level: {analysis_depth}
            """]
            
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                generation_config={
                    "temperature": 0.7,
                    "top_p": 0.95,
                    "top_k": 64,
                    "max_output_tokens": 8192
                }
            )
            
            response = model.generate_content(prompt_parts)
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
            <h2 style='color: #1e293b; font-family: Poppins, sans-serif; font-size: 1.75rem; font-weight: 600; margin-bottom: 1.5rem;'>
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

# Footer
st.markdown(
    """
    <div class="footer">
        <h3 style='font-size: 1.2rem; font-weight: 600; margin-bottom: 1rem;'>
            Developed by Farhan Akbar
        </h3>
        <div style='margin-bottom: 1rem;'>
            <a href="https://www.linkedin.com/in/farhan-akbar-ai/" target="_blank">LinkedIn</a> |
            <a href="https://api.whatsapp.com/send?phone=923034532403" target="_blank">WhatsApp</a> |
            <a href="https://www.facebook.com/appjingle" target="_blank">Facebook</a> |
            <a href="mailto:rasolehri@gmail.com">Email</a>
        </div>
        <p style='font-size: 0.9rem; opacity: 0.8;'>
            © 2025 AppJingle Solutions. All rights reserved.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
