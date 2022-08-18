from typing import Union
from pydantic import BaseModel, validator
from database.db import SessionLocal
from models.User import USER

db = SessionLocal()


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: str
    phone: Union[str, None] = None
    fullname: Union[str, None] = None
    status: Union[bool, None] = None
    
class Register(BaseModel):
    username: str
    password: str
    phone: str
    fullname: str

    @validator('password')
    def password_validate(cls, v):
        if len(v) != 8:
            raise ValueError('Parol 8 tadan kam bo`lmasligi kerak')
        return v

    @validator('username')
    def username_validate(cls, v):
        validate_my = db.query(USER).filter(
            USER.username == v,
        ).count()

        if validate_my != 0:
            raise ValueError('Bunday login aval ro`yxatga olingan.')
        return v

    @validator('phone')
    def phone_validate(cls, v):
        validate_my = db.query(USER).filter(
            USER.phone == v,
        ).count()

        if validate_my != 0:
            raise ValueError('Bunday telefon nomer aval ro`yxatga olingan.')
        if len(v) != 13:
            raise ValueError('Bu telefon raqam emas')
        return v