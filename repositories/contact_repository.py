from typing import List, Optional
from fastapi import Depends
from models.contacts import Contacts
from base.repository import Repository
from db_read import DatabaseRead, database_instance_read
from db_write import DatabaseWrite, database_instance_write

class ContactRepository(Repository):

    def __init__(self, db_read:DatabaseRead = Depends(database_instance_read), db_write:DatabaseWrite = Depends(database_instance_write)):
        super().__init__(db_read, db_write)

    async def get(self)->List[Contacts]:
        query = """
            SELECT * FROM master_contact
        """
        result = await self._db_read.fetch_rows(query, None)
        return result

    async def create(self, data:Contacts)->Contacts:
        query = """
            insert
                into
                public.master_contact
            (
                contact_name,
                contact_initial,
                contact_company,
                contact_address1,
                contact_address2,
                contact_birthday,
                contact_office_phone,
                contact_fax_phone,
                contact_mobile_phone,
                contact_home_phone,
                contact_status,
                contact_worker,
                contact_multi,
                contact_active,
                contact_remark)
            values(
            $1,
            $2,
            $3,
            $4,
            $5,
            $6,
            $7,
            $8,
            $9,
            $10,
            $11,
            $12,
            $13,
            $14, $15);
        """
        result = await self._db_write.execute(query,[data.contact_name, data.contact_initial, data.contact_company, data.contact_address1, data.contact_address2, data.contact_birthday, data.contact_office_phone,data.contact_fax_phone,data.contact_mobile_phone,data.contact_home_phone,data.contact_status,data.contact_worker,data.contact_multi,data.contact_active,data.contact_remark])
        return result

    async def delete(self, contacts_id):
        query = "DELETE FROM master_contact WHERE contact_id=$1"
        result = await self._db_write.execute(query, [contacts_id])
        return result

    async def update(self, data:Contacts)->Contacts:
        query = "UPDATE master_contact SET contact_name = $1, contact_initial = $2, contact_company = $3, contact_address1 = $4, contact_address2 = $5, contact_birthday = $6, contact_office_phone = $7, contact_fax_phone = $8, contact_mobile_phone = $9, contact_home_phone = $10, contact_status = $11, contact_worker = $12,  contact_multi = $13, contact_active = $14, contact_remark = $15 WHERE contact_id = $16 RETURNING *"
        result = await self._db_write.execute(query, [data.contact_name, data.contact_initial, data.contact_company, data.contact_address1, data.contact_address2, data.contact_birthday, data.contact_office_phone,data.contact_fax_phone,data.contact_mobile_phone,data.contact_home_phone,data.contact_status,data.contact_worker,data.contact_multi,data.contact_active,data.contact_remark, data.contact_id])
        return result

    async def read(self, contacts_id):
        query = "SELECT * FROM master_contact WHERE contact_id = $1"
        result = await self._db_read.fetch_rows(query, contacts_id)
        return result