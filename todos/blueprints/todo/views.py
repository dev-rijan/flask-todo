import pytz
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from sqlalchemy import text

from todos.blueprints.todo.forms import TodoForm, SearchForm
from todos.blueprints.todo.models import Todo

todo = Blueprint('todo', __name__, template_folder='templates')


@todo.before_request
@login_required
def before_request():
    """ Protect all of the todo endpoints. """
    pass


@todo.route('/todos', defaults={'page': 1})
@todo.route('/todos/page/<int:page>')
def list(page):
    search_form = SearchForm()

    sort_by = Todo.sort_by(request.args.get('sort', 'created_on'),
                           request.args.get('direction', 'desc'))

    order_values = '{0} {1}'.format(sort_by[0], sort_by[1])

    search_query = request.args.get('q', '')

    todo_query = Todo.query

    if current_user.role == 'user':
        todo_query = todo_query.filter_by(user_id=current_user.id)

    if search_query:
        todo_query = todo_query.filter(Todo.search_by_user(search_query))

    todos = todo_query \
        .order_by(text(order_values)) \
        .paginate(page, 20, True)

    return render_template('todo/index.html',
                           form=search_form,
                           todos=todos)


@todo.route('/todo/create', methods=['GET', 'POST'])
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

        return redirect(url_for('todo.list'))

    return render_template('todo/create.html', form=form)


@todo.route('/todo/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    todo = Todo.query.get(id)
    form = TodoForm(obj=todo)

    if form.validate_on_submit():
        form.populate_obj(todo)

        todo.todo_at = todo.todo_at.replace(tzinfo=pytz.UTC)

        todo.save()

        flash('Todo has been saved successfully.', 'success')
        return redirect(url_for('todo.list'))

    return render_template('todo/update.html', form=form, todo=todo)


@todo.route('/todo/complete/<int:id>', methods=['GET'])
def complete(id):
    todo = Todo.query.get(id)

    todo.is_complete = True
    todo.save()

    flash('Todo has been completed successfully.', 'success')
    return redirect(url_for('todo.list'))


@todo.route('/todos/bulk_delete', methods=['POST'])
def bulk_delete():
    ids = Todo.get_bulk_action_ids(request.form.getlist('bulk_ids'))

    if len(ids):
        delete_count = Todo.bulk_delete(ids)

        flash('{0} todo(s) were scheduled to be deleted.'.format(delete_count),
              'success')
    else:
        flash('No todos were deleted, something went wrong.', 'error')

    return redirect(url_for('todo.list'))
