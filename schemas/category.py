from pydantic import BaseModel


class BaseProduct(BaseModel):
    id: int


class CreateCategory(BaseModel):
    name: str

    class Config:
        from_attributes = True


class ResponseCategory(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class UpdateCategory(BaseModel):
    name: str

    class Config:
        from_attributes = True


class DeleteCategory(BaseModel):
    name: str

    class Config:
        from_attributes = True


class ReadCategory(BaseModel):
    name: str

    class Config:
        from_attributes = True