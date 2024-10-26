import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv('config.env')


# Get API keys from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
claudeai_api_key = os.getenv("CLAUDEAI_API_KEY")
googlegemini_api_key = os.getenv("GOOGLEGEMINI_API_KEY")

# Configure API keys
genai.configure(api_key=googlegemini_api_key)

# def query_openai(prompt):
    # idk yet

# def query_claudeai(prompt):
    # idk yet
    

def query_googlegemini(prompt: str) -> str:
    # wahh
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    print(response.text)

def main():
    prompt = "What is the capital of France?"
    
    # openai_response = query_openai(prompt)
    # claudeai_response = query_claudeai(prompt)
    # print("OpenAI Response:")
    # print(openai_response)
    # print("\nClaudeAI Response:")
    # print(claudeai_response)
    print("\nGoogle Gemini Response:")
    googlegemini_response = query_googlegemini(prompt)

if __name__ == "__main__":
    main()