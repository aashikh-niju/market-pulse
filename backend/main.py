from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fetch_data import get_last_5_closing_prices

app = FastAPI(
    title="Market Pulse API",
    version="1.0.0",
    description="Returns bullish/bearish/neutral signal for a stock"
)

# CORS to allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fetch_data import get_last_5_closing_prices, get_news_headlines
from momentum import calculate_daily_returns, calculate_momentum_score
from llm_handler import get_market_pulse_from_gemini

@app.get("/api/v1/stock-price")
def get_prices(ticker: str):
    try:
        prices = get_last_5_closing_prices(ticker.upper())
        returns = calculate_daily_returns(prices)
        score = calculate_momentum_score(returns)
        news = get_news_headlines(ticker.upper())

        pulse, explanation = get_market_pulse_from_gemini(ticker, score, returns, news)

        return {
            "ticker": ticker.upper(),
            "last_5_closing_prices": prices,
            "daily_returns": returns,
            "momentum_score": score,
            "news": news,
            "pulse": pulse,
            "llm_explanation": explanation
        }
    except Exception as e:
        return {"error": str(e)}


@app.get("/")
def read_root():
    return {"message": "Market Pulse API is running"}


