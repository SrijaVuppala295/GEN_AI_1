import os

import streamlit as st

from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI

from langchain_core.prompts import (
    ChatPromptTemplate
)

from langchain_core.output_parsers import (
    StrOutputParser
)


# ======================================================
# LOAD ENV VARIABLES
# ======================================================

load_dotenv()


# ======================================================
# VALIDATE API KEY
# ======================================================

if not os.getenv("MISTRAL_API_KEY"):

    st.error(
        "MISTRAL_API_KEY not found!"
    )

    st.stop()


# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(

    page_title="AI Concept Explainer",

    page_icon="🧠"
)


# ======================================================
# PAGE TITLE
# ======================================================

st.title("🧠 AI Concept Explainer")

st.caption(
    "Powered by LangChain + Mistral + Streamlit"
)


# ======================================================
# CACHE MODEL
# ======================================================

@st.cache_resource
def load_model():

    return ChatMistralAI(

        model="mistral-large-latest"
    )


model = load_model()


# ======================================================
# PROMPT TEMPLATE
# ======================================================

prompt_template = ChatPromptTemplate.from_messages([

    (
        "system",

        "You are an expert teacher. "
        "Explain complex concepts to a "
        "{audience}. "
        "Keep the answer under 3 sentences."
    ),

    (
        "human",

        "Please explain {topic}."
    )
])


# ======================================================
# OUTPUT PARSER
# ======================================================

parser = StrOutputParser()


# ======================================================
# LCEL CHAIN
# ======================================================

chain = (

    prompt_template

    |

    model

    |

    parser
)


# ======================================================
# USER INPUTS
# ======================================================

audience = st.selectbox(

    "Select Audience",

    [

        "5-year-old child",

        "College Student",

        "Senior Software Engineer",

        "Beginner Programmer"
    ]
)


topic = st.text_input(

    "Enter Topic",

    placeholder="Example: Machine Learning"
)


# ======================================================
# GENERATE BUTTON
# ======================================================

if st.button("Generate Explanation"):

    if topic.strip():

        with st.spinner("Generating response..."):

            response = chain.invoke({

                "audience": audience,

                "topic": topic
            })


        st.success("Explanation Generated")


        st.markdown("## AI Response")

        st.write(response)

    else:

        st.warning("Please enter a topic.")