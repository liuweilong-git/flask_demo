"""empty message

Revision ID: 214f0d905151
Revises: a491d4c35456
Create Date: 2022-03-06 16:17:47.302012

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '214f0d905151'
down_revision = 'a491d4c35456'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=100), nullable=False))
    # ### end Alembic commands ###
