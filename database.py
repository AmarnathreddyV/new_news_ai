import sqlite3

conn = sqlite3.connect(
    "data/articles.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    headline TEXT,
    summary TEXT,
    sentiment TEXT,
    category TEXT
)
""")

conn.commit()

def save_article_db(
    url,
    headline,
    summary,
    sentiment,
    category
):

    cursor.execute("""
    INSERT INTO articles
    (
        url,
        headline,
        summary,
        sentiment,
        category
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        url,
        headline,
        summary,
        sentiment,
        category
    ))

    conn.commit()