import os
import sqlite3
import uuid


class Database:
    def __init__(self, db_path: str = os.path.join(os.path.dirname(__file__), "db.sql")):
        self.db_path = db_path

    def __enter__(self):
        self.db_conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.db_conn.cursor()
        return self.cursor

    def __exit__(self, *args):
        self.db_conn.commit()
        self.db_conn.close()

    def __del__(self):
        self.db_conn.close()


def init_dataset():
    with Database() as db:
        db.execute("DROP TABLE IF EXISTS accounts")
        db.execute("CREATE TABLE IF NOT EXISTS accounts (username TEXT, password TEXT, amount INTEGER)")
        db.execute("INSERT INTO accounts VALUES ('user1', 'password', 100500)")
