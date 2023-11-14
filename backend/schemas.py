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
    categoria: str  # Modificado para str
    email_fornecedor: EmailStr

    @validator("categoria")
    def check_categoria(cls, v):
        # Verifica se a string v é um valor válido do Enum
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
