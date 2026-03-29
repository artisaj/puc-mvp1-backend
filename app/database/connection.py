import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[2] / "kart.db"


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pilotos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            numero_kart INTEGER NOT NULL,
            equipe TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS corridas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_corrida TEXT NOT NULL,
            resultado_json TEXT NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()
