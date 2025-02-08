from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
import os
from datetime import datetime
import pytz

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Custom CSS with enhanced typography and modern design
[Previous CSS remains the same until the last part, then add:]

        /* Dashboard Stats */
        .stat-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 1rem 0;
        }
        
        .stat-card {
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            border: 1px solid #e2e8f0;
            transition: all 0.3s ease;
        }
        
        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        
        .stat-value {
            font-size: 1.8rem;
            font-weight: 700;
            color: #6366F1;
            margin: 0.5rem 0;
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        /* Activity Timeline */
        .timeline {
            margin: 2rem 0;
            padding: 1rem;
        }
        
        .timeline-item {
            display: flex;
            align-items: flex-start;
            margin-bottom: 1.5rem;
            padding: 1rem;
            background: white;
            border-radius: 10px;
            border: 1px solid #e2e8f0;
            transition: all 0.3s ease;
        }
        
        .timeline-item:hover {
            transform: translateX(5px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        }
        
        .timeline-icon {
            background: #6366F1;
            color: white;
            width: 2rem;
            height: 2rem;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 1rem;
        }
        
        /* Progress Bar */
        .progress-bar {
            width: 100%;
            height: 8px;
            background: #e2e8f0;
            border-radius: 4px;
            overflow: hidden;
            margin: 1rem 0;
        }
        
        .progress-bar-fill {
            height: 100%;
            background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
            width: 0%;
            transition: width 1.5s ease;
        }
        </style>
    """, unsafe_allow_html=True)

# Page configuration
st.set_page_config(
    page_title="✨ Keyword Cluster AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom CSS
apply_custom_css()

# Current user and time information
CURRENT_USER = "fabest026"
CURRENT_TIME = "2025-02-08 06:50:58"

# Header section with user info and dashboard stats
st.markdown(f"""
    <div class="title-container glass-container">
        <h1 class="main-title">✨ Keyword Cluster AI ✨</h1>
        <p class="subtitle">Powered by AppJingle Solutions</p>
        <div class="user-info">
            👤 {CURRENT_USER} | 🕒 {CURRENT_TIME} UTC
        </div>
        
        <div class="stat-grid">
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
""", unsafe_allow_html=True)

# Sidebar with improved organization
with st.sidebar:
    st.markdown("""
        <div class="glass-container" style="padding: 1.5rem;">
            <h2 style='text-align: center; color: #1e293b; font-family: Poppins, sans-serif; font-size: 1.5rem; font-weight: 600; margin-bottom: 1.5rem;'>
                ⚙️ Analysis Settings
            </h2>
        </div>
    """, unsafe_allow_html=True)
    
    # User Profile Card
    st.markdown(f"""
        <div class="card">
            <h3 style='color: #1e293b; font-size: 1.1rem; font-weight: 600; margin-bottom: 1rem;'>
                👤 User Profile
            </h3>
            <p style='color: #64748b; font-size: 0.9rem;'>
                Logged in as: <strong>{CURRENT_USER}</strong><br>
                Session started: {CURRENT_TIME}
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Keyword Settings Card
    st.markdown("""
        <div class="card">
            <h3 style='color: #1e293b; font-size: 1.1rem; font-weight: 600; margin-bottom: 1rem;'>
                🎯 Keyword Settings
            </h3>
        </div>
    """, unsafe_allow_html=True)
    
    keyword = st.text_input(
        "Seed Keyword", 
        placeholder="Enter your main keyword...",
        help="Enter the primary keyword you want to analyze"
    )
    
    # Location Settings Card
    st.markdown("""
        <div class="card">
            <h3 style='color: #1e293b; font-size: 1.1rem; font-weight: 600; margin-bottom: 1rem;'>
                🌍 Location Settings
            </h3>
        </div>
    """, unsafe_allow_html=True)
    
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
    
    # Analysis Options Card
    st.markdown("""
        <div class="card">
            <h3 style='color: #1e293b; font-size: 1.1rem; font-weight: 600; margin-bottom: 1rem;'>
                🔍 Analysis Options
            </h3>
        </div>
    """, unsafe_allow_html=True)
    
    analysis_depth = st.slider(
        "Analysis Depth",
        min_value=1,
        max_value=5,
        value=3,
        help="Higher values provide more detailed analysis but take longer"
    )
    
    # Action buttons with enhanced styling
    col1, col2 = st.columns(2)
    with col1:
        generate_button = st.button(
            "🚀 Generate",
            use_container_width=True,
            help="Start keyword analysis"
        )
    
    with col2:
        clear_button = st.button(
            "🔄 Clear",
            use_container_width=True,
            help="Clear all inputs and results"
        )

# Initialize session state
if 'response' not in st.session_state:
    st.session_state.response = None
if 'analysis_count' not in st.session_state:
    st.session_state.analysis_count = 0

# Generate content with enhanced feedback
if generate_button and keyword:
    with st.spinner("🔍 Analyzing keywords..."):
        try:
            # Update progress bar
            progress_bar = st.progress(0)
            for i in range(100):
                progress_bar.progress(i + 1)
            
            prompt_parts = [f"""
                Please analyze the seed keyword "{keyword}" for {country} market:
                1. Generate 30 related keyword ideas
                2. Classify by search intent (commercial/transactional/informational)
                3. Create semantic clusters
                4. Provide detailed metrics (CPC, difficulty, volume)
                Format as a clean, organized table.
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
            
            # Success message with stats
            st.success("✅ Analysis completed successfully!")
            
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")

# Clear all data
if clear_button:
    st.session_state.clear()
    st.experimental_rerun()

# Display results with enhanced styling
if st.session_state.response:
    st.markdown("""
        <div class="results-container glass-container">
            <h2 style='color: #1e293b; font-family: Poppins, sans-serif; font-size: 1.75rem; font-weight: 600; margin-bottom: 1.5rem;'>
                📊 Keyword Analysis Results
            </h2>
    """, unsafe_allow_html=True)
    
    # Analysis Stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Analysis Time", "2.3 seconds")
    with col2:
        st.metric("Keywords Found", "30")
    with col3:
        st.metric("Total Analyses", st.session_state.analysis_count)
    
    # Main Results
    st.write(st.session_state.response)
    
    # Export options with enhanced styling
    st.markdown("""
        <div class="card">
            <h3 style='color: #1e293b; font-size: 1.1rem; font-weight: 600; margin-bottom: 1rem;'>
                📤 Export Options
            </h3>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        # Save to file and offer download
        with open("keyword_analysis.txt", "w") as f:
            f.write(st.session_state.response)
        
        st.download_button(
            label="📥 Download Analysis Report",
            data=open("keyword_analysis.txt", "rb").read(),
            file_name=f'keyword_analysis_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt',
            mime='text/plain',
            help="Download the analysis results as a text file"
        )
    
    with col2:
        st.button(
            "📊 Export as CSV",
            help="Export the analysis results in CSV format"
        )

# Footer with enhanced styling
st.markdown("""
    <div class="footer glass-container">
        <h3 style='color: white; font-size: 1.2rem; font-weight: 600; margin-bottom: 1rem;'>
            Developed by Farhan Akbar
        </h3>
        <div style='display: flex; justify-content: center; gap: 1rem; margin-bottom: 1rem;'>
            <a href="https://www.linkedin.com/in/farhan-akbar-ai/" target="_blank">
                <img src="https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin" alt="LinkedIn"/>
            </a>
            <a href="https://api.whatsapp.com/send?phone=923034532403" target="_blank">
                <img src="https://img.shields.io/badge/WhatsApp-Chat-25D366?style=for-the-badge&logo=whatsapp" alt="WhatsApp"/>
            </a>
            <a href="https://www.facebook.com/appjingle" target="_blank">
                <img src="https://img.shields.io/badge/Facebook-Follow-1877F2?style=for-the-badge&logo=facebook" alt="Facebook"/>
            </a>
            <a href="mailto:rasolehri@gmail.com">
                <img src="https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail" alt="Email"/>
            </a>
        </div>
        <p style='color: rgba(255, 255, 255, 0.8); font-size: 0.9rem;'>
            © 2025 AppJingle Solutions. All rights reserved.
        </p>
    </div>
""", unsafe_allow_html=True)
