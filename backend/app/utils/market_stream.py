import json
import asyncio
import websockets
from kafka import KafkaProducer

WS_URL = "wss://example.com/stream"
producer = KafkaProducer(bootstrap_servers="localhost:9092")

async def stream_market_data():
    async with websockets.connect(WS_URL) as websocket:
        while True:
            data = await websocket.recv()
            producer.send('market-data', json.dumps(data).encode('utf-8'))

asyncio.run(stream_market_data())
