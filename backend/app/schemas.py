from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

#? isso vai ser usado para criar os schemas que vão validar os dados de i/o da API, e pra diferir a estrutura da tabela da estrutura da API para que não haja vazamento de informações da tabela para a API, e pra que seja possível da API ter uma estrutura diferente da tabela
class ResourceType(str, Enum):
    video = "Video"
    pdf = "PDF"
    link = "link"
class ResourceBase(BaseModel):
    title: str
    description: Optional[str] = None
    resource_type: ResourceType
    url: Optional[str] = None
    tags: Optional[List[str]] = None

class ResourceCreate(ResourceBase):
    pass

class ResourceResponse(ResourceBase):
    id: int
    
    class Config:
        from_attributes = True

class SmartAssistRequest(BaseModel):
    title: str
    resource_type: ResourceType

class SmartAssistResponse(BaseModel):
    description: str
    tags: List[str]