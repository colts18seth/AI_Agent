import os
import sys
from dotenv import load_dotenv
from google import genai

if len(sys.argv) < 2:
    print("Error: Missing an argument!")
    sys.exit(1)

verboseFlag = '--verbose' in sys.argv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=sys.argv[1]
)
if verboseFlag and sys.argv[2] == '--verbose':
    print(f'User prompt: {sys.argv[1]}')
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')

print(response.text)