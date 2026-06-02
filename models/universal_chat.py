from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

# Load API keys
load_dotenv()

# ---------------------------------------------------
# SWAPPING MODELS IS AS EASY AS CHANGING THESE STRINGS
# ---------------------------------------------------

# Option A: OpenAI
# model = init_chat_model(
#     "gpt-4o-mini",
#     model_provider="openai"
# )

# Option B: Google Gemini
# model = init_chat_model(
#     "gemini-2.5-flash",
#     model_provider="google_genai"
# )

# Option C: Groq
model = init_chat_model(
    "llama-3.3-70b-versatile",
    model_provider="groq"
)

# model = init_chat_model(
#     "mixtral-8x7b-32768",
#     model_provider="groq"
# )
# ---------------------------------------------------

# Conversation messages
messages = [
    HumanMessage(
        content="Give me a one-paragraph explanation of Machine Learning."
    )
]

# Invoke the model
response = model.invoke(messages)

# Print response
print("Content:")
print(response.content)

print("\nMetadata:")
print(response.response_metadata)

print("\nUsage:")
print(response.usage_metadata)