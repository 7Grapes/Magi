import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

print("hello world")
print(f"Your API key is: {api_key}")