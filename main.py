from typing import List
from fastapi import FastAPI, Depends, status, HTTPException
from .import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm  import Session

# Creating Instance
app= FastAPI()

# creating all models in database
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()        # Create a new database session
    try:
        yield db               # Give it to the path operation function (temporarily)
    finally:
        db.close()             # Close the session when the request is done


# Post method to insert data to database
@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db:Session= Depends(get_db)):
    new_blog= models.Blog(title=request.title, body= request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# Delete method to delete data
@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session= Depends(get_db)):
   blog= db.query(models.Blog).filter(models.Blog.id==id)
   if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog of id {id} is not available')
   
   blog.delete(synchronize_session=False)
   db.commit()
   return 'Deleted Successfully'

# Put method to update data
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db:Session= Depends(get_db)):
    blog= db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog of id {id} is not available')
    blog.update(request.model_dump()) # converting pydantic model into dictionery for updating
    db.commit()
    return 'Updated Successfully'


# Get method to fetch all data from database
@app.get('/blog', response_model= List[schemas.ShowBlog])
def all_data(db:Session= Depends(get_db)):
    blogs= db.query(models.Blog).all()
    return blogs

# Get method to fetch data by id
@app.get('/blog/{id}', status_code=200, response_model= schemas.ShowBlog)
def show_by_id(id,db:Session= Depends(get_db)):
    blog= db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The blog of id {id} is not available')
    return blog
