import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_mistralai import ChatMistralAI  # Using Mistral as requested

# 1. Load your API keys from the .env file
load_dotenv()

if not os.getenv("MISTRAL_API_KEY"):
    raise ValueError("MISTRAL_API_KEY not found! Please check your .env file.")

# 2. Initialize the chat model
model = ChatMistralAI(model="mistral-large-latest")

# 3. Initialize the memory tracking object
# This object will act as our local list storing all back-and-forth messages.
memory = InMemoryChatMessageHistory()

print("==================================================")
print("   🤖 MISTRAL CHATBOT WITH MEMORY INITIALIZED   ")
print("   Type 'exit' or 'quit' to end the chat.        ")
print("==================================================")

# 4. Start the interactive terminal conversation loop
while True:
    # Get user input from the terminal
    user_input = input("\nYou: ")
    
    # Check if the user wants to break out of the program
    if user_input.strip().lower() in ['exit', 'quit']:
        print("Goodbye!")
        break
        
    # Skip empty lines
    if not user_input.strip():
        continue
        
    # Append the user's message to the active running memory history
    memory.add_message(HumanMessage(content=user_input))
    
    print("AI is thinking...")
    
    # Fetch all stored messages (the whole history) and pass them to the model
    # This allows the model to read what was said previously to maintain context!
    response = model.invoke(memory.messages)
    
    # Append the AI's response to the memory history so it remembers its own answers
    memory.add_message(AIMessage(content=response.content))
    
    # Print the response out to the user
    print(f"\nAI: {response.content}")