from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_utils import PhoneNumber

from . import models
from . import schema as clients_schema


async def create_client(db: AsyncSession, client: clients_schema.ClientIn) -> models.Client:
    db_client = models.Client(
        phone_number=client.phone_number,
        email=client.email,
        name=client.name,
        surname=client.surname,
    )

    db.add(db_client)
    await db.commit()
    await db.refresh(db_client)
    return db_client


async def delete_client(db: AsyncSession, client_id: int) -> models.Client | None:
    db_client = await db.get(models.Client, client_id)
    if not db_client:
        return None
    await db.delete(db_client)
    await db.commit()
    return db_client


async def get_client_by_id(db: AsyncSession, client_id: int) -> models.Client | None:
    return await db.get(models.Client, client_id)


async def get_client_by_phone_number(db: AsyncSession, phone_number: int | str) -> models.Client | None:
    if isinstance(phone_number, str):
        phone_number = int(phone_number)
    return (await db.execute(select(models.Client).filter(
        models.Client.phone_number == phone_number
    ))).scalars().first()


async def get_clients(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[models.Client]:
    return list((await db.execute(select(models.Client).offset(skip).limit(limit))).scalars().all())


async def update_client(db: AsyncSession, client: clients_schema.ClientInWithID) -> models.Client | None:
    db_client = await db.get(models.Client, client.id)
    if not db_client:
        return None

    db_client.phone_number = PhoneNumber(client.phone_number)
    db_client.name = client.name
    db_client.email = client.email
    db_client.surname = client.surname

    await db.commit()
    await db.refresh(db_client)

    return db_client
