from lib.util_sqlalchemy import ResourceMixin, AwareDateTime
from todos.extensions import db


class Todo(ResourceMixin, db.Model):
    __tablename__ = 'todo'

    id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    user_id = db.Column('user_id',
                        db.Integer,
                        db.ForeignKey('users.id',
                                      onupdate='CASCADE',
                                      ondelete='CASCADE'),
                        index=True,
                        nullable=False)
    description = db.Column('description', db.Text, nullable=False)
    todo_at = db.Column('todo_at', AwareDateTime(), nullable=False)
    is_complete = db.Column('is_complete', db.Boolean(), nullable=False, server_default='0')
