from datetime import datetime

from pydantic import BaseModel, Field


class PaymentBase(BaseModel):
    price: float = Field(gt=0.0, default=0.00)
    payment_type: int = 0
    payment_date: datetime


class Payment(PaymentBase):
    id: int


class PaymentCreate(PaymentBase):
    pass
