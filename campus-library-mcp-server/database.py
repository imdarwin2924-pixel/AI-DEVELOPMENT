import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "library.db"


def get_connection():
    """Create and return a connection to the library database."""
    DATA_DIR.mkdir(exist_ok=True)
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():
    """Create the books table and insert initial catalog data."""
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT UNIQUE NOT NULL,
            category TEXT NOT NULL,
            total_copies INTEGER NOT NULL,
            available_copies INTEGER NOT NULL
        )
    """)

    books = [
        (
            "Python Crash Course",
            "Eric Matthes",
            "9781593279288",
            "Programming",
            5,
            5,
        ),
        (
            "Clean Code",
            "Robert C. Martin",
            "9780132350884",
            "Software Engineering",
            4,
            2,
        ),
        (
            "Artificial Intelligence: A Modern Approach",
            "Stuart Russell and Peter Norvig",
            "9780134610993",
            "Artificial Intelligence",
            3,
            1,
        ),
        (
            "Hands-On Machine Learning",
            "Aurélien Géron",
            "9781098125974",
            "Machine Learning",
            4,
            4,
        ),
        (
            "Database System Concepts",
            "Abraham Silberschatz",
            "9780078022159",
            "Database",
            6,
            5,
        ),
        (
            "The Pragmatic Programmer",
            "David Thomas and Andrew Hunt",
            "9780135957059",
            "Programming",
            3,
            2,
        ),
        (
            "Computer Networks",
            "Andrew S. Tanenbaum",
            "9780132126953",
            "Networking",
            4,
            4,
        ),
        (
            "Operating System Concepts",
            "Abraham Silberschatz",
            "9781119800361",
            "Operating Systems",
            5,
            3,
        ),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO books (
            title,
            author,
            isbn,
            category,
            total_copies,
            available_copies
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    initialize_database()
    print(f"Library database initialized at: {DATABASE_PATH}")