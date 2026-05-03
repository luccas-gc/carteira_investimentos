from fastapi import APIRouter
from src.schemas.aporte_request_schema import AporteRequest
from src.services.aporte_service import service_adicionar_aporte, service_pegar_aporte, service_todos_aportes

aporte_router = APIRouter(prefix='/aporte', tags=["aporte"])

@aporte_router.get('/', response_model=list[AporteRequest])
async def get_aporte():
    return await service_todos_aportes()

@aporte_router.get('/{codigo}', response_model=list[AporteRequest])
async def get_aporte_id(codigo: str):
    return await service_pegar_aporte(codigo)

@aporte_router.post('/criar_aporte')
async def post_aporte(aporte: AporteRequest):
    return await service_adicionar_aporte(aporte)