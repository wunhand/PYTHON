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
    <img src="https://ss-py-email-pics.s3.us-east-1.amazonaws.com/IMG_4740.jpeg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLWVhc3QtMSJIMEYCIQCBn9a4GPHVUXv57eJtdne27ijh6JNEQTCTrS2uNk7jFQIhAJ%2F5RHvp9Q4KfMWslWU%2BJa8AvrzGcnUbF5pq5YjLNlE5KuMCCFoQABoMMDAxMDA0Mzk0ODQyIgyl%2BpnOd6IQlMCJ100qwAKGkd9kS04OKEBgqbSPujSGwo%2BGCiaR0G4qarOg21oyjjUuKLMHEyWp3cD%2FJ0McMXOIntZSOWXBLPYq4jotPny%2FOoiJ%2BWXtxyhCKIgUxJjlKOjLlVBRYM0OYIUTJgzsqxfGhDAKDHnTFhan1kC7A4xWv2OvEnIDEoy7TkdNwMMHcdeHbObFnnWKbNrFIC6WRouxP%2BGMnoh7Ozmpruk3Bvm8Eo9w7fPRNXeJtVqLYeDa%2FHjO5zxdCzsH0my03vr364Gq7CmxDDq6tLTSLzC7d0Sn%2B%2FVh7Um91GbLOREWhyVZgGBJLJh%2BgtTHf6RKgkIEyegmMhb0kV4jOv0quRWLcLMur4vD3OgeIEjCEQqAxc4Qw96oEy3H98PIB6SQt%2B8x9MFRng7kMkOKnu5Li%2FMFLM8Gx5siSjFP5lMKpPl3YbQdjTDF15ixBjqzAguGcutT0ifwqvvRuGxRQAYCKbdW%2FpvO9fgzjz6CkXbgNKkh0P9ke5MHWvjhNK9id2ruEvbJh8UFLpKw6Qf1Hpf%2BkgZ7vv5ujoZcvp5TTGU%2BfnUjeNl%2BiaCzesENHu8SdEjrG7CXOcIY87l0kznN0xDWxsOASnwXcTDjh9d7heRCkaIm12DSK6k6Xn6RUv64wo7Kb9F4%2F5hTN2vhGRzvRK0ZCcCQEea6PGMdzmD0rVmm0akgGICylydjZMjA7TrCDT9zd0RYAA49ur8xpIe%2FAyIV4P%2B5yWExQg81M8GK255dx6D4bCi5u5cyPi3303eEmSrzW4YlFTEqYd4nDZ3JB8eoN5PZiCI%2FwQ5eJveiKCRHdI8htvsR7JQOJcVDwEdzE7Vm1d9djsAw34Thzuwr0KbLsE4%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240422T094203Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Credential=ASIAQAO653FNDPTLEYQO%2F20240422%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=8b66b73b0eb2193742a9d76132496fc5ce111c2b012cd0ee8ece79ac89e48333" alt="smiley" height="50px" width="50px">
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