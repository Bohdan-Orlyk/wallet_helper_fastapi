"""Refactoring

Revision ID: 400984e4401c
Revises: 4f5259ff3cc4
Create Date: 2024-02-08 07:28:47.527532

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '400984e4401c'
down_revision: Union[str, None] = '4f5259ff3cc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('payment', 'payment_type',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('payment', 'payment_type',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
