"""empty message

Revision ID: 37d0baa1d6aa
Revises: a9af690f6c60
Create Date: 2018-03-03 18:20:09.304295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37d0baa1d6aa'
down_revision = 'a9af690f6c60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'password')
    # ### end Alembic commands ###
