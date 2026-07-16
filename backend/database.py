import psycopg

CONNECTION="postgresql://youtube:youtube@0.0.0.0:5432/youtube"

def query(statement):
    with psycopg.connect(CONNECTION) as conn:
        with conn.cursor() as cursor:
            return cursor.execute(statement)
    
def execute(statement, params):
    with psycopg.connect(CONNECTION) as conn:
        with conn.cursor() as cursor:
            return cursor.execute(statement, params)
    
