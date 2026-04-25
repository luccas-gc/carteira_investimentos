from pydantic import BaseModel

class AtivoItem(BaseModel):
    nome: str
    tipo: str
    codigo: str
    valor_unitario: float