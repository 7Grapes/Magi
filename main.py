import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('config.env')

# Get API keys from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
claudeai_api_key = os.getenv("CLAUDEAI_API_KEY")
googlegemini_api_key = os.getenv("GOOGLEGEMINI_API_KEY")

def query_openai(prompt):
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 100
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json().get("choices", [{}])[0].get("text", "")

def query_claudeai(prompt):
    url = "https://api.anthropic.com/v1/claude/completions"
    headers = {
        "Authorization": f"Bearer {claudeai_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 100
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json().get("choices", [{}])[0].get("text", "")

def query_googlegemini(prompt):
    url = "https://api.google.com/v1/gemini/completions"
    headers = {
        "Authorization": f"Bearer {googlegemini_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 100
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json().get("choices", [{}])[0].get("text", "")

def main():
    prompt = "What is the capital of France?"
    
    openai_response = query_openai(prompt)
    claudeai_response = query_claudeai(prompt)
    googlegemini_response = query_googlegemini(prompt)
    
    print("OpenAI Response:")
    print(openai_response)
    print("\nClaudeAI Response:")
    print(claudeai_response)
    print("\nGoogle Gemini Response:")
    print(googlegemini_response)

if __name__ == "__main__":
    main()