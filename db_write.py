from multiprocessing.pool import Pool
import asyncpg
from env.db_env import db_env

class DatabaseWrite():

    def __init__(self):
        self.user = db_env.database_username
        self.password = db_env.database_password
        self.host = db_env.database_hostname
        self.port = "5432"
        self.database = db_env.database_name
        self._cursor = None

        self._connection_pool:asyncpg.Pool = None
        self.con:asyncpg.Connection = None

        print("Database initialized")
        print(self)

    def __call__(self):
        print(self)
        return self

    async def connect(self):
        print("Connect")
        if not self._connection_pool:
            try:
                self._connection_pool = await asyncpg.create_pool(
                    min_size=1,
                    max_size=100,
                    command_timeout=60,
                    host=self.host,
                    port=self.port,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                )
            except Exception as e:
                print(e)

    async def execute(self, query: str, param:list):
        if not self._connection_pool:
            await self.connect()
        else:
            self.con = await self._connection_pool.acquire()
            try:
                result = await self.con.fetch(query, *param)
                return result
            except Exception as e:
                print(e)
            finally:
                await self._connection_pool.release(self.con)

database_instance_write: DatabaseWrite = DatabaseWrite()