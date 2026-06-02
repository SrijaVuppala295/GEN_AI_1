import os
import getpass
from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings

# 1. Load keys from your .env file if it exists
load_dotenv()

# 2. Ensure the Mistral API Key is available
# If MISTRALAI_API_KEY is not found in your environment, it will safely ask you to paste it.
if not os.environ.get("MISTRALAI_API_KEY"):
    os.environ["MISTRALAI_API_KEY"] = getpass.getpass("Enter API key for MistralAI: ")

# 3. Initialize Mistral Embeddings using the exact model from the documentation
embeddings = MistralAIEmbeddings(model="mistral-embed")

print("--- Initializing Official Mistral AI Embedding Engine ---")

# 4. Define the sample strings to convert into mathematical vectors
documents = [
    "LangChain makes it incredibly easy to swap between different language models.",
    "You can change your underlying LLM infrastructure by altering a single string."
]

# 5. Generate vectors for both text inputs using embed_query
print("Sending text data to Mistral servers...")
vector_1 = embeddings.embed_query(documents[0])
vector_2 = embeddings.embed_query(documents[1])

# 6. Safety check to make sure both vector structures align perfectly
assert len(vector_1) == len(vector_2), "Vector dimensions must match for similarity search."

print(f"\n[Success] Generated vectors of length {len(vector_1)}")
print("First 10 mathematical dimensions of Vector 1:")
print(vector_1[:10])