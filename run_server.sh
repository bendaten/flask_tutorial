#!/usr/bin/env bash

cd ~/PycharmProjects/flask_tutorial/
source venv/bin/activate
export FLASK_APP=microblog.py
# the following secret key is for mocking purposes only. it should be replaced once deployed to a server.
export SECRET_KEY=1c3br2ak3r5
flask run