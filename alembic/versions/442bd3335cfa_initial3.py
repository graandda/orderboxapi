"""initial3

Revision ID: 442bd3335cfa
Revises: 72bf98e2befe
Create Date: 2024-02-13 13:51:16.762590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "442bd3335cfa"
down_revision = "72bf98e2befe"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("payments", sa.Column("user_id", sa.Integer(), nullable=False))
    op.create_foreign_key(None, "payments", "users", ["user_id"], ["id"])
    op.drop_constraint("receipts_payment_id_fkey", "receipts", type_="foreignkey")
    op.drop_column("receipts", "payment_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "receipts",
        sa.Column("payment_id", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.create_foreign_key(
        "receipts_payment_id_fkey", "receipts", "payments", ["payment_id"], ["id"]
    )
    op.drop_constraint(None, "payments", type_="foreignkey")
    op.drop_column("payments", "user_id")
    # ### end Alembic commands ###
