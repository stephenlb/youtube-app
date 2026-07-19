import os
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

VIDEO_PATH = "sample_video.mp4"
CHUNK_SIZE = 1024 * 1024  # 1MB per chunk

def video_streamer(path: str):
    """Generator function to yield video chunks."""
    with open(path, mode="rb") as file_like:
        while True:
            chunk = file_like.read(CHUNK_SIZE)
            if not chunk:
                break
            yield chunk

@app.get("/video")
async def get_video():
    # Returns the stream with appropriate media type headers
    return StreamingResponse(video_streamer(VIDEO_PATH), media_type="video/mp4")
