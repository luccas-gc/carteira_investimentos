from pydantic import BaseModel

class AporteItem(BaseModel):
    id_ativo: int
    quantidade: int

    class Config:
        from_attributes = True