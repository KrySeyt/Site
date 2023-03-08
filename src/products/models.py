from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.database import Base
from .enums import Currency


class Price(Base):
    __tablename__ = "price_table"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    value: Mapped[int] = mapped_column(default=0)
    currency: Mapped[Currency] = mapped_column(default=Currency.RUB)
    product: Mapped[Product] = relationship(back_populates="price", lazy="subquery")


class Product(Base):
    __tablename__ = "product_table"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    price_id: Mapped[int] = mapped_column(ForeignKey("price_table.id"))
    price: Mapped[Price] = relationship(back_populates="product", lazy="subquery", cascade="all, delete")
    image_url: Mapped[str]
