from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import DB_CONNECTION, DB_PORT, DB_HOST, DB_PASSWORD, DB_DATABASE, DB_USERNAME

engine = create_engine('postgresql://imm:imm#0620@localhost/fastapi', echo=True)

Base = declarative_base()
Session = sessionmaker()
