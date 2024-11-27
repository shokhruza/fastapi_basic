from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.database import CreatedBaseModel


class Category(CreatedBaseModel):
    name: Mapped[str] = mapped_column(VARCHAR(255))
    products = Mapped[list['Product']] = relationship('Product', lazy='selectin', back_populates='category')
