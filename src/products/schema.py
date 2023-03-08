from pydantic import BaseModel, HttpUrl, validator, Field

from . import models


class Base(BaseModel):
    pass


class PriceBase(Base):
    value: int
    currency: models.Currency


class PriceIn(PriceBase):
    pass


class PriceInWithID(PriceBase):
    id: int


class PriceOut(PriceBase):
    id: int


class Price(PriceBase):
    id: int

    class Config:
        from_orm = True


class ProductBase(Base):
    name: str
    image_url: HttpUrl = Field(example="http://www.google.com/")


class ProductIn(ProductBase):
    price: PriceIn


class ProductInWithID(ProductIn):
    id: int
    price: PriceInWithID


class ProductOut(ProductBase):
    id: int
    price: PriceOut


class Product(ProductBase):
    id: int
    price: Price

    class Config:
        orm_mode = True
