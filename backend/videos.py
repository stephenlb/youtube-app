import database
import uuid_utils as uuid

SCHEMA="""
    CREATE TABLE IF NOT EXISTS videos (
        id TEXT PRIMARY KEY,
        upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        title TEXT DEFAULT '',
        description TEXT DEFAULT '',
        views INT DEFAULT 0,
        likes INT DEFAULT 0
    );
"""

INSERT_VIDEO="""
    INSERT INTO videos (
        id, upload_date,
        title, description,
        views, likes
    )
    VALUES (%s, NOW(), %s, %s, 0, 0)
"""

QUERY_VIDEOS="""
    SELECT *
    FROM videos
    WHERE title ILIKE %s
    OR description ILIKE %s
    LIMIT %s
"""

def setup():
    return database.query(SCHEMA)
    
def insert(title: str, description: str):
    id = str(uuid.uuid7())
    return database.execute(
        INSERT_VIDEO,
        (id, title, description),
    )

#@dataclass
#class Video():
#    id: str = ""
#    upload_date: int = 0
#    title: str = ""
#    description: str = ""
#    views: int = 0
#    likes: int = 0

async def fetch(video_id: int):
    pass

def search(query: str, limit: int = 1):
    return database.query(
        QUERY_VIDEOS,
        (query, query, limit),
    )

def upload():
    """
    import boto3
    from fastapi import FastAPI, File, UploadFile

    app = FastAPI()
    s3 = boto3.client('s3')

    BUCKET_NAME = "your-s3-bucket-name"

    @app.post("/upload-to-s3/")
    async def upload_video_to_s3(file: UploadFile = File(...)):
	# Stream the file directly from memory/temp disk to AWS S3
	s3.upload_fileobj(file.file, BUCKET_NAME, file.filename)
	
	return {"message": f"Successfully uploaded {file.filename} to S3!"}
    
    """

async def upload():
    pass
