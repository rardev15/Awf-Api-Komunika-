from pydantic import BaseModel, Field

class Contacts(BaseModel):
    contact_id: int | None = None
    contact_name: str = Field(max_length=100)
    contact_initial:str = Field(max_length=5)
    contact_company:str = Field(max_length=100, default="")
    contact_address1:str = Field(max_length=100, default="")
    contact_address2:str = Field(max_length=100, default="")
    contact_birthday:str = Field(max_length=100, default="")
    contact_office_phone:str = Field(max_length=30, default="")
    contact_fax_phone:str = Field(max_length=30, default="")
    contact_mobile_phone:str = Field(max_length=30, default="")
    contact_home_phone:str = Field(max_length=30, default="")
    contact_status:str = Field(max_length=30, default="")
    contact_worker:bool
    contact_multi:bool
    contact_active:bool
    contact_remark:str = ""