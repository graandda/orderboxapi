from datetime import datetime
from typing import List

from pydantic import BaseModel

from enums import PaymentType
from schemas.product import Product


class Payment(BaseModel):
    type: PaymentType
    amount: float


class CreateReceiptRequest(BaseModel):
    products: List[Product]
    payment: Payment


class ReceiptResponse(BaseModel):
    id: int
    products: List[Product]
    payment: Payment
    total: float
    rest: float
    created_at: datetime
