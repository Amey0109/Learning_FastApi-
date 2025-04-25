from pydantic import BaseModel

# Schema or structure of data 
class Blog(BaseModel):
    title: str
    body: str

# Get response only of title and body not id
class ShowBlog(BaseModel):
    title: str
    body: str 
    class Config():
        from_attributes=True

class User(BaseModel):
    name: str
    email: str
    password: str
    class Config():
        from_attributes=True