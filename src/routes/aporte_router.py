from fastapi import APIRouter
from src.schemas.aporte_schema import AporteItem
from src.services.aporte_service import service_adicionar_aporte, service_pegar_aporte, service_todos_aportes

aporte_router = APIRouter(prefix='/aporte', tags=["aporte"])

@aporte_router.get('/', response_model=list[AporteItem])
async def get_aporte():
    return await service_todos_aportes()

@aporte_router.get('/{id}', response_model=list[AporteItem])
async def get_aporte_id(id_ativo: int):
    return await service_pegar_aporte(id_ativo)

@aporte_router.post('/criar_aporte')
async def post_aporte(aporte: AporteItem):
    return await service_adicionar_aporte(aporte)