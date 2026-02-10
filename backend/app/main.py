from fastapi import FastAPI

from app.core.database import Base, engine
from app.modules.masters.season.model import Season
from app.modules.masters.buyer.model import Buyer
from app.modules.masters.style.model import Style
from app.modules.masters.color.model import Color
from app.modules.masters.size.model import Size
from app.modules.masters.season.router import router as season_router
from app.modules.masters.buyer.router import router as buyer_router
from app.modules.masters.style.router import router as style_router
from app.modules.masters.color.router import router as color_router
from app.modules.masters.size.router import router as size_router

app = FastAPI(title="Garment ERP API")



# REGISTER ROUTERS
app.include_router(season_router)
app.include_router(buyer_router)
app.include_router(style_router)
app.include_router(color_router)
app.include_router(size_router)

