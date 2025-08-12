import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key (from .env or OS environment variable)
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No OpenAI API key found. Set it in .env or as an environment variable.")

print(f"Your API key starts with: {api_key[:5]}...")
