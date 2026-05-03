from pydantic import BaseModel

class AporteRequest(BaseModel):
    codigo: str
    quantidade: int

    class Config:
        from_attributes = True