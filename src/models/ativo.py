from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship
from src.database.databaseConfig import Base

class Ativo(Base):
    __tablename__ = "ativo"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    tipo = Column("tipo", String)
    codigo = Column("codigo", String, unique=True)
    valor_unitario = Column("valor_unitario", Float)
    quantidade = Column("quantidade", Integer)
    aporte = relationship("Aporte", back_populates="ativo")

