import streamlit as st
from langchain_openai import OpenAI
from langchain import PromptTemplate

st.set_page_config(
    page_title = "Generador de Blog Posts",
)

st.title("Generador de Blog Posts")

openai_api_key = st.sidebar.text_input(
    "OpenAI API Key",
    type = "password"
)

def generate_response(topic):
    llm = OpenAI(openai_api_key=openai_api_key)
    template = """
    As experienced startup and venture capital writer, 
    generate a 400-word blog post about {topic}
    
    Your response should be in this format:
    First, print the blog post.
    Then, sum the total number of words on it and print the result like this: This post has X words.
    """
    prompt = PromptTemplate(
        input_variables = ["topic"],
        template = template
    )
    query = prompt.format(topic=topic)
    response = llm(query, max_tokens=2048)
    return st.write(response)


topic_text = st.text_input("Insertar tema: ")
if not openai_api_key.startswith("sk-"):
    st.warning("Escribe tu OpenAI API Key para continuar.")
if openai_api_key.startswith("sk-"):
    generate_response(topic_text)
        
