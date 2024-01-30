from fastapi import APIRouter, status, HTTPException, Depends

from src.payments.services.payments_database_service import PaymentsDbService, Example1, Example2
from src.payments.schemas import AllPaymentsSchema, PaymentSchema


payments_router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@payments_router.get("", response_model=AllPaymentsSchema)
def get_payments_history():
    """ Shows all payments """

    # payments: dict = get_payments()

    # return payments
    pass


@payments_router.get("/{payment_id}", response_model=PaymentSchema)
def get_payment_by_id(payment_id: int):
    """ Shows payment by given `id` """

    # payment: dict = get_payments(payment_id: int, month: int)

    # return payment
    pass


@payments_router.get("/{payments_month}", response_model=PaymentSchema)
def get_payments_by_month(payment_month: int):
    """ Shows payment by `month` """

    # payment: dict = get_payments(month: int)

    # return payment
    pass


@payments_router.post("")
def book_payment_to_wallet():
    """ Book the payment """
    pass


@payments_router.patch("/{payment_id}")
def update_wallet_booking():
    """ Updates payment by `id` """
    pass


@payments_router.delete("/{payment_id}")
def delete_wallet_payment(payment_id: int):
    """ Deletes payment by `id` """
    pass


