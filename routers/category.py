from celery.bin.control import status
from fastapi import APIRouter
from starlette.responses import Response

from models.categories import Category
from schemas.category import CreateCategory, ResponseCategory, UpdateCategory
from utils.orm_ import get_object_or_404


shop_router = APIRouter()

@shop_router.post('/categories')
async def create_category(category: CreateCategory) -> ResponseCategory:
    return await Category.create(**category.model_dump(exclude_unset=True))



@shop_router.get('/categories/{id}')
async def create_category(category: CreateCategory) -> ResponseCategory:
    return await Category.create(**category.model_dump(exclude_unset=True))


@shop_router.delete('/categories/{id}')
async def delete_product(_id: int):
    category = await get_object_or_404(Category, _id)
    await category.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@shop_router.patch('/categories')
async def update_category(category: UpdateCategory) -> ResponseCategory:
    return await Category.update(**category.model_dump(exclude_unset=True))


@shop_router.get('/categories')
async def list_categories() -> ResponseCategory:
    pass


