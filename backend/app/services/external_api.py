# app/services/external_api.py

import requests
import os

API_KEY = os.getenv("FMP_API_KEY")
BASE_URL = "https://financialmodelingprep.com/api/v3"

def fetch_stock_quote(symbol: str = "AAPL"):
    """Fetch current stock quote."""
    if not API_KEY:
        print("❌ API KEY Missing. Check your .env FMP_API_KEY setup.")
        return None
    try:
        url = f"{BASE_URL}/quote/{symbol}?apikey={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Check if data is empty
        if isinstance(data, list) and len(data) > 0:
            return data
        else:
            print(f"❌ No data returned for symbol: {symbol}")
            return None

    except requests.RequestException as e:
        print(f"❌ Error fetching stock quote: {e}")
        return None
