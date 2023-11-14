from pydantic import BaseModel, PositiveInt, EmailStr, validator
from enum import Enum
from datetime import datetime
from typing import Optional


class CategoriaBase(Enum):
    categoria1 = "Eletrônico"
    categoria2 = "Eletrodoméstico"
    categoria3 = "Móveis"
    categoria4 = "Roupas"
    categoria5 = "Calçados"


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: PositiveInt
    categoria: CategoriaBase
    email_fornecedor: EmailStr

    @validator("categoria")
    def check_categoria(cls, v):
        if v not in CategoriaBase:
            raise ValueError("Categoria inválida")
        return v


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    created_at: datetime = datetime.now()

    class Config:
        orm_mode = True
