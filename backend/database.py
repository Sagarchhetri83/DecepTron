import sqlite3
from config import DB_FILE

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS attacks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ip TEXT,
                    port INTEGER,
                    payload TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    conn.close()

def log_attack(ip, port, payload):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO attacks (ip, port, payload) VALUES (?, ?, ?)", (ip, port, payload))
    conn.commit()
    conn.close()
