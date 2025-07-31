import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List all available models
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"Model Name: {model.name}")
        print(f"Description: {model.description}")
        print(f"Input Token Limit: {model.input_token_limit}")
        print(f"Output Token Limit: {model.output_token_limit}")
        print("-" * 50)