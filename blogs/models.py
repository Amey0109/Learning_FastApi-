from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

#creating table structure for database to store data
class Blog(Base):
    __tablename__='blogs'

    id= Column(Integer, primary_key=True, index=True)
    title= Column(String)
    body= Column(String)
    # making foreign key to connect with user table
    user_id= Column(Integer, ForeignKey('users.id'))

    # making relationship with user table
    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__='users'

    id= Column(Integer, primary_key=True, index=True)
    name= Column(String)
    email= Column(String)
    password= Column(String)

    # making relationship with blogs table
    blogs= relationship('Blog', back_populates='creator')
