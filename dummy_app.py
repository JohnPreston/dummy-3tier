#!flask/bin/python

import os, sys, time
import argparse
from DummyApp import DummyApp
from werkzeug.contrib.fixers import ProxyFix

def main():

    parser = argparse.ArgumentParser(description='Starts the App')
    parser.add_argument("--debug", default=False, action='store_true',
                        help="define the section to be updated", required=False)

    args = parser.parse_args()
    debug = args.debug

    DummyApp.wsgi_app = ProxyFix(DummyApp.wsgi_app)
    DummyApp.run(debug=debug)

if __name__ == '__main__':
    main()
