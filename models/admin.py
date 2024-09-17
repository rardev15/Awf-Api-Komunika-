from pydantic import BaseModel, Field

class Admin(BaseModel):
  admin_id: int | None = None
  admin_name: str = Field(max_length=20)
  admin_pass: str = Field(max_length=20)
  admin_worker: str = Field(max_length=100)
  admin_rank: str = Field(max_length=10)