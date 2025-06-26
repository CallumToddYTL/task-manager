from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Optional
from .models import User
import re

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=8), 
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')
    ])
    role = SelectField('Role', choices=[('user', 'User'), ('admin', 'Admin')], validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user = User.query.filter_by(username=username.data).first()
        if existing_user:
            raise ValidationError('This username is already taken.')

    def validate_password(self, password):
        pw = password.data
        if (len(pw) < 8 or not re.search(r'[A-Z]', pw) or 
            not re.search(r'[a-z]', pw) or not re.search(r'\d', pw) or 
            not re.search(r'[^\w\s]', pw)):
            raise ValidationError(
                "Password must be at least 8 characters long and include at least one uppercase letter, "
                "one lowercase letter, one digit, and one special character."
            )   

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    status = SelectField('Status', choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')])
    assigned_user = SelectField('Assign to User (optional)', coerce=int, validators=[Optional()])
    submit = SubmitField('Save Task')

class DeleteForm(FlaskForm):
    submit = SubmitField('Delete Task')