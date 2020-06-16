from sqlalchemy import or_

from lib.util_sqlalchemy import ResourceMixin, AwareDateTime
from todos.blueprints.user.models import User
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
    todo_at = db.Column('todo_at', db.DateTime(), nullable=False)
    is_complete = db.Column('is_complete', db.Boolean(), nullable=False, server_default='0')

    user = db.relationship(User, backref='todo')

    @classmethod
    def bulk_complete(cls, ids):
        """
        Update 1 or more model instances.

        :param ids: List of ids to be updated
        :type ids: list
        :return: Number of updated instances
        """
        update_count = cls.query.filter(cls.id.in_(ids)).update(
            {cls.is_complete: True})
        db.session.commit()

        return update_count

    @classmethod
    def search_by_user(cls, query):
        """
        Search a resource by 1 or more fields.

        :param query: Search query
        :type query: str
        :return: SQLAlchemy filter
        """
        if not query:
            return ''

        search_query = '%{0}%'.format(query)
        search_chain = (User.email.ilike(search_query),
                        User.username.ilike(search_query))

        return Todo.user.has(or_(*search_chain))
