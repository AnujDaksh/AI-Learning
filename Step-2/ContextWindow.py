import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

system_prompt = "You are an expert systems architecture guide."
user_prompt = "Explain the difference between synchronous and asynchronous microservices."

# 1. Count tokens (only contents allowed, no system_instruction here)
token_check = client.models.count_tokens(
    model="gemini-3.5-flash-lite",   # valid model name
    contents=user_prompt
)

input_count = token_check.total_tokens
print(f"Input Token Count: {input_count}")

# 2. Generate content (system_instruction is valid here)
MAX_CONTEXT_LIMIT = 200000

if input_count < MAX_CONTEXT_LIMIT:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            max_output_tokens=300
        )
    )
    print("\nAPI Response Received:")
    print(response.text)
else:
    print("\nWarning: Input exceeds context window limits! Apply context trimming.")
