TABLE="""
    CREATE TABLE IF NOT EXISTS videos
    id TEXT PRIMARY KEY, -- UUID
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    title TEXT,
    description TEXT,
    views INT,
    likes INT
"""

def setup():
    pass

def connect():
    pass
    
