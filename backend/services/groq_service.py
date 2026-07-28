from groq import Groq

from backend.config import GROQ_API_KEY, MODEL_NAME


# Create Groq client
groq_client = Groq(
    api_key=GROQ_API_KEY
)


def get_ai_response(message: str, history: list):

    response = groq_client.chat.completions.create(
        model=MODEL_NAME,
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