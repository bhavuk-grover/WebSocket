import json
import asyncio
from fastapi import FastAPI, Request, WebSocket
from fastapi.templating import Jinja2Templates

app = FastAPI()
temp = Jinja2Templates(directory="templates")

with open("csvjson.json" , 'r') as file:
    stockdata = iter(json.loads(file.read()))

@app.get("/")
def read(request: Request):
    return temp.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await asyncio.sleep(2)
        data = next(stockdata)
        await websocket.send_json(data)

