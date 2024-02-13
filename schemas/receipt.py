from datetime import datetime
from typing import List

from pydantic import BaseModel

from enums import PaymentType


class Payment(BaseModel):
    type: PaymentType
    amount: float


class ReceiptProduct(BaseModel):
    name: str
    price: float
    quantity: int


class CreateReceiptRequest(BaseModel):
    products: List[ReceiptProduct]
    payment: Payment


class ReceiptResponse(BaseModel):
    id: int
    products: List[ReceiptProduct]
    payment: Payment
    total: float
    rest: float
    created_at: datetime
