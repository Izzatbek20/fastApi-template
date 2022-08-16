from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from auth.route import auth_route

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


@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})

app.include_router(auth_route)