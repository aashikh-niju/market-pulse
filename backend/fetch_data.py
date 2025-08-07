import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()  # ✅ Correct if your file is named .env

ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")

def get_last_5_closing_prices(ticker: str):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",  # CHANGED from DAILY_ADJUSTED
        "symbol": ticker,
        "apikey": ALPHA_VANTAGE_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "Time Series (Daily)" not in data:
        raise Exception(f"Error fetching stock data: {data}")

    time_series = data["Time Series (Daily)"]
    sorted_dates = sorted(time_series.keys(), reverse=True)

    closing_prices = []
    for date in sorted_dates[:5]:
        close_price = float(time_series[date]["4. close"])
        closing_prices.append(close_price)

    return closing_prices
def get_news_headlines(ticker: str):
    GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")

    url = "https://gnews.io/api/v4/search"
    params = {
        "q": ticker,
        "lang": "en",
        "max": 5,
        "token": GNEWS_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "articles" not in data:
        raise Exception(f"Error fetching news: {data}")

    headlines = []
    for article in data["articles"]:
        headlines.append({
            "title": article["title"],
            "description": article["description"],
            "url": article["url"]
        })

    return headlines

