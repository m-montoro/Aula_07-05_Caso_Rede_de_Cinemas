import sqlite3

DB_PATH = "cinema.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS cinemas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            capacidade INTEGER NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            diretor TEXT NOT NULL,
            genero TEXT NOT NULL,
            duracao_min INTEGER NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS sessoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filme_id INTEGER NOT NULL,
            cinema_id INTEGER NOT NULL,
            horario TEXT NOT NULL,
            sala TEXT NOT NULL,
            publico INTEGER DEFAULT 0,
            FOREIGN KEY (filme_id) REFERENCES filmes(id),
            FOREIGN KEY (cinema_id) REFERENCES cinemas(id)
        )
    """)

    conn.commit()
    return conn
