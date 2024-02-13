from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.models import Receipt, ReceiptProduct, User, Payment
from dependencies import get_db
from schemas.receipt import CreateReceiptRequest, ReceiptResponse
from security.auth import get_current_user

router = APIRouter(
    prefix="/receipts",
    tags=["receipts"],
    responses={404: {"description": "Not found"}},
)


db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/", response_model=None)
def create_receipt(
    receipt: CreateReceiptRequest,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    total = sum([i.price * i.quantity for i in receipt.products])
    rest = round(receipt.payment.amount - total, 2)

    # Create payment entry
    payment = Payment(type=receipt.payment.type, amount=receipt.payment.amount)
    db.add(payment)
    db.commit()
    db.refresh(payment)

    # Create receipt entry
    db_receipt = Receipt(
        user_id=current_user["id"], total=total, rest=rest, payment_id=payment.id
    )
    db.add(db_receipt)
    db.commit()
    db.refresh(db_receipt)

    # Create receipt products entries
    for product_data in receipt.products:
        receipt_product = ReceiptProduct(
            receipt_id=db_receipt.id,
            name=product_data.name,
            quantity=product_data.quantity,
            price=product_data.price,
        )
        db.add(receipt_product)
        print(receipt_product)
    db.commit()

    response_receipt = ReceiptResponse(
        id=db_receipt.id,
        products=[
            {"name": product.name, "quantity": product.quantity, "price": product.price}
            for product in receipt.products
        ],
        payment={"type": payment.type, "amount": payment.amount},
        total=total,
        rest=rest,
        created_at=db_receipt.created_at,
    )
    return response_receipt


# Endpoint to retrieve a receipt by ID
@router.get("/{receipt_id}", response_model=ReceiptResponse)
def get_receipt(receipt_id: int, db: Session = Depends(get_db)):
    db_receipt = db.query(Receipt).filter(Receipt.id == receipt_id).first()
    if db_receipt is None:
        raise HTTPException(status_code=404, detail="Receipt not found")

    return db_receipt
