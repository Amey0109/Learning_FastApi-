from fastapi import APIRouter, Depends, status
from .. import schemas, database
from sqlalchemy.orm  import Session
from ..repository import user_logic

router= APIRouter(
    prefix="/user",
    tags=['User']
)

get_db=database.get_db

# Post Method to create User
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db:Session= Depends(get_db)):
    return user_logic.create(request, db)

# Get Method to fetch data
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show_user(id: int, db:Session= Depends(get_db)):
    return user_logic.show(id, db)