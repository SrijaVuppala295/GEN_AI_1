import streamlit as st
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_mistralai import ChatMistralAI

# 1. Load API keys
load_dotenv()

# Verify API key exists
if not os.getenv("MISTRAL_API_KEY"):
    st.error("MISTRAL_API_KEY not found! Please check your .env file.")
    st.stop()

# 2. Set up the Streamlit Page
st.set_page_config(page_title="Mistral Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")
st.caption("Powered by LangChain & Streamlit")

# 3. Initialize Model (Using cache so we don't recreate it on every click)
@st.cache_resource
def get_model():
    return ChatMistralAI(model="mistral-large-latest")

model = get_model()

# 4. Initialize Memory in Session State
# This is CRUCIAL. It stops the memory from wiping when the page refreshes.
if "memory" not in st.session_state:
    st.session_state.memory = InMemoryChatMessageHistory()

# 5. Display existing chat history on the screen
for msg in st.session_state.memory.messages:
    # Check if the message is from the user or the AI
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(msg.content)

# 6. Chat Input box at the bottom of the screen
if user_input := st.chat_input("What's on your mind?"):
    
    # Immediately display the user's message on screen
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Save user message to LangChain memory
    st.session_state.memory.add_message(HumanMessage(content=user_input))
    
    # Generate and display AI response
    with st.chat_message("assistant"):
        with st.spinner("AI is thinking..."):
            # Pass the entire memory history to the model
            response = model.invoke(st.session_state.memory.messages)
            st.markdown(response.content)
            
    # Save AI response to LangChain memory
    st.session_state.memory.add_message(AIMessage(content=response.content))