from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import engine
from . import models
from .routers import resources, health
import logging

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
    )

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API running"}

#* prezando pela arquitetura, separando as rotas em arquivos diferentes, e incluindo elas na aplicação principal
app.include_router(resources.router)

app.include_router(health.router) 