from typing import List, Optional
from fastapi import Depends
from datetime import datetime
from models.company import Company
from base.repository import Repository
from db_read import DatabaseRead, database_instance_read
from db_write import DatabaseWrite, database_instance_write
from repositories.helpers.get_current_timestamps import now


class CompanyRepository(Repository):

    def __init__(self, db_read:DatabaseRead = Depends(database_instance_read), db_write:DatabaseWrite = Depends(database_instance_write)):
        super().__init__(db_read, db_write)

    async def get(self)->List[Company]:
        query = "SELECT * FROM company"
        result = await self._db_read.fetch_rows(query, None)
        return result

    async def create(self, data:Company)->Company:
        query = """INSERT INTO company(company_code, company_name, company_industry, company_address1, company_address2, company_address3, company_city, company_zip_code, company_phone1, company_phone2, company_phone3, company_fax, company_email, company_notes)values($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14) RETURNING *;"""
        result = await self._db_write.execute(query, [data.company_code, data.company_name, data.company_industry, data.company_address1, data.company_address2, data.company_address3, data.company_city, data.company_zip_code, data.company_phone1, data.company_phone2, data.company_phone3, data.company_fax, data.company_email, data.company_notes])
        return result

    async def update(self, data:Company)->Company:
        query = """UPDATE company SET company_name = $1, company_industry = $2, company_address1 = $3, company_address2 = $4, company_address3 = $5, company_city = $6, company_zip_code = $7, company_phone1 = $8, company_phone2 = $9, company_phone3 = $10, company_fax = $11, company_email = $12, company_notes = $13, updated_on = $14 WHERE company_code = $15 RETURNING *"""
        result = await self._db_write.execute(query, [data.company_name, data.company_industry, data.company_address1, data.company_address2, data.company_address3, data.company_city, data.company_zip_code, data.company_phone1, data.company_phone2, data.company_phone3, data.company_fax, data.company_email, data.company_notes, now, data.company_code])
        return result

    async def delete(self, company_code):
        query = """DELETE FROM company WHERE company_code = $1 RETURNING *"""
        result = await self._db_write.execute(query, [company_code])
        return result

    async def read(self, company_code):
        query = """SELECT * FROM company WHERE company_code = $1"""
        result = await self._db_read.fetch_rows(query, [company_code])
        print(result)
        return result