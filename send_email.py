import smtplib
import ssl
from email.message import EmailMessage

# Email details
subject = "Email from python" # Subject of the email
body = "This is an email from python code" # Body of the email
sender_email = "your-email@gmail.com"   # Sender's email address
receiver_email =  "receiver-email@gmail.com"  # Receiver's email address

# Prompt for the email account app password
password = input("Enter the app password: ") # Use an App Password for authentication


# Create the email message
message = EmailMessage()
message["from"]=sender_email
message["to"]= receiver_email
message["subject"]=subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email")

with smtplib.SMTP_SSL("smtp.gmail.com",465, context = context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email,receiver_email,message.as_string())

print("Success")