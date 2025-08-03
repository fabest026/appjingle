## loading all the environment variables
from dotenv import load_dotenv
load_dotenv() 

# Import Important libraries
import streamlit as st
import google.generativeai as genai
import os

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.5-flash-lite", # Updated model name here
  generation_config=generation_config,
)


# Navbar
st.set_page_config(
    page_title="Ai Detection Remover",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Add the Title
st.markdown(
    "<h1 style='text-align: center; color: black;'>"
    "✨ AI Content Creation Magic 🧙‍♂️"
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
<h3 style="text-align: center; color: black; font-weight: 300; font-style: italic;">🚀 Upgrade Your Content Creation with AI Assistance! 🚀<br>Effortlessly Remove Plagiarism and AI Detected Content!</h3>
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
    st.markdown("<h4>Enter Details for the Rephrasing: </h4>", unsafe_allow_html=True)

    # Blog Title
    text = st.text_area("Text/Paragraph") 

    # Primary Keyword
    #keyword = st.text_input("Keyword")
    
    # Add the Voice Tones
    voice_tones = st.sidebar.selectbox("Choose Voice Tones:", ["Formal", "Informal", "Friendly", "Bold", "Adventurous", "Witty", "Personalized", "Professional", "Casual", "Informative", "Creative", "Trendy", "Caring", "Cheerful", "Excited", "Funny", "Sad", "Serious", "Tense", "Vulnerable", "Angry", "Surprised", "Worried", "Assertive", "Confident", "Cooperative", "Encouraging" ])
    
    # Add the Writing Styles
    writing_styles = st.sidebar.selectbox("Choose Writing Styles:", ["Academic", "Conversational", "Creative", "Critical", "Descriptive", "Instructive", "Technical", "Analytical","Business", "Causal", "Emotional", "Expository", "Formal", "Informal", "Legal", "Medical", "Poetic", "Persuasive"])
    
    # Audience
    audience = st.selectbox("Audience: Who is the target audience?", ["Teenager", "Adult", "20-years-old", "30-years-old",  "40-years-old", "50-years-old", "Senior", "Everyone", "Uninformed Audience", "Neutral Audience", "Business Audience", "Researcher", "Expert Audience", "My Boss", "My Student", "My Teacher", "My Family", "My Friends", "My Colleagues"] )
    
    # Word Counter
    word_count = st.number_input("Word Count", min_value=50, max_value=3000, step=10)
    

    # Prompt
    prompt_parts = [
            f"""
            I want you to respond in the language English. You are an expert copywriter who knows everything about SEO. 

            Follow these instructions:

            1. You can write {voice_tones}, you write in an active voice, you use transition words, you never plagiarize, you can pass AI detection tests for content, and you know how to rank in the first position in search engines. Rewrite the content so it is 100% unique and remove any plagiarism. 
            2. I want you to Rephrasing around {word_count} words on {text} in the english language. Do not use jargon or complex terms. Do not write conclusions or add additional details. Rewrite to the point.     
            3. Targeted audience is {audience}. Don't add the intro and bullets to the article. Write in easy to understand style. Don't use difficult to read and synmonstic language. Write likehood a human writer. 
            4. write in human don't use complex terms like showcase, leverage, delve, craft, dig, dive, tailored etc. write unqiue
            4. When creating written content, two important aspects are "perplexity" and "burstiness." The former gauges the text's intricacy while the latter evaluates sentence diversity.
            5. Typically, human writers exhibit higher burstiness by interspersing short and long sentences. 
            6. In contrast, AI-generated sentences tend to be uniform in length.
            7. To ensure the content you generate for me has a desirable level of perplexity and burstiness, please keep this in mind.  
            8. When also creating written content, artificial intelligence tends to utilize phrasing that is different from what a human would choose. Utilize uncommon terminology to enhance the originality of the piece. 
            9. Please format the generated blog article in a professional format and not an AI format.  
            10. Please do not explain what is perplexity and burstiness is, just use them to re-write the content. Please put this in your mind. 
            11. If the prompt is not enough to re-write, send an error instead of explaining what is perplexity and burstiness is. 
            12. Please mind this. Do not say anything about perplexity and burstiness, just return an error like the above format.  Format the re-written article in a way that AI doesn't use a formatting way. 
            13. These are the settings for your response: Unique Words: Enabled,  Plagiarism: Disabled,  Anti-Plagiarism: Enabled,  Uniqueness: 100%,  Professional Writer: True Pharical Magic: True,   Please use this settings to your response, and the more uniqueness the more you'll re-write the article with unique words. 
            14. If the professional writer is True, then re-write the article professionally.  Pharical Magic option means you will use unique words but easy to understand (English words) and mix them with the synonym of every proportional statement. Or vice-versa. 
            15. And this option makes the rewritten content more engaging and interesting according to the article. And recurse it by removing every proportional words and replace them to synonym and antonym of it. Replace statements to simile too.  
            16. Now, using the concepts above, re-write the content with a high degree of perplexity and burstiness. And please use words that AI doesn't often use  
            17. Do not use very common words that AI often uses. 
            18. Please keep this in your mind. Use words that are not that common, use more unique words. Please mind this. Do not forget this.  
            19. Paraphrase every sentences, paragraph and etc to deep English. Use deep words, and unique words.  Please do not change the subject's name or the X name. 
            20. Humanize AI text by simply follow tha above instrcution to parapharse the AI Text to human likehood written. You will completely remove AI text from given content and maintain the original meaning of the content/text. 
            20. Open up the realm of exquisite watch faces when you access the Watch Face Gallery. It's a treasure trove of designs, from sleek and sophisticated to vibrant and artistic. No matter your style, there's a masterpiece waiting to adorn your wrist.



            """
            ]

    # Submit Button
    submit_button = st.button("Generate")




if submit_button:
    # Display the spinner
    with st.spinner("Thinking..."):
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


