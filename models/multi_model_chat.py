# =========================================================
# IMPORTS
# =========================================================

from dotenv import load_dotenv

# OpenAI
from langchain_openai import ChatOpenAI

# Google Gemini
from langchain_google_genai import ChatGoogleGenerativeAI

# Groq
from langchain_groq import ChatGroq

# Mistral
from langchain_mistralai import ChatMistralAI

# Message schema
from langchain_core.messages import SystemMessage, HumanMessage


# =========================================================
# LOAD API KEYS
# =========================================================

# Loads all keys from .env file
load_dotenv()


# =========================================================
# CHOOSE YOUR MODEL
# =========================================================

# ---------------------------------------------------------
# OPTION 1 : OpenAI
# Uncomment ONLY this block to use OpenAI
# ---------------------------------------------------------

# model = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0.7
# )


# ---------------------------------------------------------
# OPTION 2 : Google Gemini
# Uncomment ONLY this block to use Gemini
# ---------------------------------------------------------

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)


# ---------------------------------------------------------
# OPTION 3 : Groq
# Uncomment ONLY this block to use Groq
# ---------------------------------------------------------

# model = ChatGroq(
#     model="llama3-8b-8192",
#     temperature=0.7
# )


# ---------------------------------------------------------
# OPTION 4 : Mistral
# Uncomment ONLY this block to use Mistral
# ---------------------------------------------------------

# model = ChatMistralAI(
#     model="mistral-small",
#     temperature=0.7
# )


# =========================================================
# CREATE MESSAGES
# =========================================================

messages = [

    # System message defines AI behavior
    SystemMessage(
        content="You are a strict math professor who explains concepts clearly."
    ),

    # Human message represents user input
    HumanMessage(
        content="Explain what is ML in 500 words."
    )
]


# =========================================================
# INVOKE MODEL
# =========================================================

# Send messages to model
response = model.invoke(messages)


# =========================================================
# PRINT RESPONSE
# =========================================================

print("AI Response:")
print(response.content)


# =========================================================
# OPTIONAL : TOKEN USAGE
# =========================================================

print("\nToken Usage:")
print(response.usage_metadata)


# =========================================================
# OPTIONAL : RESPONSE METADATA
# =========================================================

print("\nResponse Metadata:")
print(response.response_metadata)