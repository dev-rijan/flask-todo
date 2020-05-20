from lib.util_sqlalchemy import ResourceMixin, AwareDateTime
from todos.extensions import db


class Todo(ResourceMixin, db.Model):
    __tablename__ = 'todo'

    db.Column('id', db.Integer, primary_key=True),
    db.Column('user_id',
              db.Integer,
              db.ForeignKey('users.id',
                            onupdate='CASCADE',
                            ondelete='CASCADE'),
              index=True,
              nullable=False),
    db.Column('description', db.Text, nullable=False),
    db.Column('todo_at', AwareDateTime(), nullable=False),
    db.Column('is_complete', db.Boolean(), nullable=False, server_default='1'),
