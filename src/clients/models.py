from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy_utils import PhoneNumber, PhoneNumberType

from src.database import Base


class Client(Base):
    __tablename__ = "client_table"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    phone_number: Mapped[PhoneNumber] = mapped_column(type_=PhoneNumberType())
    email: Mapped[str]
    name: Mapped[str]
    surname: Mapped[str]
