from langchain_huggingface import HuggingFaceEmbeddings

# 1. Initialize the Hugging Face embedding model locally
# The first run will download a lightweight model (all-MiniLM-L6-v2) to your hard drive.
# No API keys or internet connection are required after the initial download!
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# --- Scenario 1: Embedding a Single Query ---
query_text = "You are going to learn Gen AI"
query_vector = embeddings.embed_query(query_text)

print("--- Single Query Vector Generated ---")
print(query_vector[:5]) # Printing just the first 5 numbers to save space
print(f"Total numbers in this vector (Dimensions): {len(query_vector)}")

# --- Scenario 2: Embedding Multiple Documents ---
texts = [
    "Hello this is Akarsh Vyas",
    "Hello your name is YouTube",
    "And you all are very beautiful"
]
document_vectors = embeddings.embed_documents(texts)

print(f"\nSuccessfully generated {len(document_vectors)} Document Vectors.")