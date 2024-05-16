
#this code is a test (not main)

import streamlit as st
from googletrans import Translator

# Set page layout and add some CSS styling
st.markdown(
    """
    <style>
        .st-title {
            font-size: 40px;
            text-align: center;
            color: #333333;
            padding: 20px 0;
        }
        .stButton button {
            font-size: 18px;
        }
        .stText textarea {
            font-size: 18px;
            border-color: #333333;
        }
        .stText select {
            font-size: 18px;
        }
        .instructions {
            font-size: 16px;
            color: #555555;
            margin-top: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the title
st.title("Language Translation Chatbot")

# Get user input
text_input = st.text_area("Enter text to translate:")

# Define language options
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese (Simplified)": "zh-CN",
}

# Create a translator object
translator = Translator()

# Translate text
if st.button("Translate"):
    target_language = st.selectbox("Select target language:", list(languages.keys()))
    target_code = languages[target_language]
    try:
        translated_text = translator.translate(text_input, dest=target_code)
        st.write(f"Original Text: {text_input}")
        st.write(f"Translated Text: {translated_text.text}")
    except Exception as e:
        st.error("An error occurred. Please check your input and try again.")

# Provide instructions
st.sidebar.markdown("## Instructions")
st.sidebar.markdown("1. Enter the text you want to translate in the text area.")
st.sidebar.markdown("2. Select the target language from the dropdown menu.")
st.sidebar.markdown("3. Click the 'Translate' button to see the translation.")

# Supported Languages
st.sidebar.markdown("## Supported Languages")
for lang, code in languages.items():
    st.sidebar.markdown(f"- {lang} ({code})")
