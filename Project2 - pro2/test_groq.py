"""
Test script to check if Groq is configured correctly
"""
import os
from dotenv import load_dotenv

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")
print(f"Groq API Key: {groq_key[:20]}..." if groq_key and groq_key != "your_groq_api_key_here" else "NOT SET")
print(f"AI Provider: {os.getenv('AI_PROVIDER')}")
print(f"Disable AI: {os.getenv('DISABLE_AI')}")

if groq_key == "your_groq_api_key_here":
    print("\nERROR: You need to set your real Groq API key!")
    print("Get one here: https://console.groq.com/keys")
else:
    print("\nGroq key is set!")
    
    # Test the API
    try:
        from groq import Groq
        client = Groq(api_key=groq_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": "Say 'working' if you can read this"}],
            max_tokens=10
        )
        print(f"SUCCESS! Groq API Test: {response.choices[0].message.content}")
    except Exception as e:
        print(f"ERROR with Groq API: {e}")
