#!/usr/bin/env bash

cd ~/PycharmProjects/flask_tutorial/
source venv/bin/activate
# the following were moved to .env
export FLASK_APP=microblog.py
# the following secret key is for mocking purposes only. it should be replaced once deployed to a server.
#export SECRET_KEY=1c3br2ak3r5
#export MAIL_SERVER=smtp.googlemail.com
#export MAIL_PORT=587
#export MAIL_USE_TLS=1
#export MAIL_USERNAME=<sender_email> defined separately
#export MAIL_PASSWORD=<sender_email_password> defined separately
#export MS_TRANSLATOR_KEY=<azure key> defined separately
flask run