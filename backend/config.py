import os
from dotenv import load_dotenv


# Load variables from .env file
load_dotenv()


# Get Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# Validate Groq API key
if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. "
        "Please add GROQ_API_KEY to your .env file."
    )


# Groq model
MODEL_NAME = "llama-3.1-8b-instant" 