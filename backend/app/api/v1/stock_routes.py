from fastapi import APIRouter
from app.services.stock_service import get_stock_info

router = APIRouter()

@router.get("/{symbol}")
async def read_stock(symbol: str):
    return await get_stock_info(symbol)
