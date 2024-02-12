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
from enums import PaymentType, OrderSatus


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    discount = Column(Integer, nullable=False, default=0)


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    price = Column(DECIMAL, nullable=False)


class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    payment_type = Column(Enum(PaymentType), nullable=False)
    total = Column(DECIMAL, nullable=False)
    rest = Column(DECIMAL, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    status = Column(Enum(OrderSatus), nullable=False)

    user = relationship("Users")
    order_item = relationship("OrderItems")


class OrderItems(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    total = Column(DECIMAL, nullable=False)

    order = relationship("Orders")
    product = relationship("Products")
