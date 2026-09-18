import streamlit as st
from google import genai

# Page settings
st.set_page_config(page_title="Gemini AI Assistant", page_icon="✨", layout="centered")

st.title("✨ Gemini AI Assistant")
st.caption("Powered by Google Gemini & Streamlit")

# Retrieve API key from Streamlit Secrets or let user type it in sidebar
api_key = st.secrets.get("GEMINI_API_KEY", "")

with st.sidebar:
    st.header("⚙️ Configuration")
    if not api_key:
        api_key = st.text_input("Enter Gemini API Key:", type="password")
        st.markdown("[Get a Gemini API Key](https://aistudio.google.com/app/apikey)")
    else:
        st.success("API Key loaded securely!")
    
    model_name = st.selectbox(
        "Choose Gemini Model:",
        ["gemini-2.5-flash", "gemini-2.0-flash"]
    )
    
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Maintain message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User prompt input
if prompt := st.chat_input("Ask Gemini anything..."):
    if not api_key:
        st.warning("Please provide your Gemini API key in the sidebar.")
    else:
        # Display user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Call Gemini API
        client = genai.Client(api_key=api_key)
        
        with st.chat_message("assistant"):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )
                full_text = response.text
                st.markdown(full_text)
                st.session_state.messages.append({"role": "assistant", "content": full_text})
            except Exception as e:
                st.error(f"Error: {e}")