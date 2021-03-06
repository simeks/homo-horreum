"""Image tables

Revision ID: 332835b86836
Revises: 279068d14c7c
Create Date: 2017-02-17 11:13:46.173419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '332835b86836'
down_revision = '279068d14c7c'
branch_labels = None
depends_on = '52337e31da34'


def upgrade():
    op.create_table('img',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('person_id', sa.Integer, sa.ForeignKey('person.id')),
            sa.Column('type', sa.String),

            # These three are all three numbers, possibly split them up
            sa.Column('dimensions', sa.String),
            sa.Column('origin', sa.String),
            sa.Column('spacing', sa.String),
            sa.Column('npoints', sa.Integer),
    )

    op.create_table('img_data',
            sa.Column('img_id', sa.Integer, sa.ForeignKey('img.id')),
            sa.Column('data', sa.LargeBinary()) # Blob
    )


def downgrade():
    for table in ['img_data', 'img']:
        op.drop_table(table)
