#!/usr/bin/env python3
# -------------------
# program generated using chatGPT on May 21, 2026
# -------------------
import asyncio
import random
import json
from datetime import datetime
import websockets

clients = set()

def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

async def handle_client(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            data = {
                "type": "chat",
                "timestamp": now_str(),
                "message": message
            }

            dead = set()
            for client in clients:
                if client != websocket:
                    try:
                        await client.send(json.dumps(data))
                    except:
                        dead.add(client)

            clients.difference_update(dead)

    finally:
        clients.discard(websocket)

async def stock_feed():
    while True:
        price = round(random.uniform(160, 200), 2)

        data = {
            "type": "stock",
            "timestamp": now_str(),
            "symbol": "MyStock",
            "price": price
        }

        dead = set()
        for client in clients:
            try:
                await client.send(json.dumps(data))
            except:
                dead.add(client)

        clients.difference_update(dead)
        await asyncio.sleep(10)

async def main():
    async with websockets.serve(handle_client, "127.0.0.1", 8888):
        print("Server running...")
        await stock_feed()

asyncio.run(main())
