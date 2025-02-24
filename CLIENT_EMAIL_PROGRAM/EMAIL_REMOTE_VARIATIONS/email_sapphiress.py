import smtplib, ssl, csv
"""from email.mime.multipart import MIMEMultipart"""
"""from email.mime.text import MIMEText"""
"""from email.mime.image import MIMEImage"""

port = 465
smtp_server = "smtp.gmail.com"
login = "davidcaseyrep@gmail.com"
password = input("Input password and press enter: ")

"""sender_email = "davidewcaseyrep@gmail.com" """
"""recipient_email = 'davidewcasey@gmail.com, isdewc@gmail.com, pydewc@gmail.com' """


"""message = MIMEMultipart("alternative")"""
"""message["Subject"] = "Speakathon!" """
"""message["From"] = sender_email """
"""message["To"] = recipient_email """

message = """Subject: Speakathon
Welcome {name},

This is your chance to see the greatest speaker on earth!

SSSaphires
"""


"""part1 = MIMEText(text, "plain")"""
"""part2 = MIMEText(html, "html")"""

"""message.attach(part1)"""
"""message.attach(part2)"""

"""img_a = open('Banner.jpg', 'rb')"""
"""image_aa = MIMEImage(img_a.read())"""
"""img_a.close()"""

"""image_aa.add_header('Content-ID','<Banner>')"""
"""message.attach(image_aa)"""

"""img_b = open('Signature.jpg', 'rb')"""
"""image_bb = MIMEImage(img_b.read())"""
"""img_b.close()"""

"""image_bb.add_header('Content-ID','<Signature>')"""
"""message.attach(image_bb)"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(login, password)
    with open("contacts.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for potential_name, potential_email in reader:
            server.sendmail(
                login, 
                potential_email, 
                message.format(name=potential_name)
    )
    print('Sent')    