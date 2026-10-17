import os
from google import genai
from google.genai import types

# 1. Initialize the official Gemini client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

model_id = "gemini-3.5-flash-lite"

# 2. Configure concise output constraints to manage output token costs
config = types.GenerateContentConfig(
    temperature=0.1,
    max_output_tokens=150  # Enforces a strict ceiling on expensive output tokens
)

# 3. Execute generation
response = client.models.generate_content(
    model=model_id,
    contents="List 3 ways to optimize LLM API costs.",
    config=config
)

print("--- Model Response ---")
print(response.text)

# 4. Inspect token usage metadata for cost accounting
if response.usage_metadata:
    print("\n--- Cost Tracking Metadata ---")
    print(f"Input Tokens (Prompt Cost): {response.usage_metadata.prompt_token_count}")
    print(f"Output Tokens (Generation Cost): {response.usage_metadata.candidates_token_count}")
    print(f"Total Tokens: {response.usage_metadata.total_token_count}")