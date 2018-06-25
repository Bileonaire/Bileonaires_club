"""empty message

Revision ID: d9ff39eb5509
Revises: 
Create Date: 2018-06-24 00:51:48.932908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9ff39eb5509'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ride_id', sa.Integer(), nullable=False),
    sa.Column('driver_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('accepted', sa.Boolean(), nullable=True),
    sa.Column('status', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ride',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('departurepoint', sa.String(length=250), nullable=False),
    sa.Column('destination', sa.String(length=250), nullable=False),
    sa.Column('departuretime', sa.String(length=250), nullable=False),
    sa.Column('cost', sa.String(), nullable=False),
    sa.Column('maximum', sa.Integer(), nullable=False),
    sa.Column('driver_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('usertype', sa.String(length=250), nullable=False),
    sa.Column('carmodel', sa.String(length=250), nullable=True),
    sa.Column('numberplate', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('ride')
    op.drop_table('request')
    # ### end Alembic commands ###
