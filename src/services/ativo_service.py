from src.database.databaseConfig import SessionLocal
from sqlalchemy.future import select
from src.models.ativo import Ativo
from src.schemas.ativo_schema import AtivoItem

async def service_todos_ativos():
    async with SessionLocal() as session:
        resultado = await session.execute(select(Ativo))
        ativo = resultado.scalars().all()
        return ativo
    
async def service_pegar_ativo(id: int):
    async with SessionLocal() as session:
        resultado = await session.execute(select(Ativo).where(Ativo.id==id))
        ativo = resultado.scalars().first()
        return ativo
    
async def service_adicionar_ativo(ativo: AtivoItem):
    novo_ativo = Ativo(nome=ativo.nome, tipo=ativo.tipo, codigo=ativo.codigo, valor_unitario=ativo.valor_unitario, quantidade=ativo.quantidade)
    async with SessionLocal() as session:
        ativo = await session.execute(select(Ativo).where(Ativo.codigo==novo_ativo.codigo))
        ativo_existente = ativo.scalars().first()
        if not ativo_existente:
            session.add(novo_ativo)
            await session.commit()
            return {"message": "ativo adicionado"}
        else:
            return {"message": "ativo já existente"}
'''
async def service_remover_ativo(id: int):
    async with SessionLocal() as session:
        busca_ativo = await session.execute(select(Ativo).where(Ativo.id==id))
        remover_ativo = busca_ativo.scalars().first()
        if remover_ativo:
            await session.delete(remover_ativo)
            await session.commit()
            return {"message": "ativo removido"}
        else:
            return {"message": "ativo inexistente"}
'''