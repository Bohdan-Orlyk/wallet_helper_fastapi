from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.payments.schemas import Payment, PaymentCreate
from src.payments.services.payments_database_service import PaymentsDbService

from database.db import db_helper


payments_router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@payments_router.get("/", response_model=list[Payment])
async def get_payments_history(session: AsyncSession = Depends(db_helper.get_session),
                               payment_db_service: PaymentsDbService = Depends(PaymentsDbService)) -> list:
    """ Shows all payments """
    payments: list = await payment_db_service.get_payments(session=session)

    return payments


@payments_router.get("/{payment_id}", response_model=Payment)
def get_payment_by_id(payment_id: int) -> dict:
    """ Shows payment by given `id` """

    # payment: dict = get_payments(payment_id: int, month: int)

    # return payment
    pass


@payments_router.get("/{payments_month}", response_model=Payment)
def get_payments_by_month(payment_month: int) -> dict:
    """ Shows payment by `month` """

    # payment: dict = get_payments(month: int)

    # return payment
    pass


@payments_router.post("/", response_model=Payment)
async def book_payment_to_wallet(
                                payment: PaymentCreate,
                                session: AsyncSession = Depends(db_helper.get_session),
                                payment_db_service: PaymentsDbService = Depends(PaymentsDbService)) -> Payment:
    """ Book the payment """
    return await payment_db_service.create_payment(session, payment)


@payments_router.put("/{payment_id}")
def update_wallet_booking() -> dict:
    """ Updates payment by `id` """
    pass


@payments_router.delete("/{payment_id}")
def delete_wallet_payment(payment_id: int) -> dict:
    """ Deletes payment by `id` """
    pass


