from sqlalchemy.ext.asyncio import AsyncSession

from . import models as products_models
from . import schema as products_schema
from . import crud as products_crud


def price_model_to_schema(db_price: products_models.Price) -> products_schema.Price:
    return products_schema.Price(
        id=db_price.id,
        value=db_price.value,
        currency=db_price.currency,
    )


def product_model_to_schema(db_product: products_models.Product) -> products_schema.Product:
    return products_schema.Product(
        id=db_product.id,
        name=db_product.name,
        price=price_model_to_schema(db_product.price),
        image_url=db_product.image_url
    )


async def create_price(db: AsyncSession, price: products_schema.PriceIn) -> products_schema.Price:
    db_price = await products_crud.create_price(db, price)
    return price_model_to_schema(db_price)


async def delete_price(db: AsyncSession, price_id: int) -> products_schema.Price | None:
    db_price = await products_crud.delete_price(db, price_id)
    if not db_price:
        return None
    return price_model_to_schema(db_price)


async def update_price(db: AsyncSession, price: products_schema.PriceInWithID) -> products_schema.Price | None:
    db_price = await products_crud.update_price(db, price)
    if not db_price:
        return None
    return price_model_to_schema(db_price)


async def get_price_by_id(db: AsyncSession, price_id: int) -> products_schema.Price | None:
    db_price = await products_crud.get_price_by_id(db, price_id)
    if not db_price:
        return None
    return price_model_to_schema(db_price)


async def get_prices(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[products_schema.Price]:
    db_prices = await products_crud.get_prices(db, skip, limit)
    return list(map(price_model_to_schema, db_prices))


async def create_product(db: AsyncSession, product: products_schema.ProductIn) -> products_schema.Product:
    db_product = await products_crud.create_product(db, product)
    return product_model_to_schema(db_product)


async def get_product_by_id(db: AsyncSession, product_id: int) -> products_schema.Product | None:
    db_product = await products_crud.get_product_by_id(db, product_id)
    if not db_product:
        return None
    return product_model_to_schema(db_product)


async def update_product(db: AsyncSession, product: products_schema.ProductInWithID) -> products_schema.Product | None:
    db_product = await products_crud.update_product(db, product)
    if not db_product:
        return None
    await update_price(db, product.price)
    return product_model_to_schema(db_product)


async def delete_product(db: AsyncSession, product_id: int) -> products_schema.Product | None:
    db_product = await products_crud.delete_product(db, product_id)
    if not db_product:
        return None
    return product_model_to_schema(db_product)


async def get_products(db: AsyncSession, skip: int, limit: int) -> list[products_schema.Product]:
    db_products = await products_crud.get_products(db, skip, limit)
    return list(map(product_model_to_schema, db_products))
