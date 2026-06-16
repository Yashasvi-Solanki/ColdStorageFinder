from fastapi import FastAPI
from database import get_db_connection
from psycopg2.extras import RealDictCursor

app = FastAPI()

@app.get("/storages")
def get_storages():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM cold_storages;")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"storages": results}
