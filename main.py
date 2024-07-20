import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from DataBase.schemas.schemas_users import SUser, SUserAdd
from DataBase.database import get_db, engine
from DataBase.models import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.get("/sign_in")
def sign_in(email:str,password:str,db:Session=Depends(get_db)):
    user= db.query(models.User).filter(models.User.email==email).first()
    if not user:
        raise  HTTPException(status_code=400,detail="invalid email or password")
    if not pwd_context.verify(password,user.password):
        raise  HTTPException(status_code=400,detail="invalid email or password")
    return {"message":"sign in successful"}

@app.post("/sign_up", response_model=SUser)
def sign_up(user:SUserAdd,db:Session=Depends(get_db)):
    hash_password = pwd_context.hash(user.password)
    db_user = models.User(username = user.name,email = user.email ,password = hash_password)
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        return SUser.from_orm(db_user)
    except InterruptedError:
        db.rollback()
        raise  HTTPException(status_code=400,detail="User with this email already exists")

if __name__ == "__main__":
    import asyncio
    from uvicorn import Config , Server
    config = Config(app=app,host="127.0.0.1",port=8000)
    server = Server(config=config)
    asyncio.run(server.serve())



