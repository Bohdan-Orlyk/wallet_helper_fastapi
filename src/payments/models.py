from sqlalchemy import Column, ForeignKey, Integer, String, Float, TIMESTAMP

from datetime import datetime
from database.db import Base


def set_payment_date():
    return datetime.strptime(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")


class Payment(Base):
    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float, nullable=False)
    payment_date = Column(TIMESTAMP, default=set_payment_date)

    payment_type = Column(Integer, ForeignKey('payment_types.id'),  nullable=False)


class PaymentTypes(Base):
    __tablename__ = 'payment_types'

    id = Column(Integer, primary_key=True)
    type_name = Column(String)


