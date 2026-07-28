from fastapi import FastAPI
from pydantic import BaseModel

from backend.services.groq_service import get_ai_response


app = FastAPI()


class ChatRequest(BaseModel):
    message: str
    history: list = []


@app.get("/")
def home():
    return {
        "message": "AI Chatbot Backend is Running!"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Chatbot Backend"
    }

@app.post("/chat")
def chat(request: ChatRequest):

    ai_response = get_ai_response(
        message=request.message,
        history=request.history
    )

    return {
        "response": ai_response
    } 