from pydantic import BaseModel

class AporteItem(BaseModel):
    id_ativo: int
    valor_unitario: int
    quantidade: int

    class Config:
        orm_mode = True