#Imports
import pandas as pd
import smtplib, ssl, csv, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Credentials
sender_email = "davidcaseyrep@gmail.com"
password = input("Input password and press enter: ")
receiver_email = "isdewc@gmail.com"

#Mime Setup
message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

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
    <p>Hi,How are you?</p>
  </body>
</html>
"""

text1 = MIMEText(text, "plain")
html1 = MIMEText(html, "html")

message.attach(text1)
message.attach(html1)

#Server Connection
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )   