from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from src.payments.schemas import PaymentCreate
from src.payments.models import Payment


class PaymentsDbService:
    @staticmethod
    async def get_payments(session: AsyncSession) -> list[Payment]:
        stmt = select(Payment).order_by(Payment.payment_date)

        res: Result = await session.execute(stmt)
        payments = res.scalars().all()

        return list(payments)

    @staticmethod
    async def get_payment_by_id(session: AsyncSession, payment_id: int) -> Payment | None:
        payment = await session.get(Payment, payment_id)

        return payment

    @staticmethod
    async def create_payment(session: AsyncSession, payment: PaymentCreate) -> Payment:
        payment = Payment(**payment.model_dump())
        session.add(payment)
        await session.commit()

        return payment



