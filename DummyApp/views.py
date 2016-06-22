import os, json
from DummyApp import DummyApp

from flask import Flask, jsonify, request, make_response

@DummyApp.route('/')
def hello():
    return "Hello World"

