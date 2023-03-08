from sqlalchemy.ext.asyncio import AsyncSession

from . import schema as clients_schema
from . import crud as clients_crud


async def create_client(db: AsyncSession, client: clients_schema.ClientIn) -> clients_schema.Client:
    db_client = await clients_crud.create_client(db, client)
    return clients_schema.Client.from_orm(db_client)


async def delete_client(db: AsyncSession, client_id: int) -> clients_schema.Client | None:
    db_client = await clients_crud.delete_client(db, client_id)
    if not db_client:
        return None
    return clients_schema.Client.from_orm(db_client)


async def update_client(db: AsyncSession, client: clients_schema.ClientInWithID) -> clients_schema.Client | None:
    db_client = await clients_crud.update_client(db, client)
    if not db_client:
        return None
    return clients_schema.Client.from_orm(db_client)


async def get_client_by_id(db: AsyncSession, client_id: int) -> clients_schema.Client | None:
    db_client = await clients_crud.get_client_by_id(db, client_id)
    if not db_client:
        return None
    return clients_schema.Client.from_orm(db_client)


async def get_clients(db: AsyncSession, skip: int, limit: int) -> list[clients_schema.Client]:
    db_clients = await clients_crud.get_clients(db, skip, limit)
    return list(map(clients_schema.Client.from_orm, db_clients))
