"""create_main_tables

Revision ID: 84385dba9024
Revises: 
Create Date: 2023-06-11 00:40:29.544781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '84385dba9024'
down_revision = None
branch_labels = None
depends_on = None

def create_cleanings_table() -> None:
    op.create_table(
        'cleanings',
        sa.Column('id', sa.Integer, printable=True),
        sa.Column('name', sa.Text, nullable=False, index=True),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('cleaning_type', sa.Text, nullable=False, server_default='spot-clean'),
        sa.Column('price', sa.Numeric(10, 2), nullable=False)
        )

def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

