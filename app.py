import os
from typing import Tuple

import streamlit as st
from dotenv import load_dotenv
import openai

load_dotenv()  # Load environment variables from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

openai.api_key = OPENAI_API_KEY

#streamlit page configuration
st.set_page_config(
    page_title="AI-Powered Text Assistant", 
    page_icon="🤖"
)

st.title("🤖 AI-Powered Text Assistant")
st.caption("Rewrite • Summarize • Explain • Ideate • Sentiment — built to practice prompting while shipping a real app")

with st.sidebar:
    st.header("Settings")

    #Paste API key
    api_key_input = st.text_input(
        "OpenAI API Key", 
        value = OPENAI_API_KEY,
        type="password",
        help="Your key is kept only in this session.",
    )

    model_name = st.text_input(
        "Model", 
        value=DEFAULT_MODEL,
        help="e.g., gpt-3.5-turbo or gpt-4o-mini (if available)"
    )

    #Creative vs Strict 
    temperature = st.slider(
        "Creativity", 
        min_value=0.0, 
        max_value=1.0, 
        value=0.7, 
        step=0.1,
        help="Higher value = more creative but less deterministic."
    )

    #Update OpenAI client config
    if api_key_input:
        openai.api_key = api_key_input

#Core LLM call
def call_llm(system_prompt: str, user_prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"❌ LLM error: {e}"