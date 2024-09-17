from typing import Union
from routers import admin, company, login, users, contacts
from fastapi import FastAPI, Depends
from db_read import database_instance_read
from db_write import database_instance_write
from contextlib import asynccontextmanager
from repositories.user_repository import UserRepository

@asynccontextmanager
async def db_pool_lifespan_read(app: FastAPI):
    print("Start DBRead Pooling...")
    print(database_instance_read)
    yield await database_instance_read.connect()
    print("End of Pooling DBRead...")

@asynccontextmanager
async def db_pool_lifespan_write(app: FastAPI):
    print("Start DBWrite Pooling...")
    print(database_instance_write)
    yield await database_instance_write.connect()
    print("End of Pooling DBWrite...")

@asynccontextmanager
async def db_pool_lifespan(app: FastAPI):
    print("Start DB Pooling...")
    print(database_instance_read)
    print(database_instance_write)
    await database_instance_read.connect()
    await database_instance_write.connect()
    yield {"database_instance_read":database_instance_read, "database_instance_write":database_instance_write}
    print("End of DB Pooling...")

app = FastAPI(lifespan=db_pool_lifespan)
# app.include_router(users.router)
app.include_router(contacts.router)
app.include_router(company.router)
app.include_router(admin.router)
app.include_router(login.router)

@app.get("/")
async def hello_world():
    return {"hello":"world"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}