from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from . import models
from . import schema as products_schema


async def create_price(db: AsyncSession, price: products_schema.PriceIn) -> models.Price:
    db_price = models.Price(
        value=price.value,
        currency=price.currency,
    )

    db.add(db_price)
    await db.commit()
    await db.refresh(db_price)
    return db_price


async def delete_price(db: AsyncSession, price_id: int) -> models.Price | None:
    db_price = await db.get(models.Price, price_id)
    if not db_price:
        return None
    await db.delete(db_price)
    await db.commit()
    return db_price


async def update_price(db: AsyncSession, price: products_schema.PriceInWithID) -> models.Price | None:
    db_price = await db.get(models.Price, price.id)
    if not db_price:
        return None

    db_price.value = price.value
    db_price.currency = price.currency

    await db.commit()
    await db.refresh(db_price)

    return db_price


async def get_price_by_id(db: AsyncSession, price_id: int) -> models.Price | None:
    return await db.get(models.Price, price_id)


async def get_prices(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[models.Price]:
    return list((await db.execute(select(models.Price).offset(skip).limit(limit))).scalars().all())


async def create_product(db: AsyncSession, product: products_schema.ProductIn) -> models.Product:
    db_product = models.Product(
        price=await create_price(db, product.price),
        name=product.name,
        image_url=product.image_url,
    )

    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product


async def delete_product(db: AsyncSession, product_id: int) -> models.Product | None:
    db_product = await db.get(models.Product, product_id)
    if not db_product:
        return None
    await db.delete(db_product)
    await db.commit()
    return db_product


async def get_product_by_id(db: AsyncSession, product_id: int) -> models.Product | None:
    return await db.get(models.Product, product_id)


async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[models.Product]:
    stmt = select(models.Product).offset(skip).limit(limit).join(models.Price)
    result = await db.execute(stmt)
    return list(result.scalars().all())


async def update_product(db: AsyncSession, product: products_schema.ProductInWithID) -> models.Product | None:
    db_product = await db.get(models.Product, product.id)
    if not db_product:
        return None

    db_product.name = product.name
    await update_price(db, product.price)
    db_product.image_url = product.image_url

    await db.commit()
    await db.refresh(db_product)

    return db_product
