from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Resource
from app.schemas import ResourceCreate, ResourceResponse

router = APIRouter(prefix="/resources", tags=["Resources"])

#! quando receber uma requisição POST ele valida com pydantic, cria um objeto SQLAlchemy, adiciona na sessão, comita a sessão, salva no banco e retorna com ID gerado
@router.post("/", response_model=ResourceResponse)
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    db_resource = Resource(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

#! quando receber uma requisição GET ele calcula o offset e o limit, consulta o banco de dados usando SQLAlchemy, e retorna a lista de recursos paginada

@router.get("/", response_model=list[ResourceResponse])
def list_resources(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    
    #* pequena validação para proteger paginação contra valores <= 0
    if page < 1 or limit <1  :
        page = 1
        limit = 10
    
    offset = (page - 1) * limit
    
    resources = (
        db.query(Resource).offset(offset).
        limit(limit).all()
    )
    
    return resources

#! quando receber uma requisição DELETE ele consulta o banco de dados usando SQLAlchemy, se o recurso existir ele deleta e comita a sessão, se não existir ele retorna um erro 404 informando que não encontrou o recurso, caso o contrário ele retorna sucesso
@router.delete("/{resource_id}")
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = db.query(Resource).filter(Resource.id == resource_id).first()
    
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    
    db.delete(resource)
    db.commit()
    
    return {"message": "Resource deleted successfully!!"}

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Resource
from app.schemas import ResourceCreate, ResourceResponse

router = APIRouter(prefix="/resources", tags=["Resources"])

#! quando receber uma requisição POST ele valida com pydantic, cria um objeto SQLAlchemy, adiciona na sessão, comita a sessão, salva no banco e retorna com ID gerado
@router.post("/", response_model=ResourceResponse)
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    db_resource = Resource(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

#! quando receber uma requisição GET ele calcula o offset e o limit, consulta o banco de dados usando SQLAlchemy, e retorna a lista de recursos paginada

@router.get("/", response_model=list[ResourceResponse])
def list_resources(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    offset = (page - 1) * limit
    
    resources = (
        db.query(Resource).offset(offset).
        limit(limit).all()
    )
    
    return resources

#! quando receber uma requisição DELETE ele consulta o banco de dados usando SQLAlchemy que já está rastreando o objeto, quando se altera atributos e commita ele gera automaticamente a query de update, sem precisar escrever SQL manualmente
#TODO: criar um ResourceUpdate para validar os dados, permitindo atualização parcial. por enquanto vou deixar simples assim
@router.delete("/{resource_id}")
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = db.query(Resource).filter(Resource.id == resource_id).first()
    
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    
    db.delete(resource)
    db.commit()
    
    return {"message": "Resource deleted successfully!!"}
@router.put("/{resource_id}", response_model=ResourceResponse)
def update_resource(resource_id: int, resource_data: ResourceCreate, db: Session = Depends(get_db)):
    resource = db.query(Resource).filter(Resource.id == resource_id).first()
    
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    
    #* parte de ataulização dos campos
    resource.title = resource_data.title
    resource.description = resource_data.description
    resource.resource_type = resource_data.resource_type
    
    db.commit()
    db.refresh(resource)
    
    return resource