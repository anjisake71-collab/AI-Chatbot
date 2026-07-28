import streamlit as st
import requests

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI Chatbot")
st.write("Chat with your AI assistant!")


# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
user_message = st.chat_input("Type your message here...")


if user_message:

    # Display user's message
    with st.chat_message("user"):
        st.markdown(user_message)

    # Copy previous conversation history
    conversation_history = st.session_state.messages.copy()

    # Show AI thinking indicator while waiting for backend
    with st.spinner("🤖 AI is thinking..."):

        try:

            # Send message and previous history to FastAPI backend
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={
                    "message": user_message,
                    "history": conversation_history
                },
                timeout=60
            )

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Could not connect to the AI backend. "
                "Please make sure FastAPI is running."
            )

            st.stop()

        except requests.exceptions.Timeout:

            st.error(
                "⏳ The AI took too long to respond. "
                "Please try again."
            )

            st.stop()


    # Save user's message after sending it
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })


    # Get AI response
    if response.status_code == 200:

        ai_response = response.json()["response"]

        # Display AI response
        with st.chat_message("assistant"):
            st.markdown(ai_response)

        # Save AI response
        st.session_state.messages.append({
            "role": "assistant",
            "content": ai_response
        })

    else:

        st.error(
            f"❌ Backend error. Status code: {response.status_code}"
        ) 