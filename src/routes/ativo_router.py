from fastapi import APIRouter
from src.schemas.ativo_schema import AtivoItem
from src.services.ativo_service import service_pegar_ativo, service_todos_ativos, service_adicionar_ativo

ativo_router = APIRouter(prefix="/ativo", tags=["ativo"])

@ativo_router.get('/', response_model=list[AtivoItem])
async def get_ativos():
    return await service_todos_ativos()

@ativo_router.get('/{id}', response_model=AtivoItem)
async def get_ativo_id(id: int):
    return await service_pegar_ativo(id)

@ativo_router.post('/')
async def post_ativo(ativo: AtivoItem):
    return await service_adicionar_ativo(ativo=ativo)
'''
@ativo_router.delete('/{id}')
async def delete_ativo(id: int):
    return await service_remover_ativo(id)
'''