"""Refactor models to reduce repetition

Revision ID: aed5e39cea39
Revises: ad66c0678106
Create Date: 2023-05-11 23:17:12.014805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aed5e39cea39'
down_revision = 'ad66c0678106'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('goal', 'title',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('goal', 'title',
               existing_type=sa.TEXT(),
               nullable=True)
    # ### end Alembic commands ###
