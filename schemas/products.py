from pydantic import BaseModel


class BaseProduct(BaseModel):
    id: int


class CreateProduct(BaseModel):
    name: str
    description: str | None = None
    price: int
    quantity: int

    class Config:
        from_attributes = True

class ResponseProduct(BaseModel):
    id: int
    name: str
    price: int

    class Config:
        from_attributes = True



class DeleteProduct(BaseModel):
    name: str
    description: str | None = None
    price: int
    quantity: int

    class Config:
        from_attributes = True


class UpdateProduct(BaseModel):
    name: str = None
    price: int = None
    description: str = None
    quantity: int = None

    class Config:
        from_attributes = True

