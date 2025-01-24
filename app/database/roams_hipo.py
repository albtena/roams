import os
from app.database.connection.connection_sqlite import SqLiteDB
from app.util import path as Path


class RoamsHipo(SqLiteDB):

    def __init__(self):
        # En caso de una conexión mas compleja...
        # self.username = os.getenv("DATABASE_ROAMS_HIPO_USER")
        # self.passwd = os.getenv("DATABASE_ROAMS_HIPO_PASSWORD")
        # self.host = os.getenv("DATABASE_ROAMS_HIPO_HOST")
        # self.port = int(os.getenv("DATABASE_ROAMS_HIPO_PORT"))
        # self.db_name = os.getenv("DATABASE_ROAMS_HIPO_NAME")

        db_name = os.getenv("DATABASE_ROAMS_HIPO_DB")
        self.db_path = os.path.join(Path.get_current_path(), db_name)
