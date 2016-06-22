import os, sys, json, time
from flask import Flask, jsonify, Response
from flask import Flask, current_app, request
from flask.ext.sqlalchemy import SQLAlchemy

DummyApp = Flask(__name__)
DummyApp.config.from_object('config')
db = SQLAlchemy(DummyApp)

from DummyApp import views
import users

