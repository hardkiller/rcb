#!/bin/bash

./venv/bin/python server.py db init
./venv/bin/python server.py db migrate
./venv/bin/python server.py db upgrade
./venv/bin/python server.py db --help
