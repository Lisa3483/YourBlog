from pydantic import BaseModel


class SUserAdd(BaseModel):
    name:str
    email:str
    password:str

class SUser(SUserAdd):
    id:int
    name:str
    email:str
    
    class Config:
        orm_mod:True