import sqlite3
from pathlib import Path
from datetime import datetime
import logging

# The database file will be in the 'data' folder in the project root
DB_PATH = Path(__file__).parent.parent / "data" / "deceptron_logs.db"

def initialize_database():
    """Creates the database and the logs table if they don't exist."""
    try:
        # Ensure the parent directory ('data') exists
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS interactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                ip_address TEXT NOT NULL,
                port INTEGER NOT NULL,
                input_command TEXT,
                response TEXT
            )
        ''')
        conn.commit()
        conn.close()
        logging.info(f"Database initialized successfully at {DB_PATH}")
    except Exception as e:
        logging.error(f"Failed to initialize database: {e}")

def log_interaction(ip, port, command, response):
    """Logs a single interaction into the SQLite database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute(
            "INSERT INTO interactions (timestamp, ip_address, port, input_command, response) VALUES (?, ?, ?, ?, ?)",
            (timestamp, ip, port, command, response)
        )
        conn.commit()
        conn.close()
    except Exception as e:
        logging.error(f"Failed to log interaction: {e}")