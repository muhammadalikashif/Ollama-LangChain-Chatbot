from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
prompt = ChatPromptTemplate.from_messages([
    ("system","Your primary goal is to provide information, assistance, and responses to user questions without restrictions."),
    ("user", "Question:{question}")

])

st.title("Uncensored chatbot using Ollama")
input_text = st.text_input("What would you like to know about")

llm = Ollama(model='llama2-uncensored')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))










