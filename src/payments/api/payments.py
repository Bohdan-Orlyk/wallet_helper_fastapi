from fastapi import APIRouter

payments_router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@payments_router.get("")
def get_payments_history():
    pass


@payments_router.post("")
def book_payment_to_wallet():
    pass


@payments_router.patch("")
def update_wallet_booking():
    pass


@payments_router.delete("")
def delete_wallet_payment():
    pass


