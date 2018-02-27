"""empty message

Revision ID: bf2143e61e05
Revises: 
Create Date: 2018-02-27 22:51:26.414181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf2143e61e05'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('UserData',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=64), nullable=True),
    sa.Column('Description', sa.String(length=256), nullable=True),
    sa.Column('CreateDate', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('UserData')
    # ### end Alembic commands ###
