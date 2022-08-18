from database.db import engine, Base, SessionLocal
from models.User import USER
"""

Modellarimiz faqat bir marotaba create bo`ladi
Birorta modelimiz o`zgartirilib qayta run berilganda ishlamaydi faqat bir marotaba bazaga create bo`ladi

"""

Base.metadata.create_all(bind=engine)

"""
Tizimga kirish uchun super admin yaratib olamiz

=====================
=                   =
=  Login: imm       =
=  Parol: 12345678  =
=                   =  
=====================


"""

try:
    db = SessionLocal()
    user_create = USER(
        fullname='Super admin',
        phone='+998908330620',
        username='admin',
        password='$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW',
        role='super_admin'
    )
    db.add(user_create)
    db.commit()
    db.refresh(user_create)
except:
    print('Super admin oldin yaratilgan')


