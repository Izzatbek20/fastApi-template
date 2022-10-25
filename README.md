# FastAPI-template
```commandline
Izzatbek Majidov
```

## Bazani ulash

**.env.example** faylidan nusxa olib **.env** faylini yaratamiz.

```bazani ulash
DB_CONNECTION="postgresql+psycopg2"
DB_HOST=127.0.0.1
DB_PORT=5432
DB_DATABASE=fastapi
DB_USERNAME=postgres
DB_PASSWORD=imm#0620
```

## Alembic
Migratsiya

**Migratsiya uchun bazani manzilini ko`rsatishimiz kerak.**
```
sqlalchemy.url = postgresql+psycopg2://postgres:imm#0620@127.0.0.1:5432/fastapi
```

**Migratsiya uchun modelimizni ko'rsatib qo'yishimiz kerak <small><i>project/migrations/env.py<i></small>**

```
from models import User
``` 

### Migratsiyani komandalari
```
alembic revision --autogenerate -m "users"      # Migratsiya yaratiladi

alembic upgrade head                            # Migratsiyani barchasini bazaga yozish
alembic downgrade base                          # Migratsiyani barchasini bazaga qaytarish

alembic upgrade <ID>                            # ID bilan migratsiya qilish
alembic downgrade <ID>                          # ID bilan migratsiya qaytarish

alembic upgrade +1                              # Bita oldinga migratsiya yurish
alembic downgrade -1                            # Bita orqaga migratsiya qaytarish
```
