# Generative AI Development Hub: From Foundations to Full Deployment

Welcome to the **Generative AI Development Hub**. This repository contains a collection of production-ready Large Language Model (LLM) applications built using **LangChain**, **Mistral AI**, and **Streamlit**. 

The core objective of this course was to transition from basic prompt engineering into building stateful, structured, and visually appealing AI products, concluding with live web deployments.

---

## 📚 Core AI Engineering Concepts Covered

### 1. Large Language Model (LLM) Integration
* Utilized **Mistral AI** models (`mistral-small` and `mistral-large`) via LangChain integration.
* Learned how to manage model parameters, API authentication securely using environmental variables (`.env`), and handling network responses.

### 2. Advanced Prompt Engineering & System Instructions
* Transitioned from simple instructions to multi-layered **System Prompts**.
* Established behavioral guardrails to lock an LLM into a specific persona or professional domain, automatically rejecting off-topic inputs.

### 3. State Management & Conversation Memory
* Implemented LangChain's memory architecture using `InMemoryChatMessageHistory`.
* Utilized `RunnableWithMessageHistory` to seamlessly stitch memory buffers directly into the LangChain Expression Language (LCEL) chain, enabling multi-turn conversations where the AI accurately remembers past contexts.

### 4. Structured Output Parsing (Pydantic Integration)
* Solved the challenge of turning unstructured raw conversational text into strict JSON objects.
* Employed **Pydantic `BaseModel`** schemas to define strict data types (strings, optional integers, list arrays) and utilized the `PydanticOutputParser` to force the model to output machine-readable structures ready for database injection.

### 5. Multi-App Architecture & Production Deployment
* Designed a clean, subfolder-based project architecture capable of scaling across multiple features.
* Deployed live microservices on **Streamlit Community Cloud** with secure environment variables and secrets management.

---

## 🚀 Project Portfolio & Deployed Applications

This repository features 4 specialized AI applications, each proving a distinct capability in AI engineering.

### 🎬 1. CineSage (Data Extraction Engine)
* **Live Deployment:** [cinesage-movie-ai.streamlit.app](https://cinesage-movie-ai.streamlit.app/)
* **Core Tech Stack:** `PydanticOutputParser`, `ChatMistralAI`, `Pydantic BaseModel`
* **Description:** Designed to turn chaotic, unstructured human movie reviews or synopses into beautifully structured data objects. By feeding CineSage a messy paragraph, it automatically extracts and validates fields including Title, Release Year, Genre, Director, Cast List, Numerical Rating, and a concise summary.

### 💬 2. Sierra (The Core Chatbot)
* **Live Deployment:** [sierra.streamlit.app](https://sierra.streamlit.app/)
* **Core Tech Stack:** `Streamlit Chat Elements`, `InMemoryChatMessageHistory`, `RunnableWithMessageHistory`
* **Description:** A highly conversational, multi-turn AI chat companion. It handles continuous back-and-forth dialogue by managing session-based conversation memory, ensuring it recalls earlier details in the chat without breaking context or hallucinating.

### 🎭 3. Sentimental AI (Mood-Based Bot)
* **Live Deployment:** [sentimental-ai.streamlit.app](https://sentimental-ai.streamlit.app/)
* **Core Tech Stack:** `SystemPromptTemplate`, `Dynamic Tone Shifter`
* **Description:** An empathetic AI interface capable of detecting the user's emotional undertone. It utilizes smart guardrails to adjust its tone, vocabulary, and response style dynamically based on the mood of the conversation, delivering highly contextual human-centric responses.

### 📐 4. Prism AI (Prompt Template Hub)
* **Live Deployment:** [prismm-ai.streamlit.app](https://prismm-ai.streamlit.app/)
* **Core Tech Stack:** `ChatPromptTemplate`, `Contextual Injections`
* **Description:** A tool focusing on prompt template optimization. It maps single ideas into highly targeted, alternative perspective outputs based on designated target audiences, formatting guidelines, and variable constraints, proving the power of context shifting.

---

## 🛠️ Local Installation & Setup

To run any of these applications locally on your machine, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
```

### 2. Set Up a Virtual Environment & Install Dependencies
Ensure you have a master `requirements.txt` file setup in the root folder.
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory to store your private credentials:
```env
MISTRALAI_API_KEY="your_actual_mistral_api_key_here"
```

### 4. Running the Applications Locally
Execute any app by pointing Streamlit to the specific subfolder script:
```bash
# To run the Core Chatbot
streamlit run chatbot/chatbotUI.py

# To run CineSage
streamlit run CineSage/UICineSage.py
```

---

## 🌐 Production Deployment Architecture

The production environment is hosted entirely on **Streamlit Community Cloud**, utilizing a centralized repository model:
* **Continuous Integration:** Any updates pushed to the `main` branch on GitHub automatically trigger a rebuild and update the live applications within 60 seconds.
* **Secrets Security:** Application keys are securely injected via Streamlit's Encrypted TOML Vault under `Advanced Settings > Secrets`, keeping production API credentials separate from the source code.
* **Master Package Management:** A single, top-level `requirements.txt` manages dependencies uniformly for all isolated microservice routes.
