import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
print(f"API Key loaded: {api_key[:20]}..." if api_key else "NO API KEY FOUND!")
print(f"Full length: {len(api_key)}" if api_key else "")
