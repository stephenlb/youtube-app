import videos
import database
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    videos.setup()
    videos.insert("Hello", "World")
    return {"Beep": "Boop"}

@app.get("/video")
async def video(query: str, limit: int = 2):
    results = videos.search(query, limit)
    return {"videos": results}

@app.post("/video")
async def video(body: dict):
    ## ARyzenCPU - ADD VALIDITION
    title = body['title']
    description = body['description']
    videos.insert(title, description)
    return {
        "status": "success",
        "title": title,
        "description": description,
    }

## TODO Upload Videos
## -> sign URL for S3 direct upload
## -> store video metadata in DB
## -> PUT to Queue for procoessing
## -> Thumbnail

## TODO Fetch Videos
## -> homepage
## -> trending - last 7 days
## -> search
## -> infinite scroll


## TODO Task Management - Nureddin @Nooreldien
## TODO Likes API
## TODO Track views counter
## TODO 
