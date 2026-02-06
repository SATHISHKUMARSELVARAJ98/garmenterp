from fastapi import FastAPI

from app.core.database import Base, engine
from app.modules.masters.season.model import Season
from app.modules.masters.season.router import router as season_router

app = FastAPI(title="Garment ERP API")



# REGISTER ROUTERS
app.include_router(season_router)

