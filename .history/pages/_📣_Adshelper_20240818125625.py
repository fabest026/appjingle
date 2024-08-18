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
    page_title="Campaign Helper"                    
  ,
    page_icon="📣"                    
                      
                                    
                      
  ,
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Add the Title
st.markdown(
    "<h1 style='text-align: center; color: black;'>"
    "📣Social Media Campaign Helper"                    
                                                                                            
    "</h1>",
    unsafe_allow_html=True
)
                    
  
# create a subheader
st.markdown('''
<style>
h3 {
    font-family: 'Open Sans', sans-serif;
    font-size: 20px;
    line-height: 0px;
    margin-top: 0;
    margin-bottom: 24px;
    text-align: center;
    display: flex;
    justify-content: center;
}
</style>
<h3 style="text-align: center; color: black; font-weight: 300; font-style: italic;">✨ Powered by: AppJingle Services ✨</h3>                                                                                                                                                                                                                                                                                        
  
  
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
    st.markdown("<h4>Enter Details: </h4>", unsafe_allow_html=True)
    
    # Section Heading
    section_heading = st.text_input("Product")
    
    # Subpoints
    
    #subpoints = st.text_area("Subpoints (comma-separated)")
    
    # Add the Voice Tones
    #voice_tones = st.sidebar.selectbox("Meta Tones:", ["Formal", "Informal", "Friendly", "Bold", "Adventurous", "Witty", "Professional", "Casual", "Informative", "Creative", "Trendy", "Caring", "Cheerful", "Excited", "Funny", "Sad", "Serious", "Tense", "Vulnerable", "Angry", "Surprised", "Worried", "Assertive", "Confident", "Cooperative", "Encouraging" ])
    
    # Add the Writing Styles
    #writing_styles = st.sidebar.selectbox("Choose Writing Styles:", ["Academic", "Conversational", "Creative", "Critical", "Descriptive", "Instructive", "Technical", "Analytical","Business", "Causal", "Emotional", "Expository", "Formal", "Informal", "Legal", "Medical", "Poetic", "Persuasive"])
    
    # Audience
    #audience = st.selectbox("Audience: Who is the target audience?", ["Teenager", "Adult", "20-years-old", "30-years-old",  "40-years-old", "50-years-old", "Senior", "Everyone", "Uninformed Audience", "Neutral Audience", "Business Audience", "Researcher", "Expert Audience", "My Boss", "My Student", "My Teacher", "My Family", "My Friends", "My Colleagues"] )
    
    # Country
    country_options = [
        "United States", "Canada", "United Kingdom", "Australia", 
        "Germany", "France", "India", "Pakistan", "UAE", "Nepal", "Sri Lanka", 
        "Indonesia", "Philippines", "Vietnam", "Nigeria", "Brazil", "Russia", 
        "China", "Japan", "South Korea", "South Africa", "Spain", "Italy", 
        "Turkey", "Netherlands", "Belgium", "Sweden", "Switzerland", 
        "New Zealand", "Singapore", "Malaysia"
    ]
    country = st.selectbox('Country', country_options)
    #num_words = st.number_input("Number of words", min_value=250, max_value=3000, step=50)

    # Primary Keyword
    #primary_keyword = st.text_input("Primary Keyword ")
    
    # Secondary Keyword
    #secondary_keyword = st.text_input("Secondary Keyword")
    
    # Reference Article Link
    # reference_article_link = st.text_input("Reference Article Link")

    # Prompt
    prompt_parts = [
            f"""
            All text should be in English which is English. Please Write in English. {section_heading} - {country}
            - Important Note: At the end must provide label "The ad sets provided above are based on the latest data available as of date 01-11-2023, sourced from updated ad libraries, website analyses, and machine learning algorithms. "
            - I want you to act as a marketing specialist and ad expert to create a comprehensive ad campaign for the provided product or service and target location. Please follow the instructions below:
            - Input the product name and location country provided by the user.
            - Analyze the ad libraries to identify the best-performing ad sets for the target audience based on factors such as ad type, format, placement, and copy.
            - Use natural language processing to identify the key characteristics of the target audience, including age, gender, demographics, interests, and location.
            - Provide the following target audience sets for the ad campaign:
                - Age Limit sets
                - Gender Sets
                - Demographics
                - Interests
                - Specific Time Period ad should run or not run on (if applicable)
                - Locations (cities wise) to create the target audience for the ad campaign.
                - People in the location country who have recently searched for the product name (search engine data)
                - People in the location country who have recently visited websites of competitors of the product name (competitor website data)
                - People in the location country who have recently made a purchase on an ecommerce website related to the product name (ecommerce website data)
                - People in the location country who have shown interest in similar products to the product name (online forum or community data)
            - Incorporate behavioral data and psychographic information to enhance audience targeting, considering factors like lifestyle, values, attitudes, and personality traits.
            - Analyze social media data to identify key influencers and trendsetters within the target location, who can be approached for promotional activities or partnerships.
            - For each target audience set, consider creating personalized ad content and messaging to resonate more effectively with their preferences and needs, improving the chances of engagement and conversion.
            - Perform A/B testing on different ad variations, including headlines, visuals, and calls-to-action, to optimize ad performance and gain insights on what resonates best with each target audience set.
            - Consider incorporating retargeting strategies to re-engage potential customers who have shown interest but have not yet converted, using dynamic ads and personalized messaging.
            - Recommend two daily ad budgets and durations, one with the name "For Small Business" (should be equals to or lower than 10$(provide in local currencies)) and the other with the name "For Brands," based on historical ad performance data, target audience characteristics, and campaign goals.
            - Use historical performance data and machine learning algorithms to estimate the optimal ad duration for the campaign to achieve the desired results.
            - Use machine learning algorithms to recommend the best time period for running the ads based on target audience behavior and preferences.
                - This can include factors such as days of the week, times of day, and time zones.
            - Provide more than one ad set if possible.
            - For each ad set, specify the ad placement platform (e.g. Facebook Ads , Instagram Ads, Tiktok Ads) based on the most relevant platform for the target audience identified.
            - Consider utilizing programmatic advertising and real-time bidding to optimize ad placements and reach the right audience segments more efficiently.
            - For each ad set, also include ad formats (e.g., image, video, carousel, story, collection) best suited for the respective ad placement platform and target audience preferences.
            - Monitor ad performance and engagement metrics regularly, adjusting campaign strategies and ad sets as needed to improve overall results.
            - Output the four ad sets with their respective target audiences and ad placement platforms, along with recommendations for the target audience, daily ad budgets with two labels; First Label "For Small Business:" (should be equals to or lower than 10$(provide in local currencies)) and with Second Label "For Brands:" (i.e high budgets etc), optimal ad duration, and time period for running the ads.
            - Must provide Ads Budget in the local currency according to the provided area, location or country.
            - Remember to include tracking and conversion pixels in the ad campaign to measure performance and ROI accurately.
            - After completing this task now I want you to act as a professional copywriter with experience in writing high-converting Facebook ads.
            - The ad copy should be written in fluent English and should be between 100-150 words long.
            - I want you to write a Facebook ad copy for a product/service that I will provide as the following {section_heading}, using the following guidelines:
                - Create a compelling headline under 30 charaters that grabs attention and highlights the main benefit of the product/service
                - Use clear and concise language in the body copy that focuses on the benefits of the product/service and addresses any potential objections
                - Include the description of 50 charaters highlights the main benefit of the product/service
                - Include a strong call to action that encourages users to take the desired action
                - Use an image or video that visually demonstrates the product/service and resonates with the target audience
                - Research the target audience demographics, such as age, gender, location, interests, and other characteristics that would help you to have a better understanding of the target audience, and create an ad that would be more appealing to them.
                - Finally, please include the label " The ad sets provided above are based on the latest data available as of date [current date minus 2/3/5 days], sourced from updated ad libraries, website analyses, and machine learning algorithms. Please ensure that the ad sets are precise and comprehensive, with a focus on detailed aspects. Do not echo the prompts or provide unnecessary information. Stick to the main points and provide data in a complete format. Don't provide any extra text or sentence other than Ad sets.
            ]

    # Submit Button
    submit_button = st.button("Generate")

if submit_button:
    # Display the spinner
    with st.spinner("Generating...."):
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
    <a href="https://api.whatsapp.com/send?phone=923114202358"><img src="https://img.shields.io/badge/WhatsApp-Chat%20Me-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/></a>
    <a href="mailto:rasolehri@gmail.com"><img src="https://img.shields.io/badge/Email-Contact%20Me-red?style=for-the-badge&logo=email" alt="Email"/></a>
</div>
"""

# Combine CSS and HTML for the footer
st.markdown(footer_css, unsafe_allow_html=True)
st.markdown(footer_html, unsafe_allow_html=True)




      
        
        

        
