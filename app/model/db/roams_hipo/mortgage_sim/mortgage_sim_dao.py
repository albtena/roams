from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_, or_
from sqlalchemy.future import select
from app.model.db.dao import Dao
from app.model.db.roams_hipo.repository_roams_hipo import *
from app.database.roams_hipo import RoamsHipo


class MortgageSimDao(Dao):
    def __init__(self):
        self.database = RoamsHipo()
        self.conn = self.database.new_conn()
        self.table = MortgageSim

    async def get_mortgage_sims(self, element_pydantic):
        try:
            async with self.database as db:

                query = select(MortgageSim)
                query = query.filter(and_(MortgageSim.dni == element_pydantic.dni))

                result_query = await db.async_query(query)
                list = result_query.scalars().all()

                return list if list else None

        except Exception as e:
            print(f"ERROR: RoamsHipo MortgageSimDao -> get_mortgage_sims: " + str(e))
            return e
