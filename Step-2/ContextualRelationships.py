import os
from google import genai

# 1. Initialize the official Gemini client

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

model_id = "gemini-3.5-flash-lite"

# 2. Prompt demonstrating context-dependent word disambiguation
prompt = """
Analyze the word 'bank' in these two sentences:
Sentence 1: 'I deposited money in the bank.'
Sentence 2: 'I sat on the river bank.'

Explain briefly how surrounding context changes the meaning of 'bank'.
"""

# 3. Generate response showing context dependency
response = client.models.generate_content(
    model=model_id,
    contents=prompt,
    config={
        "max_output_tokens": 150,
        "temperature": 0.2,
    }
)

print("Context Analysis Output:")
print(response.text)