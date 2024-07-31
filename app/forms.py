from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from datetime import date
from flask import flash

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class AddEventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description')
    date = DateField('Event Date', validators=[DataRequired()])
    user_id = StringField('')
    submit = SubmitField('Add')

    def validate_date(form, field):
        if field.data < date.today():
            raise ValidationError("The event date cannot be in the past.")