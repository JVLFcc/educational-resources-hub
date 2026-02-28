from pydantic import BaseModel

#? isso vai ser usado para criar os schemas que vão validar os dados de i/o da API, e pra diferir a estrutura da tabela da estrutura da API para que não haja vazamento de informações da tabela para a API, e pra que seja possível da API ter uma estrutura diferente da tabela
class ResourceBase(BaseModel):
    title: str
    description: str
    resource_type: str

class ResourceCreate(ResourceBase):
    pass

class ResourceResponse(ResourceBase):
    id: int
    
    class Config:
        from_attributes = True