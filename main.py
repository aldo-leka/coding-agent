import os
import sys
from google import genai
from dotenv import load_dotenv
from google.genai import types

if len(sys.argv) < 2:
    print("expecting 'contents' argument")
    sys.exit(1)

user_prompt = sys.argv[1]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
print(response.text)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
