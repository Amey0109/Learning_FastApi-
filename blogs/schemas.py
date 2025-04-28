from typing import List
from pydantic import BaseModel

# Schema or structure of data 
class BlogBase(BaseModel):
    title: str
    body: str

# for response body of blog 
class Blog(BlogBase):
    class Config():
        from_attributes=True


class User(BaseModel):
    name: str
    email: str
    password: str
    class Config():
        from_attributes=True

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]=[] # adding one more column in response body for blogs data
    class Config():
        from_attributes= True

# Get response only of title and body not id
class ShowBlog(BaseModel):
    title: str
    body: str 
    creator: ShowUser # adding one more column in response body for user data
    class Config():
        from_attributes=True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None