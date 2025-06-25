from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Task, db, User
from .forms import TaskForm, DeleteForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    tasks = Task.query.all()
    delete_form = DeleteForm()
    return render_template('tasks.html', tasks=tasks, delete_form=delete_form)

@main.route('/task/new', methods=['GET', 'POST'])
@login_required
def new_task():
    form = TaskForm()
    users = User.query.all()
    form.assigned_user.choices = [(0, 'General (Unassigned)')] + [(user.id, user.username) for user in users]

    if form.validate_on_submit():
        user_id = form.assigned_user.data if form.assigned_user.data != 0 else None
        task = Task(
            title=form.title.data,
            description=form.description.data,
            status=form.status.data,
            user_id=user_id
        )
        db.session.add(task)
        db.session.commit()
        flash('Task created.')
        return redirect(url_for('main.dashboard'))

    return render_template('task_form.html', form=form, task=None)

@main.route('/task/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_task(id):
    task = Task.query.get_or_404(id)

    form = TaskForm(obj=task)
    users = User.query.all()
    form.assigned_user.choices = [(0, 'General (Unassigned)')] + [(user.id, user.username) for user in users]

    if request.method == 'GET':
        form.assigned_user.data = task.user_id if task.user_id is not None else 0

    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data or ''
        task.status = form.status.data
        task.user_id = form.assigned_user.data if form.assigned_user.data != 0 else None

        db.session.commit()
        flash('Task updated.')
        return redirect(url_for('main.dashboard'))

    return render_template('task_form.html', form=form, task=task)

@main.route('/task/delete/<int:id>', methods=['POST'])
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