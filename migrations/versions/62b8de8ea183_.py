"""empty message

Revision ID: 62b8de8ea183
Revises: e12fa025efe5
Create Date: 2021-09-04 23:34:55.607206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62b8de8ea183'
down_revision = 'e12fa025efe5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('content', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'content')
    # ### end Alembic commands ###