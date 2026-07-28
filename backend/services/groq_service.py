from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def get_ai_response(message: str, history: list):

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant. Explain concepts clearly and simply. Assume the user is a beginner and provide step-by-step explanations when needed."
            },
            *history,
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.choices[0].message.content
 