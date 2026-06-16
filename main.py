from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_db_connection
from psycopg2.extras import RealDictCursor
from typing import Optional

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

@app.get("/storages")
def get_storages(sort_by: Optional[str] = None):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    
    query = "SELECT * FROM cold_storages WHERE available_slots > 0"
    
    if sort_by == "price":
        query += " ORDER BY price_per_slot ASC"
    elif sort_by == "slots":
        query += " ORDER BY available_slots DESC"
        
    query += ";"
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return {"storages": results}
