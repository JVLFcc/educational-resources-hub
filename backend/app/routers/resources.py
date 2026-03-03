from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Resource
from app.schemas import ResourceCreate, ResourceResponse, SmartAssistRequest, SmartAssistResponse
from app.services.ia_services import generate_smart_description

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
def list_resources(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    offset = (page - 1) * limit

    resources = (
        db.query(Resource)
        .offset(offset)
        .limit(limit)
        .all()
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

    return {"message": "Resource deleted successfully"}


#! quando receber uma requisição DELETE ele consulta o banco de dados usando SQLAlchemy que já está rastreando o objeto, quando se altera atributos e commita ele gera automaticamente a query de update, sem precisar escrever SQL manualmente
#TODO: criar um ResourceUpdate para validar os dados, permitindo atualização parcial. por enquanto vou deixar simples assim
@router.put("/{resource_id}", response_model=ResourceResponse)
def update_resource(
    resource_id: int,
    resource_data: ResourceCreate,
    db: Session = Depends(get_db)
):
    resource = db.query(Resource).filter(Resource.id == resource_id).first()

    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")

    resource.title = resource_data.title
    resource.description = resource_data.description
    resource.resource_type = resource_data.resource_type
    resource.url = resource_data.url
    resource.tags = resource_data.tags

    db.commit()
    db.refresh(resource)

    return resource

#! quando receber uma requisição POST ele valida com pydantic, chama a função de geração de descrição inteligente, e retorna a descrição e as tags geradas
@router.post("/smart-assist", response_model=SmartAssistResponse)
def smart_assist(data: SmartAssistRequest):
    result = generate_smart_description(title = data.title, resource_type = data.resource_type.value)
    
    return result