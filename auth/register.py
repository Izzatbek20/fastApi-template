from fastapi import APIRouter, Depends
from .login import get_current_active_user
from .schema import User, Register
from models.User import USER

from sqlalchemy.orm.session import Session
from database.db import get_db

register_route = APIRouter(tags=['Auth'])

@register_route.post('/register', response_model=User ,summary="Adminlarni ro`yxatga olish")
async def register(data: Register, db: Session = Depends(get_db), current_user : User = Depends(get_current_active_user)):
    user = USER(
        fullname=data.fullname,
        phone=data.phone,
        username=data.username,
        password=data.password,
        token='pme',
        role='pme',
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return ['message', user]