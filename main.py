from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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
    """
    return templates.TemplateResponse('index.html', {"request": request})



# Auth
app.include_router(auth_route)
app.include_router(register_route)