from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from src.payments.schemas import PaymentCreate, PaymentBase
from src.payments.models import Payment, PaymentTypes


def _transform_payment_type(payment: Payment, payment_type_name: PaymentTypes) -> dict:
    payment_dict = payment.__dict__
    payment_dict["payment_type"] = payment_type_name

    payment_dict.pop('_sa_instance_state', None)

    return payment_dict


class PaymentsDbService:
    @staticmethod
    async def get_all_payments(session: AsyncSession) -> list[Payment]:
        stmt = (select(Payment, PaymentTypes.type_name)
                .join(PaymentTypes, Payment.payment_type == PaymentTypes.id)
                .order_by(Payment.payment_date))

        res: Result = await session.execute(stmt)
        payments = res.all()  # .scalars()

        result_list = []
        for payment, payment_type_name in payments:
            payment_dict = _transform_payment_type(payment, payment_type_name)

            result_list.append(Payment(**payment_dict))

        return result_list

    @staticmethod
    async def get_payment_by_id(session: AsyncSession, payment_id: int) -> Payment | None:
        stmt = (
            select(Payment, PaymentTypes.type_name)
            .join(PaymentTypes, Payment.payment_type == PaymentTypes.id)
            .filter(Payment.id == payment_id)
        )

        res: Result = await session.execute(stmt)
        result = res.first()

        if result is not None:
            payment, payment_type_name = result
            payment_dict = _transform_payment_type(payment, payment_type_name)

            return Payment(**payment_dict)
        else:
            return None

    @staticmethod
    async def create_payment(session: AsyncSession, payment: PaymentCreate) -> Payment:
        payment = Payment(**payment.model_dump())

        session.add(payment)
        await session.commit()

        return payment
