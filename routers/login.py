import bcrypt
import asyncpg
from fastapi import APIRouter, Depends
from models.login import Login
from repositories.admin_repository import AdminRepository

from typing import Union
from pydantic import BaseModel

class Response(BaseModel):
  code: int
  message: str|bool
  data: None|dict|list

router = APIRouter()

tags_list = ["Login"]

@router.post("/login/", tags=tags_list)
async def login(login:Login, repo:AdminRepository = Depends(AdminRepository)):
  result = await repo.login(login)
  # konidisi 1. dimana jika username salah, maka password pun pasti salah karena untuk mendapatkan password yang di input oleh user yang akan digunakan sebagai pembanding pada password yang sesungguhnya diperlukan username yang benar agar query berhasil mendapatkan 1 row data termasuk password yang sesungguhnya.
  if not result:
    return Response(code=500, message="Username atau password tidak ditemukan!", data=None)
  # kondisi 2, dimana jika username nya betul maka query akan berhasil mendapatkan 1 row data
  else:
    result = result[0]
    userBytes = login.admin_pass.encode('utf-8')
    # checking password
    password = result["admin_pass"].encode('utf-8')
    result = bcrypt.checkpw(userBytes, password)
    # cek apakah password true, jika true maka artinya username dan password nya sudah benar
    if (result):
      
      return Response(code=200, message="Login Success!", data=None)
    # namun jika false, maka hanya username nya saja yang betul, dan untuk keamanan. berikan informasi bahwa ada username atau password yang salah tanpa memberitahu secara spesifik mana yang salah sesungguhnnya.
    else:
      return Response(code=500, message="Username or password is invalid!", data=None)
