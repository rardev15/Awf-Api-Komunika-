from fastapi import Depends
from models.users import Users
from base.repository import Repository
from db_read import DatabaseRead, database_instance_read
from db_write import DatabaseWrite, database_instance_write

class UserRepository(Repository):
    
    def __init__(self, db_read:DatabaseRead = Depends(database_instance_read), db_write:DatabaseWrite = Depends(database_instance_write)):
        super().__init__(db_read, db_write)
    
    async def get(self):
        result = Users.model_validate(dict(await self._db_read.fetch_rows("SELECT * FROM users")))
        print(result)
        return result