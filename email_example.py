# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

textfile = "README.md"

# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

me = "siacespark@gmail.com"
you = "siacespark@gmail.com"
msg['Subject'] = f"The contents of {textfile}"
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost', 1025)
s.send_message(msg)
s.quit()