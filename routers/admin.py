import asyncpg
from fastapi import APIRouter, Depends
from jwt import JWTBearer
from models.admin import Admin
from repositories.admin_repository import AdminRepository

from typing import Union
from pydantic import BaseModel

class Response(BaseModel):
  code: int
  message: str
  data: None|dict|list

router = APIRouter()

tags_list = ["admin"]

@router.get("/admin/", tags=tags_list)
async def get_admin(repo:AdminRepository = Depends(AdminRepository),dependencies=[Depends(JWTBearer())]):
  result = await repo.get()
  return result

@router.post("/admin/", tags=tags_list)
async def create_admin(admin:Admin, repo:AdminRepository = Depends(AdminRepository)):
  result = await repo.create(admin)
  print(result)
  return Response(code=200, message="Success", data=dict(result[0]))
