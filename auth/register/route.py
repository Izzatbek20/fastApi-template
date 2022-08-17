from fastapi import APIRouter

register_route = APIRouter(tags=['Adminlarni ro`yxatga olish'])

@register_route.post('/register', summary="Adminlarni ro`yxatga olish")
async def register():
    pass