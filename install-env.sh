#!/bin/bash

rm -rf ./venv
mkdir ./venv
virtualenv ./venv
./venv/bin/activate


# Под Debian необходимо поставить библиотеки
# apt install default-libmysqlclient-dev
# apt-get install python3-dev

# необходимые переменные окружения
export FLASK_APP=server.py

# обновляем сам пакетный менеджер
./venv/bin/pip install --upgrade pip

./venv/bin/pip install Flask

./venv/bin/pip install flask-sqlalchemy

./venv/bin/pip install flask-migrate

./venv/bin/pip install flask-script

./venv/bin/pip install configparser

./venv/bin/pip install mysqlclient

./venv/bin/pip install Flask-Mail

./venv/bin/pip install jsonschema
