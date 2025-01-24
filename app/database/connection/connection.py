from time import sleep

from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker


from app.util import asynchrony as Async


class Connection:
    # Para sesiones SQLAlchemy
    session = None
    engine = None

    driver = None
    username = None
    passwd = None
    host = None
    port = None
    db_name = None

    ################################################################
    ######################### SQLAlchemy ###########################
    ################################################################
    def new_conn(self):
        try:
            return (
                str(self.driver)
                + "://"
                + str(self.username)
                + ":"
                + str(self.passwd)
                + "@"
                + str(self.host)
                + ":"
                + str(self.port)
                + "/"
                + str(self.db_name)
            )

        except Exception as e:
            print("ERROR: Connection -> new_conn: " + str(e))

        return None

    def __enter__(self):
        self.session = self._create_session()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.session.close()
        self.session = None

    def _create_session(self):
        self.engine = create_engine(self.new_conn())
        session_maker = sessionmaker(bind=self.engine, expire_on_commit=False)
        return session_maker()

    async def __aenter__(self):
        self.session = await self._create_async_session()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self.session:
            await self.session.close()
            self.session = None

        if self.engine:
            await self.engine.dispose()
            self.engine = None

    async def _create_async_session(self):
        try:
            self.engine = create_async_engine(self.new_conn())
            async_session_maker = async_sessionmaker(
                self.engine, expire_on_commit=False
            )
            return async_session_maker()

        except Exception as e:
            print("ERROR: Connection -> create_async_session: " + str(e))

    ##################################
    # Operaciones NATIVAS ASINCRONAS #
    ##################################
    async def async_query(self, stmt):
        try:
            async with self.session.begin():
                return await self.session.execute(stmt)
        except Exception as e:
            print("ERROR: Connection -> async_query: " + str(e))
            return e

    async def async_get(self, element, ident):
        try:
            async with self.session.begin():
                result = await self.session.get(element, ident)
                return result
        except Exception as e:
            print("ERROR: Connection -> async_get: " + str(e))
            return e

    async def async_insert(self, element):
        try:
            async with self.session.begin():
                self.session.add(element)
                return element
        except Exception as e:
            print("ERROR: Connetion -> async_insert: " + str(e))
            return e

    async def async_merge(self, element):
        try:
            async with self.session.begin():
                await self.session.merge(element)
        except Exception as e:
            print("ERROR: Connetion -> async_merge: " + str(e))
            return e

        return element

    async def async_delete(self, element):
        try:
            async with self.session.begin():
                await self.session.delete(element)
                return True
        except Exception as e:
            print("ERROR: Connetion -> async_delete: " + str(e))
            return e
