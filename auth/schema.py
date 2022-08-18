from typing import Union
from pydantic import BaseModel

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