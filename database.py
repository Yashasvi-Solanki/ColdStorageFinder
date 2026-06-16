import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv


load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = f"postgresql://postgres:{DB_PASSWORD}@localhost:5432/agri_storage"

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn
