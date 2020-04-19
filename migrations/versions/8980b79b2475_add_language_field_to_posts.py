"""add language field to posts

Revision ID: 8980b79b2475
Revises: 199faab844e2
Create Date: 2020-04-18 16:07:47.507245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8980b79b2475'
down_revision = '199faab844e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
