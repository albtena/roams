from time import sleep

from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_, inspect, or_, desc, asc, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select


class Dao:

    MAX_ROWS = 1000
    MAX_ROWS_FRACTIONAL_QUERY = 20

    # Parametros a implementar por cada clase Dao
    database = None
    conn = None
    table = None

    limit = None
    offset = None

    async def insert(self, element_pydantic):
        try:
            element = self._init_object_sqlalchemy(element_pydantic)
            async with self.database as db:
                return await db.async_insert(element)

        except Exception as e:
            print("ERROR: Dao -> insert: " + str(e))
            return e

    async def update(self, element_pydantic):
        try:
            element = self._init_object_sqlalchemy(element_pydantic)
            async with self.database as db:
                return await db.async_merge(element)

        except Exception as e:
            print("ERROR: Dao -> update: " + str(e))
            return e

    async def get(self, element, ident=None):
        try:

            async with self.database as db:
                class_name = (
                    element.__class__
                )  # Devuelve que el nombre del tipo de objeto (Tabla en BBDD)
                if not ident:
                    mapper = inspect(class_name)
                    primary_key_name = mapper.primary_key[0].name
                    ident = getattr(element, primary_key_name)
                return await db.async_get(class_name, ident)

        except Exception as e:
            print("ERROR: Dao -> get: " + str(e))
            return e

    async def delete(self, element_pydantic, ident=None):
        try:
            element = self._init_object_sqlalchemy(element_pydantic)
            element_exists = await self.get(element, ident)

            async with self.database as db:
                if element_exists:
                    return await db.async_delete(element_exists)
                else:
                    return False
        except Exception as e:
            print("ERROR: Dao -> delete: " + str(e))
            return e

    async def exists(self, element, match_columns):
        try:
            async with self.database as db:
                filter_conditions = {
                    column.name: getattr(element, column.name)
                    for column in match_columns
                }
                stmt = select(element.__class__).filter_by(**filter_conditions)

                result = await db.async_query(stmt)
                element_exists = result.first()

                return True if element_exists else False

        except Exception as e:
            print("ERROR: Dao -> exists: " + str(e))
            return e

    async def get_or_insert(self, element, match_columns):
        try:
            async with self.database as db:
                filter_conditions = {
                    column.name: getattr(element, column.name)
                    for column in match_columns
                }
                stmt = select(element.__class__).filter_by(**filter_conditions)

                result = await db.async_query(stmt)
                result = result.first()

                if result:
                    element_exists = result[0]
                    return element_exists

                return await db.async_insert(element)

        except Exception as e:
            print("ERROR: Dao -> get_or_insert: " + str(e))
            return e

    def set_offset_limit(self, offset, limit):
        self.limit = limit
        self.offset = offset

    def _init_object_sqlalchemy(self, element_pydantic):
        try:
            attributes = element_pydantic.model_dump(
                exclude_none=True, exclude_unset=True
            )
            return self.table(**attributes)
        except Exception as e:
            print(f"ERROR: Dao -> init_object_sqlalchemy: " + str(e))
        return None
