from .database import Base
from sqlalchemy import Column, Integer, String


class Events(Base):
    __tablename__ = 'Events'
    __table_args__ = {'schema': 'dbo'}

    id= Column(Integer, primary_key=True, index=True)
    EventName= Column(String)
    Code= Column(String)
    StartDate= Column(String)
    EndDate= Column(String)

class User(Base):
    __tablename__ = 'Users'
    __table_args__ = {'schema': 'dbo'}

    id= Column(Integer, primary_key=True, index=True)
    username= Column(String)
    password= Column(String)
    phone_number= Column(String)
