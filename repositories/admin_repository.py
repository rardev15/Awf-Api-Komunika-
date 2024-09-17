import bcrypt
from typing import List, Optional
from fastapi import Depends
from models.admin import Admin
from base.repository import Repository
from db_read import DatabaseRead, database_instance_read
from db_write import DatabaseWrite, database_instance_write
from models.login import Login

class AdminRepository(Repository):
    def __init__(self, db_read:DatabaseRead = Depends(database_instance_read), db_write:DatabaseWrite = Depends(database_instance_write)):
          super().__init__(db_read, db_write)

    async def get(self)->List[Admin]:
      query = """SELECT * FROM admin"""
      result = await self._db_read.fetch_rows(query, None)
      return result

    async def create(self, data:Admin)->Admin:
      bytes = data.admin_pass.encode('utf-8')
      salt = bcrypt.gensalt()
      hash = bcrypt.hashpw(bytes, salt)
      query = """INSERT INTO admin (admin_name, admin_pass, admin_worker, admin_rank) VALUES ($1, $2, $3, $4) RETURNING *"""
      result = await self._db_write.execute(query, [data.admin_name, hash.decode('utf-8'), data.admin_worker, data.admin_rank])
      return result

    async def login(self, data:Login)->Login|None:
      query = """SELECT * FROM admin WHERE admin_name = $1"""
      result = await self._db_read.fetch_rows(query, [data.admin_name])
      if(len(result) > 0):
         return [dict(record) for record in result]
      return None