"""initial2

Revision ID: 72bf98e2befe
Revises: 6f3e58f044a0
Create Date: 2024-02-13 13:49:05.716189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "72bf98e2befe"
down_revision = "6f3e58f044a0"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("receipts", sa.Column("payment_id", sa.Integer(), nullable=False))
    op.create_foreign_key(None, "receipts", "payments", ["payment_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "receipts", type_="foreignkey")
    op.drop_column("receipts", "payment_id")
    # ### end Alembic commands ###
