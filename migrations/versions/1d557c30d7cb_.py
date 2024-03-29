"""empty message

Revision ID: 1d557c30d7cb
Revises: 370e82f9bc0f
Create Date: 2019-06-06 23:06:29.835104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d557c30d7cb'
down_revision = '370e82f9bc0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('name', table_name='person')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('name', 'person', ['name'], unique=True)
    # ### end Alembic commands ###
