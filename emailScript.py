#Script to Send out emails

import sys
import smtplib, ssl
import getpass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#TODO: Read in list of emails from txt file
#TODO: ability to send images/attachments

myAddress = "" #your email goes here
toAddress = "" #recipient email goes here
subject = "Subject goes here"
body = "hello there"

def sendMessage(myAddress, toAdress, subject, body):
    message = MIMEMultipart()
    message['From'] = myAddress
    message['To'] = toAddress
    message['Subject'] = subject
    body = "Juwon is testing a script to send emails."
    message.attach(MIMEText(body,'plain'))

    password = getpass.getpass("Enter Email password:")

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(myAddress, password)
    server.send_message(message)
    print("Email Sent!")
    server.quit()

sendMessage(myAddress,toAddress,subject,body)