# FastAPI-template
```commandline
Izzatbek Majidov
```



##Bazani ulash
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

```sqlalchemy.url = postgresql+psycopg2://postgres:imm#0620@127.0.0.1:5432/fastapi```

**Migratsiya uchun modelimizni ko'rsatib qo'yishimiz kerak**

```
from myapp import mymodel
from models import User
``` 


**Migratsiya yaratiladi**

```alembic revision --autogenerate -m "users"``` 

**Migratsiyani bazaga yozish**

```alembic upgrade head``` 
