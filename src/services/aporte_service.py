from src.schemas.aporte_request_schema import AporteRequest
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from src.models.aporte import Aporte
from src.models.ativo import Ativo
from src.database.databaseConfig import SessionLocal
from src.services.ativo_service import service_pegar_ativo

# Retorna Todo o Histórico de Aportes
async def service_todos_aportes():
    async with SessionLocal() as session:
        resultado = await session.execute(select(Aporte).options(joinedload(Aporte.ativo)))
        aportes = resultado.scalars().all()
        return [{"codigo": aporte.ativo.codigo, "quantidade": aporte.quantidade} for aporte in aportes]
    
# Retorna o Histórico de Aportes de um determinado ativo
async def service_pegar_aporte(codigo: str):
    async with SessionLocal() as session:
        carregar_aportes = await session.execute(select(Aporte).join(Aporte.ativo).options(joinedload(Aporte.ativo)).where(Ativo.codigo==codigo))
        aportes = carregar_aportes.scalars().all()
        if aportes:
            return [{"codigo": aporte.ativo.codigo, "quantidade": aporte.quantidade} for aporte in aportes]
        else:
            return {"message": "Não há nesse ativo"}
        
# Adiciona Aporte em um ativo
async def service_adicionar_aporte(aporte: AporteRequest):
    ativo = await service_pegar_ativo(aporte.codigo)
    if ativo:
        novo_aporte = Aporte(id_ativo = ativo.id, quantidade=aporte.quantidade)
        async with SessionLocal() as session:
            session.add(novo_aporte)
            await session.commit()
            return {"codigo": {ativo.codigo}}
    else:
        return {"message": "ativo inexistente"}
