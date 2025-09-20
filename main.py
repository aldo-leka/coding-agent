import os
import sys
from google import genai
from dotenv import load_dotenv

if len(sys.argv) < 2:
    print("expecting 'contents' argument")
    sys.exit(1)

contents = sys.argv[1]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
response = client.models.generate_content(model="gemini-2.0-flash-001", contents=contents)
print(response.text)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
