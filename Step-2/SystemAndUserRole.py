import os
from google import genai
from google.genai import types

# 1. Initialize the official Gemini client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

model_id = "gemini-3.8-flash"

# 2. Configure System Instructions and Generation Parameters
config = types.GenerateContentConfig(
    system_instruction="You are a senior staff software engineer. Provide clear, concise architecture explanations.",
    temperature=0.2,
    max_output_tokens=3000
)

# 3. Construct the prompt
prompt = "What is the primary role of the Messages API system parameter?"

# 4. Invoke model execution using generate_content_stream
print("--- Assistant Response (Streaming) ---")
response_stream = client.models.generate_content_stream(
    model=model_id,
    contents=prompt,
    config=config
)

# 5. Iterate through the stream chunks and print text in real-time
for chunk in response_stream:
    print(chunk.text, end="", flush=True)

print("\n\n--- Stream Completed ---")