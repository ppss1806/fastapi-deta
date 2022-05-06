from fastapi import FastAPI, Request
from deta import Deta
import time
import os

if os.getenv('DETA_RUNTIME', False):
    deta = Deta()
    async_db = deta.AsyncBase("test")


app = FastAPI()


@app.get("/")
async def root():
    return "Hello World!"


@app.get("/myip")
async def get_myip(request: Request):
    item = {"ip": request.client.host, "time": time.time()}

    if os.getenv('DETA_RUNTIME', False):
        await async_db.insert(item)

    return item
