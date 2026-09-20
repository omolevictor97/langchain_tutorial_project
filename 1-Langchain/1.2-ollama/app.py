import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
load_dotenv('../../.env')

# Langsmith Tracking

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

prompt = ChatPromptTemplate(
    [
        ('system', 'You are a Ph.D / professor level AI assistant, you can\'t but answer all questions thrwon at you, perfectly'),
        ('user', 'Question: {question}')
    ]
)

# Streamlit framework
st.title('Langchain Demo with Llama2')
input_text = st.text_input("Hi, what do you have in mind, can I help???")

# Using Llama 2 model
llm = Ollama(model="gemma:2b")
# outputparser
output_parser = StrOutputParser()
# chain
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke(
        {"question": input_text}
    ))

