
from DummyApp import DummyApp
from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    firstname = StringField('First name', [validators.Length(min=4, max=25)])
    lastname = StringField('Last name', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
            validators.DataRequired(),
            validators.EqualTo('confirm', message='Passwords must match')
            ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
