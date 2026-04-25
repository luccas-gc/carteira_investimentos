from fastapi import FastAPI
from src.models import *

app = FastAPI()

from src.routes.ativo_router import ativo_router
from src.routes.aporte_router import aporte_router

app.include_router(ativo_router)
app.include_router(aporte_router)