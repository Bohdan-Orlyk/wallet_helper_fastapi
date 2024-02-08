from datetime import datetime

from pydantic import BaseModel, Field


class PaymentBase(BaseModel):
    price: float = Field(gt=0.0, default=0.00)
    payment_type: int = 0


class Payment(PaymentBase):
    id: int
    payment_date: datetime
    payment_type: str


class PaymentCreate(PaymentBase):
    payment_type: int = 0


class PaymentCreateSuccess(BaseModel):
    status: int = 201
    message: str
