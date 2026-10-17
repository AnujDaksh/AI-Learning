import os
from google import genai

# 1. Initialize the official Gemini client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

print("Sending request to Gemini...")
print("Generating text with controlled inference parameters...")
# 3. Simple text generation demonstrating auto-regressive decoding
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Give a creative one-line slogan for an Indian street food startup.",
    config={
        "temperature": 0.7,      # Controls randomness (stochastic behavior)
        "top_p": 0.95,           # Restricts token choices to nucleus probability
        "max_output_tokens": 60  # Enforces output token constraints
    }
)

print("\nModel Output:")
print(response.text)