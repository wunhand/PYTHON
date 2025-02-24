import smtplib, ssl, os, imghdr
from email.message
import EmailMessage

port = 465
smtp_server = "smtp.gmail.com"
login = "davidcaseyrep@gmail.com"
password = input("Input password and press enter: ")

sender_email = "davidewcaseyrep@gmail.com"
recipient_email = 'isdewc@gmail.com'
msg = EmailMessage()

msg["Subject"] = "Speakathon!"
message["From"] = sender_email
message["To"] = recipient_email

msg.set_content("""\
    Welcome, 

    This is your chance to see the greatest speaker on earth!

    SSSaphires
    """)
msg.add_alternative = ("""\
<!Doctype html>
    <html>
        <body>
            <img src="CID:Banner">
            <br>
            <br>
            <p>"Welcome,"</p>
            <br>
            <br>
            <p>"This is your chance to see the greatest speaker on earth!"</p>
            <br>
            <br>
            <img src="CID:Signature">
        </body>
    </html>
""", subtype='html')

with smtplib.SMTP_SSL(smtp_server, port) as smtp:
    smtp.login(login, password)
    smtp.send_message(msg)
print('Sent')    