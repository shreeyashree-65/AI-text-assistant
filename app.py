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
    
#Prompts
def build_summarize_prompt(text: str) -> Tuple[str, str]:
    system = (
    "You are a concise assistant. Return exactly three bullet points that capture the key ideas."
    )
    user = f"Summarize the following text in exactly three bullet points.\n\n{text}"
    return system, user

def build_rewrite_prompt(text: str, tone: str) -> Tuple[str, str]:
    system = "You are a skilled editor who rewrites text while preserving meaning."
    user = (
    f"Rewrite the text in a {tone} tone. Keep it clear and concise.\n\nText:\n{text}"
    )
    return system, user

def build_explain_prompt(text: str, level: str) -> Tuple[str, str]:
    system = "You explain complex topics using simple words and examples."
    user = (
    f"Explain the following to a {level}. Use short sentences and examples.\n\n{text}"
    )
    return system, user

def build_ideas_prompt(topic: str, n: int) -> Tuple[str, str]:
    system = "You are a creative brainstorming partner who outputs numbered ideas."
    user = f"Give me {n} creative, distinct ideas for: {topic}"
    return system, user

def build_sentiment_prompt(text: str) -> Tuple[str, str]:
    system = (
    "You are a precise sentiment classifier. Output only one word: Positive, Negative, or Neutral."
    )
    user = f"Classify the sentiment of this text. Output only one word.\n\n{text}"
    return system, user

#Main UI body
MODE_OPTIONS = [
    "Summarize",
    "Rewrite",
    "Explain",
    "Idea Generator",
    "Sentiment Analysis",
]

mode = st.selectbox("Choose a feature", MODE_OPTIONS)

if mode == "Idea Generator":
    input_label = "Enter your topic or problem statement"
else:
    input_label = "Paste your text"


text = st.text_area(input_label, height=180)

if mode == "Rewrite":
    col1, col2 = st.columns(2)
    with col1:
        tone = st.selectbox(
            "Tone",
            ["professional", "friendly", "concise", "enthusiastic", "empathetic"],
            index=0,
        )
    with col2:
        pass
elif mode == "Explain":
    level = st.selectbox(
        "Audience",
        ["12-year-old", "beginner", "non-technical adult", "college student"],
        index=0,
    )
elif mode == "Idea Generator":
    n_ideas = st.slider("Number of ideas", 3, 10, value=5)