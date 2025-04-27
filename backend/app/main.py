from dotenv import load_dotenv
from pathlib import Path
import os

# 💥 1. Load .env manually before anything else
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

# 💥 2. Confirm .env is loaded
print("DATABASE_URL Loaded:", os.getenv("DATABASE_URL"))

# 💥 3. Now import FastAPI and your other modules
from fastapi import FastAPI
from app.api.v1 import stock_routes
from app.db.database import create_db_connection

# 💥 4. Initialize FastAPI app
app = FastAPI(title="Hifengo Financial API", version="1.0.0")

@app.on_event("startup")
async def startup_event():
    await create_db_connection()

# 💥 5. Include routes
app.include_router(stock_routes.router, prefix="/api/v1/stocks", tags=["Stocks"])
from dotenv import load_dotenv
from pathlib import Path
import os

# Load .env early
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

print("DATABASE_URL Loaded:", os.getenv("DATABASE_URL"))

from fastapi import FastAPI
from app.api.v1 import stock_routes
from app.db.database import create_db_connection

app = FastAPI(title="Hifengo Financial API", version="1.0.0")

@app.on_event("startup")
async def startup_event():
    await create_db_connection()

app.include_router(stock_routes.router, prefix="/api/v1/stocks", tags=["Stocks"])
