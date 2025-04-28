# app/services/scheduler.py

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.services.external_api import fetch_stock_quote
from app.db.database import async_session
from app.db.models import StockData

scheduler = AsyncIOScheduler()

async def scheduled_fetch():
    """Fetch multiple stock symbols every X minutes and store in DB."""
    symbols = ["AAPL", "GOOG", "TSLA", "MSFT", "AMZN"]  # Extend list as needed
    async with async_session() as session:
        for symbol in symbols:
            data = fetch_stock_quote(symbol)
            if data and isinstance(data, list) and len(data) > 0:
                stock_info = data[0]
                new_stock = StockData(
                    symbol=stock_info.get("symbol"),
                    price=stock_info.get("price"),
                    volume=stock_info.get("volume", 0)
                )
                session.add(new_stock)
        await session.commit()
        print("✅ Background fetch complete.")

def start_scheduler():
    """Start the background scheduler."""
    scheduler.add_job(scheduled_fetch, "interval", minutes=30)  # Every 30 min
    scheduler.start()
    print("⏰ Scheduler started.")
