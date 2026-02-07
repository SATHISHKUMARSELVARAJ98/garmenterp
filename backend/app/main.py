from fastapi import FastAPI

from app.core.database import Base, engine
from app.modules.masters.season.model import Season
from app.modules.masters.season.router import router as season_router
from app.modules.masters.buyer.model import Buyer
from app.modules.masters.buyer.router import router as buyer_router
from app.modules.masters.style.router import router as style_router

app = FastAPI(title="Garment ERP API")



# REGISTER ROUTERS
app.include_router(season_router)
app.include_router(buyer_router)
app.include_router(style_router)

