import smtplib
import sys
from email.message import EmailMessage
 
CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com",
    "mint": "@tmomail.net"
}
 
EMAIL = "EMAIL"
PASSWORD = "PASSWORD"
 
def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    msg = EmailMessage()
    msg['Subject'] = 'SUBJECT'
    msg['From'] = auth[0]
    msg['To'] = recipient
    msg.set_content("\n"+message)
 
    server.send_message(msg)
 
 
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"Usage: python3 {sys.argv[0]} <PHONE_NUMBER> <CARRIER> <MESSAGE>")
        sys.exit(0)
 
    phone_number = sys.argv[1]
    carrier = sys.argv[2]
    message = sys.argv[3]
 
    send_message(phone_number, carrier, message)
