from fastapi import APIRouter

router = APIRouter()

#! quando receber uma requisição GET ele retorna um JSON com a chave "status" e o valor "ok", indicando que a API está funcionando corretamente
@router.get("/health")
def health_check():
    return {"status": "ok"}