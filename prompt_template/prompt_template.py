import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Load API keys
load_dotenv()

if not os.getenv("MISTRAL_API_KEY"):
    raise ValueError("MISTRAL_API_KEY not found! Please check your .env file.")

# 2. Initialize the Model
model = ChatMistralAI(model="mistral-large-latest")

# 3. Create the Prompt Template
# Notice the {audience} and {topic} variables in curly braces!
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert teacher. Explain complex concepts strictly to a {audience}. Keep it under 3 sentences."),
    ("human", "Please explain {topic}.")
])

# 4. Initialize an Output Parser
# This cleans up the AI's response, stripping away all the LangChain metadata 
# (like token counts) and just giving us the pure text string.
parser = StrOutputParser()

# 5. BUILD THE CHAIN USING LCEL (The Pipe Operator)
# This reads as: Take the prompt, send it to the model, send the result to the parser.
chain = prompt_template | model | parser

print("--- AI Concept Explainer Initialized ---")

# 6. Invoke the chain by passing a dictionary of our variables
print("\nExplaining to a 5-year-old:")
response_1 = chain.invoke({
    "audience": "5-year-old child",
    "topic": "Machine Learning"
})
print(response_1)


print("\nExplaining to a Senior Software Engineer:")
response_2 = chain.invoke({
    "audience": "Senior Software Engineer",
    "topic": "Machine Learning"
})
print(response_2)