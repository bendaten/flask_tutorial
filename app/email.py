from threading import Thread
from flask import current_app
from flask_mail import Message

from app import mail


def send_async_email(the_app, msg):
    with the_app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    # since the mail is sent asynchronously current_app may be dynamically linked to another app by the time
    # the email is actually sent, therefore we need the actual object and not its link
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()
