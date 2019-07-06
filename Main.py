# https://realpython.com/python-send-email/

import smtplib
import email
import ssl
import os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

host = 'smtp.gmail.com'
port = 465 # this is the port required by Gmail when encrypting with ssl
context = ssl.create_default_context() # Create a secure SSL context

sender = 'dummy.daemony@gmail.com'
receiver = 'emil.karpowicz@gmail.com'
password = 'Polska01'


# Create a multipart message and create headers

message = MIMEMultipart()
message['Subject'] = 'Multipart email test'
message['From'] = sender
message['To'] = receiver

# Add body to email

message.attach(MIMEText("This is my message",'plain'));

filename = "myfile.jpg"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)


# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    "attachment; filename= %(filename)s" % globals()
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

try:
    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(sender,password)
        server.sendmail(sender, receiver, text)
        print("Your email has beed send successfully!")
except Exception as e:
    print("Error: ")
    print(e)