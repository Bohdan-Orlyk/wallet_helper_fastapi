from datetime import datetime

from pydantic import BaseModel, Field
from enum import Enum


class PaymentTypes(Enum):
    HOME: str = "Home"
    SHOPS: str = "Shops"
    OTHER: str = "Other"


class AllPaymentsSchema(BaseModel):
    payment_id: int
    total_price: float = Field(gt=0.0, default=0.00)
    type: PaymentTypes = PaymentTypes.OTHER
    by_date: datetime  # = .now().strftime('%Y-%b')  # change to f"{date_from=:} - {date_to=:}


class PaymentSchema(BaseModel):
    payment_id: int
    price: float = Field(gt=0.0, default=0.00)
    type: PaymentTypes = PaymentTypes.OTHER
    payment_month: datetime  # = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # change to date_of_payment




