from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..hashing import Hash

def create(request: schemas.User, db:Session):    
    new_user= models.User(name= request.name, email=request.email, password=Hash.bcrypt(request.password) ) # storing password in hash or encrypted code
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id: int, db:Session):
    user= db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The User of id {id} is not available')
    return user