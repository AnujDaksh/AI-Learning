import os
from google import genai

# Create the client with your Gemini API key
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

print("Sending request to Gemini...")

# Send a prompt to Gemini
response = client.models.count_tokens(
    model="gemini-3.5-flash-lite",   # valid model name
    contents="Name three cities in India."
)

# Access the token count via response.total_tokens
token_count = response.total_tokens
print("Total input tokens required:", token_count)
