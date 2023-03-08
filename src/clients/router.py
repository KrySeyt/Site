from fastapi import APIRouter, Depends, Path, Body, Query
from sqlalchemy.ext.asyncio import AsyncSession

from . import schema as clients_schema
from . import service as clients_service

from ..dependencies import get_db_stub


router = APIRouter(tags=["Clients"])


@router.post(
    "/client/",
    response_model=clients_schema.ClientOut,
)
async def create_client(
        db: AsyncSession = Depends(get_db_stub),
        client: clients_schema.ClientIn = Body()
) -> clients_schema.Client:
    return await clients_service.create_client(db, client)


@router.delete(
    "/client/{client_id}",
    response_model=clients_schema.ClientOut | None
)
async def delete_client(
        db: AsyncSession = Depends(get_db_stub),
        client_id: int = Path()
) -> clients_schema.Client | None:
    return await clients_service.delete_client(db, client_id)


@router.put(
    "/client/",
    response_model=clients_schema.ClientOut | None
)
async def update_client(
        db: AsyncSession = Depends(get_db_stub),
        client: clients_schema.ClientInWithID = Body()
) -> clients_schema.Client | None:
    return await clients_service.update_client(db, client)


@router.get(
    "/client/{client_id}",
    response_model=clients_schema.ClientOut | None
)
async def get_client(
        db: AsyncSession = Depends(get_db_stub),
        client_id: int = Path()
) -> clients_schema.Client | None:
    return await clients_service.get_client_by_id(db, client_id)


@router.get(
    "/clients/",
    response_model=list[clients_schema.ClientOut]
)
async def get_clients(
        db: AsyncSession = Depends(get_db_stub),
        skip: int = Query(default=0),
        limit: int = Query(default=100)
) -> list[clients_schema.Client]:
    return await clients_service.get_clients(db, skip, limit)
