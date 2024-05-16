import streamlit as st
from googletrans import Translator

st.title("Language Translation Chatbot")
st.sidebar.header("User Input")

text_input = st.sidebar.text_area("Enter text to translate:")
target_language = st.sidebar.selectbox("Select target language:", ["en", "es", "fr", "de", "zh-CN", "hi", "bn", "te"])

translator = Translator()

if st.sidebar.button("Translate"):
    try:
        translated_text = translator.translate(text_input, dest=target_language)
        st.write(f"Original Text: {text_input}")
        st.write(f"Translated Text: {translated_text.text}")
    except Exception as e:
        st.error("An error occurred. Please check your input and try again.")

st.sidebar.markdown("---")
st.sidebar.markdown("**Instructions:**")
st.sidebar.markdown("1. Enter the text you want to translate in the text area.")
st.sidebar.markdown("2. Select the target language from the dropdown menu.")
st.sidebar.markdown("3. Click the 'Translate' button to see the translation.")
st.sidebar.markdown("---")
st.sidebar.markdown("**Supported Languages:**")
st.sidebar.markdown("- English (en)")
st.sidebar.markdown("- Spanish (es)")
st.sidebar.markdown("- French (fr)")
st.sidebar.markdown("- German (de)")
st.sidebar.markdown("- Chinese (Simplified) (zh-CN)")
