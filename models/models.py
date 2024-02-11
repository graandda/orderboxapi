from db.engine import Model
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
from enums import PaymentType,OrderSatus


class Customer(Model):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    discount = Column(Integer, nullable=False, default=0)


class Product(Model):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    price = Column(DECIMAL, nullable=False)


class Order(Model):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, nullable=False)
    customer_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    pyment_type = Column(Enum(PaymentType), nullable=False)
    total = Column(DECIMAL, nullable=False)
    rest = Column(DECIMAL, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    status = Column(Enum(OrderSatus), nullable=False)


class OrderItems(Model):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, nullable=False)
    order_id = Column(Integer, ForeignKey("order.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    total = Column(DECIMAL, nullable=False)
