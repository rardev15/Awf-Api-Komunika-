import asyncpg
from fastapi import APIRouter, Depends
from models.company import Company
from repositories.company_repository import CompanyRepository

from typing import Union
from pydantic import BaseModel

class Response(BaseModel):
  code: int
  message: str
  data: None|dict|list

router = APIRouter()

tags_list = ["Company"]

@router.get("/company/", tags=tags_list)
async def get_company(repo:CompanyRepository = Depends(CompanyRepository)):
  result = await repo.get()
  return Response(code=200, message="Success", data=[dict(record) for record in result])

@router.post("/company/", tags=tags_list)
async def create_company(company:Company, repo:CompanyRepository = Depends(CompanyRepository)):
  result = await repo.create(company)
  return Response(code=200, message="Success", data=[dict(record) for record in result])

@router.put("/company/", tags=tags_list)
async def update_company(company:Company, repo:CompanyRepository = Depends(CompanyRepository)):
  result = await repo.update(company)
  if not result:
    return Response(code=200, message=f"Failed, company code {company.company_code} not found", data=None)
  else:
    return Response(code=200, message="Success", data=[dict(record) for record in result])

@router.delete("/company/{company_code}", tags=tags_list)
async def delete_company(company_code: str, repo:CompanyRepository = Depends(CompanyRepository)):
  result = await repo.delete(company_code)
  return Response(code=200, message="Success", data=[dict(record) for record in result])

@router.get("/company/{company_code}", tags=tags_list)
async def read_company(company_code: str, repo:CompanyRepository = Depends(CompanyRepository)):
  result = await repo.read(company_code)
  print(result)
  return result