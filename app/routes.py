from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Task, db
from .forms import TaskForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@main.route('/task/new', methods=['GET', 'POST'])
@login_required
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            status=form.status.data,
            user_id=current_user.id
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('task_form.html', form=form, task=None)

@main.route('/task/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_task(id):
    task = Task.query.get_or_404(id)

    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.status = form.status.data
        db.session.commit()
        return redirect(url_for('main.dashboard'))

    return render_template('task_form.html', form=form, task=task)

@main.route('/task/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)

    if current_user.role != 'admin':
        flash("Only admins can delete tasks.")
        return redirect(url_for('main.dashboard'))

    form = DeleteForm()
    if form.validate_on_submit():
        db.session.delete(task)
        db.session.commit()
        flash("Task deleted.")
        return redirect(url_for('main.dashboard'))

    return render_template('confirm_delete.html', task=task, form=form)