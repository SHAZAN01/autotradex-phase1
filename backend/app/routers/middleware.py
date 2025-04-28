# app/routers/middleware.py

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.external_api import fetch_stock_quote
from app.db.database import get_db
from app.db.models import StockData
import asyncio

router = APIRouter()

@router.post("/fetch-stock")
async def fetch_and_store_stock(symbol: str = "AAPL", db: AsyncSession = Depends(get_db)):
    """Fetch stock data from external API and store in DB."""
    data = await asyncio.to_thread(fetch_stock_quote, symbol)
    if data and isinstance(data, list) and len(data) > 0:
        stock_info = data[0]

        new_stock = StockData(
            symbol=stock_info.get("symbol", ""),
            price=stock_info.get("price", 0.0),
            volume=stock_info.get("volume", 0),
        )
        db.add(new_stock)
        await db.commit()
        await db.refresh(new_stock)
        return {"message": "Stock data fetched and stored successfully.", "symbol": symbol}
    else:
        return {"error": "Failed to fetch or parse stock data."}
