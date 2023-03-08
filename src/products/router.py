from fastapi import APIRouter, Depends, Path, Body, Query
from sqlalchemy.ext.asyncio import AsyncSession

from . import schema as products_schema
from . import service as products_service

from ..dependencies import get_db_stub


router = APIRouter(tags=["Products"])


@router.post(
    "/product/",
    response_model=products_schema.ProductOut
)
async def create_product(
        db: AsyncSession = Depends(get_db_stub),
        product: products_schema.ProductIn = Body()
) -> products_schema.Product:
    return await products_service.create_product(db, product)


@router.delete(
    "/product/{product_id}",
    response_model=products_schema.ProductOut | None
)
async def delete_product(
        db: AsyncSession = Depends(get_db_stub),
        product_id: int = Path()
) -> products_schema.Product | None:
    return await products_service.delete_product(db, product_id)


@router.put(
    "/product/",
    response_model=products_schema.ProductOut | None
)
async def update_product(
        db: AsyncSession = Depends(get_db_stub),
        product: products_schema.ProductInWithID = Body()
) -> products_schema.Product | None:
    return await products_service.update_product(db, product)


@router.get(
    "/product/{product_id}",
    response_model=products_schema.ProductOut | None
)
async def get_product(
        db: AsyncSession = Depends(get_db_stub),
        product_id: int = Path()
) -> products_schema.Product | None:
    return await products_service.get_product_by_id(db, product_id)


@router.get(
    "/products/",
    response_model=list[products_schema.ProductOut]
)
async def get_products(
        db: AsyncSession = Depends(get_db_stub),
        skip: int = Query(default=0),
        limit: int = Query(default=100)
) -> list[products_schema.Product]:
    return await products_service.get_products(db, skip, limit)
