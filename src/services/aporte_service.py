from src.schemas.aporte_schema import AporteItem
from sqlalchemy.future import select
from src.models.aporte import Aporte
from src.database.databaseConfig import SessionLocal
from src.services.ativo_service import service_pegar_ativo

async def service_todos_aportes():
    async with SessionLocal() as session:
        resultado = await session.execute(select(Aporte))
        aporte = resultado.scalars().all()
        return aporte
    
async def service_pegar_aporte(id_ativo: int):
    async with SessionLocal() as session:
        resultado = await session.execute(select(Aporte).where(Aporte.id_ativo==id_ativo))
        aporte = resultado.scalars().all()
        if aporte:
            return aporte
        else:
            return {"message": "Não há aportes"}
        
async def service_adicionar_aporte(aporte: AporteItem):
    if await service_pegar_ativo(aporte.id_ativo):
        novo_aporte = Aporte(id_ativo=aporte.id_ativo, quantidade=aporte.quantidade)
        async with SessionLocal() as session:
            session.add(novo_aporte)
            await session.commit()
            return {"message": "aporte adicionado"}
    else:
        return {"message": "ativo inexistente"}
