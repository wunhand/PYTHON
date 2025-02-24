import smtplib
import ssl
import csv
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

sender_email = "davidcaseyrep@gmail.com"
password = input("Input password and press enter: ")

message = MIMEMultipart("alternative")
message["Subject"] = "Speakathon!"
message["From"] = sender_email
message["To"] = recipient_email

text = """\
Welcome {name},

This is your chance to see the greatest speaker on earth!

SSSaphires
"""
html = """\
<html>
    <body>
        <img src="CID:Banner">
        <br>
        <br>
        <p>"Welcome " + {name}</p>
        <br>
        <br>
        <p>"This is your chance to see the greatest speaker on earth!"</p>
        <br>
        <br>
        <img src="CID:Signature">
    </body>
</html>
"""

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

im1 = open('Banner.jpg', 'rb')
image1 = MIMEImage(im1.read())
im1.close()

image1.add_header('Content-ID','<Banner>')
message.attach(image1)

im2 = open('Signature.jpg', 'rb')
image2 = MIMEImage(im2.read())
im2.close()

image2.add_header('Content-ID','<Signature>')
message.attach(image2)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    with open("Contacts.csv") as csv_file:
        jobs = csv.reader(csv_file)
        next(jobs)
        for name, email in jobs:
            email_text=text_content.format(name, email)
            message.attach(MIMEText(email_text))
            server.sendmail(
                sender_email, 
                recipient_email,
                message,
            )
    print(f'Complete!')
