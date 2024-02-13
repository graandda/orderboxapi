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


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, nullable=False)
    type = Column(Enum(PaymentType), nullable=False)
    amount = Column(DECIMAL, nullable=False)

    receipt = relationship("Receipt", uselist=False, back_populates="payment")


class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    payment_id = Column(Integer, ForeignKey("payments.id"), nullable=False)
    total = Column(DECIMAL, nullable=False)
    rest = Column(DECIMAL, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))

    user = relationship("User", back_populates="receipts")
    products = relationship("ReceiptProduct", back_populates="receipt")
    payment = relationship("Payment", uselist=False, back_populates="receipt")


class ReceiptProduct(Base):
    __tablename__ = "receipt_products"

    id = Column(Integer, primary_key=True, nullable=False)
    receipt_id = Column(Integer, ForeignKey("receipts.id"), nullable=False)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL, nullable=False)

    receipt = relationship("Receipt", back_populates="products")
