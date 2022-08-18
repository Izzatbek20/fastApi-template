from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import DB_CONNECTION, DB_PORT, DB_HOST, DB_PASSWORD, DB_DATABASE, DB_USERNAME

# SQLALCHEMY_DATABASE_URL = "sqlite:///<DB_PATH>/<DB_NAME>.db" # sqlite
SQLALCHEMY_DATABASE_URL = f'{DB_CONNECTION}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}' #postgresql

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()