"""updated student in teacher class

Revision ID: e1c9bf2f4617
Revises: 7df83d2bc0f6
Create Date: 2025-06-02 02:13:35.683756

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1c9bf2f4617'
down_revision: Union[str, None] = '7df83d2bc0f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
