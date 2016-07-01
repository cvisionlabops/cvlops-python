#!/usr/bin/env python
import os

from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from jinja2 import Environment

DEFAULT_TEMPLATE=os.path.dirname(os.path.abspath(__file__))+'/generic.jinja2'

def send(subject, users, data={}, template=DEFAULT_TEMPLATE):
    """
    Send mail to user, admin

    
    :param subject: string, Email Subject
    :param users: List of users mail addresses
    :param data: Dictionary with key/value items for jinja2 template
    :param template: Path to template to render (default to use generic.jinja2)

    Additional information.
    -----------------------

    Example: cvl_mail.send("subject", "skubriev@cvisionlab.com", { 'body':'body', 'sender':'admin@server' } )
    """

    file = open(template, 'r')
    template = file.read()

    rt = Environment().from_string(template).render(**data)
    msg = MIMEText(rt, 'html')

    msg['Subject'] = subject
    msg.preamble = 'Preamble'
    FROM = "root"
    msg['From'] = FROM

    server = SMTP('localhost')

    for user in users:
        server.sendmail(FROM, [user], msg.as_string())

    server.quit()
