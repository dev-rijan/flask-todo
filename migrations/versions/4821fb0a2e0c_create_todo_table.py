from alembic import op
import sqlalchemy as sa


"""create todo table

Revision ID: 4821fb0a2e0c
Revises: 
Create Date: 2020-05-17 08:54:47.722907

"""

# revision identifiers, used by Alembic.
revision = '4821fb0a2e0c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('todo',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('user_id',
                              sa.Integer,
                              sa.ForeignKey('users.id',
                                            onupdate='CASCADE',
                                            ondelete='CASCADE'),
                              index=True,
                              nullable=False),
                    sa.Column('description', sa.Text, nullable=False),
                    sa.Column('todo_at', sa.DateTime(), nullable=False),
                    sa.Column('document', sa.String(50)),
                    sa.Column('is_complete', sa.Boolean(), nullable=False, server_default='0'),
                    sa.Column('created_on', sa.TIMESTAMP),
                    sa.Column('updated_on', sa.TIMESTAMP))


def downgrade():
    op.drop_table('todo')
