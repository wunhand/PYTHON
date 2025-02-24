#Imports
import pandas as pd
import smtplib, ssl, csv, os, base64
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#Credentials
sender_email = "davidcaseyrep@gmail.com"
password = input("Input password and press enter: ")
receiver_email = ['davidewcasey@gmail.com', 'pydewc@gmail.com', 'isdewc@gmail.com']

#Mime Setup
message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = ", ".join(receiver_email)

text = """\
Hi,
How are you right now?
"""

html = """\
<!Dotype html>
<html lang="en"> 
<html>
  <head>
    <title>Email Automation</title>
  </head?
  <body>
    <img src="cid:smiley1">
    <p>Hi,How are you?</p>
    <img src="cid:smiley2">
  </body>
</html>
"""

text1 = MIMEText(text, "plain")
html1 = MIMEText(html, "html")

message.attach(text1)
message.attach(html1)

fp = open('smiley1.jpg', 'rb')
image1 = MIMEImage(fp.read())
fp.close()
image1.add_header('Content-ID', '<smiley1>')
message.attach(image1)

fp = open('smiley2.jpg', 'rb')
image2 = MIMEImage(fp.read())
fp.close()
image2.add_header('Content-ID', '<smiley2>')
message.attach(image2)

#Server Connection
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )   