from flask import Blueprint, render_template, redirect, url_for

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    return redirect(url_for('todo.list'))
