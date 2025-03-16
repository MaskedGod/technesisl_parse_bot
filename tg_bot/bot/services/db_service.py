import sqlite3

DB_PATH = "db.sqlite"


def init_db():
    """Инициализация базы данных."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            xpath TEXT NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


def save_to_db(dataframe):
    """Сохранение данных в базу данных."""
    conn = sqlite3.connect(DB_PATH)
    dataframe.to_sql("products", conn, if_exists="append", index=False)
    conn.close()
