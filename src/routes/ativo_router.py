from fastapi import APIRouter
from src.databaseConfig import db, SessionLocal
from src.models.ativo import Ativo
from sqlalchemy.future import select
from src.schemas.ativo_schema import AtivoItem 

ativo_router = APIRouter(prefix="/ativo", tags=["ativo"])

@ativo_router.get('/', response_model=list[AtivoItem])
async def todos_ativos():
    async with SessionLocal() as session:
        resultado = await session.execute(select(Ativo))
        ativo = resultado.scalars().all()
        return ativo

@ativo_router.get('/{id}', response_model=AtivoItem)
async def pegar_ativo(id: int):
    async with SessionLocal() as session:
        resultado = await session.execute(select(Ativo).where(Ativo.id==id))
        ativo = resultado.scalars().first()
        return ativo

@ativo_router.post('/')
async def adicionar_ativo(ativo: AtivoItem):
    novo_ativo = Ativo(nome=ativo.nome, tipo=ativo.tipo, codigo=ativo.codigo, valor_unitario=ativo.valor_unitario)
    async with SessionLocal() as session:
        session.add(novo_ativo)
        await session.commit()
        return {"message": "ativo adicionado"}