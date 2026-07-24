from fastapi import FastAPI
import sqlite3
app = FastAPI(title="SQLite3 Learning")


conn = sqlite3.connect("test.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos(
               id INTEGER PRIMARY KEY,
               TITLE TEXT,
               STATUS TEXT
               )
""")
conn.commit()