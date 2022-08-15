from fastapi import FastAPI

from auth.route import auth_route

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

@app.get('/')
async def main():
    return {
        'message': 'Biz ishladik',
    }

app.include_router(auth_route)