import asyncpg
from fastapi import APIRouter, Depends
from models.contacts import Contacts
from repositories.contact_repository import ContactRepository

from typing import Union
from pydantic import BaseModel

class Response(BaseModel):
    code: int
    message: str
    data:None|dict|list

router = APIRouter()

tags_list = ["Contacts"]

@router.get("/contacts/", tags=tags_list)
async def get_contacts(repo:ContactRepository = Depends(ContactRepository)):
    result = await repo.get()
    # return result
    return Response(code=200,message="Success",data=[dict(record) for record in result])

@router.post("/contacts", tags=tags_list)
async def create_contact(contacts:Contacts, repo:ContactRepository = Depends(ContactRepository)):
    result = await repo.create(contacts)
    return result

@router.delete("/contacts/{contacts_id}", tags=tags_list)
async def delete_contact(contacts_id: int, repo:ContactRepository = Depends(ContactRepository)):
    result = await repo.delete(contacts_id)
    print(contacts_id)
    return result

@router.put("/contacts/", tags=tags_list)
async def update_contact(contacts:Contacts, repo:ContactRepository = Depends(ContactRepository)):
    result = await repo.update(contacts)
    if not result:
        return Response(code=500,message="ID tidak ditemukan",data=None)
    else:
        return Response(code=200,message="Success",data=dict(result[0]))

@router.get("/contacts/{contacts_id}", tags=tags_list)
async def read_contact(contacts_id: int, repo:ContactRepository = Depends(ContactRepository)):
    result = await repo.read(contacts_id)
    return result