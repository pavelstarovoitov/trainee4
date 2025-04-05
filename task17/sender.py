#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
import os
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import argparse


load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")     # Get email from .env file
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")   # Get password from .env file


def send_email(recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())

        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--body')           # Set -b for accepting email body
    parser.add_argument('-s', '--subject') 	  # Set -s for accepting email subject
    args = parser.parse_args()
    # recipient = "pavelstarovoitov91@gmail.com"
    recipient = "trainee4@easytechapps.com"
    subject = args.subject
    if not subject:
        subject = "Test email"                    # if user didn't set email subject than set default email subject
    body = args.body
    if not body:
        body = "test email from python script"    # if user didn't set email body than set default email body
    send_email(recipient, subject, body)          # send email
