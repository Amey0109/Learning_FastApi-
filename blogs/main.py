from fastapi import FastAPI
from .import models
from .database import engine
from .routers import blog, user, authentication
# Creating Instance
app= FastAPI()

# creating all models in database
models.Base.metadata.create_all(engine)

# Adding Login routes
app.include_router(authentication.router)

# Adding blogs routes
app.include_router(blog.router)

#Adding user routes
app.include_router(user.router)






