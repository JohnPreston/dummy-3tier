import os, json
from DummyApp import DummyApp

from flask import Flask, jsonify, request, make_response, render_template

@DummyApp.route('/')
def hello():
    return render_template('index.j2')
