from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.models import Receipt, ReceiptItem, User
from dependencies import get_db
from schemas.receipt import CreateReceiptRequest, ReceiptResponse
from security.auth import get_current_user

router = APIRouter(
    prefix="/receipts",
    tags=["receipts"],
    responses={404: {"description": "Not found"}},
)


db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/receipts/", response_model=ReceiptResponse)
def create_receipt(receipt: CreateReceiptRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_receipt = Receipt(
        user_id=current_user.id,
        payment_type=receipt.payment_type,
        total=receipt.total,
        rest=receipt.rest
    )
    db.add(db_receipt)
    db.commit()
    db.refresh(db_receipt)

    for item in receipt.items:
        db_receipt_item = ReceiptItem(
            receipt_id=db_receipt.id,
            product_id=item.product_id,
            quantity=item.quantity,
            total=item.total
        )
        db.add(db_receipt_item)
    db.commit()
    db.refresh(db_receipt)

    return db_receipt


# Endpoint to retrieve a receipt by ID
@router.get("/receipts/{receipt_id}", response_model=ReceiptResponse)
def get_receipt(receipt_id: int, db: Session = Depends(get_db)):
    db_receipt = db.query(Receipt).filter(Receipt.id == receipt_id).first()
    if db_receipt is None:
        raise HTTPException(status_code=404, detail="Receipt not found")

    return db_receipt

