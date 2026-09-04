"""add created_at to contacts

Revision ID: 4dd01c9af687
Revises: 1c1d1169e6d7
Create Date: 2026-09-03 12:52:24.411505

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4dd01c9af687'
down_revision: Union[str, Sequence[str], None] = '1c1d1169e6d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "contacts",
        sa.Column("created_at", sa.DateTime(), nullable=True)
    )

    op.execute(
        "UPDATE contacts SET created_at = CURRENT_TIMESTAMP "
        "WHERE created_at IS NULL"
    )

    op.alter_column(
        "contacts",
        "created_at",
        nullable=False
    )


def downgrade() -> None:
    op.drop_column('contacts', 'created_at')
    # ### end Alembic commands ###
