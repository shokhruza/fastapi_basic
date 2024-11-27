from contextlib import asynccontextmanager
from typing import Optional

from faker.proxy import Faker
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request

from models import db, Product
from routers.products import shop_router


fake = Faker()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.create_all()
    print("Project ishga tushdi")
    app.include_router(shop_router)
    yield
    print("Project toxtadi")


app = FastAPI(lifespan=lifespan)


# @app.get("/files/{file_path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}
#
#
# @app.get("/files/media/{data}")
# async def read_file(data: str):
#     return {"file_path": data, "msg": "bu boshqa"}
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: Optional[float] = None
#     tax: float | None = None
#
#
# @app.post('/')
# async def root(item: Item):
#     return item
#
#
# @app.get("/hello/{name}")
# async def say_hello(request: Request):
#     name = request.path_params.get('name')
#     return {"message": f"Hello {name}"}
#
#
# @app.get("/generate-products/{count}")
# async def generate_products(count: int):
#     products = []
#     for _ in range(count):
#         product = Product(
#             name=fake.name(),
#             description=fake.text(max_nb_chars=200),
#             price=fake.random_int(min=1, max=1000),
#             quantity=fake.random_int(min=0, max=100)
#         )
#         products.append(product)
#
#     return {"message": f"{count} ta product qo'shildi"}
