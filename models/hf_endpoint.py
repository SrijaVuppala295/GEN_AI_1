import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# 1. Load the environment variables
load_dotenv()

if "HUGGINGFACEHUB_API_TOKEN" not in os.environ and "HF_TOKEN" in os.environ:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.environ["HF_TOKEN"]

# 2. Initialize the Serverless Endpoint
# We swapped to Llama-3-8B-Instruct because HF's API natively recognizes it as a Chat Model
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct", 
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
)

# 3. Wrap it in the ChatHuggingFace class for conversational abilities
model = ChatHuggingFace(llm=llm)

# 4. Invoke the model
response = model.invoke("Who are you?")

# 5. Print the result
print(response.content)