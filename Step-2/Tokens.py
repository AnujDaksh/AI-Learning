import os
from google import genai

# Create the client with your Gemini API key
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

print("Sending request to Gemini...")

# Send a prompt to Gemini
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",   # valid model name
    contents="Name three cities in India."
)

# Print the response
print(response.text)

# Check token usage returned by Anthropic API
print("Input tokens used:", response.usage_metadata.prompt_token_count)
print("Output tokens used:", response.usage_metadata.candidates_token_count)
print("Total tokens used:", response.usage_metadata.total_token_count)
