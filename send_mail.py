import smtplib
from email.mime.text import MIMEText
import os

# Securely load SMTP credentials from environment variables
smtp_server = os.getenv("SMTP_SERVER", "live.smtp.mailtrap.io")
login = os.getenv("SMTP_LOGIN", "api")
password = os.getenv("SMTP_PASSWORD", "1a2b2c4d5e6f7g")

port = 587
sender_email = "mailtrap@example.com"
receiver_email = "new@example.com"  # Corrected spelling

text = """\
Hi,
Check out the new post on the Mailtrap blog:
SMTP Server for Testing: Cloud-based or Local?
https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/
Feel free to let us know what content would be useful for you!
"""

# Create the email message
message = MIMEText(text, "plain")
message["Subject"] = "Plain text email"
message["From"] = sender_email
message["To"] = receiver_email

try:
    # Establish connection with the SMTP server
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()  # Secure the connection
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print('Email sent successfully.')
except Exception as e:
    print(f"Failed to send email: {e}")
