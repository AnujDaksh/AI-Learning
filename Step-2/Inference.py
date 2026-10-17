import os
from google import genai
from google.genai import types

# 1. Initialize the developer client with your AQ. key
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# 2. Use the new Interactions API with the required gemini-3.8-flash model
print("Sending request to Gemini...")
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words"
)

# 3. Print the text response from the model
print("\nResponse:")
print(interaction.output_text)
