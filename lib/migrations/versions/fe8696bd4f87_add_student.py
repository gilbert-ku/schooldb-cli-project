"""add student

Revision ID: fe8696bd4f87
Revises: be99b821c492
Create Date: 2023-09-07 11:00:56.446223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fe8696bd4f87'
down_revision: Union[str, None] = 'be99b821c492'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
