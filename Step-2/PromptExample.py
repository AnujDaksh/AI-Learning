import os
from google import genai
from google.genai import types

# 1. Initialize the official Gemini client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

model_id = "gemini-3.5-flash-lite"

# 2. Constructing an anatomically complete prompt layout
# Role & Instructions
role_instruction = "You are a precise data extraction assistant."

# Context, Task, Constraints, and Output Format combined cleanly
structured_prompt = """
<context>
Customer Feedback: "The mobile app login screen crashes every time I try to sign in using biometrics on iOS. Fix this immediately!"
</context>

<task>
Analyze the feedback and categorize the core issue.
</task>

<constraints>
- Use ONLY the provided feedback text.
- Do not assume unstated details.
</constraints>

<output_format>
Return a JSON object with keys: "category", "sentiment", and "urgency".
</output_format>
"""

# 3. Execute generation request with structured prompt
response = client.models.generate_content(
    model=model_id,
    contents=structured_prompt,
    config=types.GenerateContentConfig(
        system_instruction=role_instruction,
        temperature=0.1,  # Low temperature for strict adherence
        max_output_tokens=200
    )
)

print("--- Structured Prompt Output ---")
print(response.text)