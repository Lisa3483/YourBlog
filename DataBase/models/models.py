from sqlalchemy import  Column, Integer, String , create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    

    

def create_tables():
    engine = create_engine("postgresql://postgres:123@localhost/YourBlog")
    Base.metadata.create_all(engine)

create_tables()