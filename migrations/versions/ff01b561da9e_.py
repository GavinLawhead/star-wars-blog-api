"""empty message

Revision ID: ff01b561da9e
Revises: 
Create Date: 2022-05-04 15:06:42.169413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff01b561da9e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('charachters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('charachter_name', sa.String(length=120), nullable=False),
    sa.Column('home_planet', sa.String(length=120), nullable=True),
    sa.Column('persons_age', sa.Integer(), nullable=False),
    sa.Column('persons_species', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favourites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_name', sa.String(length=120), nullable=True),
    sa.Column('rotation_speed', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('planet_name'),
    sa.UniqueConstraint('planet_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    op.drop_table('people')
    op.drop_table('favourites')
    op.drop_table('charachters')
    # ### end Alembic commands ###