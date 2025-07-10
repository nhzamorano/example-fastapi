"""add content column to posts table

Revision ID: e4ffd028d970
Revises: 01e5588c9bf3
Create Date: 2025-07-04 17:39:42.873054

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4ffd028d970'
down_revision: Union[str, Sequence[str], None] = '01e5588c9bf3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
