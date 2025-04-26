import asyncio
import websockets
import json
from kafka import KafkaProducer

# Connect to your broker's WebSocket API here
WS_URL = "wss://example.com/stream"  # Alpaca or Polygon.io URL
producer = KafkaProducer(bootstrap_servers='localhost:9092')  # Assuming Kafka local setup

async def stream_market_data():
    async with websockets.connect(WS_URL) as websocket:
        while True:
            data = await websocket.recv()
            producer.send('market-data', json.dumps(data).encode('utf-8'))

asyncio.run(stream_market_data())
