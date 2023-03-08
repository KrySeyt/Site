import pathlib

from fastapi import APIRouter, Request
from starlette.responses import FileResponse
from starlette.templating import Jinja2Templates


router = APIRouter(tags=["React"])

templates = Jinja2Templates(directory="src")


@router.get("/static/{path_to_static:path}")
async def get_static(path_to_static: str):
    path = pathlib.Path(__file__).parent.resolve().joinpath("build/static/").joinpath(path_to_static)
    return FileResponse(path)


@router.get("/")
async def react(request: Request):
    return templates.TemplateResponse("pages/build/index.html", {"request": request})


@router.get("/catalog")
async def react(request: Request):
    return templates.TemplateResponse("pages/build/index.html", {"request": request})
