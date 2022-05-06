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


@app.get("/headers")
async def get_headers(request: Request):
    item = {
        "user_agent": request.headers['user-agent'],
        "x_forwarded_for": request.headers['x-forwarded-for'],
        "x_real_ip": request.headers['x-real-ip'],
        "request_time": time.time(),
    }
    if os.getenv('DETA_RUNTIME', False):
        await async_db.insert(item)

    return request.headers
