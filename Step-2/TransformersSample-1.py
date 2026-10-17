import os
from google import genai

# 1. Initialize the official Gemini client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

model_id = "gemini-3.5-flash-lite"

# 2. Retrieve model metadata to inspect operational boundaries
model_info = client.models.get(model=model_id)

print(f"Model Name: {model_info.name}")
print(f"Input Token Limit: {model_info.input_token_limit}")
print(f"Output Token Limit: {model_info.output_token_limit}")

# 3. Simple text generation demonstrating auto-regressive decoding
response = client.models.generate_content(
    model=model_id,
    contents="Why are decoder-only architectures preferred for general text generation? Answer in 2 bullet points.",
    config={
        "max_output_tokens": 150,
        "temperature": 0.2
    }
)

print("\nModel Output:")
print(response.text)