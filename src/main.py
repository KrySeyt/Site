from fastapi import FastAPI

from .clients.router import router as clients_router
from .products.router import router as products_router
from .events import close_db_session
from .dependencies import get_db, get_db_stub


app = FastAPI()

app.include_router(clients_router)
app.include_router(products_router)

app.add_event_handler("shutdown", close_db_session)

app.dependency_overrides[get_db_stub] = get_db
