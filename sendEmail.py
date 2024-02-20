
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("some email text")
msg['Subject'] = "Subject"
msg['From'] = 'davsuar@amazon.com'
msg['To'] = 'davsuar@amazon.com'
smtp = smtplib.SMTP("mail-relay.amazon.com")
smtp.sendmail(msg['From'], [msg['To']], msg.as_string())
smtp.quit()