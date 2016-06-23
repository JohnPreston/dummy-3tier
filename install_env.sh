#!/usr/bin/env bash

git clone https://github.com/johnpreston/dummy-3tier ~/dummy-3tier
sudo yum install mysql mysql-devel gcc python-pip python-virtualenv -y MySQL-python
sudo pip install pip --upgrade
cd ~/dummy-3tier
virtualenv dummy_env
source dummy_env/bin/activate
pip install flask Flask-WTF flask-sqlalchemy requests gunicorn supervisor mysql-python
supervisord -c ~/dummy-3tier/supervisord.conf

pip install nginx -y
# Script the import of the NGINX configuration file
