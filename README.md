# AI-text-assistant
A multi-purpose LLM app that rewrites, summarizes, explains, generates ideas, and classifies text.

##  Features
-  **Summarize**: Condense long text into 3 bullet points.  
-  **Rewrite**: Rewrite text in different tones (professional, friendly, concise, enthusiastic, empathetic).  
-  **Explain**: Break down complex topics for different audiences (kids, beginners, adults, college students).  
-  **Idea Generator**: Generate multiple creative ideas for a topic or problem statement.  
-  **Sentiment Analysis**: Classify text sentiment as Positive, Negative, or Neutral.  
-  Clean Streamlit UI with sidebar configuration.

## 📂 Project Structure

```
AI-text-assistant/
│── app.py # Main Streamlit app
│── requirements.txt # Python dependencies
│── .env # Environment variables (API keys)
│── README.md # Project documentation
```

## ⚙️ Setup Instructions

### 1️. Clone the repository
```bash
git clone https://github.com/your-username/AI-text-assistant.git
cd AI-text-assistant
```

### 2️. Create and activate a virtual environment
```bash
python -m venv .venv
# Activate it:
.venv\Scripts\activate
```

### 3️. Install dependencies
```bash
pip install -r requirements.txt
pip install openai==0.28
```

### 4️. Add your OpenAI API Key
```bash
#Create a .env file in the project root:
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
```

### 5️. Run the app
```bash
streamlit run app.py
```

##  License

This project is licensed under the MIT License

##  Author

**SHREEYA P S** - [shreeyashree-65](https://github.com/shreeyashree-65)

