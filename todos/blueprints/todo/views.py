import pytz
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from todos.blueprints.todo.forms import TodoForm
from todos.blueprints.todo.models import Todo

todo = Blueprint('todo', __name__, template_folder='templates')


@todo.route('/todos', methods=['GET', 'POST'])
@login_required
def todos():
    pass


@todo.route('/todo/create', methods=['GET', 'POST'])
@login_required
def create():
    todo = Todo()

    form = TodoForm()

    if form.validate_on_submit():
        form.populate_obj(todo)

        if not todo.user_id:
            todo.user_id = current_user.id

        todo.todo_at = todo.todo_at.replace(tzinfo=pytz.UTC)

        todo.save()

        flash('Todo been created successfully.', 'success')

        return redirect(url_for('admin.users'))

    return render_template('todo/create.html', form=form)
