import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Use Gemini Flash model
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash-001")

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)

def get_market_pulse_from_gemini(ticker, momentum_score, daily_returns, news_list):
    news_text = "\n".join([f"- {n['title']}: {n['description']}" for n in news_list])

    prompt = f"""
You are a financial assistant. Based on the momentum score and news headlines, determine if the stock {ticker} is bullish, bearish, or neutral for tomorrow. Explain your reasoning.

Momentum Score: {momentum_score}
Daily Returns: {daily_returns}

News:
{news_text}

Respond in this format:
pulse: bullish / bearish / neutral
explanation: your explanation in one sentence
"""

    try:
        response = model.generate_content(prompt)
        message = response.text.strip()
        lines = message.splitlines()

        pulse = None
        explanation = ""

        for line in lines:
            if line.lower().startswith("pulse:"):
                pulse = line.split(":")[-1].strip().lower()
            elif line.lower().startswith("explanation:"):
                explanation = line.split(":", 1)[-1].strip()

        return pulse, explanation

    except Exception as e:
        return None, f"Gemini Error: {str(e)}"
