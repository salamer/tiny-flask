from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time
import asyncio

app = FastAPI()


async def fake_video_streamer():
    for i in range(30):
        await asyncio.sleep(0.1)
        print(f"yielding {i}")
        yield f"some fake video bytes\n"


@app.get("/")
async def main():
    return StreamingResponse(fake_video_streamer())

@app.get("/gen")
async def gen():
    return "Hello\n" * 1000