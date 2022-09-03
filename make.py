import argparse
import os

location = os.getcwd()+'\ '.strip() # proyektimiz local manzili
parser = argparse.ArgumentParser(description='FastAPI template uchun terminal buyruqlar qatori.')

parser.add_argument('name', type=str, help='Model, router va schema nomi.')

parser.add_argument('--model', action='store_true', help='Model.')
parser.add_argument('--route', action='store_true', help='Route.')
parser.add_argument('--schema', action='store_true', help='Schema.')

args = parser.parse_args()


'''
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
'''

# route
if args.name and args.route:
    file = args.name.lower()+'.py'
    path = location+'routes'
    text = f'from fastapi import APIRouter, Depends, HTTPException, status\n' \
           f'from auth.login import get_current_active_user # Auth\n' \
           f'from auth.schema import User # Auth\n' \
           f'from pydantic import ValidationError # Validatsiya\n' \
           f'\n' \
           f'from sqlalchemy.orm.session import Session # db sessiya\n' \
           f'from database.db import get_db # db sessiya\n' \
           f'\n' \
           f'# Model va schema\n' \
           f'from models.{args.name.lower()} import {args.name.upper()}\n' \
           f'from schemas.{args.name.lower()} import {args.name.capitalize()}Post, {args.name.capitalize()}Put, {args.name.capitalize()}Response\n' \
           f'\n' \
           f'\n' \
           f'{args.name.lower()}_route = APIRouter(tags=[\'{str(args.name.capitalize())}\'])' \
           f'\n' \
           f'\n' \
           f'# Route' \
           f'\n' \
           f'@{args.name.lower()}_route.get(\'/{args.name.lower()}\' ,summary="Chaqirish", response_model={args.name.capitalize()}Response, status_code=status.HTTP_200_OK)\n' \
           f'async def {args.name.lower()}_get(db: Session = Depends(get_db), current_user : User = Depends(get_current_active_user)):\n' \
           f'   """\n' \
           f'   ## Get\n' \
           f'   """\n' \
           f'   pass\n' \
           f'\n' \
           f'\n' \
           f'@{args.name.lower()}_route.post(\'/{args.name.lower()}\' ,summary="Yaratish", response_model={args.name.capitalize()}Response, status_code=status.HTTP_201_CREATED)\n' \
           f'async def {args.name.lower()}_post(data: {args.name.capitalize()}Post, db: Session = Depends(get_db), current_user : User = Depends(get_current_active_user)):\n' \
           f'   """\n' \
           f'   ## Post\n' \
           f'   * name: **string**\n' \
           f'   """\n' \
           f'   try:\n' \
           f'       pass\n' \
           f'   except ValidationError as e:\n' \
           f'       raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e)' \
           f'\n' \
           f'\n' \
           f'@{args.name.lower()}_route.put(\'/{args.name.lower()}\' ,summary="O`zgartirish", response_model={args.name.capitalize()}Response, status_code=status.HTTP_200_OK)\n' \
           f'async def {args.name.lower()}_put(data: {args.name.capitalize()}Put, db: Session = Depends(get_db), current_user : User = Depends(get_current_active_user)):\n' \
           f'   """\n' \
           f'   ## Put\n' \
           f'   * name: **string**\n' \
           f'   """\n' \
           f'   try:\n' \
           f'       pass\n' \
           f'   except ValidationError as e:\n' \
           f'       raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e)' \
           f'\n' \
           f'\n' \
           f'@{args.name.lower()}_route.delete(\'/{args.name.lower()}\' ,summary="O`chirish", response_model={args.name.capitalize()}Response, status_code=status.HTTP_200_OK)\n' \
           f'async def {args.name.lower()}_delete(db: Session = Depends(get_db), current_user : User = Depends(get_current_active_user)):\n' \
           f'   """\n' \
           f'   ## Delete\n' \
           f'   """\n' \
           f'   pass\n' \
           f'\n' \
           f'\n' \

    if os.path.isfile(f"{path}\{file}") == False:
        with open(os.path.join(path, file), 'w') as fp:
            fp.write(text)
            fp.close()
        print('Route yaratildi!')
    else:
        print(f'{args.name.lower()}.py route mavjud!')

# model
if args.name and args.model:
    file = args.name.lower()+'.py'
    path = location+'models'
    text = f'from database.db import Base\n' \
           f'from sqlalchemy import Column, Integer, String, DateTime, Boolean\n' \
           f'import datetime\n' \
           f'\n' \
           f'\n' \
           f'\n' \
           f'# Model' \
           f'\n' \
           f'class {args.name.upper()}(Base):\n' \
           f'   __tablename__ = "{args.name.lower()}"\n' \
           f'   id = Column(Integer, primary_key=True, autoincrement=True)\n' \
           f'\n' \
           f'   status = Column(Boolean, default=True)\n' \
           f'   created_at = Column(DateTime, default=datetime.datetime.utcnow)\n' \
           f'   updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)\n' \

    if os.path.isfile(f"{path}\{file}") == False:
        with open(os.path.join(path, file), 'w') as fp:
            fp.write(text)
            fp.close()
        print('Model yaratildi!')
    else:
        print(f'{args.name.lower()}.py model mavjud!')

# schema
if args.name and args.schema:
    file = args.name.lower()+'.py'
    path = location+'schemas'
    text = f'from pydantic import BaseModel, validator\n' \
           f'from database.db import SessionLocal\n' \
           f'from models.{args.name.lower()} import {args.name.upper()}\n' \
           f'\n' \
           f'db = SessionLocal()\n' \
           f'\n' \
           f'\n' \
           f'# Schema' \
           f'\n' \
           f'class {args.name.capitalize()}Post(BaseModel):\n' \
           f'   name: str\n' \
           f'\n' \
           f'   @validator(\'name\')\n' \
           f'   def name_validate(cls, v):\n' \
           f'       if v != str:\n' \
           f'           raise ValueError(\'Name matn bo`lishi kerak\')\n' \
           f'       return v' \
           f'\n' \
           f'\n' \
           f'class {args.name.capitalize()}Put(BaseModel):\n' \
           f'   name: str\n' \
           f'\n' \
           f'   @validator(\'name\')\n' \
           f'   def name_validate(cls, v):\n' \
           f'       if v != str:\n' \
           f'           raise ValueError(\'Name matn bo`lishi kerak\')\n' \
           f'       return v' \
           f'\n' \
           f'\n' \
           f'class {args.name.capitalize()}Response(BaseModel):\n' \
           f'   detail: str\n' \
           f'\n' \
           f''

    if os.path.isfile(f"{path}\{file}") == False:
        with open(os.path.join(path, file), 'w') as fp:
            fp.write(text)
            fp.close()
        print('Schema yaratildi!')
    else:
        print(f'{args.name.lower()}.py schema mavjud!')
