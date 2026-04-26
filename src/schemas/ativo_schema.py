from pydantic import BaseModel

class AtivoItem(BaseModel):
    nome: str
    tipo: str
    codigo: str
    valor_unitario: float #preço p/unidade

    class Config:
        orm_mode = True