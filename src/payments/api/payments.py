from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.payments.schemas import Payment, PaymentCreate, PaymentCreateSuccess
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

    payments: list = await payment_db_service.get_all_payments(session=session)

    return payments


@payments_router.get("/{payment_id}", response_model=Payment)
async def get_payment_by_id(payment_id: int,
                            session: AsyncSession = Depends(db_helper.get_session),
                            payment_db_service: PaymentsDbService = Depends(PaymentsDbService)) \
                            -> Payment:
    """ Shows payment by given `id` """

    payment_by_id = await payment_db_service.get_payment_by_id(session=session, payment_id=payment_id)

    if payment_by_id is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"There is no payment with id: {payment_id}"
        )

    return payment_by_id


@payments_router.get("/{payments_month}", response_model=Payment)
def get_payments_by_month(payment_month: int) -> dict:
    """ Shows payment by `month` """

    # payment: dict = get_payments(month: int)

    # return payment
    pass


@payments_router.post("/", response_model=PaymentCreateSuccess)
async def book_payment_to_wallet(payment: PaymentCreate,
                                 session: AsyncSession = Depends(db_helper.get_session),
                                 payment_db_service: PaymentsDbService = Depends(PaymentsDbService)) \
                                 -> dict:
    """ Book the payment """
    try:
        await payment_db_service.create_payment(session, payment)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="There is no payment_type like that"
                            )

    return {
            "status": status.HTTP_201_CREATED,
            "message": f"Payment booked"
    }


@payments_router.put("/{payment_id}")
def update_wallet_booking() -> dict:
    """ Updates payment by `id` """
    pass


@payments_router.delete("/{payment_id}")
def delete_wallet_payment(payment_id: int) -> dict:
    """ Deletes payment by `id` """
    pass
