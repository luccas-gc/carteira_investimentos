from fastapi import APIRouter
from src.models.aporte import Aporte
from src.databaseConfig import db, SessionLocal
from sqlalchemy.future import select

aporte_router = APIRouter(prefix='/aporte', tags=["aporte"])

@aporte_router.get('/')
async def todos_aportes():
    async with SessionLocal() as session:
        resultado = await session.execute(select(Aporte))
        aportes = resultado.scalars().all()
        return aportes

@aporte_router.get('/{id}')
async def pegar_aporte(id: int):
    pass

@aporte_router.post('/criar_aporte')
async def adicionar_aporte(id_ativo: int, valor_unitario: int, quantidade: int):
    return {"message": "aporte registrado"}