from db import sqlite_db


class DbService:
    def __init__(self):
        self.sqlite_service = sqlite_db

    def drop_tables(self, table_name):
        with self.sqlite_service as db:
            db.cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            db.connection.commit()
            print("Tables are dropped...")
