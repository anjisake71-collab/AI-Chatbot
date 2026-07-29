from fastapi import FastAPI
from pydantic import BaseModel

from backend.services.query_service import rewrite_query
from backend.services.rag_service import retrieve_context
from backend.services.groq_service import generate_rag_response


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

    print("\n========== CHAT START ==========")

    # 1. Receive user message
    print("STEP 1: Received message")
    print("Message:", request.message)

    # 2. Rewrite follow-up question
    print("STEP 2: Starting query rewrite")

    rewritten_query = rewrite_query(
        request.message,
        request.history
    )

    print("STEP 3: Query rewrite completed")
    print("Rewritten query:", rewritten_query)

    # 3. Retrieve relevant information
    print("STEP 4: Starting RAG retrieval")

    context = retrieve_context(
        rewritten_query
    )

    print("STEP 5: RAG retrieval completed")
    print("Retrieved context:")
    print(context)

    # 4. Generate final answer
    print("STEP 6: Starting Groq response generation")

    ai_response = generate_rag_response(
        question=request.message,
        context=context,
        history=request.history
    )

    print("STEP 7: Groq response completed")
    print("AI response:", ai_response)

    print("========== CHAT END ==========\n")

    return {
        "response": ai_response
    } 