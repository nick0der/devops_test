import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from sqlalchemy import create_engine
from ssl import create_default_context
from variables import email, password

file = sys.argv[1]
receiver = sys.argv[2]
subject = 'Mykola-Popyk-343 Lab5'

engine = create_engine('sqlite:///{}'.format(file), echo = False)
connection = engine.connect()
request = 'SELECT DISTINCT ip_address from access_logs'
ips = connection.execute(request)

#body = 'Unique ips: \n"+", '.join(map(lambda row: row['ip_address'],ips))
body = "Hello world!!!"

message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = email
message["To"] = receiver
message.attach(MIMEText(body, "plain"))

context = create_default_context()
with SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
    server.login(email, password)
    server.sendmail(email, receiver, message.as_string())

connection.close()
