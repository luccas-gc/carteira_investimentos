from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from src.databaseConfig import Base

class Aporte(Base):
    __tablename__ = "aporte"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_ativo = Column("ativo", Integer, ForeignKey("ativo.id"))
    valor_unitario = Column("valor_unitario", Float)
    quantidade = Column("quantidade", Integer)
    ativo = relationship("Ativo", back_populates="aporte")
