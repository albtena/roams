from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_, or_
from sqlalchemy.future import select
from app.model.db.dao import Dao
from app.model.db.roams_hipo.repository_roams_hipo import *
from app.database.roams_hipo import RoamsHipo


class UserDao(Dao):
    def __init__(self):
        self.database = RoamsHipo()
        self.conn = self.database.new_conn()
        self.table = User

    async def get_user(self, element_pydantic):
        try:
            async with self.database as db:

                query = select(User)
                query = query.filter(and_(User.dni == element_pydantic.dni))

                result_query = await db.async_query(query)
                user = result_query.scalars().all()

                return user[0] if user else None

        except Exception as e:
            print(f"ERROR: RoamsHipo UserDao -> get_user: " + str(e))
            return e
