from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
import os

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Custom CSS for better UI
def apply_custom_css():
    st.markdown("""
        <style>
        /* Main container */
        .main {
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        /* Header styling */
        .title-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .main-title {
            color: white !important;
            font-size: 2.5rem !important;
            font-weight: 700 !important;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        
        .subtitle {
            color: rgba(255, 255, 255, 0.9) !important;
            text-align: center;
            font-size: 1.1rem !important;
            font-weight: 400;
        }
        
        /* Sidebar styling */
        .css-1d391kg {
            background-color: #f8f9fa;
            padding: 2rem 1rem;
        }
        
        /* Form elements */
        .stTextInput > div > div > input {
            background-color: white;
            padding: 0.5rem;
            border-radius: 5px;
            border: 1px solid #e0e0e0;
        }
        
        .stSelectbox > div > div > select {
            background-color: white;
            padding: 0.5rem;
            border-radius: 5px;
            border: 1px solid #e0e0e0;
        }
        
        /* Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 0.5rem 2rem;
            border-radius: 5px;
            font-weight: 600;
            width: 100%;
            transition: transform 0.2s;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
        }
        
        /* Results container */
        .results-container {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-top: 2rem;
        }
        
        /* Tables */
        .dataframe {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
        }
        
        .dataframe th {
            background-color: #f8f9fa;
            padding: 0.75rem;
            text-align: left;
            border-bottom: 2px solid #dee2e6;
        }
        
        .dataframe td {
            padding: 0.75rem;
            border-bottom: 1px solid #dee2e6;
        }
        
        /* Footer */
        .footer {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem;
            border-radius: 10px;
            margin-top: 2rem;
            text-align: center;
        }
        
        .footer a {
            color: white;
            text-decoration: none;
            margin: 0 0.5rem;
        }
        
        .footer a:hover {
            text-decoration: underline;
        }
        
        /* Loading spinner */
        .stSpinner > div {
            border-color: #667eea !important;
        }
        </style>
    """, unsafe_allow_html=True)

# Page configuration
st.set_page_config(
    page_title="Keyword Cluster AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom CSS
apply_custom_css()

# Header section
st.markdown("""
    <div class="title-container">
        <h1 class="main-title">✨ Keyword Cluster AI ✨</h1>
        <p class="subtitle">Powered by AppJingle Solutions</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>Input Settings</h2>", unsafe_allow_html=True)
    
    # Input fields with better organization
    with st.expander("Keyword Settings", expanded=True):
        keyword = st.text_input("Seed Keyword", 
                              placeholder="Enter your main keyword here...")
    
    with st.expander("Location Settings", expanded=True):
        country_options = [
            "United States", "United Kingdom", "Canada", "Australia", 
            "Germany", "France", "India", "Japan", "Brazil", "Spain",
            # Add more countries as needed
        ]
        country = st.selectbox('Target Country', 
                             options=country_options,
                             index=0)
    
    # Action buttons
    col1, col2 = st.columns(2)
    with col1:
        generate_button = st.button("🚀 Generate", use_container_width=True)
    with col2:
        clear_button = st.button("🔄 Clear All", use_container_width=True)

# Main content area
if 'response' not in st.session_state:
    st.session_state.response = None

# Generate content
if generate_button and keyword:
    with st.spinner("🔍 Analyzing keywords..."):
        try:
            # Your existing generation logic here
            prompt_parts = [f"""
                Please analyze the seed keyword "{keyword}" for {country} market:
                1. Generate 30 related keyword ideas
                2. Classify by search intent (commercial/transactional/informational)
                3. Create semantic clusters
                4. Provide detailed metrics (CPC, difficulty, volume)
                Format as a clean, organized table.
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
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Clear all data
if clear_button:
    st.session_state.clear()
    st.experimental_rerun()

# Display results
if st.session_state.response:
    st.markdown("<div class='results-container'>", unsafe_allow_html=True)
    st.markdown("### 📊 Keyword Analysis Results")
    st.write(st.session_state.response)
    
    # Export options
    col1, col2 = st.columns(2)
    with col1:
        # Save to file and offer download
        with open("keyword_analysis.txt", "w") as f:
            f.write(st.session_state.response)
        
        st.download_button(
            label="📥 Download Analysis",
            data=open("keyword_analysis.txt", "rb").read(),
            file_name='keyword_analysis.txt',
            mime='text/plain',
        )
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>Developed by Farhan Akbar</p>
        <div>
            <a href="https://www.linkedin.com/in/farhan-akbar-ai/" target="_blank">LinkedIn</a> |
            <a href="https://api.whatsapp.com/send?phone=923034532403" target="_blank">WhatsApp</a> |
            <a href="https://www.facebook.com/appjingle" target="_blank">Facebook</a> |
            <a href="mailto:rasolehri@gmail.com">Email</a>
        </div>
    </div>
""", unsafe_allow_html=True)
