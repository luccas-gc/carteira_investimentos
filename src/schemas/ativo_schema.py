from pydantic import BaseModel

class AtivoItem(BaseModel):
    nome: str
    tipo: str
    codigo: str
    valor_unitario: float #preço p/unidade
    quantidade: int = 0

    class Config:
        from_attributes = True