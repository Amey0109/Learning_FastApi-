from fastapi import FastAPI
from .routers import orm_query, normal_query, procedure,user, authrntication
from . import models
from . database import engine

app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authrntication.router)
app.include_router(user.router)
app.include_router(orm_query.router)
app.include_router(normal_query.router)
app.include_router(procedure.router)






