import streamlit as st

from src.chatbot import FAQChatbot


# Page configuration
st.set_page_config(
    page_title="E-Commerce FAQ Chatbot",
    page_icon="💬"
)


# Page title
st.title("💬 E-Commerce FAQ Chatbot")
st.write("Ask me anything about online shopping.")


# Load chatbot
chatbot = FAQChatbot("data/faqs.csv")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat input
question = st.chat_input("Type your question...")


# Process question
if question:

    # Display user message
    with st.chat_message("user"):
        st.write(question)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    # Get chatbot response
    answer, score = chatbot.get_response(question)

    # Display chatbot response
    with st.chat_message("assistant"):
        st.write(answer)

    # Save chatbot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })