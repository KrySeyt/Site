import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .clients.router import router as clients_router
from .products.router import router as products_router
from .pages.router import router as pages_router
from .events import close_db_session
from .dependencies import get_db, get_db_stub


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


app = FastAPI()

app.include_router(clients_router)
app.include_router(products_router)
app.include_router(pages_router)

app.mount("/src/pages/build/", StaticFiles(directory=BASE_DIR + "/src/pages/build/"), name="front")

app.add_event_handler("shutdown", close_db_session)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.dependency_overrides[get_db_stub] = get_db
