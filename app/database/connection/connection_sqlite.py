from time import sleep
from app.database.connection.connection import Connection


class SqLiteDB(Connection):
    driver = "sqlite+aiosqlite"

    db_path = None

    def new_conn(self):
        """
        Genera la URL de conexión para SQLite.
        """
        try:
            return f"{self.driver}:///{self.db_path}"  # Genera la conexión con SQLite
        except Exception as e:
            print("ERROR: SQLiteDB -> new_conn: " + str(e))
            return None
