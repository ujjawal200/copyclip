import sqlite3
import os
from datetime import datetime

DB_DIR = os.path.expanduser("~/.copyclip")
DB_PATH = os.path.join(DB_DIR, "history.db")
MAX_ITEMS = 20


def _connect():
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS clips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )"""
    )
    conn.commit()
    return conn


def add_clip(text: str):
    text = text.strip()
    if not text:
        return
    conn = _connect()
    # Remove duplicate if exists
    conn.execute("DELETE FROM clips WHERE text = ?", (text,))
    conn.execute(
        "INSERT INTO clips (text, timestamp) VALUES (?, ?)",
        (text, datetime.now().isoformat()),
    )
    # Keep only last MAX_ITEMS
    conn.execute(
        "DELETE FROM clips WHERE id NOT IN (SELECT id FROM clips ORDER BY id DESC LIMIT ?)",
        (MAX_ITEMS,),
    )
    conn.commit()
    conn.close()


def get_clips() -> list[tuple[int, str, str]]:
    conn = _connect()
    rows = conn.execute(
        "SELECT id, text, timestamp FROM clips ORDER BY id DESC LIMIT ?", (MAX_ITEMS,)
    ).fetchall()
    conn.close()
    return rows


def clear_all():
    conn = _connect()
    conn.execute("DELETE FROM clips")
    conn.commit()
    conn.close()
