import os
from google import genai

# 1. Initialize the official Gemini client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 2. Define text to convert into continuous vector embeddings
query_text = "How do I fix a flat bicycle tire?"

# 3. Request embeddings using Google's embedding model
response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=query_text
)

# 4. Extract the continuous float vector (the embedding)
embedding_vector = response.embeddings[0].values

print(f"Text: '{query_text}'")
print(f"Embedding Vector Length (Dimensions): {len(embedding_vector)}")
print(f"First 5 Vector Values: {embedding_vector[:5]}")