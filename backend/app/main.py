from fastapi import FastAPI
from .db import engine
from . import models
from .routers import resources

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API running"}

app.include_router(resources.router) #* prezando pela arquitetura, separando as rotas em arquivos diferentes, e incluindo elas na aplicação principal