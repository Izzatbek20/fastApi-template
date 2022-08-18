from fastapi import APIRouter, Depends, HTTPException, status
from .login import get_current_active_user, get_password_hash
from .schema import User, Register
from models.User import USER
from pydantic import ValidationError

from sqlalchemy.orm.session import Session
from database.db import get_db
from enum import Enum
import json

class Role(str, Enum):
    admin = 'admin'
    user = 'user'

register_route = APIRouter()


@register_route.post('/register' ,summary="Adminlarni ro`yxatga olish", status_code=status.HTTP_201_CREATED)
async def register(data: Register, role: Role, db: Session = Depends(get_db), current_user : User = Depends(get_current_active_user)):
    """
    Yangi userni bazaga qo`shish

    f'
    :param data:
    :param role:
    :param db:
    :param current_user:
    :return:
    """
    try:
        validate_username = db.query(USER).filter(
            USER.username==data.username,
        ).count()
        validate_phone = db.query(USER).filter(
            USER.phone==data.phone,
        ).count()
        # if validate_username == 0 and validate_phone == 0:
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
        # else:
        #     if validate_phone > 0:
        #         raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Bunday telefon nomer aval ro`yxatga olingan.')
        #     if validate_username > 0:
        #         raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Bunday telefon login aval ro`yxatga olingan.')

    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e)
