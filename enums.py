from enum import Enum


class PaymentType(str, Enum):
    cash = "cash"
    cashless = "cashless"


class OrderSatus(str, Enum):
    failed = "failed"
    success = "success"
