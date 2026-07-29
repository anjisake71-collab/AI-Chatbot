from groq import Groq

from backend.config import GROQ_API_KEY


client = Groq(
    api_key=GROQ_API_KEY
)


def rewrite_query(
    question: str,
    history: list = None
) -> str:

    if history is None:
        history = []

    # If there is no conversation history,
    # the current question can be used directly.
    if not history:
        return question

    conversation_history = ""

    for message in history:
        role = message.get("role", "")
        content = message.get("content", "")

        conversation_history += (
            f"{role}: {content}\n"
        )

    prompt = f"""
You are a query rewriting assistant.

Rewrite the user's latest question into a clear,
standalone search query.

Use the conversation history to understand
references such as:
- it
- they
- this
- that
- these
- those

Do not answer the question.

Return only the rewritten search query.

Conversation History:
{conversation_history}

Latest User Question:
{question}

Standalone Search Query:
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip() 