"""Increase length of password_hash and refresh_token columns

Revision ID: 7e75c999da74
Revises: 
Create Date: 2024-06-13 13:23:10.890169

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7e75c999da74'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.String(length=256),
               existing_nullable=False)
        batch_op.alter_column('refresh_token',
               existing_type=mysql.VARCHAR(length=256),
               type_=sa.String(length=512),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('refresh_token',
               existing_type=sa.String(length=512),
               type_=mysql.VARCHAR(length=256),
               existing_nullable=True)
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=256),
               type_=mysql.VARCHAR(length=128),
               existing_nullable=False)

    # ### end Alembic commands ###
