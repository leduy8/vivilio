"""additional fields for Review

Revision ID: 51bb4eafa23d
Revises: 685910623ffe
Create Date: 2021-09-05 23:42:04.806694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51bb4eafa23d'
down_revision = '685910623ffe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('review', sa.Column('overview', sa.String(length=50), nullable=True))
    op.add_column('review', sa.Column('star', sa.Integer(), nullable=True))
    op.add_column('review', sa.Column('started', sa.Date(), nullable=True))
    op.add_column('review', sa.Column('finished', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('review', 'finished')
    op.drop_column('review', 'started')
    op.drop_column('review', 'star')
    op.drop_column('review', 'overview')
    # ### end Alembic commands ###
