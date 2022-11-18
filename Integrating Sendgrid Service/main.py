import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *


def send_email():
    from_email = Email('vijay.annamalai001@gmail.com')
    to_email = To('dhinavasudevan@gmail.com')
    subject = 'Sending with SendGrid is Fun'
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, to_email, subject, content)

    try:
        sg = SendGridAPIClient('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')
        response = sg.send(mail)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


send_email()