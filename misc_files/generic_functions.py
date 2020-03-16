import random
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def generate_string(length=10):
    letter = string.ascii_letters
    otp = "".join(random.choice(letter)for _ in range(length))
    return otp


def verify_mail_send(to_address, name, link):
    msg = MIMEMultipart()
    msg['From'] = 'django project Email'
    msg['to'] = to_address
    msg['subject'] = "Verify Link Mail"

    body = "Hey {}! Your verify link is {}".format(name,link)
    msg.attach(MIMEText(body,"plain"))
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("neehee6343@gmail.com","neeraj12345")
    text = msg.as_string()
    server.sendmail("neehee6343@gmail.com", to_address,text)