from .database import Base
from sqlalchemy import  Column, Integer,String


class User(Base):
    __tablename__='User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    contact = Column(String)
