"""add user sessions

Revision ID: ac90c5860f93
Revises: 16cd13631263
Create Date: 2026-09-29 11:51:06.037532

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac90c5860f93'
down_revision: Union[str, Sequence[str], None] = '16cd13631263'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'user_sessions',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('user_id', sa.UUID(), nullable=False),
        sa.Column('session_token', sa.String(length=128), nullable=False),
        sa.Column('expires_at', sa.DateTime(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
            ondelete='CASCADE'
        ),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(
        op.f('ix_user_sessions_expires_at'),
        'user_sessions',
        ['expires_at'],
        unique=False
    )

    op.create_index(
        op.f('ix_user_sessions_session_token'),
        'user_sessions',
        ['session_token'],
        unique=True
    )

    op.create_index(
        op.f('ix_user_sessions_user_id'),
        'user_sessions',
        ['user_id'],
        unique=False
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        op.f('ix_user_sessions_user_id'),
        table_name='user_sessions'
    )

    op.drop_index(
        op.f('ix_user_sessions_session_token'),
        table_name='user_sessions'
    )

    op.drop_index(
        op.f('ix_user_sessions_expires_at'),
        table_name='user_sessions'
    )

    op.drop_table('user_sessions')
