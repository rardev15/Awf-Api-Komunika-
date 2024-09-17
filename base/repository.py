from fastapi import Depends
from db_read import DatabaseRead, database_instance_read
from db_write import DatabaseWrite, database_instance_write

class Repository:
    
    _db_read:DatabaseRead
    
    _db_write:DatabaseWrite
    
    def __init__(self, db_read:DatabaseRead = Depends(database_instance_read), db_write:DatabaseWrite = Depends(database_instance_write)):
        self._db_read = db_read
        self._db_write = db_write