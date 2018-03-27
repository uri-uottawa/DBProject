"""empty message

Revision ID: 704e89cb8f64
Revises: 5c822007d9fa
Create Date: 2018-03-23 08:32:22.670690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '704e89cb8f64'
down_revision = '5c822007d9fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurant', sa.Column('types', sa.VARCHAR(length=20), nullable=False))
    op.drop_column('restaurant', 'type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurant', sa.Column('type', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
    op.drop_column('restaurant', 'types')
    # ### end Alembic commands ###
