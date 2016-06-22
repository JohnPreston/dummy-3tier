import os, sys, json, time
from flask import Flask, jsonify, Response
from flask import Flask, current_app, request

DummyApp = Flask(__name__)
DummyApp.config.from_object('config')

from DummyApp import views
