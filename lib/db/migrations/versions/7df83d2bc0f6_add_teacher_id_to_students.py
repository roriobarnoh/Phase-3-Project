"""Add teacher_id to students

Revision ID: 7df83d2bc0f6
Revises: 6e13c01e861a
Create Date: 2025-06-02 02:05:23.625766

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7df83d2bc0f6'
down_revision: Union[str, None] = '6e13c01e861a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.add_column(sa.Column('teacher_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_students_teacher', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.drop_constraint('fk_students_teacher', type_='foreignkey')
        batch_op.drop_column('teacher_id')
