from typing import Union
from fastapi import Depends, APIRouter, HTTPException, status

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm.session import Session

from datetime import datetime, timedelta

from .schema import UserResponse
from database.db import get_db
from models.User import USER
from auth.schema import TokenData, Token, User
from config.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, password):
    return pwd_context.verify(plain_password, password)


def get_user(db, username: str):
    user = db.query(USER).filter(USER.username==username).first()
    return user

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials!",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.status:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

auth_route = APIRouter()

@auth_route.post("/token", response_model=Token, summary='Access Token uchun login qiling')
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login qilish uchun yuborasiz:
     * username: **string**
     * password: **string**

   Yuborishingiz shart emas:
    * grant_type: **string**
    * scope: **string**
    * client_id: **string**
    * client_secret: **string**

    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=" yLoginoki parol xato!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

@auth_route.get("/me", summary='O`zingiz haqingizda to`liq ma`lumot', response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """
    Login qilib kirganingizda o'zingiz haqingizdagi ma'umotlaringizni shu yerdan olishingiz mumkun
    """
    data = dict()
    data["id"] = current_user.id
    data["username"] = current_user.username
    data["fullname"] = current_user.fullname
    data["phone"] = current_user.phone
    data["role"] = current_user.role
    data["created_at"] = current_user.created_at
    data["updated_at"] = current_user.updated_at
    return data
