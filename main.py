import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Bazaga super admin qo`shish
from database.db import SessionLocal
from models.User import USER

# Auth
from auth.login import auth_route
from auth.register import register_route

# Boshqa routerlar





templates = Jinja2Templates(directory="templates")
description = """
Bu FastAPI uchun shablon.

## Auth
* **None**
"""

app = FastAPI(
    title='FastAPI Template',
    description=description,
    version='0.0.1',
    contact={
        'name': 'Izzatbek Majidov',
        'url': 'https://github.com/Izzatbek20',
    },
    docs_url='/docs', # None o`chirish
    redoc_url='/redoc', # None o`chirish
)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/', response_class=HTMLResponse, summary='Assosiy domain.')
async def main(request: Request):
    """
    Assosiy domain.

    Bu api ishlaganda bazaga super user qo`shiladi auth uchun

    Login: admin
    Parol: secret
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
        print('Super admin oldinroq yaratilgan')

    return templates.TemplateResponse('index.html', {"request": request})



# Auth
app.include_router(auth_route, tags=['Auth'])
app.include_router(register_route, tags=['Auth'])


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)