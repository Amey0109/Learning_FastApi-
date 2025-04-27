from fastapi import APIRouter, Depends, status
from .. import schemas, database
from typing import List
from sqlalchemy.orm  import Session
from ..repository import blog_logic

get_db= database.get_db
router= APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

# Get method to fetch all data from database
@router.get('/', response_model= List[schemas.ShowBlog])
def all_data(db:Session= Depends(get_db)):
    return blog_logic.get_all(db)

# Post method to insert data to database
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db:Session= Depends(get_db)):
    return blog_logic.create(request, db)

# Delete method to delete data
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db:Session= Depends(get_db)):
    return blog_logic.destroy(id,db)

# Put method to update data
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db:Session= Depends(get_db)):
    return blog_logic.update(id, request,db)

# Get method to fetch data by id
@router.get('/{id}', status_code=200, response_model= schemas.ShowBlog)
def show_by_id(id,db:Session= Depends(get_db)):
    return blog_logic.show(id,db)

