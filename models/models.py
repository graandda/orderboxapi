from sqlalchemy.orm import relationship

from db.engine import Base
from sqlalchemy import (
    Column,
    Integer,
    TIMESTAMP,
    DECIMAL,
    text,
    Enum,
    ForeignKey,
    String,
)
from enums import PaymentType


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    login = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    discount = Column(Integer, nullable=False, default=0)

    receipts = relationship("Receipt", back_populates="user")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    price = Column(DECIMAL, nullable=False)


class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    payment_type = Column(Enum(PaymentType), nullable=False)
    total = Column(DECIMAL, nullable=False)
    rest = Column(DECIMAL, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))

    user = relationship("User", back_populates="receipts")
    products = relationship("ReceiptItem", back_populates="receipt")


class ReceiptItem(Base):
    __tablename__ = "receipt_items"

    id = Column(Integer, primary_key=True, nullable=False)
    receipt_id = Column(Integer, ForeignKey("receipts.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    total = Column(DECIMAL, nullable=False)

    receipt = relationship("Receipt", back_populates="products")
    product = relationship("Product")
