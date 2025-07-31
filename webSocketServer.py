from fastapi import FastAPI, WebSocket
from webSocketManager import WebSocketManager
# import threading
import asyncio
from datetime import datetime

app = FastAPI()

manager = WebSocketManager()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    async def push_message():
        '''推送訊息'''
        now = datetime.now()
        await websocket.send_text(f"Ping from server:{now}")

    async def interval_sender():
        '''定時執行'''
        while True:
            await push_message()
            await asyncio.sleep(5)

    sender_task = asyncio.create_task(interval_sender())

    try:
        while True:
            data = await websocket.receive_text()
            response = f"Server received: {data}"
            await manager.send_personal_message(response, websocket)
            sender_task
    except:
        manager.disconnect(websocket)
