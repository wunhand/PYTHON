#Imports
import pandas as pd
import smtplib, ssl, csv, os, base64
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#CSV File
csvdata = []
with open('contacts.csv' , 'r') as file:
     reader = csv.reader(file)
     for row in reader:
         csvdata.append (
             row
         )
     csvdata.pop(0)

#Credentials
sender_email = "davidcaseyrep@gmail.com"
password = input("Input password and press enter: ")
#receiver_email = ['davidewcasey@gmail.com', 'pydewc@gmail.com', 'isdewc@gmail.com']

#For Loop

for item in csvdata:
    name = item[0]
    email = item[1]
    #Mime Setup
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = email

    text = """\
    Hi,
    How are you right now?
    """

    html = f"""\
    <!Dotype html>
    <html lang="en"> 
    <html>
    <head>
        <title>Email Automation</title>
    </head?
    <body>
        <img src="https://ss-py-email-pics.s3.us-east-1.amazonaws.com/IMG_4740.jpeg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLWVhc3QtMiJHMEUCICj78H1dcuU3CpVRmzdGsKAuFZSzA3gqTq0p7VDBK5e7AiEAhzeH%2FFvjyoQWLT8eBjHF%2BrbJQQ23iX7Lo%2F4Jo3sZLYwq7AIIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgwwMDEwMDQzOTQ4NDIiDCZ%2BZtEAGKwthaI14SrAAmQ%2BSq%2BQhe8MKcaz6XThImRf84ilx9bUB0Ku5pIx1BYji3jDhC%2Bakf0jbk7t5L9DTTLicbHW%2FitSdf1%2BpQYtAlqGXE1CTAOtZtGmjd0YG%2FvFXQqskdLOT7vrrndQqqVpcXLyzpDmka3Gd0H6QBpRkr4Y9GaxnsUAF47STpUGfGaAlgYT%2Fcr01aRxEGr0XE0oKLiGC7oWFGO8rSrDb5lf28Uoee7Q7EEmPkxsY6I%2FtvFQeQ28hMPfGQ%2BWeR2THmaNmKb54lcupd2M10ze7XNtJc44Xti4qLRlzQZje0w9kFrXwH6k5NOTH7FJHywfge2R3LQ12Jdop0Ty6Y2chjJDExO5jS2%2Bu%2B8rFIzSK0ZBhaYcS1YX4usej21%2FPhB7%2BhnDwGCvnkwx68jIAarn4nvx95GHO0%2B3sD9fsF5KsJj12AqJMJuPq7EGOrQCw73lWNTzsaOCpZ1YQeYZ%2Fml5HzjrJ%2BGGZww5d4%2Bt%2BJ7RoYUTpfb1w9MAXkfCDDJod%2Fdn36ZBOs%2FW6Xoyx5sD%2Fxgw4pAf7o%2BnMUsrjDHuHSwRaeH125aov%2BcgZhnq1%2F%2FtmnXVjWHjfsHnj4TATToNb3qWKxut%2F17G2zKGjcXGvhCqAmFx9RotGruU%2BrEArarAbRE8omr1oSmMmhqOXr1orr8wOviPXugcn4ZKDn4EISyAONXKV4s043dRdzElpcgXklb67Dvz4YMc7sLDeiO56PljIktXAmcD4B3ZGbm%2BojzMCVkH8Rjso8ygWtXDQenzHswql0GpGhTi2JJ6Z%2FGLlXkeUkSubmUl613422g8GQFFsmHskJuYcQ7hi8%2Bl6WFv%2BEe4lcAtEh3pd74mEJzh8Sj713c%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240425T211510Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Credential=ASIAQAO653FNLQX4HDF2%2F20240425%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=dc3346c80017bf10081997c6b5ccfecddb12a87921558fad187b67b7bd7da687">
        <p>Hi {name},How are you?</p>
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
            sender_email, {email}, message.as_string()
        )