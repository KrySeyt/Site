from __future__ import annotations

from enum import Enum

from sqlalchemy import ForeignKey, LargeBinary
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.database import Base


class Currency(Enum):
    USD = "USD"
    RUB = "RUB"
    EURO = "EURO"


class Price(Base):
    __tablename__ = "price_table"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    value: Mapped[int] = mapped_column(default=0)
    currency: Mapped[Currency] = mapped_column(default=Currency.RUB)


class Product(Base):
    __tablename__ = "product_table"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    price_id: Mapped[int] = mapped_column(ForeignKey("price_table.id"))
    price: Mapped[Price] = relationship()
    image = Mapped[LargeBinary]
