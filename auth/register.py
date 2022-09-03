from fastapi import APIRouter, Depends, HTTPException, status
from .login import get_current_active_user, get_password_hash
from .schema import User, Register, RegisterResponse
from models.User import USER
from pydantic import ValidationError

from sqlalchemy.orm.session import Session
from database.db import get_db
from enum import Enum

class Role(str, Enum):
    admin = 'admin'
    user = 'user'

register_route = APIRouter()


@register_route.post('/register' ,summary="Adminlarni ro`yxatga olish", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
async def register(data: Register, role: Role, db: Session = Depends(get_db), current_user : User = Depends(get_current_active_user)):
    """
    Yangi userni bazaga qo`shish

    * username: **string**
    * password: **string**
    * phone: **string** m: +998908330620
    * fullname: **string**
    """
    try:
        user = USER(
            fullname=data.fullname,
            phone=data.phone,
            username=data.username,
            password=get_password_hash(data.password),
            role=role,
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        if user:
            raise HTTPException(status_code=status.HTTP_201_CREATED, detail='Qo`shildi')
        else:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=user)

    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e)
