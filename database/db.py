import sqlite3

from abc import ABC, abstractmethod


class Database(ABC):
    """
    Database context manager
    """
    def __init__(self, driver) -> None:
        self.driver = driver

    @abstractmethod
    def connect_to_database(self):
        pass

    def __enter__(self):
        self.connection = self.connect_to_database()
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exception_type, exc_val, traceback):
        self.cursor.close()
        self.connection.close()


class SQLiteDatabase(Database):
    """
    SQLite database context manager
    """
    DB_NAME = "wallet.db"  # .env

    def __init__(self) -> None:
        self.driver = sqlite3
        super().__init__(self.driver)

    def connect_to_database(self):
        return self.driver.connect(self.DB_NAME)


sqlite_db = SQLiteDatabase()
