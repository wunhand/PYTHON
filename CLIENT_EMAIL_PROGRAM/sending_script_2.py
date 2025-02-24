message = MIMEMultipart("alternative")
message["Subject"] = "Speakathon!"
message["From"] = sender_email
message["To"] =

text = """\
Welcome,

This is your chance to see the greatest speaker on earth!

SSSaphires
"""
html = """\
<html>
    <body>
        <img src="CID:Banner">
        <br>
        <br>
        <p>"Welcome"</p>
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

