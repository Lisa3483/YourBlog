import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class SUserAdd(BaseModel):
    name:str
    email:str
    password:str

class SUser(SUserAdd):
    id:int


'''@app.post("/sign_up")
async def sign_up(user:SUserAdd):
    users.append(user)
    return True     '''

@app.get("/sign_up")
def sign_in():
    a = "123"
    return {"data":a}       

