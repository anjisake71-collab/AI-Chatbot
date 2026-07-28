from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

app = FastAPI()

groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


class ChatRequest(BaseModel):
    message: str
    history: list = [] 


@app.get("/")
def home():
    return {"message": "AI Chatbot Backend is Running!"}


@app.post("/chat")
def chat(request: ChatRequest):

    response = groq_client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Explain concepts clearly and simply. Assume the user is a beginner and provide step-by-step explanations when needed."
        },
        *request.history,
        {
            "role": "user",
            "content": request.message
        }
    ]
)

    return {
        "response": response.choices[0].message.content
    }   