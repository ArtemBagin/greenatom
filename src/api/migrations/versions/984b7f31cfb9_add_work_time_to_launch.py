"""add work time to launch

Revision ID: 984b7f31cfb9
Revises: 00319c33339e
Create Date: 2024-03-28 18:35:40.768130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '984b7f31cfb9'
down_revision: Union[str, None] = '00319c33339e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('launch', sa.Column('work_time', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('launch', 'work_time')
    # ### end Alembic commands ###