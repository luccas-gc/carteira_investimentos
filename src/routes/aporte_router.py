from fastapi import APIRouter
from src.models.aporte import Aporte
from src.databaseConfig import db, SessionLocal
from sqlalchemy.future import select
from src.schemas.aporte_schema import AporteItem
from src.routes.ativo_router import todos_ativos

aporte_router = APIRouter(prefix='/aporte', tags=["aporte"])

@aporte_router.get('/', response_model=list[AporteItem])
async def todos_aportes():
    async with SessionLocal() as session:
        resultado = await session.execute(select(Aporte))
        aportes = resultado.scalars().all()
        return aportes

@aporte_router.get('/{id}', response_model=AporteItem)
async def pegar_aporte(id: int):
    async with SessionLocal() as session:
        resultado = await session.execute(select(Aporte).where(Aporte.id==id))
        aporte = resultado.scalars().first()
        if aporte:
            return aporte
        else:
            return {"message": "Não há aportes"}

@aporte_router.post('/criar_aporte')
async def adicionar_aporte(aporte: AporteItem):
#if todos_ativos():
    novo_aporte = Aporte(id_ativo=aporte.id_ativo, valor_unitario=aporte.valor_unitario, quantidade=aporte.quantidade)
    async with SessionLocal() as session:
        session.add(novo_aporte)
        await session.commit()
        return {"message": "aporte adicionado"}
