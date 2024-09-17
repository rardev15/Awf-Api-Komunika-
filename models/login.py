from pydantic import BaseModel, Field

class Login(BaseModel):
  admin_name: str = Field(max_length=20)
  admin_pass: str = Field(max_length=20)
