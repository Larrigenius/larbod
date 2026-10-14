"""Make session expiry timezone-aware.

Revision ID: b7e2c91a4f60
Revises: ac90c5860f93
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "b7e2c91a4f60"
down_revision: Union[str, Sequence[str], None] = "ac90c5860f93"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "user_sessions",
        "expires_at",
        existing_type=sa.DateTime(timezone=False),
        type_=sa.DateTime(timezone=True),
        existing_nullable=False,
        postgresql_using="expires_at AT TIME ZONE 'UTC'",
    )


def downgrade() -> None:
    op.alter_column(
        "user_sessions",
        "expires_at",
        existing_type=sa.DateTime(timezone=True),
        type_=sa.DateTime(timezone=False),
        existing_nullable=False,
        postgresql_using="expires_at AT TIME ZONE 'UTC'",
    )
