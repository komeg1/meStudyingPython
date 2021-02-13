import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket


def send_mail(text, subject, from_email, to_emails=[]): #text - your main message, subject - e-mail's subject, from e-mail - input your e-mail
    assert isinstance(to_emails, list)
    msg=MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    msg_str = msg.as_string()

    #login to smtp
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)

    server.quit()

print("Before using check if you have disabled captcha verification: (https://accounts.google.com/DisplayUnlockCaptcha)\n\n")
print("Before using check if you have enabled less secure applications access: (https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4MjVCTmoD7krOcSrbTQdHbc9GkoW5EawkG0Y2nT36bOTdm5nrpHlyncPoo0NLs5WNQXoiH5FNv9G587rUtZMu3MSXLyg)\n\n")
check = input("You will have to provide Gmail username and Gmail password to continue. Do you want to continue? (Y/N): ")

if check == "Y":
    username = input("Provide your Gmail username: \n\n")
    password = input("Provide your Gmail password: \n\n")
    subject = input("Please provide a subject of your message: \n\n")
    message = input("Please provide your message: \n\n")
    hm = int(input("To how many people you want to send your message?: \n\n"))
    print("Provide e-mail(s). One in each line:\n")
    to_emails=[]
    for i in range(0, hm):
        to_email = input("\n")
        to_emails.append(to_email)

    send_mail(message, subject, username, to_emails)

