from app.db.database import async_session
from app.db.models import StockData

from sqlalchemy.future import select

async def get_stock_info(symbol: str):
    async with async_session() as session:
        result = await session.execute(select(Stock).where(Stock.symbol == symbol))
        stock = result.scalars().first()
        if stock:
            return {
                "symbol": stock.symbol,
                "name": stock.name,
                "price": stock.price,
                "market_cap": stock.market_cap,
            }
        return {"error": "Stock not found"}
