from pydantic import BaseModel, Field

class Company(BaseModel):
  company_code: str = Field(max_length=10)
  company_name: str = Field(max_length=80, default="")
  company_industry: str = Field(max_length=50, default="")
  company_address1: str = Field(max_length=200, default="")
  company_address2: str = Field(max_length=200, default="")
  company_address3: str = Field(max_length=200, default="")
  company_city: str = Field(max_length=50, default="")
  company_zip_code: str = Field(max_length=10, default="")
  company_phone1: str = Field(max_length=50, default="")
  company_phone2: str = Field(max_length=50, default="")
  company_phone3: str = Field(max_length=50, default="")
  company_fax: str = Field(max_length=50, default="")
  company_email: str = Field(max_length=100, default="")
  company_notes: str = ""