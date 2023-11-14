from sqlalchemy.orm import Session
import models, schemas


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = (
        db.query(models.Product).filter(models.Product.id == product_id).first()
    )
    db.delete(db_product)
    db.commit()
    return db_product


def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = (
        db.query(models.Product).filter(models.Product.id == product_id).first()
    )
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db.commit()
    return db_product
