import sqlite3
import os


DB_PATH = "database/stories.db"


def connect():

    os.makedirs("database", exist_ok=True)

    return sqlite3.connect(DB_PATH)



def create_database():

    db = connect()

    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stories
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT UNIQUE,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    db.commit()
    db.close()



def story_exists(content):

    db = connect()

    cursor = db.cursor()

    cursor.execute(
        "SELECT id FROM stories WHERE content=?",
        (content,)
    )

    result = cursor.fetchone()

    db.close()

    return result is not None



def save_story(title, content):

    db = connect()

    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO stories(title,content)
        VALUES(?,?)
        """,
        (title, content)
    )

    db.commit()
    db.close()
