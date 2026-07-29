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
# Backend URL
# -----------------------------

BACKEND_URL = "http://127.0.0.1:8000"


# -----------------------------
# Title
# -----------------------------

st.title("🤖 AI Chatbot")

st.write(
    "Ask questions about the AI knowledge base."
)


# -----------------------------
# Initialize Chat History
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Clear Chat
# -----------------------------

if st.button("🗑️ Clear Chat"):

    st.session_state.messages = []

    st.rerun()


# -----------------------------
# Display Chat History
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# -----------------------------
# User Input
# -----------------------------

user_message = st.chat_input(
    "Ask a question..."
)


# -----------------------------
# Send Message
# -----------------------------

if user_message:

    # Show user message
    with st.chat_message("user"):

        st.markdown(user_message)


    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )


    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = requests.post(
                    f"{BACKEND_URL}/chat",
                    json={
                        "message": user_message,
                        "history": st.session_state.messages
                    },
                    timeout=120
                )


                response.raise_for_status()


                data = response.json()


                # Your backend returns:
                # {"response": ai_response}

                answer = data.get(
                    "response",
                    "No answer was returned."
                )


                # Display AI response
                st.markdown(answer)


                # Save AI response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )


            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Cannot connect to FastAPI backend. "
                    "Please make sure the backend is running."
                )


            except requests.exceptions.Timeout:

                st.error(
                    "⏳ The AI response took too long. "
                    "Please try again."
                )


            except requests.exceptions.HTTPError as e:

                st.error(
                    f"❌ Backend error: {e}"
                )


            except Exception as e:

                st.error(
                    f"❌ Unexpected error: {e}"
                )
                