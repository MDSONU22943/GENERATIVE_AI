import os
from dotenv import load_dotenv
import google.generativeai as genai

# .env load
load_dotenv()

# API key read
api_key = os.getenv("GOOGLE_API_KEY")

# configure gemini
genai.configure(api_key=api_key)

response = genai.embed_content(
    model="models/text-embedding-004",
    content="AI is transforming the world"
)

embedding = response["embedding"]

print(len(embedding))
print(embedding[:10])