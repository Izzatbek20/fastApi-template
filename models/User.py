from database.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
import datetime

class USER(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(50))
    phone = Column(String(20), unique=True)
    username = Column(String(50), unique=True)
    password = Column(String(255), nullable=False)
    status = Column(Boolean, default=True)
    role = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.datetime.utcnow)

    def __repr__(self):
        return "<User(id='{}', fullname='{}', username='{}')>".format(
            self.id, self.fullname, self.username)
