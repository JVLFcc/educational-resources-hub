from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .schemas import ResourceCreate, ResourceResponse
from .db import engine, get_db
from . import models
from .models import Resource

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API running"}

#! quando receber uma requisição POST ele valida com pydantic, cria um objeto SQLAlchemy, adiciona na sessão, comita a sessão, salva no banco e retorna com ID gerado
@app.post("/resources", response_model=ResourceResponse)
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    db_resource = Resource(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    
    return db_resource