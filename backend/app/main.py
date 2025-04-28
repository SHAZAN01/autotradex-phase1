# app/main.py

from dotenv import load_dotenv
from pathlib import Path
import os

# 💥 1. Load .env manually before anything else
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

# 💥 2. Confirm .env is loaded
print("✅ DATABASE_URL Loaded:", os.getenv("DATABASE_URL"))

# 💥 3. Import FastAPI and internal modules
from fastapi import FastAPI
from app.api.v1 import stock_routes  # Your stock APIs (Phase 2)
from app.db.database import create_db_connection  # Database connection creator
from app.routers import middleware  # 👈 Middleware router we created in Phase 3
from app.services.scheduler import start_scheduler  # 👈 Scheduler (background fetch)

# 💥 4. Initialize FastAPI app
app = FastAPI(
    title="Hifengo Financial API",
    version="1.0.0",
    description="Backend Middleware for Real-Time Financial Data Streaming and Storage",
)

# 💥 5. Startup Event
@app.on_event("startup")
async def startup_event():
    print("🚀 Starting up Hifengo Backend...")
    await create_db_connection()
    start_scheduler()

# 💥 6. Include API Routers
app.include_router(stock_routes.router, prefix="/api/v1/stocks", tags=["Stocks"])
app.include_router(middleware.router, prefix="/api/v1/middleware", tags=["Middleware"])

# 💥 7. Root Health Check
@app.get("/")
async def root():
    return {"message": "Welcome to Hifengo Financial API 🚀"}
