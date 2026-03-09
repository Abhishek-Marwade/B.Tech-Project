
import google.generativeai as genai
import os

# Use the hardcoded key from other files since env var might not be set in this shell context yet
# (Ideally we move to env vars soon)
genai.configure(api_key="AIzaSyAbtZG_lJffkDVOx2da3C23kQdAV8JpAvs")

print("Listing available models...")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"Name: {m.name}")


