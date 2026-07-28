import streamlit as st
import requests


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.title("🤖 AI Chatbot")

    st.write(
        "Welcome to your AI assistant. "
        "Ask questions and have a conversation."
    )

    st.divider()

    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = []

        st.rerun()

    st.divider()

    st.subheader("📊 Chat Information")

    # Create message count
    message_count = len(st.session_state.get("messages", []))

    st.write(
        f"Messages in conversation: {message_count}"
    )

    st.divider()

    st.caption(
        "Built with Streamlit + FastAPI + Groq"
    )


# -----------------------------
# Main Page
# -----------------------------

st.title("🤖 AI Chatbot")

st.write(
    "Chat with your AI assistant!"
)


# -----------------------------
# Create Chat History
# -----------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# -----------------------------
# Display Previous Messages
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# -----------------------------
# Chat Input
# -----------------------------

user_message = st.chat_input(
    "Type your message here..."
)


# -----------------------------
# Process User Message
# -----------------------------

if user_message:

    # Display user's message
    with st.chat_message("user"):

        st.markdown(user_message)


    # Copy previous conversation history
    conversation_history = (
        st.session_state.messages.copy()
    )


    # Show AI thinking indicator
    with st.spinner("🤖 AI is thinking..."):

        try:

            # Send request to FastAPI
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


    # Save user's message
    st.session_state.messages.append({

        "role": "user",

        "content": user_message

    })


    # -----------------------------
    # Handle AI Response
    # -----------------------------

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

            f"❌ Backend error. "
            f"Status code: {response.status_code}"

        ) 