# 🤖 AI Chatbot

A full-stack AI chatbot application built with **Streamlit**, **FastAPI**, and **Groq LLM**.

The project demonstrates how to build an AI-powered conversational application with a separate frontend, backend API, AI service layer, environment-based configuration, conversation history, and error handling.

---

## 🚀 Features

- 🤖 AI-powered conversational chatbot
- 💬 Chat interface using Streamlit
- ⚡ FastAPI backend
- 🧠 Conversation history
- 🔄 Context-aware conversations
- 🗑️ Clear chat functionality
- ⏳ AI response loading indicator
- 🛡️ Backend connection error handling
- ⏱️ Request timeout handling
- 🔐 Environment variable configuration
- 🔑 Secure Groq API key management
- ❤️ Backend health check endpoint
- 📊 Chat message counter
- 🧩 Separated AI service layer
- 📦 Dependency management with requirements.txt

---

## 🏗️ Project Architecture

```text
User
  │
  ▼
Streamlit Frontend
(frontend/app.py)
  │
  │ HTTP Request
  ▼
FastAPI Backend
(backend/main.py)
  │
  │ get_ai_response()
  ▼
Groq Service Layer
(backend/services/groq_service.py)
  │
  ▼
Groq LLM
  │
  ▼
AI Response
  │
  ▼
Streamlit Frontend 