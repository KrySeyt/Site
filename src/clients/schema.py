from sqlalchemy_utils import PhoneNumber
from pydantic import BaseModel, EmailStr, validator, Field


class Base(BaseModel):
    pass


class ClientBase(Base):
    phone_number: str = Field(example="+79789123456")
    email: EmailStr
    name: str
    surname: str

    @validator("phone_number", pre=True)
    def phone_number_correct(cls, phone_number: str | PhoneNumber) -> str:
        if isinstance(phone_number, PhoneNumber):
            phone_number = phone_number.e164
        if not (70000000000 < int(phone_number) < 79999999999):
            raise ValueError("Phone number is incorrect")
        return phone_number

    @validator("name")
    def capitalize_name(cls, name: str) -> str:
        return name.capitalize()

    @validator("surname")
    def capitalize_surname(cls, surname: str) -> str:
        return surname.capitalize()


class ClientIn(ClientBase):
    pass


class ClientInWithID(ClientIn):
    id: int


class ClientOut(ClientBase):
    id: int


class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True

