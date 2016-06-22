import os, json
from DummyApp import DummyApp, db

from flask import Flask, jsonify, request, make_response, render_template, redirect, flash
from forms import RegistrationForm
from users import Users

@DummyApp.route('/')
def hello():
    return render_template('index.j2')

@DummyApp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Users(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
        user.add_user(user)
        flash('Thanks for registering')
        return redirect('/')
    return render_template('register.j2', form=form)

@DummyApp.route('/healthcheck')
def healthCheck():
    """
    Returns 200 OK if the DB count returns a value
    """
    db_user_count = int(db.session.query(Users).count())
    if (db_user_count) > 0:
        return "OK, we have %d users" % (db_user_count)
    else:
        return "There are users"

